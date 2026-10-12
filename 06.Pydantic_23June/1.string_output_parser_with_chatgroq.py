from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

result = llm.invoke("what is the capital of Iran?")

parser_obj = StrOutputParser()

final_result = parser_obj.invoke(result)

print(final_result)