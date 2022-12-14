import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

def main() :
  st.set_page_config(
    page_icon="π",
    page_title="λλ§μ μλ¦¬μ¬",
    layout="wide")
  st.image('κ°μ.png')
  st.write('* μ΅μ΄ κ°μ κ³ κ°λμ 3ν μμ¬ λ¬΄λ£ μμ¬κΆμ΄ λΆμ¬λ©λλ€')

  st.subheader('μ λ³΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ')

  i_name = st.text_input('μ΄λ¦μ μλ ₯ν΄μ£ΌμΈμ :')
  i_birth = st.date_input('μλμμΌμ μλ ₯ν΄μ£ΌμΈμ :')
  checkbox_btn1 = st.checkbox('μλ ₯μλ£!')
  if checkbox_btn1 :
    i_secure = pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0,2].astype(str)
    i_password = st.text_input('λΉλ°λ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ :', type="password")
    checkbox_btn2 = st.checkbox('μλ ₯μλ£')
    if checkbox_btn2 :
      if i_secure == i_password:
        st.success('λ‘κ·ΈμΈλμμ΅λλ€!')
        df = pd.DataFrame({'item_list': ['1νκΆ(μ’λμ )', '10νκΆ(μ’λμ )', '30νκΆ(μ’λμ )', '1κ°μ(κΈ°κ°μ )', '3κ°μ(κΈ°κ°μ )', '6κ°μ(κΈ°κ°μ )','12κ°μ(κΈ°κ°μ )'],
                           'price_list': ['6,000μ', '55,000μ', '150,000μ', '150,000μ', '400,000μ', '750,000μ','1,400,000μ']})
        item = st.multiselect('κ°μνμ€ μκΈμ λ₯Ό μ νν΄μ£ΌμΈμ', df.loc[:, 'item_list'])
        ind = df.loc[df.item_list.isin(item), 'price_list'].to_list()
        if item :
          st.write(f'μ ννμ  μκΈμ  : {item}μ΄λ©°')
          st.write(f'κ²°μ νμ€ κΈμ‘μ {ind[0]}μλλ€.')
          o, s, t, f = st.number_input('μΉ΄λλ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ', 0, 9999), st.text_input('', type="password"), st.text_input('', type="password"), st.number_input('', 0, 9999)
          checkbox_btn3 = st.checkbox('μλ ₯μλ£!!')
          if checkbox_btn3:
            ans = st.text_input(f' μ 4μλ¦¬κ° {o}μ΄λ©°, λ§μ§λ§ 4 μλ¦¬κ° {f}μ΄ λ§μ΅λκΉ?(Y/N)')
            if ans == 'Y' or 'y' :
              card_num_list = [o, int(s), int(t), f]
              pd.DataFrame(pd.read_csv(f'Secure_DB/{i_name}{i_birth}.csv')).iloc[0, 3] = card_num_list
            else : st.write('μ²΄ν¬λ°μ€λ₯Ό ν΄μ ν ν, μ λ³΄λ₯Ό μμ ν΄μ£ΌμΈμ.')
        else: pass
      else : st.error('λΉλ°λ²νΈκ° μΌμΉνμ§ μμ΅λλ€.')



main()