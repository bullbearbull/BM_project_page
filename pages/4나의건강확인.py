import streamlit as st
import pandas as pd
import numpy as np
from time import localtime
from time import strftime
import time
from pandas.core.reshape.tile import to_datetime
import shelve
import altair as alt
import warnings
warnings.filterwarnings('ignore')

def main():
    st.set_page_config(
        page_icon="👋",
        page_title="나만의 요리사",
        layout="wide")
    st.image('Banner.png')

    st.header('건강정보 입력시스템')
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
                health_data = pd.DataFrame(pd.read_csv(f'Health_DB/{i_name}{i_birth}.csv'))
                health_data.set_index('측정일자')
                st.dataframe(health_data.style.highlight_max(axis=0))
                chart_dia = alt.Chart(health_data).mark_circle().encode(x='측정일자', y='혈당(㎎/ℓ)')
                chart_bps = alt.Chart(health_data).mark_circle().encode(x='측정일자', y='혈압(수축기), mmHg')
                chart_bpd = alt.Chart(health_data).mark_circle().encode(x='측정일자', y='혈압(이완기), mmHg')

                st.altair_chart(chart_dia, use_container_width=True)
                st.altair_chart(chart_bps, use_container_width=True)
                st.altair_chart(chart_bpd, use_container_width=True)


            else: st.error('비밀번호가 일치하지 않습니다.')


main()