import streamlit as st
import joblib 
import pandas as pd
from os import listdir
from os.path import isfile, join

def data_check(df):
    # df = pd.read_csv(datapath)
    necessary_columns = ['battery_power', 'px_height', 'px_width', 'ram']
    missing_columns = []
    for nec_col in necessary_columns:
        if nec_col not in df:
            missing_columns.append(nec_col)
    if missing_columns == []:
        return 0
    else:
        return missing_columns

def data_preps(df):
    # df = pd.read_csv(datapath)
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
#st.write(data)

if data:
    if st.button('Подтвердить'):
        df = pd.read_csv(data)
        missing_columns = data_check(df)
        if missing_columns == 0:
            st.write('Результаты предсказаний')
            preds = model.predict(data_preps(df))
            st.write(preds)
            save_button(preds)
        else:
            st.write('Не хватает колонок:')
            st.write(missing_columns)
            st.write('Проверьте ваш датасет.')

else:
    filenames = [f for f in listdir('datasets/') if isfile(join('datasets/', f))]
    option = st.selectbox('Выбрать из доступных:',options=filenames)
    if st.button('Подтвердить выбор'):
        df = pd.read_csv(join('datasets/', option))
        missing_columns = data_check(df)
        if missing_columns == 0:
            st.write('Результаты предсказаний для', option)
            preds = model.predict(data_preps(df))
            st.write(preds)
            save_button(preds)
        else:
            st.write('Не хватает колонок:')
            st.write(missing_columns)
            st.write('Проверьте ваш датасет.')

