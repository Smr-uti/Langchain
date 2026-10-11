from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

class ReviewAnalysis(TypedDict):
    summary : Annotated[str,"Provide summary in one line not more that that"]
    sentiment : Annotated[Literal["Positie", "Negative"], "only in positive, negative or neutral"]

structured_output_obj = llm.with_structured_output(ReviewAnalysis)

feedback_input = """ The Amazon app has become frustrating to use. It frequently takes a long time to load product pages, and the search results are often cluttered with sponsored listings, making it difficult to find relevant products. The app occasionally crashes during checkout, which is very inconvenient. Navigation also feels confusing after recent updates, and customer support is not always easy to reach through the app. Overall, the experience needs significant improvement in terms of performance, usability, and reliability"""

result=structured_output_obj.invoke(feedback_input)

print(result)



    
