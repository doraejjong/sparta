import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

choiceMovie = db.movies.find_one({'title':'월-E'})
choiceStar = choiceMovie['star']



