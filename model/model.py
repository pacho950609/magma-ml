from training.training import varValues, resValues
from dataProcessing.dataProcessing import getThroughputRange, getThroughput
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from dataAnalysis.dataAnalysis import processPrediction, processPredictionRange
from sklearn.linear_model import LinearRegression

pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

def trainModel():
    X_train, X_test, y_train, y_test = train_test_split(varValues, resValues, random_state=0)
    pipe.fit(X_train, y_train)
    res = accuracy_score(pipe.predict(X_test), y_test)
    print(res)

def runModel():
    trainModel()
    for x in range(100):
        throughputRange = getThroughput()
        if len(throughputRange) > 0:
            res = pipe.predict([throughputRange])[0]
            print('prediction:')
            print(res)
            processPrediction(res)
        time.sleep(10)

def runModelRange():
    trainModel()
    for x in range(200):
        throughputRange = getThroughputRange()
        if len(throughputRange) > 0:
            timeSerie = list(map(lambda throughput: [throughput[0]],throughputRange))
            throughput = list(map(lambda throughput: throughput[1],throughputRange))
            reg = LinearRegression().fit(timeSerie, throughput)
            maxTime = timeSerie[len(throughputRange) - 1][0]
            predictedFutureSeconds = 50
            predictedTime = maxTime + predictedFutureSeconds
            prediction = reg.predict([[predictedTime]])
            print('prediction:')
            print(prediction)
            processPredictionRange(prediction)
        time.sleep(10)