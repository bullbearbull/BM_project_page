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
    st.header('실제 구현시, 회원정보는 지문으로 식별')
    i_name = st.text_input('식사하시는 분 성함을 입력해주세요 :')
    i_birth = st.date_input('식사하시는 분 생년월일을 입력해주세요 :')
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
                temp_time = strftime('%H:%m', tm)