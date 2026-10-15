
# Groq वरील LLM model वापरण्यासाठी ChatGroq import करतो
from langchain_groq import ChatGroq

# Structured output तयार करण्यासाठी Parser आणि Schema import करतो
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

# Prompt template तयार करण्यासाठी PromptTemplate import करतो
from langchain_core.prompts import PromptTemplate

# .env file मधील environment variables load करण्यासाठी import करतो
from dotenv import load_dotenv

# .env file मधील variables load करतो
load_dotenv()

# AI कडून कोणत्या प्रकारचा output हवा आहे,
# त्यासाठी schema तयार करतो
schema = [
    ResponseSchema(name="fact1", description="First fact about the topic"),
    ResponseSchema(name="fact2", description="Second fact about the topic"),
    ResponseSchema(name="fact3", description="Third fact about the topic"),
]

# Groq वरील AI model initialize करतो
llm = ChatGroq(model="openai/gpt-oss-20b")

# Schema च्या आधारे structured output parser तयार करतो
parser_obj = StructuredOutputParser.from_response_schemas(schema)

# AI ला topic आणि output format च्या सूचना देणारा prompt तयार करतो
prompt = "Write three facts about {topic} \n {format_instructions}"

# Parser कडून मिळणाऱ्या format instructions prompt मध्ये
# आधीच सेट करतो, त्यामुळे त्या invoke करताना पुन्हा द्याव्या लागत नाहीत
prompt_obj = PromptTemplate(
    template=prompt,
    partial_variables={
        "format_instructions": parser_obj.get_format_instructions()
    }
)

# Topic ची value देऊन final prompt तयार करतो
prompt = prompt_obj.invoke({
    "topic": "impact of climate change on human"
})

# तयार केलेला prompt AI model ला पाठवून response मिळवतो
response = llm.invoke(prompt)

# AI च्या response ला schema नुसार structured data मध्ये parse करतो
final_response = parser_obj.invoke(response)

# अंतिम structured output स्क्रीनवर दाखवतो
print(final_response)
