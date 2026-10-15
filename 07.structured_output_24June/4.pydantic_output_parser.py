from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-20b")

class ReviewAnalysis(BaseModel):
    summary: str=Field(min_length = 20, description = "short summary")
    sentiment: Literal["Positive", "Negative", "Neutral"]= Field(description="sentiment of the review")

parser_obj = PydanticOutputParser(pydantic_object = ReviewAnalysis)

prompt = "This is the review:{review} \n {format_instructions}"

prompt_obj = PromptTemplate(template = prompt, partial_variables={"format_instructions": parser_obj.get_format_instructions()})

feedback_input = "The Amazon app is generally useful for browsing and purchasing products online. It offers a wide selection of items, convenient payment options, and order tracking features. However, the app can sometimes be slow to load, and finding specific products may require scrolling through many sponsored results. While it gets the job done for most shopping needs, there is room for improvement in terms of performance and user experience. Overall, it's an average shopping app that works as expected most of the time."

final_prompt = prompt_obj.invoke(
    {
        "review":feedback_input
    }
)

response = llm.invoke(final_prompt)
final_response = parser_obj.invoke(response)
print(final_response)