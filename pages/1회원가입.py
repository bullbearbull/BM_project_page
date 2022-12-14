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
    page_icon="π",
    page_title="λλ§μ μλ¦¬μ¬",
    layout="wide")

  st.image('Banner.png')

  st.title('νμκ°μ')
  st.write('β» μ¬μ©μ μ΄λ €μμ΄ μμΌμλ©΄ μ§μμκ² νΈνκ² λ§μν΄μ£Όμ­μμ€.')

  i_name = st.text_input('μ΄λ¦μ μλ ₯ν΄μ£ΌμΈμ :')
  i_birth = st.date_input('μλμμΌμ μλ ₯ν΄μ£ΌμΈμ :')
  sex_cat = ['μ¬μ±', 'λ¨μ±']
  i_sex = st.multiselect('μ±λ³μ μ νν΄μ£ΌμΈμ :', sex_cat)
  dis_cat = ['λΉλ¨', 'κ³ νμ', 'κ΄μ μΌ', 'νμ§ν', 'μμΌ', 'μΉλ§€', 'κ°μ§ν', 'μνκΈ°μ§ν']
  i_disease = st.multiselect('μ§λ³μ μλ ₯ν΄μ£ΌμΈμ :', dis_cat)
  i_number = st.text_input('λ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ :(μμ 010-0000-0000)')
  i_password = st.text_input('μ¬μ©νμ€ λΉλ°λ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ :', type="password")
  i_password_check = st.text_input('λ€μ νλ² μλ ₯ν΄μ£ΌμΈμ:', type="password")
  if i_password == i_password_check:
    i_secure = pd.DataFrame({'name': [i_name], 'birth': [i_birth], 'password': [i_password], 'card_number':['']})
    i_data = pd.DataFrame({'name': [i_name], 'birth': [i_birth], 'sex': [i_sex], 'disease': [i_disease], 'phone_num': [i_number], 'pay': [0]})
    i_data.set_index('name', inplace=True)
    i_secure.set_index('name', inplace=True)
    checkbox_btn = st.checkbox('μλ ₯μλ£')
    if checkbox_btn:
      i_data.to_csv(f'ID_DB/{i_name}{i_birth}.csv')
      i_secure.to_csv(f'Secure_DB/{i_name}{i_birth}.csv')
      tm = localtime()
      temp_time = strftime('%Y-%m-%d', tm)
      df = pd.DataFrame({'μΈ‘μ μΌμ' : [temp_time],'νλΉ(γ/β)' : [0],'νμ(μμΆκΈ°), mmHg' : [0],'νμ(μ΄μκΈ°), mmHg' : [0]})
      df.to_csv(f'Health_DB/{i_name}{i_birth}.csv')
      df = pd.DataFrame({'μμ₯μΌμ':[0], 'μμ₯μκ°':[0], 'ν΄μ₯μκ°':[0], 'μμ¬μκ°':[0], 'μμ¬λ':[0], 'κΈ°νΌ':[0]})
      df.to_csv(f'Meal_DB/{i_name}{i_birth}.csv')
      st.success('κ°μμ΄ μλ£λμμ΅λλ€.')
    else : pass
  else : st.error("λΉλ°λ²νΈκ° μΌμΉνμ§ μμ΅λλ€")




main()

