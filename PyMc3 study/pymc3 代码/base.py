# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:18:00 2017

@author: Cabbage
base backend for traces
"""

import pymc3 as pm
import itertools as itl

import numpy as np
import warnings
import theano.tensor as tt#tensor:张量操作库

from pm.model import modelcontext
 

class BackendError(Exception):
    pass

class BaseTrace(object):
    supports_sampler_stats=False
    
    
    def __init__(self,name,model=None,vars=None,test_point=None):
        self.name=name
    
        model=modelcontext(model)
        self.model=model
        if vars is None:
        
           vars=model.unobserved_RVs
        self.vars=vars
        self.varnames=[var.name for var in vars]
        self.fn=model.fastfn(vars)
    
        if test_point is None:
            test_point=model.test_point
        else:
        
            test_point=model.test_point.copy()
            test_point_.updata(test_point)
            test_point=test_point_
        var_values=list(zip(self.varnames,self.fn(test_point)))
        self.var_shapes={var:value.shape for var,value in var_values}
        self.var_dtypes={var:value.dtype for var,value in var_values}
    
        self.chain=None
        self._is_base_setup=False
        self.sampler_vars=None
    
    def _set_sampler_vars(self,sampler_vars):
        if sampler_vars is not None and not self.supports_sampler_stats:
            raise ValueError("Backend does not support sampler stats")
        if self._is_base_setup and self.sampler_vars!=sampler_vars:
            raise ValueError("Can't change sampler_vars")
        if sampler_vars is None:
            self.sampler_vars=None
            return
        
        dtypes={}
        for stats in sampler_vars:
            for key,dtype in stats.items():
                if dtype.setdefault(key,dtype)!=dtype:
                    raise ValueError("Sampler statistic %s appears with different types"% key)
        self.sampler_vars=sampler_vars
    
    def setup(self,draws,chain,sampler_vars=None):
        self._set_sampler_vars(sampler_vars)
        self._is_base_setup=True
     
    def record(self,point,sampler_states=None):
        raise NotImplementedError

    def close(self):
        pass

    def __getitem__(self,idx):
        if isinstance(idx,slice):
            return self._slice(idx)
        try:
            return self.point(int(idx))
        except (ValueError,TypeError):
            raise ValueError("Can only index with slice or integer")
        

    def __len__(self):
        raise NotImplementedError
    
    def get_values(self,varname,burn=0,thin=1):
        raise NotImplementedError
    
    def get_sampler_stats(self,varname,sampler_idx=None,burn=0,thin=1):
        if not self.supports_sampler_stats:
            raise ValueError("This backend does not support sampler stats")
        if sampler_idx is not None:
            return self._get_sampler_stats(varname,sampler_idx,burn,thin)
        sampler_idxs=[i for i,s in enumerate(self.sampler_vars) if varname in s]
    
        if not sampler_idxs:
            raise KeyError("Unknown sampler stat %s"% varname)
        vals=np.stack([self._get_sampler_stats(varname,i,burn,thin) for i in sampler_idxs],axis=-1)
        if vals.shape[-1]==1:
            return vals[...,0]
        else:
            return vals
        
    def _get_sampler_stats(self,varname,sampler_idx,burn,thin):
        raise NotImplementedError()
    
    def _slice(self,idx):
        raise NotImplementedError
    
    def point(self,idx):
        raise NotImplementedError
    
    def stat_names(self):
        if self.supports_sampler_stats:
            names=set()
            for vars in self.sampler_vars or []:
                names.update(vars.keys())
            return names
        else:
            return set()
        
class MultiTrace(object):
    def __init__(self,straces):
        self._straces={}
        for strace in straces:
            if strace.chain in self._straces:
                raise ValueError("Chains are not nique")
            self._straces[straces.chain]=strace
    def __repr__(self):
        template='<{}:{} chains,{} iterations,{} variables>'
        return template.format(self.__class__.__name__,self.nchains,len(self),len(self.varnames))
        
    def nchains(self):
        return len(self._straces)
        
    def chains(self):
        return list(sorted(self._straces.keys()))
    
    def __getitem__(self,idx):
        if isinstance(idx,slice):
            return self._slice(idx)
        try:
            return self.point(int(idx))
        except (ValueError,TypeError):
            pass
        
        if isinstance(idx,tuple):
            var,vslice=idx
            burn,thin=vslice.start,vslice.step
            if burn is None:
                burn=0
            if thin is None:
                thin=1
        else:
            var=idx
            burn,thin=0,1
        var=str(var)
        if var in self.varnames:
            if var in self.stat_names:
                warnings.warn("Attribute access on a trace object is ambigous,\
                               sampler statistic and model variable share a name ,use trace.get_values or trace.get_sampler_stats.")
            return self.get_values(var,burn=burn,thin=thin)
        if var in self.stat_names:
            return self.get_sampler_stats(var,burn=burn,thin=thin)
        raise KeyError("Unknown variable %s"% var)
        
     #_attrs=set(['_straces','narnames','chains','stat_names','supports_sampler_stats'])
     _attrs = set(['_straces', 'varnames', 'chains', 'stat_names', 
                  'supports_sampler_stats']) 


    def __getattr__(self,name):
        if name in self._attrs:
            raise AttributeError
            
        name=str(name)
        if name in self.varnames:
            if name in self.stat_names:
                warnings.warn("Attribute access on a trace object is ambigous,\
                               sampler statistic and model variable share a name ,use trace.get_values or trace.get_sampler_stats. ")
            return self.get_values(name)
        if name in self.stat_names:
            return self.get_sampler_stats(name)
        raise AttributeError("'{}'object has no attribute'{}'".format(type(self).__name__,name))

    def __len__(self):
        chain=self.chains[-1]
        return len(self._straces[chain])
        
        
    def varnames(self):
        chain=self.chains[-1]
        return self._straces[chain].varnames
    
    def stat_names(self):
        if not self._straces:
            return set()
        sampler_vars=[s.sampler_vars for s in self._straces.values()]
        if not all(svars==sampler_vars[0] for svars in sampler_vars):
            raise ValueError("Inivdual chains contain different sampler stats")
        names=set()
        for trace in self._straces.values():
            if trace.sampler_vars in None:
                continue
            for vars in trace.sampler_vars:
                names.update(vars.keys())
        return names
        
    def add_values(self,vals):
        for k,v in vals.items():
            if k self.varnames:
                raise ValueError("Variable name {} already exists ".format(k))
             self.varnames.append(k)
             
             chains=self._straces
             l_samples=len(self)*len(self.chains)
             l_v=len(v)
             if l_v != l_samples:
                 warnings.warn("the length of the values you are trying to add ({})does not match the nummber({})of total samples in the trace\
                                (chains*iterations)".format(l_v,l_samples))
              v=np.squeeze(v.reshape(len(chains),len(self),-1)
              
              for idx,chain in enumerate(chains.values()):
                  chain.samples[k]=v[idx]
                  dummy=tt.as_tensor_variable([],k)
                  chain.vars.append(dummy)
              

    def get_values(self,varname,burn=0,thin=1,combine=True,chains=None,squeeze=True):
        if chains is None:
            chains=self.chains
        varname=str(varname)
        try:
            results=[self._straces[chain].get_values(varname,burn,thin) for chain in chains]
        except TypeError:
            results=[self._straces[chain].get_values(varname,burn,thin)]
        return _squeeze_cat(results,combine,squeeze)
        
        
    def get_sampler_stats(self,varname,burn=0,thin=1,combine=True,chains=None,squeeze=True):
        if varname not in self.stat_nmaes:
            raise KeyError("unknown sampler statistic %s"% varname)
        if chains is None:
            chains=self.chains
        try:
            chains=iter(chains)
        except TypeError:
            chains=[chains]
        results=[self._straces[chain].get_sampler_stats(varname,None,burn,thin) for chain in chains]
        return _squeeze_cat(results,combine,squeeze)
                 
    def _slice(self,idx):
        new_traces=[trace._slice(idx) for trace in self._straces.values()]
        return MultiTrace(new_traces)
            
            
    def point(self,idx,chain=None):
        if chain is None:
            chain=self.chains[-1]
        return self._straces[chain].point(idx)
        
    def points(self,chains=None)
        if chains in None:
            chains=self.chains
        return itl.chain.from_iterable(self._straces[chain] for chain in chains)
        
    def merge_traces(mtraces):
        base_mtrace=mtraces[0]
        for new_mtrace in mtraces[1:]:
            for new_chain,strace in new_mtrace._straces.items():
                if new_chain in base_mtrace._straces:
                    raise ValueError("Chains are not unique")
                base_mtrace._straces[new_chain]=strace
        return base_mtrace
        
    def _squeeze_cat(results,combine,squeeze):
        if combine:
            results=np.concatenate(results)
            if not squeeze:
                results=[results]
        else:
           if squeeze and len(results)==1:
               results=results[0]
        return results
           
            
            
           
            
    
    
       
        
        
        
        
        
        
        