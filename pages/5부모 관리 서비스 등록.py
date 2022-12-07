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
  st.image('with_together2.png')
  st.header('토탈 케어 서비스')
  st.subheader('월 50,000원')
  st.write('서비스 내용 :')
  st.write('1. 실시간 건강 측정 데이터 확인 가능')
  st.write('2. 식사 후 매일 맞춤형 영양제를 제공합니다.') ## 제휴 건강식품 업체와의 협약을 통한
  st.write('3. 매주 건강 분석 보고서 제공 및 전문가 상담 월 1회 제공') ## 제휴 병원의 의료진을 통한 상담
  i_name = st.text_input('본인의 성함을 기입해주세요:')
  i_pnum = st.text_input('본인의 휴대폰 번호를 입력해주세요')
  p_name = st.text_input('부모님의 성함을 기입해주세요:')
  p_birth = st.date_input('부모님의 생년월일을 입력해주세요 :')
  checkbox_btn1 = st.checkbox('입력완료!')
  if checkbox_btn1:
    i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{p_name}{p_birth}.csv')).iloc[0, 2].astype(str)
    i_password = st.text_input('부모님의 비밀번호를 입력해주세요 :', type="password")
    checkbox_btn2 = st.checkbox('입력완료')
    if checkbox_btn2:
      if i_secure == i_password:
        st.write('부모님의 건강정보를 받아보시겠습니까?')

        df = pd.DataFrame({'보호자 이름':[i_name],'보호자 휴대폰 번호':[i_pnum], '피보호자 이름':[p_name], '피보호자 생년월일':[p_birth], })
        p_name


main()
