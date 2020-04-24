import jsonlib,http.client
connection = http.client.HTTPConnection('18.217.240.250', 80)
connection.connect()
connection.request('GET', '/parse/classes/water_consumption', "", {
       "X-Parse-Application-Id": "0bfc45c8be2b2e93f018041ff949fe6d09233c0a",
       "X-Parse-REST-API-Key": "avbs",
       "Content-Type": "application/json"
     })
result = jsonlib.loads(connection.getresponse().read())
print(result)

        
