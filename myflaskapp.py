""" myflaskapp.py: This script contains the Flask REST API endpoints for the Word API and
                    Zillow Real Estate API.
"""


from flask import Flask, request
from pymongo import MongoClient
import quandlToMongo

import configparser
config = configparser.ConfigParser()
config.read('configuration.ini')


app = Flask(__name__)
#TODOpytests

quandlToMongo.populateMongo() #populates MongoDB tables

client = MongoClient(config['DEFAULT']['mongoDBurl'])
db = client['zillowDB']

rentCollection = db['median_rental']
soldCollection = db['median_sold']
SQFTCollection = db['median_SQFT']


@app.route("/word_count")
def word_count():
    ''' This method provides a Flask API endpoint that takes a sentence as input
        and returns the total count of the words in that sentence.
    '''
    words = str(request.args.get('words'))
    total = len(words.split())
    return "The total words in the string are: " + str(total)

@app.route("/getMedianSold")
def soldPrice():
    ''' This method provides a Flask API endpoint that GETS/returns
        Zillow Median Sold Price for All Homes in San Jose, CA
        Returned data is in JSON format.
    '''
    data = soldCollection.find({})
    output = str(list(data))
    return output

@app.route("/getMedianRent")
def rentPrice():
    ''' This method provides a Flask API endpoint that GETS/returns
        Zillow Median Rental Price For All Homes in San Jose, CA
        Returned data is in JSON format.
    '''
    data = rentCollection.find({})
    output = str(list(data))
    return output

@app.route("/getMedianSQFT")
def SQFTPrice():
    ''' This method provides a Flask API endpoint that GETS/returns
        Zillow Median Sold Price Per Square Foot For All Homes in San Jose, CA
        Returned data is in JSON format.
    '''
    data = SQFTCollection.find({})
    output = str(list(data))
    return output

if __name__ == '__main__':
    app.run()