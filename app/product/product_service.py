from bson import ObjectId
from app.library.mongodb import get_db
from app.product.product_model import Product

db = get_db()
COLLECTION_NAME = "product"

def find_products() -> list[Product]:
    try:
        products = list(db.get_collection(COLLECTION_NAME).find())
        return [Product(**product) for product in products]
    except Exception as e:
        print(e)
        raise e

def insert_product(product: Product) -> ObjectId:
    try:
        return db.get_collection(COLLECTION_NAME).insert_one(product.dict(by_alias=True)).inserted_id
    except Exception as e:
        print(e)
        raise e