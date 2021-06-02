
import http.client
import json #transform obtained strings into dictionaries

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
#if we just apply this, we'll just obtain (ping:1, server is working)
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
#print(response.read()) #we obtain b'{"ping":1}'; b:the info been streamed is in bytes, we need to change it by .decode
print(response.status,response.reason)
answer_decoded = response.read().decode()
print(type(answer_decoded), answer_decoded)
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)
if dict_response["ping"] == 1:
    print("PING OK!! The database is running")
else:
    print("The database is down")
#:id = id of the gene sent to server