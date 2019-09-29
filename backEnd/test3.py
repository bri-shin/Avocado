import requests, json

url1 = "http://127.0.0.1:5000/get-restaurant-data"
url2 = "http://127.0.0.1:5000/get-chef-data"
url3 = "http://127.0.0.1:5000/get-foodie-data"
url4 = "http://127.0.0.1:5000/create-restaurant"

payload = {
    "RestID": "Rest001",
}

payload1 = {
    "CustID": "Cust001",
}

payload3 = {
    "ChefID": "Chef001",
}

payload4 = {
    "Cuisine" : [ "Japanese", "Fusion", "Korean" ],
    "position":{
      "lat": 4.55661151,
      "lng": 5.56615511
    },
    "Name" : "HalalKart",
    "History" : ["Chef00"],
    "Occupancy Limit" : 40,
    "Open Schedule" : {
      "Friday" : "7-8pm",
      "Monday" : "",
      "Saturday" : "9-11am",
      "Sunday" : "",
      "Thursday" : "3-5pm",
      "Tuesday" : "10-12pm",
      "Wednesday" : "12-1pm"
    },
    "Rental Rate" : 50,
    "RestID" : "Rest004"
  }

res = requests.post(url1,data=json.dumps(payload), headers={'Content-Type' : 'application/json'})
res2 = requests.post(url2,data=json.dumps(payload3), headers={'Content-Type' : 'application/json'})
res3 = requests.post(url3,data=json.dumps(payload1), headers={'Content-Type' : 'application/json'})
res4 = requests.post(url4,data=json.dumps(payload4), headers={'Content-Type' : 'application/json'})

print(res.content)
print()
print(res2.content)
print()
print(res3.content)
print()
print(res4.content)
print()

