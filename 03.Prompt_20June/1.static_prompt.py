print("Start Program")
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

result = llm.invoke("Provide report on climate change?")

print(result)