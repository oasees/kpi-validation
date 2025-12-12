import requests
import numpy as np
from requests.adapters import HTTPAdapter, Retry
import os

s = requests.Session()


data = np.load('iris_data.npy')
node_ip = os.environ.get("NODE_IP")
model_port = os.environ.get("MODEL_PORT")

retries = Retry(total=100, backoff_factor=0.01)
s.mount('http://', HTTPAdapter(max_retries=retries))

response = s.post(f'http://{node_ip}:{model_port}/predict', 
                json={'data': data.tolist()})
y_pred = response.json()['predictions']


y_true = np.load('iris_target.npy')


accuracy = sum(1 for true, pred in zip(y_true, y_pred) if true == pred) / len(y_true)
print(f"Accuracy: {accuracy:.4f}")
print(y_pred)
