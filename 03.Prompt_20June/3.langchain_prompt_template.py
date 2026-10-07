from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# stored the prompt in tmpl  variable.
tmpl = "Write a poem about {subject} in a {tone} tone with {lines} lines"

prompt_obj = PromptTemplate(
    template = tmpl 
)

subject = input("Provide a subject:")
tone = input("Provide a mood/tone:")
lines = input("Enter the lines of the poem:")

complete_prompt = prompt_obj.invoke({
    "subject":subject,
    "tone":tone,
    "lines":lines
})

# print(complete_prompt)

final_prompt = complete_prompt.text

llm = ChatGroq(model="openai/gpt-oss-20b")

result = llm.invoke(final_prompt)

print(result.content)