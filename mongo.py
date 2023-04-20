import os

from pymongo import MongoClient

cluster = MongoClient(os.getenv('MONGO_URI'))

db = cluster["Python"]

# To create a database:
# collection_name = db[collection_name]
