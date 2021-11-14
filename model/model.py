from training.training import varValues, resValues
from dataProcessing.dataProcessing import getThroughputRange
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

def trainModel():
    print(varValues)
    print(resValues)

    # load the iris dataset and split it into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(varValues, resValues, random_state=0)

    # fit the whole pipeline
    pipe.fit(X_train, y_train)


    # we can now use it like any other estimator
    res = accuracy_score(pipe.predict(X_test), y_test)
    print(res)

def runModel():
    trainModel()
    print(pipe.predict([[200,150,100]]))
    for x in range(6):
        getThroughputRange()
        time.sleep(7)