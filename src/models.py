# coding:utf-8
from datetime import datetime

from mongokit import Document, Connection

connection = Connection('localhost', 27017)
DB_NAME = 'ruguojiu'
user_coll = connection.DB_NAME.users


@connection.register
class User(Document):
    __collection__ = user_coll.name
    __database__ = DB_NAME
    structure = {
        'email': unicode,
        'mobile': unicode,
        'created_at': datetime
    }
    required_fields = ['email', 'mobile']
    use_dot_notation = True

    @classmethod
    def get_all_add(cls):
        return list(connection.User.find())


