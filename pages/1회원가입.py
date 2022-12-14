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

  st.title('회원가입')
  st.write('※ 사용에 어려움이 있으시면 직원에게 편하게 말씀해주십시오.')

  i_name = st.text_input('이름을 입력해주세요 :')
  i_birth = st.date_input('생년월일을 입력해주세요 :')
  sex_cat = ['여성', '남성']
  i_sex = st.multiselect('성별을 선택해주세요 :', sex_cat)
  dis_cat = ['당뇨', '고혈압', '관절염', '폐질환', '위염', '치매', '간질환', '소화기질환']
  i_disease = st.multiselect('질병을 입력해주세요 :', dis_cat)
  i_number = st.text_input('번호를 입력해주세요 :(예시 010-0000-0000)')
  i_password = st.text_input('사용하실 비밀번호를 입력해주세요 :', type="password")
  i_password_check = st.text_input('다시 한번 입력해주세요:', type="password")
  if i_password == i_password_check:
    i_secure = pd.DataFrame({'name': [i_name], 'birth': [i_birth], 'password': [i_password], 'card_number':['']})
    i_data = pd.DataFrame({'name': [i_name], 'birth': [i_birth], 'sex': [i_sex], 'disease': [i_disease], 'phone_num': [i_number], 'pay': [0]})
    i_data.set_index('name', inplace=True)
    i_secure.set_index('name', inplace=True)
    checkbox_btn = st.checkbox('입력완료')
    if checkbox_btn:
      i_data.to_csv(f'ID_DB/{i_name}{i_birth}.csv')
      i_secure.to_csv(f'Secure_DB/{i_name}{i_birth}.csv')
      tm = localtime()
      temp_time = strftime('%Y-%m-%d', tm)
      df = pd.DataFrame({'측정일자' : [temp_time],'혈당(㎎/ℓ)' : [0],'혈압(수축기), mmHg' : [0],'혈압(이완기), mmHg' : [0]})
      df.to_csv(f'Health_DB/{i_name}{i_birth}.csv')
      df = pd.DataFrame({'입장일자':[0], '입장시간':[0], '퇴장시간':[0], '식사시간':[0], '식사량':[0], '기피':[0]})
      df.to_csv(f'Meal_DB/{i_name}{i_birth}.csv')
      st.success('가입이 완료되었습니다.')
    else : pass
  else : st.error("비밀번호가 일치하지 않습니다")




main()

