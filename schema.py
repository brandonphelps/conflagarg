#!/usr/bin/env python3

from collections import OrderedDict

class Schema(self):
    def __init__(self):
        """
        A class for defining a conflagarg schema.
        """
        self._params = OrderedDict() #preserve the user-defined order
        
    def sections(self):
        """
        Returns the sections as part of this schema.
        """
        return list(self._params.keys())
    
    def add_section(self, section):
        if section in self._params:
            raise ValueError("Section is already part of schema.")
        self._params[section] = None
        
    def params(self):
        """
        Returns the parameters currently part of this schema.
        """
        return dict(self._params)
    
    def add_param(self, key, value=None, section=None, required=False, check=None):
        """
        Add a parameter definition to the schema.
        """
        if check and not hasattr(check, '__call__'):
            raise ValueError("check must be a function.")
        else:
            check = lambda: True
        
        s = section
        if not len(self._params) and s is None:
            #There are no sections. We should not require the dev to define
            #any.
            s = "Global"
        self._params[s] = (key,  value, required, check)