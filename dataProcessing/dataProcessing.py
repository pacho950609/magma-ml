import requests
import json
import time

URL = 'http://localhost:9090'
OutDataUsageQuery = 'sum(ue_reported_usage{IMSI="IMSI901700100001111",direction="up"})'
OutThroughputQuery = 'avg(rate(ue_reported_usage{IMSI="IMSI901700100001111",direction="up"}[5m]))'



def getThroughputRange():
    end = time.time()
    start = end - 180
    path = URL + '/api/v1/query_range?query='+ OutThroughputQuery +'&start='+ str(start) + '&end='+ str(end) +'&step=10'
    print(path)
    response = requests.get(path)
    print(response.json()['data']['result'][0]['values'])