from copy import deepcopy
import unittest
from freezegun import freeze_time
from datetime import datetime
from unittest.mock import patch
from mongomock import MongoClient
from app.product.product_model import Product
from app.product.product_service import find_products, insert_product

mock_db = MongoClient()["test"]

@freeze_time("2021-01-01")
@patch("app.product.product_service.db.get_collection")
#@patch.object(product_service, "db", return_value=collection)
class TestFindProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = [{"name": "test", "price": 100.0, "isDeleted": False, "createdAt": datetime.utcnow()}]
        cls.mock_collection = mock_db["product"]
        print(cls.product)
        cls.mock_collection.insert_many(deepcopy(cls.product))
        print(cls.product)
        return super().setUpClass()
    
    
    def test_find_products(self, collection):
        collection.return_value = self.mock_collection
        actual = find_products()
        self.assertEqual(len(actual), len(self.product))
        self.assertTrue(self.product[0].items() <= actual[0].dict(by_alias=True).items())

@freeze_time("2021-01-01")
@patch("app.product.product_service.db.get_collection")
class TestInsertOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = [{"name": "test", "price": 100.0, "isDeleted": False, "createdAt": datetime.utcnow()}]
        cls.mock_collection = mock_db["product"]
        return super().setUpClass()
    
    def test_insert_one_new_product(self, collection):
        collection.return_value = self.mock_collection
        new_product = Product(**deepcopy(self.product[0]))
        actual_id = insert_product(new_product)
        actual = self.mock_collection.find_one({"_id": actual_id})
        self.assertDictEqual(new_product.dict(by_alias=True), actual)


if __name__ == '__main__':
    unittest.main()