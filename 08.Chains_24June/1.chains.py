from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = "Generate 5 interesting fact about {topic}"

prompt_obj = PromptTemplate(template = prompt)

llm = ChatGroq(model = "openai/gpt-oss-20b")

parser_obj = StrOutputParser()

chain = prompt_obj | llm | parser_obj

result = chain.invoke({
    "topic": "climate change"
})

print(result)

chain.get_graph().print_ascii()