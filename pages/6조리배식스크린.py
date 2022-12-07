import streamlit as st
import pandas as pd
import numpy as np
from time import localtime
from time import strftime
import time
from pandas.core.reshape.tile import to_datetime
import shelve

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
                temp_time = strftime('%H:%M', tm)
                df = pd.DataFrame({'입장일자':[temp_day], '입장시간':[temp_time], '퇴장시간':[''], '식사시간':[''], '식사량':[''], '기피':['']})
                health_data = pd.read_csv(f'ID_DB/{i_name}{i_birth}.csv')
                disease_list = health_data['disease'].to_string().replace('[', '').replace(']', '').replace("'", '').replace('0', '').replace(' ', '').split(',')

                consider_list = []
                for disease in disease_list:
                    if disease == '고혈압':
                        consider_list.append('저염식')
                    elif disease == '당뇨' :
                        consider_list.append('저당')
                        consider_list.append('대체당')
                    elif disease == '관절염' :
                        consider_list.append('칼슘')
                        consider_list.append('비타민D')
                        consider_list.append('마그네슘')
                        consider_list.append('아연')
                        consider_list.append('철분')
                    elif disease == '위염' :
                        consider_list.append('부드러움')
                        consider_list.append('고단백')
                        consider_list.append('저염')
                        consider_list.append('저지방')
                    elif disease == '치매' :
                        consider_list.append('견과류')
                        consider_list.append('해산물')
                        consider_list.append('엽산(푸른채소)')
                    elif disease == '간질환' :
                        consider_list.append('고단백')
                        consider_list.append('알리신(마늘)')
                        consider_list.append('저당')
                    elif disease == '소화기질환' :
                        consider_list.append('저지방')
                        consider_list.append('저염')
                        consider_list.append('부드러움')
                    else : st.write(f'{disease}을 주의해주세요')
                consider_list = set(consider_list)
                st.subheader(f'입장시간 :{tm.tm_hour}시{tm.tm_min}분')
                st.header(f'고객명 : {i_name}님')
                st.header(f'{consider_list}')
                st.header('으로 배식해주세요')
                meal_data = pd.read_csv(f'Meal_DB/{i_name}{i_birth}.csv')
                df = pd.concat([meal_data, df], axis=0, join='inner', ignore_index=True)
                df.to_csv(f'Meal_DB/{i_name}{i_birth}.csv')
            else:st.error('비밀번호가 일치하지 않습니다.')


main()