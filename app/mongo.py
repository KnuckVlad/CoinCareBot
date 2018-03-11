# module working with mongo
from pymongo import MongoClient
from config import database_name, collection_name

client = MongoClient('localhost', 27017)
db = client[database_name]
music = db[collection_name]


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