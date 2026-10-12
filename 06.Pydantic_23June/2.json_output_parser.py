from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-20b")
               
tmpl="provide a short report on {topic} \n {format_instruction}"

parser=JsonOutputParser()

prompt_obj=PromptTemplate(template=tmpl,
                          partial_variables={"format_instruction":parser.get_format_instructions()})

final_prompt=prompt_obj.invoke({
    "topic":"climate change"
})

query=final_prompt.text

result=llm.invoke(query)

final_result=parser.invoke(result)

print(final_result)