from flask import Flask, request
from pymongo import MongoClient
import jsonify #add to requirements.txt or uninstall
import pandas





########## tutorial - end ##########

app = Flask(__name__)
#pytests
#get real estate graph for city(x) for dates(x to y) LIKE (Trulia trend_

#get average for city(x) fro dates(x to y)

#get percentile(P) average for city(x) from dates(x to y)?



@app.route("/word_count")
def word_count():
    words = str(request.args.get('words'))
    total = len(words.split())
    return "The total words in the string are: " + str(total)

if __name__ == '__main__':
    app.run()