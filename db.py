from pymongo import MongoClient
from cfg import MONGO_URI, DATABASE_NAME1, DATABASE_NAME2, NEW_DATABASE_NAME


def get_connection():
    return MongoClient(MONGO_URI)


def get_database1():
    connection = get_connection()
    return connection[DATABASE_NAME1]


def get_database2():
    connection = get_connection()
    return connection[DATABASE_NAME2]


def get_new_database():
    connection = get_connection()
    return connection[NEW_DATABASE_NAME]
