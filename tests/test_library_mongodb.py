# import unittest
# from unittest.mock import patch
# import mongomock
# import app.library.mongodb as mongodb_library
# from app.library.mongodb import insert_one

# COLLECTION_NAME = "testcollection"
# mock_db = mongomock.MongoClient("localhost", 27017)["test"]


# @patch.object(mongodb_library, "get_db", return_value=mock_db)
# class TestInsertOne(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.mocked_collection = mock_db[COLLECTION_NAME]
#         return super().setUpClass()

#     def setUp(self) -> None:
#         return super().setUp()

#     def tearDown(self) -> None:
#         self.mocked_collection.drop()
#         return super().tearDown()

#     def test_should_return_inserted_id(self, mongo_mock):
#         # Arrange
#         expected = {"name": "John Doe", "age": 30}
#         # Act
#         result = insert_one(COLLECTION_NAME, expected)
#         # Assert
#         self.assertIsNotNone(result)
#         actual: dict = self.mocked_collection.find_one({"_id": result})
#         self.assertTrue(expected.items() <= actual.items())


# if __name__ == "__main__":
#     unittest.main()
