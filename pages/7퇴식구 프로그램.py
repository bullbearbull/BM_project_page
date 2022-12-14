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
    st.write('์ค์  ๊ตฌํ์, ํ์์ ๋ณด๋ ์ง๋ฌธ์ผ๋ก ์๋ณ')
    i_name = st.text_input('์์ฌ ๋ง์น์  ๋ถ์ ์ฑํจ์ ์๋ ฅํด์ฃผ์ธ์ :')
    i_birth = st.date_input('์์ฌ ๋ง์น์  ๋ถ์ ์๋์์ผ์ ์๋ ฅํด์ฃผ์ธ์ :')
    checkbox_btn1 = st.checkbox('์๋ ฅ์๋ฃ!')
    if checkbox_btn1:
        i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 2].astype(str)
        i_password = st.text_input('๋น๋ฐ๋ฒํธ๋ฅผ ์๋ ฅํด์ฃผ์ธ์ :', type="password")
        checkbox_btn2 = st.checkbox('์๋ ฅ์๋ฃ')
        if checkbox_btn2:
            if i_secure == i_password:
                st.success('๋ก๊ทธ์ธ๋์์ต๋๋ค!')
                tm = localtime()
                temp_day = strftime('%Y-%m-%d', tm)
                temp_time = strftime('%H:%M', tm)
                meal_quantity = st.slider('์์ฌ๋์ ์๋ ฅํด์ฃผ์ธ์(์ค์  ๊ตฌํ์, ์นด๋ฉ๋ผ๋ก ์ธ์):', 0, 100)
                hate_food = st.text_input('๊ธฐํผํ ์์ฌ๋ฃ๋ฅผ ์๋ ฅํด์ฃผ์ธ์(์ค์  ๊ตฌํ์, ์นด๋ฉ๋ผ๋ก ์ธ์):')
                checkbox_btn3 = st.checkbox('์๋ ฅ์๋ฃ!!')
                if checkbox_btn3:
                    meal_data = pd.read_csv(f'Meal_DB/{i_name}{i_birth}.csv')
                    st.write(meal_data)
                    time_list = len(meal_data.์์ฅ์ผ์.to_list())
                    st.write(meal_data.iloc[time_list-1 , 1], temp_day)
                    if meal_data.iloc[time_list-1 , 1] == temp_day :
                        meal_data.loc[meal_data.์์ฅ์ผ์ == temp_day, 'ํด์ฅ์๊ฐ'] = temp_time
                        meal_data.loc[meal_data.์์ฅ์ผ์ == temp_day, '์์ฌ๋'] = [meal_quantity]
                        meal_data.loc[meal_data.์์ฅ์ผ์ == temp_day, '๊ธฐํผ'] = [hate_food]
                        start_time = meal_data.loc[meal_data.์์ฅ์ผ์ == temp_day, '์์ฅ์๊ฐ']
                        st.write(start_time)
                        meal_data.loc[meal_data.์์ฅ์ผ์ == temp_day, '์์ฌ์๊ฐ'] = temp_time
                        # meal_data = pd.read_csv(f'Meal_DB/{i_name}{i_birth}.csv')
                        # meal_data[]
                        # meal_data = pd.concat([meal_data, df], axis=0, join='inner', ignore_index=True)
                        st.write(meal_data)
                        meal_data.to_csv(f'Meal_DB/{i_name}{i_birth}.csv', index=False)
                        st.success('์์ฌ๋์ด ์๋ ฅ๋์์ต๋๋ค!')
                    else: st.error('์ฒ๋ฆฌ๊ณผ์  ์ค ์ค๋ฅ๊ฐ ๋ฐ์ํ์์ต๋๋ค, ๊ด๋ฆฌ์๋ฅผ ๋ถ๋ฌ์ฃผ์ธ์!')
                else:pass
            else:st.error('๋น๋ฐ๋ฒํธ๊ฐ ์ผ์นํ์ง ์์ต๋๋ค.')

main()
