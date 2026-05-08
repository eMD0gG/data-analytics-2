import streamlit as st
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

import prompts

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="AI Data Analyst", layout="wide")

if not api_key:
    st.error("Критическая ошибка: GROQ_API_KEY не найден в .env файле")
    st.stop()

st.title("🤖 Аналитический ИИ-агент")

uploaded_file = st.file_uploader("Загрузите CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Датасет загружен успешно.")
    
    query = st.text_input("Ваш вопрос по данным:")

    if st.button("Анализировать"):
        llm = ChatGroq(
            temperature=0, 
            model_name="llama-3.3-70b-versatile",
            api_key=api_key
        )

        prefix_prompt = f"{prompts.ROLES_AND_SAFETY}\n{prompts.ANALYSIS_GUIDE}"

        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            agent_type="tool-calling",
            allow_dangerous_code=True,
            prefix=f"{prompts.ROLES_AND_SAFETY}\n{prompts.ANALYSIS_GUIDE}",
            max_iterations=10,
            extra_ids=None,
            include_df_in_prompt=True,
            agent_executor_kwargs={"handle_parsing_errors": True} 
    )

        with st.spinner("Агент анализирует данные..."):
            try:
                result = agent.invoke({"input": query})
                st.markdown(result["output"])
                
                chart_files = glob.glob("chart*.png")
                
                if chart_files:
                    for chart_file in sorted(chart_files):
                        st.image(chart_file)
                        os.remove(chart_file)
            except Exception as e:
                st.warning("Агент столкнулся с ошибкой форматирования, но вот его мысли:")
                st.write(str(e))