# Making a quiz Python program with open trivia DB
# api call: https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple

import requests, json, pprint

req = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
print(req.status_code)              # is 200 which means we all good
print(req.text)                     # content of our API call
print(type(req.text))               # JSON text stored as a String, now we need to parse this - using module json

req_json = json.loads(req.text)     # turn our String text into a Python dictionary
print(type(req_json))               # type went from str to dict

pprint.pprint(req_json)             # pprint is a module that makes printing JSON easier instead of referring to chrome
print("\n")

# Actually making sense of the JSON - remember that we have a DICTIONARY.
print(req_json)                                 # the entire thing
print(req_json["response_code"])                # grabbing key from our dictionary (we have two, response_code and category)
print(req_json["results"])                      # grabbing our more relevant key, RESULTS, which is a LIST
print(req_json["results"][0]["category"])

# earlier we did JSON --> Python dictionary, now let's do the reverse
Chris = { "Name" : " Christopher", "Age" : 20 }
Chris_json = json.dumps(Chris)
print(type(Chris))
print(type(Chris_json))

# completed quiz program will be in test13.py