import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

def main() :
  st.set_page_config(
    page_icon="👋",
    page_title="나만의 요리사",
    layout="wide")
  st.image('가입.png')
  st.write('* 최초 가입 고객님은 3회 식사 무료 식사권이 부여됩니다')

  st.subheader('정보를 입력해주세요')

  i_name = st.text_input('이름을 입력해주세요 :')
  i_birth = st.date_input('생년월일을 입력해주세요 :')
  checkbox_btn1 = st.checkbox('입력완료!')
  if checkbox_btn1 :
    i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0,2].astype(str)
    i_password = st.text_input('비밀번호를 입력해주세요 :', type="password")
    checkbox_btn2 = st.checkbox('입력완료')
    if checkbox_btn2 :
      if i_secure == i_password:
        st.success('로그인되었습니다!')
        df = pd.DataFrame({'item_list': ['1회권(종량제)', '10회권(종량제)', '30회권(종량제)', '1개월(기간제)', '3개월(기간제)', '6개월(기간제)','12개월(기간제)'],
                           'price_list': ['6,000원', '55,000원', '150,000원', '150,000원', '400,000원', '750,000원','1,400,000원']})
        item = st.multiselect('가입하실 요금제를 선택해주세요', df.loc[:, 'item_list'])
        ind = df.loc[df.item_list.isin(item), 'price_list'].to_list()
        if item :
          st.write(f'선택하신 요금제 : {item}이며')
          st.write(f'결제하실 금액은 {ind[0]}입니다.')
          o, s, t, f = st.number_input('카드번호를 입력해주세요', 0, 9999), st.text_input('', type="password"), st.text_input('', type="password"), st.number_input('', 0, 9999)
          checkbox_btn3 = st.checkbox('입력완료!!')
          if checkbox_btn3:
            ans = st.text_input(f' 앞 4자리가 {o}이며, 마지막 4 자리가 {f}이 맞습니까?(Y/N)')
            if ans == 'Y' or 'y' :
              card_num_list = [o, int(s), int(t), f]
              pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 3] = card_num_list
            else : st.write('체크박스를 해제한 후, 정보를 수정해주세요.')
        else: pass
      else : st.error('비밀번호가 일치하지 않습니다.')



main()