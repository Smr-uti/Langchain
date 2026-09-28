from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash")

response = llm.invoke("Why we use langchain for AI application dedelopment?")
# print(response)
print(response.content)

# query="what is the capital of china?"

# result=llm.invoke(query)

# print(result.content)
