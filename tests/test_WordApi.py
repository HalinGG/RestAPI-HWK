#
#
# import configparser
# config = configparser.ConfigParser()
# config.read('configuration.ini')
# import sys, os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

import myflaskapp
#
# # Bring your packages onto the path

# # Now do your import
#from myflaskapp import word_count

def test_word_count():
    assert myflaskapp.word_count()("One Two Three") == 3

