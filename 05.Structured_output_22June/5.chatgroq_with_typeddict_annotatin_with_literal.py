from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

class ReviewAnalysis(TypedDict):
    summary : Annotated[str,"Provide summary in one line not more that that"]
    sentiment : Annotated[Literal["Positie", "Negative"], "only in positive, negative or neutral"]
from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")
class ReviewAnalysis(TypedDict):
    summary:Annotated[str,"Provide summary in 1 line not more than that"]
    sentiment:Annotated[Literal["Positive","Negative","Neutral"],"only in positive , negative and neutral"]
    pros:Annotated[Optional[list[str]],"list of all pros mentioned"]
    cons:Annotated[Optional[list[str]],"list of all cons mentioned"]

structured_output_obj=llm.with_structured_output(ReviewAnalysis)

feedback_input="""
The Amazon app is generally useful for browsing and purchasing products online. It offers a wide selection of items, convenient payment options, and order tracking features. However, the app can sometimes be slow to load, and finding specific products may require scrolling through many sponsored results. While it gets the job done for most shopping needs, there is room for improvement in terms of performance and user experience. Overall, it's an average shopping app that works as expected most of the time."""

result=structured_output_obj.invoke(feedback_input)

#print(result)

print(result["pros"][0])


    




    
