import requests
import json

URL = 'http://localhost:9090'

def getUserBandwith():
    response = requests.get(URL + '/api/v1/query?query=up')
    print(response.json()['data']['result'][0]['value'])