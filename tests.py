from sklearn.metrics import accuracy_score as acc
import pandas as pd
import joblib
import catboost
from appcp1 import data_check

# check if data is ok
def test_data_check_posititve(datapath):
  assert data_check(datapath) == 0

# check if data is NOT ok and there are missing columns 
def test_data_check_negative():
  assert data_check('testdata/test_neg.csv') == ['battery_power', 'px_height', 'px_width', 'ram']

# check if model prediction results
def test_pred(datapath, modelpath):
  df = pd.read_csv(datapath)
  df_X = df.loc[:,['battery_power', 'px_height', 'px_width', 'ram']].values
  with open(modelpath, 'rb') as f:
    model = joblib.load(f)
  preds = model.predict(df_X)
  assert acc(df.price_range.values, preds) >= 0.8
