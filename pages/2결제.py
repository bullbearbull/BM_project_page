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
        image = st.image('BM_project_page/가입.png')
        df_item = {'item_list' : ['1회권(종량제)', '10회권(종량제)', '30회권(종량제)', '1개월(기간제)', '3개월(기간제)', '6개월(기간제)', '12개월(기간제)'],
                   'price_list' : ['6,000원', '55,000원', '150,000원', '150,000원', '400,000원', '750,000원', '1,400,000원']}

        item = st.multiselect('가입하실 요금제를 선택해주세요', df_item.iloc[:, 'item_list'])
        st.write(f'선택하신 요금제는 {item}으로, 금액은 {df_item.loc[(df_item.item_list == item),df_item.price_list]}입니다.')
      else : st.error('비밀번호가 일치하지 않습니다.')



main()