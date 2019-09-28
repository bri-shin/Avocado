'''
Backend server for Avocado - HackNY 2019 
'''

# Flask Imports
import flask
from flask import request

# Firebase Imports
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# Python Import
import requests
import json

# Starting Up

app = flask.Flask(__name__)

cred = credentials.Certificate(
    "tofu-hack-firebase-adminsdk-c151z-fe8bbb6fc3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tofu-hack.firebaseio.com/'
})

RESTAURANTS = db.reference('restaurants')
FOODIES = db.reference('foodies')
CHEFS = db.reference('chefs')

########### RESTAURANT FUNCTIONS ##############


@app.route("/get-restaurant-data", methods=['POST'])
def getRestaurantData():
    RestID = request.json['RestID']
    response = RESTAURANTS.order_by_child('RestID').equal_to(RestID).get()
    for key, value in response.items():
        print(value)
    return(value)

########### END OF RESTAURANT FUNCTIONS ###########


########## CHEF FUCTIONS #######################

@app.route("/get-chef-data", methods=['POST'])
def getRestaurantData():
    ChefID = request.json['RestID']
    response = RESTAURANTS.order_by_child('RestID').equal_to(ChefID).get()
    for key, value in response.items():
        print(value)
    return(value)


########### END OF CHEF FUNCTIONS ###########


########## FOODIE FUCTIONS #######################

@app.route("/get-foodie-data", methods=['POST'])
def getRestaurantData():
    FoodieID = request.json['RestID']
    response = RESTAURANTS.order_by_child('RestID').equal_to(FoodieID).get()
    for key, value in response.items():
        print(value)
    return(value)

########### END OF FOODIE FUNCTIONS ###########


########## GOOGLE MAPS FUNCTIONS #######################

########### END OF GOOGLE MAPS FUNCTIONS ###########


########## MISC FUCTIONS #######################

########### END OF MISC FUNCTIONS ###########
