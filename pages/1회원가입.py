import streamlit as st
import pandas as pd
import numpy as np
from time import localtime
from time import strftime
import time
from pandas.core.reshape.tile import to_datetime
import shelve

def main() :
  st.set_page_config(
    page_icon="👋",
    page_title="나만의 요리사",
    layout="wide")

  st.title('👋 나만의 요리사 👋')
  st.subheader('회원가입을 도와드리겠습니다')
  st.subheader('사용에 어려움이 있으시면 옆에 있는 직원에게 이야기해주세요')
  st.subheader('언제든 편하게 말씀해주세요!')
  st.write('최초 가입 고객 한정')
  st.write('3회 식사 이용권 증정')

  i_name = st.text_input('이름을 입력해주세요 :')
  i_birth = st.date_input('생년월일을 입력해주세요 : (예시 601020')
  sex_cat = ['여성', '남성']
  i_sex = st.multiselect('성별을 선택해주세요 :', sex_cat)
  dis_cat = ['당뇨', '고혈압', '관절염', '폐질환', '위염', '치매', '간질환', '소화기질환']
  i_disease = st.multiselect('질병을 입력해주세요 :', dis_cat)
  i_number = st.text_input('번호를 입력해주세요 :(예시 010-0000-0000)')
  i_password = st.text_input('사용하실 비밀번호를 입력해주세요 :', type="password")
  i_password_check = st.text_input('다시 한번 입력해주세요:', type="password")
  if i_password == i_password_check:
    pass
  else: st.error("비밀번호가 일치하지 않습니다")
  i_secure = pd.DataFrame({'name':[i_name], 'birth':[i_birth], 'password' : [i_password]})
  i_data = pd.DataFrame({'name': [i_name], 'birth': [i_birth], 'sex': [i_sex], 'disease': [i_disease], 'phone_num':[i_number]})
  i_data.set_index('name', inplace=True)
  i_secure.set_index('name', inplace=True)
  checkbox_btn = st.checkbox('입력완료')
  if checkbox_btn :
    i_data.to_csv(f'ID_DB/{i_name}{i_birth}.csv')
    i_secure.to_csv(f'Secure_DB/{i_name}{i_birth}.csv')
    st.success('가입이 완료되었습니다.')
    time.sleep(2)


main()

