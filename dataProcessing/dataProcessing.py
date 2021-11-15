import requests
import json
import time

URL = 'http://localhost:9090'
OutDataUsageQuery = 'sum(ue_reported_usage{IMSI="IMSI901700100001111",direction="up"})'
OutThroughputQuery = 'avg(rate(ue_reported_usage{IMSI="IMSI901700100001111",direction="up"}[2m]))'


def transformThroughputRange(throughputRange):
    return list(map(lambda throughput: float(throughput[1]), throughputRange))

def transformThroughput(throughput):
    return [float(throughput[1])]


def getThroughputRange():
    end = time.time()
    start = end - 240
    # path = URL + '/api/v1/query_range?query='+ OutThroughputQuery +'&start='+ str(start) + '&end='+ str(end) +'&step=40'
    path = URL + '/api/v1/query?query='+ OutThroughputQuery
    print('Throughput path: ' + path)
    response = requests.get(path)

    if len(response.json()['data']['result']) == 0:
        print('saltoooooooooooooo')
        return []

    throughputRange = response.json()['data']['result'][0]['value']
    transformedThroughput = transformThroughput(throughputRange)
    print('Transformed throughput:')
    print(transformedThroughput)
    return transformedThroughput