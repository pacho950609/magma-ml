from training.training import varValues, resValues
from dataProcessing.dataProcessing import getThroughputRange
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from integration.integration import upgradeBandwidthCall

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
    for x in range(6):
        throughputRange = getThroughputRange()
        res = pipe.predict([throughputRange])[0]
        print('prediction:')
        print(res)
        if(res == 0):
            print('Call upgrade bandwidth')
            upgradeBandwidthCall()
        
        time.sleep(7)