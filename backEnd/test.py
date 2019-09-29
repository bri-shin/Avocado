import requests
import json

url1 = "http://127.0.0.1:5000/get-restaurant-data"
url2 = "http://127.0.0.1:5000/get-chef-data"
url3 = "http://127.0.0.1:5000/get-foodie-data"
<<<<<<< HEAD
match_url = "http://127.0.0.1:5000/create-match"
=======
>>>>>>> e09d4c2d1e0e0c2584e59f3a39415ba7b3f58eca

payload1 = {
    "RestID": "Rest001",
}

<<<<<<< HEAD
payload2 = {
    "ChefID": "Chef001",
}

payload3 = {
    "CustID": "Cust001",
}

match_info = {
    'ChefID': 'Chef001', 'Cuisine': ['Korean'], 'Description': "Spicy Tteokbokki", 'Ingredients': ['ricecake'], 'RestID': 'Rest002', 'Schedule': {'Friday': '7-8pm', 'Monday': '', 'Saturday': '', 'Sunday': '5-6pm', 'Thursday': '', 'Tuesday': '', 'Wednesday': ''}, 'Status': 'True'
}

res1 = requests.post(url1, data=json.dumps(payload1), headers={
                     'Content-Type': 'application/json'})
res2 = requests.post(url2, data=json.dumps(payload2), headers={
                     'Content-Type': 'application/json'})
res3 = requests.post(url3, data=json.dumps(payload3), headers={
                     'Content-Type': 'application/json'})

match_res = requests.post(match_url, data=json.dumps(match_info), headers={
    'Content-Type': 'application/json'
})

print(res1.content)
print("\n")
print(res2.content)
print("\n")
print(res3.content)

=======
payload1 = {
    "CustID": "Cust001",
}

payload3 = {
    "ChefID": "Chef001",
}


res = requests.post(url3,data=json.dumps(payload1), headers={'Content-Type' : 'application/json'})
>>>>>>> e09d4c2d1e0e0c2584e59f3a39415ba7b3f58eca

