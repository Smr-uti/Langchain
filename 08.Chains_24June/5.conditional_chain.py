from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

class Feedback(BaseModel):
    sentiment:Literal["positive","negative"]=Field(description="give the sentiment of the feedback")

llm = ChatGroq(model= "openai/gpt-oss-20b")

parser_obj= StrOutputParser()

parser_obj2= PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(
    template ="classify the sentiment of following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"], 
    partial_variables={"format_instruction":parser_obj2.get_format_instructions()}
)

classifier_chain= prompt1 | llm | parser_obj2

prompt2=PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback} ",
    input_variables=["feedback"]
)

prompt3=PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback} ",
    input_variables=["feedback"]
)

branch_chain= RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | llm | parser_obj),
    (lambda x:x.sentiment == "negative", prompt3 | llm | parser_obj),
    RunnableLambda( lambda x: "Could not fine sentiment")
)

chain= classifier_chain | branch_chain

result= chain.invoke({ 
    "feedback": "This is the very good phone"
})

print(result)

chain.get_graph().print_ascii()