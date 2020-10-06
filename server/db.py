from flask_pymongo import pymongo
CONNECT_PARAMS = "mongodb+srv://pavellap:A9MphHHvmrsJrJ2i@firstcluster.cxefr.mongodb.net/<dbname>?retryWrites=true&w" \
                 "=majority "

client = pymongo.MongoClient(CONNECT_PARAMS)
db = client.get_database('fullstack-todo')
user_collection = pymongo.collection.Collection(db, 'user_collection')


