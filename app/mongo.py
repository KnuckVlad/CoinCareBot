# module working with mongo
from pymongo import MongoClient
from config import DATABASE_NAME, DATABASE_COLLECTION_NAME

client = MongoClient('localhost', 27017)
db = client[DATABASE_NAME]
music = db[DATABASE_COLLECTION_NAME]


def select_all():
    """ Получаем все строки """
    return music.find({})


def select_single(rownum):
    """ Получаем одну строку с номером rownum """
    return music.find_one({"id": rownum})


def count_rows():
    """ Считаем количество строк """
    rows = music.count()
    print('Mongo rows: ' + str(rows))
    return rows


def close():
    """ Закрываем текущее соединение с БД """
    client.close()