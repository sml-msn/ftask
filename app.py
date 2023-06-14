import streamlit as st
import joblib 
import pandas as pd
from os import listdir
from os.path import isfile, join


def data_preps(datapath):
    df = pd.read_csv(datapath)
    df = df.loc[:,['battery_power', 'px_height', 'px_width', 'ram']]
    return df.values

def save_button(preds):
    st.download_button(
        label="Сохранить как CSV",
        data=pd.DataFrame(preds).to_csv(index=True),
        file_name='predictions.csv',
        mime='text/csv',
    )

with open('models/cat_clf_mdl.joblib', 'rb') as f:
    model = joblib.load(f)
    
st.title('Что почем?')
data = st.file_uploader("Upload file", type=['csv'])

if data:
    if st.button('Подтвердить'):
        preds = model.predict(data_preps(data))
        st.write(preds)
        save_button(preds)

else:
    filenames = [f for f in listdir('datasets/') if isfile(join('datasets/', f))]
    option = st.selectbox('Выбрать из доступных:',options=filenames)
    if st.button('Подтвердить выбор'):
        st.write(join('datasets/', option))
        preds = model.predict(data_preps(join('datasets/', option)))
        st.write(preds)
        save_button(preds)

