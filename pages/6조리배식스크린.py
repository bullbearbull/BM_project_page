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
        page_icon="π",
        page_title="λλ§μ μλ¦¬μ¬",
        layout="wide")
    st.image('Banner.png')
    st.header('μ€μ  κ΅¬νμ, νμμ λ³΄λ μ§λ¬ΈμΌλ‘ μλ³')
    i_name = st.text_input('μμ¬νμλ λΆ μ±ν¨μ μλ ₯ν΄μ£ΌμΈμ :')
    i_birth = st.date_input('μμ¬νμλ λΆ μλμμΌμ μλ ₯ν΄μ£ΌμΈμ :')
    checkbox_btn1 = st.checkbox('μλ ₯μλ£!')
    if checkbox_btn1:
        i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 2].astype(str)
        i_password = st.text_input('λΉλ°λ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ :', type="password")
        checkbox_btn2 = st.checkbox('μλ ₯μλ£')
        if checkbox_btn2:
            if i_secure == i_password:
                st.success('λ‘κ·ΈμΈλμμ΅λλ€!')
                tm = localtime()
                temp_day = strftime('%Y-%m-%d', tm)
                temp_time = strftime('%H:%M', tm)
                df = pd.DataFrame({'μμ₯μΌμ':[temp_day], 'μμ₯μκ°':[temp_time], 'ν΄μ₯μκ°':[''], 'μμ¬μκ°':[''], 'μμ¬λ':[''], 'κΈ°νΌ':['']})
                health_data = pd.read_csv(f'ID_DB/{i_name}{i_birth}.csv')
                disease_list = health_data['disease'].to_string().replace('[', '').replace(']', '').replace("'", '').replace('0', '').replace(' ', '').split(',')

                consider_list = []
                for disease in disease_list:
                    if disease == 'κ³ νμ':
                        consider_list.append('μ μΌμ')
                    elif disease == 'λΉλ¨' :
                        consider_list.append('μ λΉ')
                        consider_list.append('λμ²΄λΉ')
                    elif disease == 'κ΄μ μΌ' :
                        consider_list.append('μΉΌμ')
                        consider_list.append('λΉνλ―ΌD')
                        consider_list.append('λ§κ·Έλ€μ')
                        consider_list.append('μμ°')
                        consider_list.append('μ² λΆ')
                    elif disease == 'μμΌ' :
                        consider_list.append('λΆλλ¬μ')
                        consider_list.append('κ³ λ¨λ°±')
                        consider_list.append('μ μΌ')
                        consider_list.append('μ μ§λ°©')
                    elif disease == 'μΉλ§€' :
                        consider_list.append('κ²¬κ³Όλ₯')
                        consider_list.append('ν΄μ°λ¬Ό')
                        consider_list.append('μ½μ°(νΈλ₯Έμ±μ)')
                    elif disease == 'κ°μ§ν' :
                        consider_list.append('κ³ λ¨λ°±')
                        consider_list.append('μλ¦¬μ (λ§λ)')
                        consider_list.append('μ λΉ')
                    elif disease == 'μνκΈ°μ§ν' :
                        consider_list.append('μ μ§λ°©')
                        consider_list.append('μ μΌ')
                        consider_list.append('λΆλλ¬μ')
                    else : st.write(f'{disease}μ μ£Όμν΄μ£ΌμΈμ')
                consider_list = set(consider_list)
                st.subheader(f'μμ₯μκ° :{tm.tm_hour}μ{tm.tm_min}λΆ')
                st.header(f'κ³ κ°λͺ : {i_name}λ')
                st.header(f'{consider_list}')
                st.header('μΌλ‘ λ°°μν΄μ£ΌμΈμ')
                meal_data = pd.read_csv(f'Meal_DB/{i_name}{i_birth}.csv')
                df = pd.concat([meal_data, df], axis=0, join='inner', ignore_index=True)
                df.to_csv(f'Meal_DB/{i_name}{i_birth}.csv')
            else:st.error('λΉλ°λ²νΈκ° μΌμΉνμ§ μμ΅λλ€.')


main()