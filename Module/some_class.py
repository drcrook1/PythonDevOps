"""
Author: David Crook
Copyright: Microsoft Corporation - 2019

Simple module with very basic mathematical functionality.
This module is a class object and maintains state.
"""
from numbers import Number

class SomeClass():
    """
    some basic class with basic functionality
    """
    x = None
    y = None
    
    def __init__(self, x = None, y = None):
        """
        initialization function with optional parameters.
        """
        self.x = x
        self.y = y
    
    def validate_self(self):
        """
        validates all values in object
        Returns: True/False if object is valid or not.
        """
        x_valid = isinstance(self.x, Number)
        y_valid = isinstance(self.y, Number)
        if(x_valid and y_valid):
            return True
        else:
            return False
    
    def total_value(self):
        """
        Simply returns the total value of x + y
        """
        if(self.validate_self()):
            return self.x + self.y
        else:
            raise ValueError("SomeClass is invalid, please correctly set your x and y values.")
