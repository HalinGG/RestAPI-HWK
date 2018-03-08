import quandl
from urllib.request import urlopen
from pymongo import MongoClient
from bson import json_util

import configparser
config = configparser.ConfigParser()
config.read('configuration.ini')


quandl.ApiConfig.api_key = 'wSJyei4z9c8ykqryY8i6'

client = MongoClient(config['DEFAULT']['mongoDBurl'])
db = client['zillowDB']
rentCollection = db['median_rental']
soldCollection = db['median_sold']
SQFTCollection = db['median_SQFT']


def populateMongo():
    upload(rentCollection, "https://www.quandl.com/api/v3/datasets/ZILLOW/C8_MRPAH.json?api_key=wSJyei4z9c8ykqryY8i6")
    upload(soldCollection, "https://www.quandl.com/api/v3/datasets/ZILLOW/C8_MSPAH.json?api_key=wSJyei4z9c8ykqryY8i6")
    upload(SQFTCollection, "https://www.quandl.com/api/v3/datasets/ZILLOW/C8_MSPFAH.json?api_key=wSJyei4z9c8ykqryY8i6")

#response.getcode() returns the HTTP status code (404 not found, 200 OK, etc.)
def upload(collection, url):
    status = 100 #HTTP "continue" status code
    if collection.count() != 1:
        response = urlopen(url)
        data = json_util.loads(response.read())
        if collection.count() == 0:
            collection.insert(data)
        if collection.count() > 1:
            collection.drop()
            collection.insert(data)
        status = response.getcode()
    return status


#Upload Median Sold Price - All Homes|MSPAH
#print(quandl.get('ZILLOW/C8_MSPAH', start_date='2010-01-01', end_date='2018-03-07'))
#Median Sold Price Per Square Foot - All Homes|MSPFAH
#print(quandl.get('ZILLOW/C8_MSPFAH', start_date='2010-01-01', end_date='2018-03-07'))
#Median Rental Price - All Homes|MRPAH
#print(quandl.get('ZILLOW/C8_MRPAH', start_date='2010-01-01', end_date='2018-03-07'))


