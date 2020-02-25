#!/usr/bin/python3
'''Tests for City class'''
import models
from models.base_model import BaseModel
from models.city import City
import os
import unittest


class _city(unittest.TestCase):
    '''start tests'''

    def test_docstring(self):
        '''test if funcions, methods, classes
        and modules have docstring'''
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.city.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(City.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/city.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/city.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/city.py', os.X_OK)
        self.assertTrue(is_exec_true)
