import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

query = "Provide report on climate change?"

result = llm.invoke(query)

print(result.content)