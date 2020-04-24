######## This returns the last 30 days usage  ##########
######## for every user for a given project  ##########

def monthly_usage():
    #modules
    import json, requests
    #Server Auth parameters
    PARSE_HOSTNAME = 'http://18.217.240.250:80'
    PARSE_APP_ID = '0bfc45c8be2b2e93f018041ff949fe6d09233c0a'
    PARSE_REST_API_KEY = 'avbs'
    PARSE_MASTER_KEY = "f75085d79e3b1be6c900daa39df56dabf28ca435"
    #table for project 
    endpoint = '/parse/classes/LANDTUSAGE'
    headers = {"X-Parse-Application-Id": PARSE_APP_ID, 
           "X-Parse-REST-API-Key": PARSE_REST_API_KEY, 
           "Content-Type": "application/json",
             "X-Parse-Master-Key": PARSE_MASTER_KEY  }
    r = requests.get(PARSE_HOSTNAME + endpoint, headers=headers)
    output = dict(r.json())
    #cleaning unwanted columns
    for keys,values in output.items():
        for i in values:
            del i["createdAt"]
            del i["updatedAt"]
            del i["objectId"]
            del i["Misc"]
            del i["Kitchen"]
            del i["Bathroom"]
            del i["yearly"]
            del i["week"]
    print(output)        
monthly_usage()
