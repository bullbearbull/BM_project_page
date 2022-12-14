import streamlit as st
import pandas as pd
import numpy as np
from time import localtime
from time import strftime
import time
from pandas.core.reshape.tile import to_datetime
import shelve
import warnings
warnings.filterwarnings('ignore')


def main():
    st.set_page_config(
        page_icon="๐",
        page_title="๋๋ง์ ์๋ฆฌ์ฌ",
        layout="wide")
    st.image('Banner.png')

    st.header('๊ฑด๊ฐ์ ๋ณด ์๋ ฅ์์คํ')

    i_name = st.text_input('์ด๋ฆ์ ์๋ ฅํด์ฃผ์ธ์ :')
    i_birth = st.date_input('์๋์์ผ์ ์๋ ฅํด์ฃผ์ธ์ :')
    checkbox_btn1 = st.checkbox('์๋ ฅ์๋ฃ!')
    if checkbox_btn1:
        i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 2].astype(str)
        i_password = st.text_input('๋น๋ฐ๋ฒํธ๋ฅผ ์๋ ฅํด์ฃผ์ธ์ :', type="password")
        checkbox_btn2 = st.checkbox('์๋ ฅ์๋ฃ')
        if checkbox_btn2:
            if i_secure == i_password:
                st.success('๋ก๊ทธ์ธ๋์์ต๋๋ค!')
                df = pd.read_csv(f'Health_DB/{i_name}{i_birth}.csv')
                i_diabetes = st.number_input('ํ๋น(ใ/โ)์ ์๋ ฅํด์ฃผ์ธ์ :', 1, 999)
                i_blood_pressure_systolic = st.number_input('ํ์(์์ถ๊ธฐ), mmHg์ ์๋ ฅํด์ฃผ์ธ์ :', 1, 999)
                i_blood_pressure_diastolic = st.number_input('ํ์(์ด์๊ธฐ), mmHg์ ์๋ ฅํด์ฃผ์ธ์ :', 1, 999)
                checkbox_btn3 = st.checkbox('์๋ ฅ์๋ฃ!!')
                if checkbox_btn3 :
                    tm = localtime()
                    temp_time = strftime('%Y-%m-%d', tm)
                    health_data = pd.DataFrame(
                        {'์ธก์ ์ผ์': [temp_time], 'ํ๋น(ใ/โ)': [i_diabetes], 'ํ์(์์ถ๊ธฐ), mmHg': [i_blood_pressure_systolic],
                         'ํ์(์ด์๊ธฐ), mmHg': [i_blood_pressure_diastolic]})
                    df = pd.concat([df, health_data], axis=0, join='inner', ignore_index=True)
                    df.to_csv(f'Health_DB/{i_name}{i_birth}.csv')
                    st.success('์๋ ฅ์ด ์๋ฃ๋์์ต๋๋ค!')
            else: st.error('๋น๋ฐ๋ฒํธ๊ฐ ์ผ์นํ์ง ์์ต๋๋ค.')



main()