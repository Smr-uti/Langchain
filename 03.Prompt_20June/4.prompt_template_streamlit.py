import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

print("GOOGLE_API_KEY loaded:", bool(os.getenv("GOOGLE_API_KEY")))

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash")

tmpl="write a poem about {subject} in a {tone} tone with {lines} lines"

prompt_obj=PromptTemplate(template=tmpl)

st.title("Poem Generator")

new_subject=st.text_input("provide a subject:")
new_tone=st.text_input("provide a mood/tone:")
lines=st.text_input("Enter lines of the poem to create:")

complete_prompt=prompt_obj.invoke({
    "subject":new_subject,
    "tone":new_tone,
    "lines":lines
})

final_prompt=complete_prompt.text

if st.button("Generate"):
    if final_prompt:
        result=llm.invoke(final_prompt)
        st.write(result.content)
    else:
        st.warning("please submit your question first")