#ToDo make mock up DB

from pymongo import MongoClient
import myflaskapp.quandlToMongo
import myflaskapp.myflaskapp

#MongoDB setup
myflaskapp.quandlToMongo.populateMongo()  # populates MongoDB tables
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['zillowDB']

soldCollection = db['median_sold']
rentCollection = db['median_rental']
SQFTCollection = db['median_SQFT']



#Takes a python String slice of MongoDB output and checks for a date
def test_date_sold():
    assert '2016-06-30' in myflaskapp.myflaskapp.getZillow(soldCollection)[500:600]

#Takes a python String slice of MongoDB output and checks for a median value
def test_median_sold():
    assert '804250.0' in myflaskapp.myflaskapp.getZillow(soldCollection)[800:900]


#Takes a python String slice of output and checks for a date
def test_date_rent():
    assert '2018-01-31' in myflaskapp.myflaskapp.getZillow(rentCollection)[500:600]

#Takes a python String slice of output and checks for a median value
def test_median_rent():
    assert '3300.0' in myflaskapp.myflaskapp.getZillow(rentCollection)[800:900]



#Takes a python String slice of output and checks for a date
def test_date_SQFT():
    assert '2017-06-30' in myflaskapp.myflaskapp.getZillow(SQFTCollection)[600:700]

#Takes a python String slice of MongoDB output and checks for a median value
def test_median_SQFT():
    assert '568.0' in myflaskapp.myflaskapp.getZillow(SQFTCollection)[900:999]
