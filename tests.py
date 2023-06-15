from sklearn.metrics import accuracy_score as acc
import pandas as pd
import joblib
import catboost

def test_pred(datapath, modelpath):
  df = pd.read_csv(datapath)
  df_X = df.loc[:,['battery_power', 'px_height', 'px_width', 'ram']].values
  with open(modelpath, 'rb') as f:
    model = joblib.load(f)
  preds = model.predict(df_X)
  assert acc(df.price_range.values, preds) >= 0.8