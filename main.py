from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain.llms import CTransformers
from streamlit_extras.buy_me_a_coffee import button
# from dotenv import load_dotenv
# load_dotenv()


# chat_model = llama
# llm = CTransformers(
#     model="llama-2-7b-chat.ggmlv3.q2_K.bin",
#     model_type="llama"
# )

# buy me a coffee
button(username="namseokyoo", floating=True, width=221)


Chat_model = ChatOpenAI()
llm = ChatOpenAI()

st.title('인공지능 시인 :sunglasses:')

content = st.text_input('시의 주제를 입력해 주세요', )

if st.button('시 작성 요청하기'):
    with st.spinner('시를 쓰고 있습니다...'):
        result = llm.predict(content + "에 대한 시를 써줘")
        # result = llm.predict("please write a poem about" + content + ":")
        # result = llm.predict("hello")
        st.write(result)
