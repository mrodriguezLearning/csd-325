import requests
import json

response = requests.get("https://anapioficeandfire.com/api/houses/378") 


# create a formatted string of the Python JSON object
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())