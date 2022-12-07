import streamlit as st
import pandas as pd
import numpy as np
from time import localtime
from time import strftime
from pandas.core.reshape.tile import to_datetime
import shelve
import warnings
warnings.filterwarnings('ignore')



def main() :
  password = 1234567890
  st.title('고객 관리 계정')
  i_pass = st.number_input('관리자 비밀번호를 입력해주세요 :', 0, 9999999999)
  if i_pass == password :
    st.success('관리자 로그인 성공')

  else : st.error('관리자 로그인 실패')
main()