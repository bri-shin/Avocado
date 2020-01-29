'''
Backend server for Avocado - HackNY 2019 

Made by abdullah zameek, brian shin, yung ju rick kim and amber li
'''

# Flask Imports
import flask
from flask import request
from flask_cors import CORS

# Firebase Imports
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# Python Import
import requests
import json

# Starting Up

app = flask.Flask(__name__)
CORS(app)

cred = credentials.Certificate(
    "tofu-hack-firebase-adminsdk-c151z-fe8bbb6fc3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tofu-hack.firebaseio.com/'
})

RESTAURANTS = db.reference('restaurants')
FOODIES = db.reference('foodies')
CHEFS = db.reference('chefs')
RSVP = db.reference('RSVP')
MATCHED = db.reference('matched')

########### RESTAURANT FUNCTIONS ##############

@app.route("/get-all-restaurants", methods=['GET'])
def getAllRestaurants():
    response = RESTAURANTS.get()
    return(json.dumps(response))

@app.route("/get-all-chefs", methods=['GET'])
def getAllChefs():
    response = CHEFS.get()
    return(json.dumps(response))


@app.route("/get-all-foodies", methods=['GET'])
def getAllFoodies():
    response = FOODIES.get()
    return(json.dumps(response))

@app.route("/get-restaurant-data", methods=['POST'])
def getRestaurantData():
    RestID = request.json['RestID']
    response = RESTAURANTS.order_by_child('RestCORS(app)ID').equal_to(RestID).get()
    for key, value in response.items():
        print(key)
        print(value)
    return(value)

@app.route("/create-restaurant", methods=['POST'])
def createRestaurant():
    RestID = request.json['RestID']
    Name = request.json['Name']
    Cuisine = request.json['Cuisine']
    History = request.json['History']
    Occ_Limit = request.json['Occupancy Limit']
    Open_Sch = request.json['Open Schedule']
    Rent_Rate = request.json['Rental Rate']
    Position = request.json['position']


    payload = {
        "Cuisine": Cuisine,
        "History" : History,
        "Name" : Name,
        "Occupancy Limit" : Occ_Limit,
        "Open Schedule" : Open_Sch,
        "Rental Rate" : Rent_Rate,
        "RestID" : RestID,
        "position": Position
    }

    restaurant = RESTAURANTS.push(payload)
    return(RestID)

########### END OF RESTAURANT FUNCTIONS ###########


########## CHEF FUCTIONS #######################
@app.route("/get-chef-data", methods=['POST'])
def getChefData():
    ChefID = request.json['ChefID'] 
    response = CHEFS.order_by_child('ChefID').equal_to(ChefID).get()
    for key, value in response.items():
        print(value)
    return(value)

########### END OF CHEF FUNCTIONS ###########


########## FOODIE FUCTIONS #######################
@app.route("/get-foodie-data", methods=['POST'])
def getFoodieData():
    FoodieID = request.json['CustID'] 
    response = FOODIES.order_by_child('CustID').equal_to(FoodieID).get()
    for key, value in response.items():
        print(value)
    return(value)

@app.route("/add-favorite", methods=['POST'])
def addFavorite():
    favorite_chef = request.json['ChefID']
    foodieID = request.json['CustID']
    foodie = FOODIES.order_by_child('CustID').equal_to(foodieID).get()
    print(foodie)
    foodie['1']['Favorites'].append(favorite_chef)
    FOODIES.update({
        '1': foodie['1']
    })
    # print("running add favorite")
    # print(type(FOODIES.child))
    return favorite_chef


########### END OF FOODIE FUNCTIONS ###########


########## GOOGLE MAPS FUNCTIONS #######################

########### END OF GOOGLE MAPS FUNCTIONS ###########


########## MISC FUCTIONS #######################
@app.route("/create-match", methods=['POST'])
def createMatch():
    match = request.json
    create_match = MATCHED.push(match)
    return create_match

@app.route("/get-match-by-restid", methods=['POST'])
def getMatchByRestID():
    RestID = request.json['RestID'] 
    response = MATCHED.order_by_child('RestID').equal_to(RestID).get()
    return(dict(response.items()))

@app.route("/get-match-by-chefid", methods=['POST'])
def getMatchByChefID():
    ChefID = request.json['ChefID'] 
    response = MATCHED.order_by_child('ChefID').equal_to(ChefID).get()
    return (dict(response.items()))

@app.route("/get-pending-matches-by-chefid", methods=['POST'])
def getPendingMatchesByChefID():
    ChefID = request.json['ChefID'] 
    count = 0
    returnDict = {}
    response = MATCHED.order_by_child('ChefID').equal_to(ChefID).get()
    for key, value in response.items():
         if(value['Status'] == 0):
             returnDict[count] = value
             count+=1
    return(returnDict)

@app.route("/get-pending-matches-by-restid", methods=['POST'])
def getPendingMatchesByRestID():
    RestID = request.json['RestID'] 
    count = 0
    returnDict = {}
    response = MATCHED.order_by_child('RestID').equal_to(RestID).get()
    for key, value in response.items():
         if(value['Status'] == 0):
             returnDict[count] = value
             count+=1
    return(returnDict)

@app.route("/get-accepted-matches-by-restid", methods=['POST'])
def getAcceptedMatchesByRestID():
    RestID = request.json['RestID'] 
    count = 0
    returnDict = {}
    response = MATCHED.order_by_child('RestID').equal_to(RestID).get()
    for key, value in response.items():
         if(value['Status'] == 1):
             returnDict[count] = value
             count+=1
    return(returnDict)

@app.route("/get-accepted-matches-by-chefid", methods=['POST'])
def getAcceptedMatchesByChefID():
    ChefID = request.json['ChefID'] 
    count = 0
    returnDict = {}
    response = MATCHED.order_by_child('ChefID').equal_to(ChefID).get()
    for key, value in response.items():
         if(value['Status'] == 1):
             returnDict[count] = value
             count+=1
    return(returnDict)

@app.route("/get-rejected-matches-by-chefid", methods=['POST'])
def getRejectedMatchesByChefID():
    ChefID = request.json['ChefID'] 
    count = 0
    returnDict = {}
    response = MATCHED.order_by_child('ChefID').equal_to(ChefID).get()
    for key, value in response.items():
         if(value['Status'] == 2):
             returnDict[count] = value
             count+=1
    return(returnDict)

@app.route("/get-rejected-matches-by-restid", methods=['POST'])
def getRejectedMatchesByRestID():
    RestID = request.json['RestID'] 
    count = 0
    returnDict = {}
    response = MATCHED.order_by_child('RestID').equal_to(RestID).get()
    for key, value in response.items():
         if(value['Status'] == 2):
             returnDict[count] = value
             count+=1
    return(returnDict)

########### END OF MISC FUNCTIONS ###########
