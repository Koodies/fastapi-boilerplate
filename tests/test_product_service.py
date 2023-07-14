from copy import deepcopy
import unittest
from freezegun import freeze_time
from datetime import datetime
from unittest.mock import patch
from mongomock import MongoClient
from app.product.product_model import Product
from app.product.product_service import (
    delete_product,
    find_product,
    find_products,
    insert_product,
)

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
        cls.mock_collection.insert_many(deepcopy(cls.product))
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
class TestFindProductById(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product = {
            "name": "test",
            "price": 100.0,
            "isDeleted": False,
            "createdAt": datetime.utcnow(),
        }
        cls.mock_collection = mock_db["product"]
        return super().setUpClass()

    def setUp(self) -> None:
        self.object_id = self.mock_collection.insert_one(
            deepcopy(self.product)
        ).inserted_id
        return super().setUp()

    def tearDown(self) -> None:
        self.mock_collection.drop()
        return super().tearDown()

    def test_find_one_product(self, collection):
        collection.return_value = self.mock_collection
        actual = find_product(self.object_id)
        self.assertTrue(self.product.items() <= actual.dict(by_alias=True).items())


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
        cls.product = {
            "name": "test",
            "price": 100.0,
            "isDeleted": False,
            "createdAt": datetime.utcnow(),
        }
        cls.mock_collection = mock_db["product"]
        return super().setUpClass()

    def setUp(self) -> None:
        self.object_id = self.mock_collection.insert_one(
            deepcopy(self.product)
        ).inserted_id
        return super().setUp()

    def tearDown(self) -> None:
        self.mock_collection.drop()
        return super().tearDown()

    def test_delete_one_product(self, collection):
        collection.return_value = self.mock_collection
        actual = delete_product(self.object_id)
        self.assertEqual(actual.deleted_count, 1)
        expected = self.mock_collection.find_one({"_id": self.object_id})
        self.assertIsNone(expected)

    def test_with_unknown_object_id(self, collection):
        collection.return_value = self.mock_collection
        actual_id = "123456789012345678901234"
        actual = delete_product(actual_id)
        self.assertEqual(actual.deleted_count, 0)
        expected: dict = self.mock_collection.find_one({"_id": self.object_id})
        self.assertTrue(self.product.items() <= expected.items())

    def test_with_invalid_object_id_should_return_exception(self, collection):
        collection.return_value = self.mock_collection
        actual_id = "12345678asdcasss45678901234"
        with self.assertRaises(Exception):
            delete_product(actual_id)
        expected: dict = self.mock_collection.find_one({"_id": self.object_id})
        self.assertTrue(self.product.items() <= expected.items())


if __name__ == "__main__":
    unittest.main()
