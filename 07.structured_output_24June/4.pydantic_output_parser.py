from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal, Annotated, Optional
from dotenv import load_dotenv

# .env फाईल मधील API key लोड करा
load_dotenv()

# Groq मधील AI मॉडेल सुरू करा
llm = ChatGroq(model="openai/gpt-oss-20b")

# AI ने उत्तर कोणत्या फॉरमॅटमध्ये द्यायचे त्याचा (Class) तयार करा
class ReviewAnalysis(BaseModel):
    # summary: किमान २० अक्षरांचा छोटा सारांश असला पाहिजे
    summary: str = Field(min_length=20, description="short summary")
    # sentiment: उत्तर फक्त "Positive", "Negative" किंवा "Neutral" यापैकीच एक असावे
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(description="sentiment of the review")
    pros:Annotated[Optional[list[str]],"list of all pros mentioned"]
    cons:Annotated[Optional[list[str]],"list of all cons mentioned"]

# Pydantic ऑब्जेक्टचा वापर करून Parser तयार करा
parser_obj = PydanticOutputParser(pydantic_object=ReviewAnalysis)

# प्रॉम्प्टचा साचा (Template) तयार करा
prompt = "This is the review:{review} \n {format_instruction}"

prompt_obj = PromptTemplate.from_template(prompt)

prompt_obj = prompt_obj.partial(format_instruction= {"format_instruction":parser_obj.get_format_instructions()})

# प्रॉम्प्टमध्ये नियमांच्या सूचना (format_instructions) जोडा
# prompt_obj = PromptTemplate(
#     template=prompt, 
#     partial_variables={"format_instructions": parser_obj.get_format_instructions()}
# )

# विश्लेषणासाठी दिलेला युझरचा रिव्ह्यू (Feedback Input)
feedback_input = "The Amazon app is generally useful for browsing and purchasing products online. It offers a wide selection of items, convenient payment options, and order tracking features. However, the app can sometimes be slow to load, and finding specific products may require scrolling through many sponsored results. While it gets the job done for most shopping needs, there is room for improvement in terms of performance and user experience. Overall, it's an average shopping app that works as expected most of the time."

# प्रॉम्प्टमध्ये रिव्ह्यूची माहिती भरून फायनल प्रॉम्प्ट तयार करा
final_prompt = prompt_obj.invoke(
    {
        "review": feedback_input
    }
)

# AI मॉडेलला प्रॉम्प्ट पाठवून उत्तर मिळवा
response = llm.invoke(final_prompt)

# AI कडून आलेले उत्तर Pydantic नियमांनुसार पार्स (Parse) करा
final_response = parser_obj.invoke(response)

# अंतिम निकाल प्रिंट करा
print(final_response)