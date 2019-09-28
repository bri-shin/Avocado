import requests, json

url1 = "http://127.0.0.1:5000/get-restaurant-data"

payload = {
    "RestID": "Rest001",
}

res = requests.post(url1,data=json.dumps(payload), headers={'Content-Type' : 'application/json'})

print(res.content)