from bson import ObjectId
from app.library.mongodb import get_db
from app.product.product_model import Product

db = get_db()
COLLECTION_NAME = "product"

def find_products() -> list[Product]:
    try:
        products = list(db.collection(COLLECTION_NAME).find())
        return [Product(**product) for product in products]
    except Exception as e:
        print(e)
        raise e
    
def find_product(id: ObjectId) -> Product:
    try:
        product = db.collection(COLLECTION_NAME).find_one({"_id": ObjectId(id)})
        return Product(**product)
    except Exception as e:
        print(e)
        raise e

def insert_product(product: Product) -> ObjectId:
    try:
        return db.collection(COLLECTION_NAME).insert_one(product.dict(by_alias=True)).inserted_id
    except Exception as e:
        print(e)
        raise e

    
def delete_product(id: ObjectId) -> None:
    try:
        return db.collection(COLLECTION_NAME).delete_one({"_id": ObjectId(id)})
    except Exception as e:
        print(e)
        raise e