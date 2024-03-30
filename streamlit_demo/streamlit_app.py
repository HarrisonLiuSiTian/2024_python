"""
@文件名: streamlit_app.py
@作者: HarrisonLiu
@日期: 2024-03-29：23-01-29
@描述:
@Version : 0.0.0
"""
from data import load_data
import streamlit as st
from pandasai import SmartDataframe
from pandasai.callbacks import BaseCallback
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser
import os


class StreamlitCallback(BaseCallback):
    def __init__(self, container) -> None:
        """Initialize callback handler."""
        self.container = container

    def on_code(self, response: str):
        self.container.code(response)


class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)

    def format_dataframe(self, result):
        st.dataframe(result["value"])
        return

    def format_plot(self, result):
        st.image(result["value"])
        return

    def format_other(self, result):
        st.write(result["value"])
        return


st.write("# Chat with Credit Card Fraud Dataset 🦙")
df = load_data("./data")
with st.expander("🔎 Dataframe Preview"):
    st.write(df.tail(100))
query = st.text_area("🗣️ Chat with Dataframe")
container = st.container()
if query:
    llm = OpenAI(api_token="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")
    query_engine = SmartDataframe(df, config={"llm": llm})
    # query_engine = SmartDataframe(
    #     df,
    #     config={
    #         "llm": llm,
    #         "response_parser": StreamlitResponse,
    #         "callback": StreamlitCallback(container),
    #     }
    # )
    answer = query_engine.chat(query)
    st.write(answer)
