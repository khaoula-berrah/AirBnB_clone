#!/usr/bin/env python3

import unittest
import uuid
import datetime
from models.base_model import BaseModel

"""
    Module UnitTest of BaseModel class.
"""


class test_base_model(unittest.TestCase):
    """
        test_base_model class.

        To Do a Unit test for BaseModel class.
    """
    def test_instantiation(self):
        """ method that tests the instantiation of base_model """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")


if __name__ == '__main__':
    unittest.main()
