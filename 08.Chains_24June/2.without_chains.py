from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = "Generate 5 intretsing fact about {topic}"
prompt_obj = PromptTemplate(template = prompt, input_variables= ["topic"])

llm = ChatGroq(model = "openai/gpt-oss-20b")

parser_obj = StrOutputParser()

final_prompt = prompt_obj.invoke({
    "topic": "Agentic AI"
})

# print(final_prompt)

result = llm.invoke(final_prompt)

print(result)