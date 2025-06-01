import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

st.set_page_config(page_title="Prompt Rewriter", page_icon="📝")
# Set your OpenAI API key (or use Streamlit Secrets if deploying securely)
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# UI Enhancement
st.markdown("""
    <style>
    textarea {
        background-color: #d67474 !important;
        color: white !important;
        border: 1px solid #bb5e5e;
        border-radius: 6px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)
# Set up the prompt template
template = """
You are a helpful prompt rewriter.
Rewrite this prompt to make it more clear and detailed:

Original Prompt: {original_prompt}

Improved Prompt:"""
prompt = PromptTemplate.from_template(template)

llm = OpenAI(temperature=0.7, model = 'gpt-4o-mini')
chain = prompt | llm

st.title("💬 Prompt Rewriter Tool")
st.markdown("Make your AI prompts clearer, smarter, and more effective! 🚀")

user_input = st.text_area("👨‍💻 Enter your raw prompt below:", height=150)

if st.button("🔁 Rewrite Prompt"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            result = chain.invoke({"original_prompt": user_input})
        st.success("Here's your improved prompt:")
        st.code(result, language="markdown")
    else:
        st.warning("Please enter a prompt to rewrite.")
