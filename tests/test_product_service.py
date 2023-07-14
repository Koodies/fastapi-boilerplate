from copy import deepcopy
import unittest
from freezegun import freeze_time
from datetime import datetime
from unittest.mock import patch
from mongomock import MongoClient
from app.product.product_model import Product
from app.product.product_service import delete_product, find_products, insert_product

mock_db = MongoClient()["test"]


@freeze_time("2021-01-01")
@patch("app.product.product_service.db.collection")
class TestFindProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = [
            {
                "name": "test",
                "price": 100.0,
                "isDeleted": False,
                "createdAt": datetime.utcnow(),
            }
        ]
        cls.mock_collection = mock_db["product"]
        print(cls.product)
        cls.mock_collection.insert_many(deepcopy(cls.product))
        print(cls.product)
        return super().setUpClass()

    def test_find_products(self, collection):
        collection.return_value = self.mock_collection
        actual = find_products()
        self.assertEqual(len(actual), len(self.product))
        self.assertTrue(
            self.product[0].items() <= actual[0].dict(by_alias=True).items()
        )


@freeze_time("2021-01-01")
@patch("app.product.product_service.db.collection")
class TestInsertOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = [
            {
                "name": "test",
                "price": 100.0,
                "isDeleted": False,
                "createdAt": datetime.utcnow(),
            }
        ]
        cls.mock_collection = mock_db["product"]
        return super().setUpClass()

    def test_insert_one_new_product(self, collection):
        collection.return_value = self.mock_collection
        new_product = Product(**deepcopy(self.product[0]))
        actual_id = insert_product(new_product)
        actual = self.mock_collection.find_one({"_id": actual_id})
        self.assertDictEqual(new_product.dict(by_alias=True), actual)


@freeze_time("2021-01-01")
@patch("app.product.product_service.db.collection")
class TestDeleteOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = [
            {
                "name": "test",
                "price": 100.0,
                "isDeleted": False,
                "createdAt": datetime.utcnow(),
            }
        ]
        cls.mock_collection = mock_db["product"]
        return super().setUpClass()

    def setUp(self) -> None:
        self.mock_collection.insert_many(deepcopy(self.product))
        return super().setUp()

    def tearDown(self) -> None:
        self.mock_collection.drop()
        return super().tearDown()

    def test_delete_one_product(self, collection):
        collection.return_value = self.mock_collection
        actual_id = self.mock_collection.find_one({"name": "test"})["_id"]
        delete_product(actual_id)
        actual = self.mock_collection.find_one({"_id": actual_id})
        self.assertIsNone(actual)

    def test_delete_one_product_not_found(self, collection):
        collection.return_value = self.mock_collection
        actual_id = "123456789012345678901234"
        delete_product(actual_id)
        actual = self.mock_collection.find_one({"_id": actual_id})
        self.assertIsNone(actual)


if __name__ == "__main__":
    unittest.main()
