'''
Backend server for Avocado - HackNY 2019 
'''

# Flask Imports
from flask
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
    "seec-pennapps-firebase-adminsdk-7zh6f-41c2a963c2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seec-pennapps.firebaseio.com/'
})

########### RESTAURANT FUNCTIONS ##############


########### END OF RESTAURANT FUNCTIONS ###########


########## CHEF FUCTIONS #######################


########### END OF CHEF FUNCTIONS ###########


########## FOODIE FUCTIONS #######################

########### END OF FOODIE FUNCTIONS ###########


########## GOOGLE MAPS FUNCTIONS #######################

########### END OF GOOGLE MAPS FUNCTIONS ###########


########## MISC FUCTIONS #######################

########### END OF MISC FUNCTIONS ###########
