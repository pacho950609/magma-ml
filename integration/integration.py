import requests
import json

URL = 'http://localhost:5000'

def upgradeBandwidthCall():
    response = requests.get(URL + '/bandwidth/upgrade')


def downgradeBandwidthCall():
    response = requests.get(URL + '/bandwidth/downgrade')