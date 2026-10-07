from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

tmpl="write a poem about {subject} in a {tone} tone with {lines} lines"

prompt_obj=PromptTemplate(
    template=tmpl
)

subject=input("provide a subject:")
tone=input("provide a mood/tone:")


complete_prompt=prompt_obj.invoke({
    "subject":subject,
    "tone":tone,
})

#print(complete_prompt)

final_prompt=complete_prompt.text

llm=ChatGroq(model="openai/gpt-oss-20b")

result=llm.invoke(final_prompt)

print(result.content)