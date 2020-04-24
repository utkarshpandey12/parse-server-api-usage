#########  This returns daily consumption   ############
#########  of water across kitchen,bathroom ############
#########  and misc. for all the users      ############

def daily_usage():
    #modules
    import json, requests
    #Initialising total usage variables
    kitchen= 0.0
    bathroom = 0.0
    others = 0.0
    total = 0.0
    #Server Auth parameters
    PARSE_HOSTNAME = 'http://18.217.240.250:80'
    PARSE_APP_ID = '0bfc45c8be2b2e93f018041ff949fe6d09233c0a'
    PARSE_REST_API_KEY = 'avbs'
    #table for usage
    endpoint = '/parse/classes/LANDTUSAGE'
    headers = {"X-Parse-Application-Id": PARSE_APP_ID, 
           "X-Parse-REST-API-Key": PARSE_REST_API_KEY, 
           "Content-Type": "application/json"}
    r = requests.get(PARSE_HOSTNAME + endpoint, headers=headers)
    output = dict(r.json())
    #removing umwanted keys
    for keys,values in output.items():
        for i in values:
            i.pop("objectId")
            i.pop("createdAt")
            i.pop("updatedAt")
            i.pop("deviceID")
            i.pop("week")
            i.pop("monthly")
            i.pop("yearly")       
    #Aggregating kitchen,bathroom etc usage for all users        
    for key,value in output.items():
        for j in value:
            kitchen += (int(j["Kitchen"]))/1000
            bathroom += (int(j["Bathroom"]))/1000
            others += (int(j["Misc"]))/1000
    total = kitchen+bathroom+others    
    return {"daily_results":[{"kitchen":kitchen,"bathroom":bathroom,"Misc":others,"total":total}]}        
daily_usage()
