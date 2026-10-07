from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

length = input("Enter a length of the report (short/medium/long):")
subject = input("Provide a subject on which you want to create a report:")

prompt = "Provide {} report on {}." .format(length,subject)

result = llm.invoke(prompt)

print(result.content)