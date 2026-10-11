from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

class ReportReview(TypedDict):
    Title : str
    Overview : str
    disadvantage : str
    remedy : str

structured_model=llm.with_structured_output(ReportReview)

# query="provide a report on climate change"

# result1=llm.invoke(query)

input="""
## Short Report on Climate Change

Climate change refers to long-term shifts in global temperatures and weather patterns. While climate has changed naturally over Earth’s history, current climate change is mainly driven by human activities, especially the burning of fossil fuels such as coal, oil, and gas. These activities release greenhouse gases, including carbon dioxide and methane, which trap heat in the atmosphere.

The effects of climate change are already being observed worldwide. Global temperatures are rising, glaciers and ice sheets are melting, sea levels are increasing, and extreme weather events such as heatwaves, droughts, floods, and storms are becoming more frequent and intense. Climate change also threatens ecosystems, agriculture, water supplies, and human health.

To address climate change, countries and communities need to reduce greenhouse gas emissions by using renewable energy, improving energy efficiency, protecting forests, and adopting cleaner transportation. Adaptation is also important, including building climate-resilient infrastructure, improving disaster preparedness, and protecting vulnerable communities.

In conclusion, climate change is one of the most serious global challenges today. Urgent action is needed from governments, businesses, and individuals to reduce its impacts and protect the planet for future generations.
"""

result=structured_model.invoke(input)

print(result)