from flask import Flask, request
from pymongo import MongoClient
import quandlToMongo
from pprint import pprint

quandlToMongo.populateMongo() #populates MongoDB tables

app = Flask(__name__)
#TODOpytests


client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['zillowDB']

rentCollection = db['median_rental']
soldCollection = db['median_sold']
SQFTCollection = db['median_SQFT']


@app.route("/word_count")
def word_count():
    words = str(request.args.get('words'))
    total = len(words.split())
    return "The total words in the string are: " + str(total)

@app.route("/getMedianSold")
def soldPrice():
    data = soldCollection.find({})
    output = str(list(data))
    return output

@app.route("/getMedianRent")
def rentPrice():
    data = rentCollection.find({})
    output = str(list(data))
    return output

@app.route("/getMedianSQFT")
def SQFTPrice():
    data = SQFTCollection.find({})
    output = str(list(data))
    return output

if __name__ == '__main__':
    app.run()