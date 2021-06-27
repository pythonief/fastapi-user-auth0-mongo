from bson.objectid import ObjectId


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class MongoMixinBaseModel():
    id: ObjectIdStr = None

    class Config():
        orm_mode = True
        fields = {'id': '_id'}
