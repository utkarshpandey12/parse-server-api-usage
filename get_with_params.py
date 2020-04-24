#get with params
import json, requests
PARSE_HOSTNAME = 'http://18.217.240.250:80'
PARSE_APP_ID = '0bfc45c8be2b2e93f018041ff949fe6d09233c0a'
PARSE_REST_API_KEY = 'avbs'
endpoint = '/parse/classes/LANDTUSAGE'
headers = {"X-Parse-Application-Id": PARSE_APP_ID, 
           "X-Parse-REST-API-Key": PARSE_REST_API_KEY, 
           "Content-Type": "application/json"}
params = {"where":json.dumps({
       "deviceID": "0001"
     })}
r = requests.get(PARSE_HOSTNAME + endpoint,params = params, headers=headers)
print(r.json())
