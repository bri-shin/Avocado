import requests
import json

url1 = "http://127.0.0.1:5000/get-pending-matches-by-chefid"
url2 = "http://127.0.0.1:5000/get-chef-data"
url3 = "http://127.0.0.1:5000/get-foodie-data"
all_rest_url = "http://127.0.0.1:5000/get-all-restaurants"
match_url = "http://127.0.0.1:5000/create-match"
fav_url = "http://127.0.0.1:5000/add-favorite"

url4 = "http://127.0.0.1:5000/get-match-by-chefid"
url5= "https://avocadohackny.appspot.com/get-all-restaurants"


payload1 = {
    "RestID": "Rest001",
}

payload2 = {
    "ChefID": "Chef001",
}

payload3 = {
    "CustID": "Cust001",
}

match_info = {
    'ChefID': 'Chef001', 'Cuisine': ['Korean'], 'Description': "Kimchi", 'Ingredients': ['Cabbage'], 'RestID': 'Rest001', 'Schedule': {'Friday': '7-8pm', 'Monday': '', 'Saturday': '', 'Sunday': '5-6pm', 'Thursday': '', 'Tuesday': '', 'Wednesday': ''}, 'Status': 1
}

payload4 = {
    "ChefID" : "Chef001"
}


res1 = requests.post(url1, data=json.dumps(payload4), headers={'Content-Type': 'application/json'})


# res5 = requests.get(url5,headers={'Content-Type': 'application/json'})

# res2 = requests.post(url2, data=json.dumps(payload2), headers={
#                      'Content-Type': 'application/json'})
# res3 = requests.post(url3, data=json.dumps(payload3), headers={
#                      'Content-Type': 'application/json'})

# match_res = requests.post(match_url, data=json.dumps(match_info), headers={
#     'Content-Type': 'application/json'})

print(res1.content)
print("\n")
# print(res2.content)
# print("\n")
# print(res3.content)
# print("\n\n\n")
# print(all_rest.content)


