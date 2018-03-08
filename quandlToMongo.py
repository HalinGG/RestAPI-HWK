import quandl
import sys
from urllib.request import urlopen
import json
from pymongo import MongoClient
from bson import json_util

quandl.ApiConfig.api_key = 'wSJyei4z9c8ykqryY8i6'

#Median Sold Price - All Homes|MSPAH
#print(quandl.get('ZILLOW/C8_MSPAH', start_date='2010-01-01', end_date='2018-03-07'))

#Median Sold Price Per Square Foot - All Homes|MSPFAH
#print(quandl.get('ZILLOW/C8_MSPFAH', start_date='2010-01-01', end_date='2018-03-07'))

#Median Rental Price - All Homes|MRPAH
#print(quandl.get('ZILLOW/C8_MRPAH', start_date='2010-01-01', end_date='2018-03-07'))

#Json to mongoDB




client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['zillowDB']
rentCollection = db['median_rental']

# This uploads
def upload(collection, url):
if rentCollection.count() != 1:
    myurl = "https://www.quandl.com/api/v3/datasets/ZILLOW/C8_MRPAH.json?api_key=wSJyei4z9c8ykqryY8i6"
    response = urlopen(myurl)
    data = json_util.loads(response.read())
    if rentCollection.count() == 0:
        rentCollection.insert(data)
    if rentCollection.count() > 1:
        rentCollection.drop()
        rentCollection.insert(data)





