from langchain.chat_models import ChatOpenAI
import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()

# 말을 이어서하는 모드
# from langchain.llms import OpenAI
# llm = OpenAI()
# result =llm.predict("오늘 기분이 약간 별로야, 날 좀 응원해줄 수 있니?")


# 채팅을 하는 모드
chat_model = ChatOpenAI()

st.title('인공지능 시인 :sunglasses:')

content = st.text_input('시의 주제를 입력해 주세요', )

if st.button('시 작성 요청하기'):
    with st.spinner('시를 쓰고 있습니다...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
