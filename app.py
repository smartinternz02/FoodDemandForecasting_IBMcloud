import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask, request, render_template
from connect_to_deployed_model import connect


app = Flask(__name__, template_folder="templates")

@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

@app.route('/home', methods = ["GET"])
def about():
    return render_template('index.html')

@app.route('/upload.html', methods = ["GET"])
def page():
    return render_template('upload.html')

@app.route('/pred', methods = ["POST","GET"])
def predict():
    
    homepageFeatured = request.form['homepageFeatured']
    if (homepageFeatured.casefold() == 'yes'):
        homepageFeatured = 1
    elif (homepageFeatured.casefold() == 'no'):
        homepageFeatured = 0
    else:
        prediction_val = "Invalid value provided for 'Homepage Featured'"
        
        
    emailer = request.form['email']
    if (emailer.casefold() == 'yes'):
        emailer = 1
    elif (emailer.casefold() == 'no'):
        emailer = 0
    else:
        prediction_val = "Invalid value provided for 'Emailer for Promotion'"
        
        
    oparea = request.form['oparea']
    try:
        oparea = float(oparea)
    except:
        prediction_val = "Invalid value provided for 'Op Area'"
    
    
    
    cuisine = request.form['cuisine']
    if (cuisine.casefold() == 'continental'):
        cuisine = 0
    elif (cuisine.casefold() == 'indian'):
        cuisine = 1
    elif (cuisine.casefold() == 'italian'):
        cuisine = 2
    elif (cuisine.casefold() == 'thai'):
        cuisine = 3
    else:
        prediction_val = "Invalid value provided for 'Cuisine'"
    
    citycode = request.form['citycode']
    try:
        citycode = float(citycode)
    except:
        prediction_val = "Invalid value provided for 'City Code'"    
    
    regioncode = request.form['regioncode']
    try:
        regioncode = float(regioncode)
    except:
        prediction_val = "Invalid value provided for 'Region Code'"
    
    category = request.form['category']
    if (category.casefold() == 'beverages'):
        category = 0
    elif (category.casefold() == 'biryani'):
        category = 1
    elif (category.casefold() == 'desert'):
        category = 2
    elif (category.casefold() == 'extras'):
        category = 3
    elif (category.casefold() == 'fish'):
        category = 4
    elif (category.casefold() == 'other snacks'):
        category = 5
    elif (category.casefold() == 'pasta'):
        category = 6
    elif (category.casefold() == 'pizza'):
        category = 7
    elif (category.casefold() == 'rice bowl'):
        category = 8
    elif (category.casefold() == 'salad'):
        category = 9
    elif (category.casefold() == 'sandwich'):
        category = 10
    elif (category.casefold() == 'seafood'):
        category = 11
    elif (category.casefold() == 'soup'):
        category = 12
    else:
        prediction_val = "Invalid value provided for 'Category'"

    if ('Invalid' in prediction_val):
        return render_template('upload.html', prediction_val = prediction_val)
    
    print("[INFO] Loading Model...")
    prediction_val = connect([homepageFeatured, emailer, oparea, cuisine, citycode, regioncode, category])
    #with open('fdemand.pkl', 'rb') as file:
    #    model = pickle.load(file)
    print("[INFO] Model Loaded Successfully")
    #temp = request.form.values()
    
        

    
    #print([x for x in temp])
    #input_features = [float(x) for x in request.form.values()]
    #features_value = [np.array(input_features)]
    #print(f'features value = {features_value}')

    #features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine', 'city_code',
    #'region_code', 'category']
    #prediction = model.predict(features_value)
    #global output
    #output = str(round(prediction[0],2))
    #print(output)
    return render_template('upload.html', prediction_val = prediction_val)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)