import requests, json

url1 = "http://127.0.0.1:5000/get-restaurant-data"
url2 = "http://127.0.0.1:5000/get-chef-data"
url3 = "http://127.0.0.1:5000/get-foodie-data"

payload = {
    "RestID": "Rest001",
}

payload1 = {
    "CustID": "Cust001",
}

payload3 = {
    "ChefID": "Chef001",
}


res = requests.post(url3,data=json.dumps(payload1), headers={'Content-Type' : 'application/json'})

print(res.content)