Overview
========
Take Home Assignment for Rest APIs

Write the code for the problem below in the language of your choice:

Count Words in a String

Explain how you would deal with each of the following issues:

-DNS is not working

-Website is encountering timeout


Create a GitHub repo for the following project:

-Get a dataset of your choosing (i.e. Quandl, Open Movie Database, etc.)

-Populate data into a database

Build an API with following components:

-Endpoints

-Methods

-Status Codes

-README with documentation of API

-Bonus: Unit and integration tests


Requirements
------------

To install and run you need:

- Python 3.6+ (Older versions should work with print "minor changes")
- pyenv (or replace `pyvenv` with `virtualenv`)
- git (to clone this repository)
- MongoDB installed on local/server

Installation
------------

These steps install cloned code, dependencies and virtual environment.

    $ git clone https://github.com/HalinGG/RestAPI-HWK.git

    $ cd RestAPI-HWK
activate your pyenv or virtualenv and run::
    pip install -r requirements.txt


Steps to install MongoDB: https://docs.mongodb.com/manual/administration/install-community/


Running all Rest APIs
=================

Start MongoDB by executing "mongod" file::
    mongod

This should start mongoDB at: http://127.0.0.1:27017/
Note: MongoDB Url can be changed in the configuration.ini

Run "myflaskapp.py" to start the Flask Web Server at: http://127.0.0.1:5000/


How to Use WordAPI
------------------
This is a Rest API that returns the total count of words from input.

Enter input into URL in the form::

    http://127.0.0.1:5000/word_count?words=my sentence to count


Answers to your Questions
-------------------------

How would you deal with DNS not working?
If DNS is not working, I would send user requests to the IP address of the server my
application is hosted on instead of using DNS. Also, this fix could be automated in python
and we could include automated DNS trouble shooting such as clearing DNS cache, ping ip, etc.


How would you deal with the website encountering timeout?
If many users are experiencing timeout issues, the server this application
is hosted on should restart itself and team notified(error codes and logs).
A timeout of 100 seconds could be set.
Monitoring and testing should help the team catch issues early to determine
if this is an issue with the client or server side.



Notes
------

Flask will output HTTP Status codes to the python console::
    127.0.0.1 - - [08/Mar/2018 00:25:57] "GET /getMedianRent HTTP/1.1" 200 -
    127.0.0.1 - - [08/Mar/2018 00:34:02] "GET /getMedianASDF HTTP/1.1" 404 -

