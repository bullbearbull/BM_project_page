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
    page_icon="๐",
    page_title="๋๋ง์ ์๋ฆฌ์ฌ",
    layout="wide")
  st.image('with_together2.png')
  st.header('ํ ํ ์ผ์ด ์๋น์ค')
  st.subheader('์ 50,000์')
  st.write('์๋น์ค ๋ด์ฉ :')
  st.write('1. ์ค์๊ฐ ๊ฑด๊ฐ ์ธก์  ๋ฐ์ดํฐ ํ์ธ ๊ฐ๋ฅ')
  st.write('2. ์์ฌ ํ ๋งค์ผ ๋ง์ถคํ ์์์ ๋ฅผ ์ ๊ณตํฉ๋๋ค.') ## ์ ํด ๊ฑด๊ฐ์ํ ์์ฒด์์ ํ์ฝ์ ํตํ
  st.write('3. ๋งค์ฃผ ๊ฑด๊ฐ ๋ถ์ ๋ณด๊ณ ์ ์ ๊ณต ๋ฐ ์ ๋ฌธ๊ฐ ์๋ด ์ 1ํ ์ ๊ณต') ## ์ ํด ๋ณ์์ ์๋ฃ์ง์ ํตํ ์๋ด
  i_name = st.text_input('๋ณธ์ธ์ ์ฑํจ์ ๊ธฐ์ํด์ฃผ์ธ์:')
  i_pnum = st.text_input('๋ณธ์ธ์ ํด๋ํฐ ๋ฒํธ๋ฅผ ์๋ ฅํด์ฃผ์ธ์')
  p_name = st.text_input('๋ถ๋ชจ๋์ ์ฑํจ์ ๊ธฐ์ํด์ฃผ์ธ์:')
  p_birth = st.date_input('๋ถ๋ชจ๋์ ์๋์์ผ์ ์๋ ฅํด์ฃผ์ธ์ :')
  checkbox_btn1 = st.checkbox('์๋ ฅ์๋ฃ!')
  if checkbox_btn1:
    i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{p_name}{p_birth}.csv')).iloc[0, 2].astype(str)
    i_password = st.text_input('๋ถ๋ชจ๋์ ๋น๋ฐ๋ฒํธ๋ฅผ ์๋ ฅํด์ฃผ์ธ์ :', type="password")
    checkbox_btn2 = st.checkbox('์๋ ฅ์๋ฃ')
    if checkbox_btn2:
      if i_secure == i_password:
        st.write('๋ถ๋ชจ๋์ ๊ฑด๊ฐ์ ๋ณด๋ฅผ ๋ฐ์๋ณด์๊ฒ ์ต๋๊น?')

        df = pd.DataFrame({'๋ณดํธ์ ์ด๋ฆ':[i_name],'๋ณดํธ์ ํด๋ํฐ ๋ฒํธ':[i_pnum], 'ํผ๋ณดํธ์ ์ด๋ฆ':[p_name], 'ํผ๋ณดํธ์ ์๋์์ผ':[p_birth], })
        p_name


main()
