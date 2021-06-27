import json
from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import BooleanField, StringField


class BaseMongoMixin():
    def object(self, **kwargs):
        return {
            '_id': self.pk,
            **kwargs
        }
        

class User(Document, BaseMongoMixin):
    fullname = StringField(required=True, max_length=120)
    email = StringField(required=True, max_length=120, unique=True)
    is_admin = BooleanField(default=False)

    def object(self):
        return super().object(fullname=self.fullname, email = self.email, is_admin=self.is_admin)
    # 
