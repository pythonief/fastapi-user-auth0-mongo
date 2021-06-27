from mongoengine import *
from mongoengine.connection import connect

from app import config


client = connect(
    host=config.DB_CONFIG['DB_URI']
)
