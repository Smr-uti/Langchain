import os
from dotenv import load_dotenv

load_dotenv(override = True)

api_key = os.getenv("GROQ_API_KEY")

print("api key loaded successfully", api_key[0:20])

from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-20b")

result = llm.invoke("Skincare Routine for 30 year old women")

print(result)
