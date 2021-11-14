import requests
import json
import time

URL = 'http://localhost:9090'
OutDataUsageQuery = 'sum(ue_reported_usage{IMSI="IMSI901700100001111",direction="up"})'
OutThroughputQuery = 'avg(rate(ue_reported_usage{IMSI="IMSI901700100001111",direction="up"}[5m]))'


def transformThroughput(throughputRange):
    return list(map(lambda throughput: throughput[1], throughputRange))


def getThroughputRange():
    end = time.time()
    start = end - 180
    path = URL + '/api/v1/query_range?query='+ OutThroughputQuery +'&start='+ str(start) + '&end='+ str(end) +'&step=10'
    print('Throughput path: ' + path)
    response = requests.get(path)
    throughputRange = response.json()['data']['result'][0]['values']
    print('Throughput response:')
    print(throughputRange)
    transformedThroughput = transformThroughput(throughputRange)
    print('Transformed throughput:')
    print(transformedThroughput)