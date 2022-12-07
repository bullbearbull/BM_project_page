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

    st.header('건강정보 입력시스템')
    st.header('실제 구현시, 회원정보는 지문으로 식별')

    st.subheader('입력 대상의 정보를 확인하겠습니다.')

    i_name = st.text_input('이름을 입력해주세요 :')
    i_birth = st.date_input('생년월일을 입력해주세요 :')
    checkbox_btn1 = st.checkbox('입력완료!')
    if checkbox_btn1:
        i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 2].astype(str)
        i_password = st.text_input('비밀번호를 입력해주세요 :', type="password")
        checkbox_btn2 = st.checkbox('입력완료')
        if checkbox_btn2:
            if i_secure == i_password:
                st.success('로그인되었습니다!')
                df = pd.read_csv(f'Health_DB/{i_name}{i_birth}.csv')
                i_diabetes = st.number_input('혈당(㎎/ℓ)을 입력해주세요 :', 1, 999)
                i_blood_pressure_systolic = st.number_input('혈압(수축기), mmHg을 입력해주세요 :', 1, 999)
                i_blood_pressure_diastolic = st.number_input('혈압(이완기), mmHg을 입력해주세요 :', 1, 999)
                checkbox_btn3 = st.checkbox('입력완료!!')
                if checkbox_btn3 :
                    tm = localtime()
                    temp_time = strftime('%Y-%m-%d', tm)
                    health_data = pd.DataFrame(
                        {'측정일자': [temp_time], '혈당(㎎/ℓ)': [i_diabetes], '혈압(수축기), mmHg': [i_blood_pressure_systolic],
                         '혈압(이완기), mmHg': [i_blood_pressure_diastolic]})
                    df = pd.concat([df, health_data], axis=0, join='inner', ignore_index=True)
                    df.to_csv(f'Health_DB/{i_name}{i_birth}.csv')
                    st.success('입력이 완료되었습니다!')
            else: st.error('비밀번호가 일치하지 않습니다.')



main()