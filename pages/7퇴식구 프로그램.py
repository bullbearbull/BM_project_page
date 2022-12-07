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
        page_icon="👋",
        page_title="나만의 요리사",
        layout="wide")
    st.image('Banner.png')
    st.write('실제 구현시, 회원정보는 지문으로 식별')
    i_name = st.text_input('식사 마치신 분의 성함을 입력해주세요 :')
    i_birth = st.date_input('식사 마치신 분의 생년월일을 입력해주세요 :')
    checkbox_btn1 = st.checkbox('입력완료!')
    if checkbox_btn1:
        i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 2].astype(str)
        i_password = st.text_input('비밀번호를 입력해주세요 :', type="password")
        checkbox_btn2 = st.checkbox('입력완료')
        if checkbox_btn2:
            if i_secure == i_password:
                st.success('로그인되었습니다!')
                tm = localtime()
                temp_day = strftime('%Y-%m-%d', tm)
                temp_time = strftime('%H:%M', tm)
                meal_quantity = st.slider('식사량을 입력해주세요(실제 구현시, 카메라로 인식):', 0, 100)
                hate_food = st.text_input('기피한 식재료를 입력해주세요(실제 구현시, 카메라로 인식):')
                checkbox_btn3 = st.checkbox('입력완료!!')
                if checkbox_btn3:
                    meal_data = pd.read_csv(f'Meal_DB/{i_name}{i_birth}.csv')
                    st.write(meal_data)
                    time_list = len(meal_data.입장일자.to_list())
                    st.write(meal_data.iloc[time_list-1 , 1], temp_day)
                    if meal_data.iloc[time_list-1 , 1] == temp_day :
                        meal_data.loc[meal_data.입장일자 == temp_day, '퇴장시간'] = temp_time
                        meal_data.loc[meal_data.입장일자 == temp_day, '식사량'] = [meal_quantity]
                        meal_data.loc[meal_data.입장일자 == temp_day, '기피'] = [hate_food]
                        start_time = meal_data.loc[meal_data.입장일자 == temp_day, '입장시간']
                        st.write(start_time)
                        meal_data.loc[meal_data.입장일자 == temp_day, '식사시간'] = temp_time
                        # meal_data = pd.read_csv(f'Meal_DB/{i_name}{i_birth}.csv')
                        # meal_data[]
                        # meal_data = pd.concat([meal_data, df], axis=0, join='inner', ignore_index=True)
                        st.write(meal_data)
                        meal_data.to_csv(f'Meal_DB/{i_name}{i_birth}.csv', index=False)
                        st.success('식사량이 입력되었습니다!')
                    else: st.error('처리과정 중 오류가 발생하였습니다, 관리자를 불러주세요!')
                else:pass
            else:st.error('비밀번호가 일치하지 않습니다.')

main()
