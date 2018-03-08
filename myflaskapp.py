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

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return jsonify(error='Authentication required'), 401, \
        {'WWW-Authenticate': 'Basic realm="Login Required"'}

# error
#     raise klass(message, resp.status_code, resp.text, resp.headers, code)
# quandl.errors.quandl_error.NotFoundError: (Status 404) (Quandl Error QECx02) You have submitted an incorrect Quandl code. Please check your Quandl codes and try again

if __name__ == '__main__':
    app.run()