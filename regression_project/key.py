import json


with open('/Users/jpxmaestas/Desktop/personal/api/kaggle.json', 'r') as f:
    data = json.load(f)

# Now 'data' contains the JSON data as a Python dictionary or list
print(data)
