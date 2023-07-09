from bson import InvalidDocument, ObjectId
from pydantic.json import ENCODERS_BY_TYPE

class PydanticObjectId(ObjectId):
    """
    Object Id field. Compatible with Pydantic.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, bytes):
            v = v.decode("utf-8")
        try:
            return PydanticObjectId(v)
        except InvalidDocument:
            raise TypeError("Id must be of type PydanticObjectId")

    @classmethod
    def __modify_schema__(cls, field_schema: dict):
        field_schema.update(
            type="string",
            example="5eb7cf5a86d9755df3a6c593",
        )


ENCODERS_BY_TYPE[
    PydanticObjectId
] = str  # it is a workaround to force pydantic make json schema for this field