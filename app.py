#test
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

st.title("【提出課題】LLM機能を搭載したWebアプリを開発しよう")

selected_item = st.radio(
    "相談したいAIを選択してください。",
    ["ダイエットの専門家", "お金の専門家"]
)

st.divider()

input_message = st.text_input(label="相談内容を入力してください。")

if st.button("実行"):
    st.divider()
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    if input_message:
        if selected_item == "ダイエットの専門家":
            system_message = "ダイエットの専門家として相談に応じてください."
        else:
            system_message = "お金の専門家として相談に応じてください."
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=input_message),
        ]
        result = llm(messages)
        st.write(f"{selected_item}AIの回答: **{result.content}**")
    else:
        st.error("質問内容を入力してから「実行」ボタンを押してください。")

