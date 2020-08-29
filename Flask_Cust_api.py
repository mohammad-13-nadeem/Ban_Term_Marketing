# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:46:28 2020

@author: 91989
"""


from flask import Flask , request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('forest2.pkl' , 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict' , methods = ['GET'])
def predict():
    
    
    """
    Let's predict the potential Term Subscription Customers
    This is using docstrings for specifications.
    ---
    
    parameters:
        - name : age
          in : query
          type : number
          required : true
        - name : job
          in : query
          type : number
          required : true
        - name : marital
          in : query
          type : number
          required : true
        - name: education
          in : query
          type : number
          required : true
        - name : balance
          in : query
          type : number
          required : true
        - name : loan
          in : query
          type : number
          required : true
        - name : poutcome
          in : query
          type : number
          required : true
    responses:
          200:
            description : The Output Values
            
    """
    
    age = request.args.get('age')
    job = request.args.get('job')
    marital = request.args.get('marital')
    education = request.args.get('education')
    balance = request.args.get('balance')
    loan = request.args.get('loan')
    poutcome = request.args.get('poutcome')
    
    prediction = classifier.predict([[age,job,marital,education,balance,loan,poutcome]])
    print(prediction)
    return "Hello , the answer is " + str(prediction)

if __name__ == '__main__' : 
    app.run()
    
   
        
    
    