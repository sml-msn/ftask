from sklearn.metrics import accuracy_score as acc
import pandas as pd
import joblib

def test_pred(datapath, modelpath):
  df = pd.read_csv(datapath)
  df_X = df.loc[:,['battery_power', 'px_height', 'px_width', 'ram']].values
  model = joblib.load(modelpath)
  preds = model.predict(df_X)
  assert acc(df.price_range.values, df_X) >= 0.8