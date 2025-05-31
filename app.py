import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# Set your OpenAI API key (or use Streamlit Secrets if deploying securely)
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# Set up the prompt template
template = """
You are a helpful prompt rewriter.
Rewrite this prompt to make it more clear and detailed:

Original Prompt: {original_prompt}

Improved Prompt:"""
prompt = PromptTemplate.from_template(template)

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Create chain using new LangChain syntax
chain = prompt | llm

# Streamlit UI
st.set_page_config(page_title="Prompt Rewriter", page_icon="📝")
st.title("💬 Prompt Rewriter Tool")
st.markdown("Make your AI prompts clearer, smarter, and more effective! 🚀")

# Input box
user_input = st.text_area("👨‍💻 Enter your raw prompt below:", height=150)

# Button to trigger rewriting
if st.button("🔁 Rewrite Prompt"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            result = chain.invoke({"original_prompt": user_input})
        st.success("Here's your improved prompt:")
        st.code(result, language="markdown")
    else:
        st.warning("Please enter a prompt to rewrite.")
