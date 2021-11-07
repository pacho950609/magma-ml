from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import requests

# create a pipeline object
pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)

# print(X,y)
print(len(X))
print(len(y),y)

response = requests.get('http://localhost:9090/api/v1/query?query=up')
print('aca')
print(response.json()['data']['result'][0]['value'])
print('aca2')
response2 = requests.get('https://localhost:9443/magma/v1/lte/uniandes_network_01/subscribers/IMSI901700100001113',cert=('../../admin_operator.pem','../../admin_operator.pem'),verify=False)
print(response2.json())