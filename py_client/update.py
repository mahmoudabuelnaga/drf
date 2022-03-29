import requests

endpoint = "http://localhost:8000/api/products/1/update"

data = {
    "title":"Mahmoud 5145151",
    "price": 65241.45
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
