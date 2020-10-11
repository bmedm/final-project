from config import DBURL
from pymongo import MongoClient

client = MongoClient(DBURL)
db = client.get_database()