#!/usr/bin/python3
import unittest
from  models import BaseModel
import datetime
from models import *

class TestingBaseModel(unittest.TestCase):
    """BaseModel class test """
    def  setup(self):
        """
        testing objects setup
        """
        self.model1_test = BaseModel()
        self.model2_test = BaseModel()

    def setup_instantiation_test(self):
        """
        testing to_json method  of BaseModel class
         """
        self.assertTrue(hasattr(self.model1_test, "id"))
        self.assertTrue(hasattr(self.model1_test, "__class__"))
        self.assertTrue(hasattr(self.model1_test, "created_at"))
        self.assertTrue(hasattr(self.model1_test, "updated_at"))
        
    def setup_reinstantiation_test
        self.assertIsInstance(self.model2_test, BaseModel)
        self.assertTrue(self.model1_test.id != self.model2_test.id)
        m1_obj = self.model1_test.created_at
        m2_obj = self.model2_test.created_at
        self.assertTrue(m1_obj != m2_obj)
        self.assertTrue(type(m1_obj) is datetime.datetime)

    def test_save(self):
        """
        testing if save updates the updated_at attribute
        """
        self.assertFalse(hasattr(self.model1_test, "updated_at"))
        self.model1_test.save()
        self.assertTrue(hasattr(self.model1_test, "updated_at"))
        old_time_obj= self.model2_test.update_at
        self.model2_test.save()
        self.assertNotEqual(old_time_obj, self.model2.updated_at)

    def test_to_json(self):
        """
        testing to_json method regarding  output & in-memory objects
        """
        modelid_test = self.model1_test.id
        jsondict_test = self.model1_test.to_json()
        self.assertNotEqual(jsondict_test, self.model1_test.__dict__)
        self.assertEqual(jsondict_test["id"], self.model1_test.__dict__["id"])
        self.assertNotEqual(jsondict_test["created_at"],
                            self.model1_test.__dict__["created_at"])
        self.assertNotEqual(type(jsondict_test["created_at"]),
                            type(self.model1_test.__dict__["created_at"]))

if __name__ == '__main__':
    unittest.main()
