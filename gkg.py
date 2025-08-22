import streamlit as st

st. title('gyukyulgyu')

name = st. text_input('이름:')
choice = st.selectbox('고르세요:', ['남규현','이민규','김은결','김건호'])


choice_data = {
  '남규현': {
        '특징': '방밸을 즐기며 코 사이즈가 가로 8cm, 세로 9cm를 소유함'
  },
  '이민규': {
        '특징': '2반에서 왕따담당'
},
  '김은결': {
        '특징': '예대도 강탈예정'
  }, 
  '김건호': {
        '특징': '3도 화상입음'
  }
}
if st.button('특징 생성'):
    if choice in mbti_data:
        특징 = choice_data[mbti]['특징']
        직업 = choice_data[mbti]['직업']
        잘_맞는_mbti = ', '.join(mbti_data[mbti]['잘 맞는 MBTI'])

        st.write(f"{name}님! 당신의 MBTI 유형은 {mbti}입니다!")
        st.write(f"**특징**: {특징}")
        st.write(f"**어울리는 직업**: {직업}")
        st.write(f"**잘 맞는 MBTI 유형**: {잘_맞는_mbti}")
    else:
        st.write(f"{name}님! 아직 {mbti} 유형에 대한 정보가 없습니다.")
