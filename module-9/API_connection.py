import requests

response = requests.get("https://anapioficeandfire.com/api/houses/378") 
print(response.status_code)