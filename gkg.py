import streamlit as st

st. title('gyukyulgyu')

name = st. text_input('이름:')
choice = st.selectbox('고르세요:', ['남규현','이민규','김은결','김건호'])


choice_data = {
  '남규현': {
        '특징': '방밸을 즐기며 코 사이즈가 가로 8cm, 세로 9cm를 소유함'
  },
  '이민규': {
        '특징': '2반에서 왕따담당, 예준이 없으면 숨을못쉼 스킨십을 안해줘서 연애를 포기함 '
},
  '김은결': {
        '특징': '미대도 광탈예정, 80만원 지출예정'
  }, 
  '김건호': {
        '특징': '3도 화상입음'
  }
}
if st.button('특징 생성'):
    if choice in choice_data:
        특징 = choice_data[choice]['특징']

        st.write(f"{name}님! 당신의 원픽 특징은 {choice}입니다!")
        st.write(f"**특징**: {특징}")
else:
        st.write(f"{name}님! 아직 {choice} 유형에 대한 정보가 없습니다.")
