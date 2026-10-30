from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm= ChatGroq(model="openai/gpt-oss-20b")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a details report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Provide five liner summary on follwing {text} ",
    input_variables=["text"]
)

runnable= RunnableSequence(prompt1,llm,parser,prompt2,llm,parser)

result= runnable.invoke({
    "topic":"Climate change"
})

print(result)

runnable.get_graph().print_ascii()