from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

tmpl = "Write a report about {subject} in a {tone} tone with {lines} lines"

prompt_obj = PromptTemplate(template = tmpl)

prompt_obj.save("report_template.json")