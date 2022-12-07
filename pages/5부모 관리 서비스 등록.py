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
def main() :
  st.set_page_config(
    page_icon="👋",
    page_title="나만의 요리사",
    layout="wide")
  st.image('Banner.png')
  st.subheader('부모님의 끼니 문제와 건강 문제를 함께 해결해봐요')
  p_name = st.text_input('부모님의 성함을 기입해주세요:')
  p_birth = st.date_input('부모님의 생년월일을 입력해주세요 :')
  checkbox_btn1 = st.checkbox('입력완료!')
  if checkbox_btn1:
    i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{p_name}{p_birth}.csv')).iloc[0, 2].astype(str)
    i_password = st.text_input('부모님의 비밀번호를 입력해주세요 :', type="password")
    checkbox_btn2 = st.checkbox('입력완료')
    if checkbox_btn2:
      if i_secure == i_password:
        df = pd.DataFrame
        p_name


main()
