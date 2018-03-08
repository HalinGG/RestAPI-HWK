Overview
=======
Take Home Assignment for Rest APIs

Write the code for the problem below in the language of your choice:
Count Words in a String
Explain how you would deal with each of the following issues:
DNS is not working
Website is encountering timeout
Create a GitHub repo for the following project:
Get a dataset of your choosing (i.e. Quandl, Open Movie Database, etc.)
Populate data into a database
Build an API with following components:
Endpoints
Methods
Status Codes
README with documentation of API
Bonus: Unit and integration tests


WordApi
=======

This is a Rest API that returns the total count of words from input.

Step 1:
Install python Requirements:

For python 2.x run::
    pip install -r requirements.txt

for python 3.x run::
    pip3 install -r requirements.txt Run "myflaskapp.py" to start the Flask Web Server

Step 2:
Enter input into URL in the form::

    http://127.0.0.1:5000/word_count?words=my sentence to count

This Rest API uses the Flask framework and was written in python version 3.6.4

The requirements.txt can be used to install required packages through pip.


Answers to your Questions
-------------------------

How you would deal with DNS not working?
If DNS is not working, I would have send requests to the
IP address of the server my application is hosted on instead of using DNS. Also, this fix could be automated in python
and we could include automated DNS trouble shooting such as clearing DNS cache, ping ip, etc.

How would you deal with the website encountering timeout?
If many users are experiencing timeout issues, the server this application
is hosted on should restart itself and team notified. A timeout of 100 seconds could be set and
error code should be sent to the user and our team (logs).

Monitoring and testing should help the team be alerted of these issues early to determine
if this is an issue with the client or server side.


Automate music lyrics analytics Rest api with SQL alchemy
Runs pandas statistics on music lyrics

fault tolerant DNS and timeout automation

security: Oauth(pingID same use in both places) SAML TLS JWT

Docker?