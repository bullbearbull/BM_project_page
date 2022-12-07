import pandas as pd
import streamlit as st

def main() :
  st.set_page_config(
    page_icon="👋",
    page_title="나만의 요리사",
    layout="wide")

  st.title('👋 나만의 요리사 👋')
  st.subheader('결제하시겠습니까?')
  st.subheader('사용에 어려움이 있으시면 옆에 있는 직원에게 이야기해주세요')
  st.subheader('언제든 편하게 말씀해주세요!')
  i_name = st.text_input('이름을 입력해주세요 :')
  i_birth = st.date_input('생년월일을 입력해주세요 : (예시 601020')
  checkbox_btn1 = st.checkbox('입력완료!')
  if checkbox_btn1 :
    i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0,2].astype(str)
    st.write(i_secure)
    i_password = st.text_input('비밀번호를 입력해주세요 :', type="password")
    checkbox_btn2 = st.checkbox('입력완료')
    if checkbox_btn2 :
      if i_secure == i_password:
        st.header('종량제 식권 구매')
        st.write('서비스 소개 : 원하시는 때에 식사를 하실 수 있습니다!')
        st.write('이용기한 : 3개월')
        st.write('1회 이용권 : 7000원')
        st.write('10회 이용권 : 60000원')
        st.write('30회 이용권 : 160000원')

        st.write('')
        st.header('기간제 식권 구매')
        st.header('서비스 소개 : 식사를 포함해 정기적인 ')

      else : st.error('비밀번호가 일치하지 않습니다.')



main()