# Module: Requests (making HTTP requests in Python): python3 -m pip install requests to install to Python 3 directory

# The Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers.
# HTTP works as a request-response protocol between a client and server.
# A web browser may be the client, and an application on a computer that hosts a web site may be the server.
# Example: A client (browser) submits an HTTP request to the server; then the server returns a response to the client.
# The response contains status information about the request and may also contain the requested content.

# HTTP Methods
# GET
# POST
# PUT
# HEAD
# DELETE
# PATCH
# OPTIONS

import requests
get_test = requests.get("https://google.ca")    # you get the html css js code of if you were to navigate to that page
print(get_test.status_code)                     # status code 200 - successful, 403 - forbidden, 404 - not found
print(get_test.headers)
# print(get_test.text)                          # all the code of that homepage. not useful, but we will parse it
                                                # our browser intreprets this and generate something readable

# Making a quiz Python app using open trivia db. generate a link; going to it gives you the data in a JSON format
# https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple - our api request
# JSON - JavaScript object notation, a JavaScript object is like a Python dictionary, has all the info for us
# re: test12.py