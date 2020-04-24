users = {}
data = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct",
        "nov","dec"]
import jsonlib,http.client
import datetime
connection = http.client.HTTPConnection('18.217.240.250', 80)
connection.connect()
connection.request('GET', '/parse/classes/LANDTUSAGE', '', {
       "X-Parse-Application-Id": "0bfc45c8be2b2e93f018041ff949fe6d09233c0a",
       "X-Parse-REST-API-Key": "avbs"
     })
result = jsonlib.loads(connection.getresponse().read())
print(result)
'''for key,values in result.items():
    for i in values:
        users[i["objectId"]] = {"deviceID":i["deviceID"],"kitchen":0,"bathroom":0,"others":0,
                                "week":[0,0,0,0,0,0,0],"monthly":
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                                 ,0,0,0,0,0,0,0,0,0,0],"yearly":
                                {'jan': [0], 'feb': [0], 'mar': [0], 'apr': [0],
'may': [0],'jun': [0],'jul': [0], 'aug': [0], 'sep': [0], 'oct': [0],
                                 'nov': [0], 'dec': [0]}}
for keys,values in users.items():
    for key,value in values.items():
        if key=="kitchen" or key=="bathroom" or key=="others":
            value = 0
        elif key=="week" or key=="monthly":
            value.pop(0)
            value.append(5)
print(users)'''
for keys,values in result.items():
    for i in values:
        users[i["objectId"]] = {"deviceID":i["deviceID"],"kitchen":i["Kitchen"],
                              "bathroom":i["Bathroom"],"others":i["Misc"],
                              "week":i["week"],"yearly":i["yearly"][0],
                              "monthly":i["monthly"]}
              
"""for key,value in users.items():
    for keys,values in value.items():
        if keys=="week" or keys=="monthly":
            for i in range(len(values)):
                values[i] = float(values[i])
        elif keys=="yearly":
            for keyed,valued in values.items():
                valued[0] = float(valued[0])"""
            
#print(users)           
        

