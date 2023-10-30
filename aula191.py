import requests

# http:// -> porta 80
# https:// -> porta 443


url = 'http://localhost:8000/'
response = requests.get(url)
print(response)

#print(response)
#print(response.headers)
#print(response.text)
#print(response.json())