""" myflaskapp.py: This script contains the Flask REST API endpoints for the Word API and
                    Zillow Real Estate API.
"""


from flask import Flask, request
from pymongo import MongoClient
from importlib.machinery import SourceFileLoader
quandlToMongo = SourceFileLoader("quandToMongo", "/Users/halgarci/PycharmProjects/WordApi/myflaskapp/quandlToMongo.py").load_module()

#import myflaskapp.quandlToMongo

quandlToMongo.populateMongo()  # populates MongoDB tables

#MongoDB setup
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['zillowDB']

rentCollection = db['median_rental']
soldCollection = db['median_sold']
SQFTCollection = db['median_SQFT']

app = Flask(__name__)

@app.route("/word_count")
def word_count():
    ''' This method provides a Flask API endpoint that takes a sentence as input
        and returns the total count of the words in that sentence.
    '''
    words = str(request.args.get('words'))
    return "The total words in the string are: " + getCount(words)

@app.route("/getMedianSold")
def soldPrice():
    ''' This method provides a Flask API endpoint that GETS/returns
        Zillow Median Sold Price each year for All Homes in San Jose, CA
        Returned data is in JSON format.
    '''
    return getZillow(soldCollection)

@app.route("/getMedianRent")
def rentPrice():
    ''' This method provides a Flask API endpoint that GETS/returns
        Zillow Median Rental Price each year For All Homes in San Jose, CA
        Returned data is in JSON format.
    '''
    return getZillow(rentCollection)

@app.route("/getMedianSQFT")
def SQFTPrice():
    ''' This method provides a Flask API endpoint that GETS/returns
        Zillow Median Sold Price Per Square Foot each year For All Homes in San Jose, CA
        Returned data is in JSON format.
    '''
    return getZillow(SQFTCollection)


def getCount(words):
    ''' This python method takes a sentence as input
            and returns the total count of the words in that sentence.
    '''
    total = len(words.split())
    return str(total)

def getZillow(collection):
    ''' This python method takes a collection as input
        and returns the data stored in that collection.
    '''
    data = collection.find({})
    output = str(list(data))
    return output

if __name__ == '__main__':
    app.run()