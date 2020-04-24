import jsonlib,http.client
import datetime
connection = http.client.HTTPConnection('18.217.240.250', 80)
connection.connect()
connection.request('GET', '/parse/schemas', '', {
       "X-Parse-Application-Id": "0bfc45c8be2b2e93f018041ff949fe6d09233c0a",
       "X-Parse-REST-API-Key": "avbs",
       "X-Parse-Master-Key": "f75085d79e3b1be6c900daa39df56dabf28ca435"
     })
result = jsonlib.loads(connection.getresponse().read())
print(result)
