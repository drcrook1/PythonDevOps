"""
Author: David Crook
Copyright: Microsoft Corporation - 2019

Tests module.py
"""
import sys
import os
import pytest
sys.path.append("../app/") #append path to add location of actual app
import app.module as m

class TestModule(object):
    """
    Tests Module for various cases.
    """
    def setUp(self):
        pass
    
    def test_testing(self):
        assert(True)
    
    def test_multiply(self):
        r = m.multiply(2,4)
        assert(r == 8)
    
    def test_divide(self):
        r = m.divide(2,4)
        assert(r == 0.5)
        