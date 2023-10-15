
from pkgutil import get_importer

import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in: #wb=write, rb=read
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
   dv = pickle.load(f_in)

#def train():
customer = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0,1]
print(y_pred)

  #result = {
  #   "prob": float(y_pred)
  #}
  #print(result)  
  #return result