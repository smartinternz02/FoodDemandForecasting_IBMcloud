import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
def connect(prediction_parameters):
    if ('' in prediction_parameters or ' ' in prediction_parameters):
        return
    API_KEY = "cEO6LcRR6DprEzUmw03tRsl5rirCEwg0Lj9VySBw8Rhl"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine',
                                             'city_code', 'region_code', 'category'], "values": [prediction_parameters]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8cd0f51b-6229-4f50-9e4c-fc533bc0ef0c/predictions?version=2022-01-20', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    prediction_val = response_scoring.json()['predictions'][0]['values'][0][0]
    print(f"Number of Orders = {round(prediction_val,1)}")
    return round(prediction_val,1)