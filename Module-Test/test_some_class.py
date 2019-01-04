"""
Author: David Crook
Copyright: Microsoft Corporation - 2019

Tests some_class.py
"""
import sys
import os
import pytest
sys.path.append("../app/") #append path to add location of actual app
from app.some_class import SomeClass

class TestSomeClass(object):
    """
    Tests Module for various cases.
    """
    def setUp(self):
        pass
    
    def test_testing(self):
        assert(True)
    
    def test_initialization_optional_parameters(self):
        inst = SomeClass(x = 2, y = 4)
        assert(inst.x == 2)
        assert(inst.y == 4)
    
    def test_total_value(self):
        inst = SomeClass(x = 2, y = 4)
        r = inst.total_value()
        assert(6 == r)
        