
import requests

url = 'http://localhost:9696/predict_flask'

client = {"job": "retired", "duration": 445, "poutcome": "success"}

requests.post(url, json=client)

requests.post(url, json=client).json()

response = requests.post(url, json=client).json()
print(response)