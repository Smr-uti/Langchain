
# AI च्या output ला JSON format मध्ये parse करण्यासाठी JsonOutputParser import करतो
from langchain_core.output_parsers import JsonOutputParser

# Prompt template तयार करण्यासाठी PromptTemplate import करतो
from langchain_core.prompts import PromptTemplate

# Groq वरील AI model वापरण्यासाठी ChatGroq import करतो
from langchain_groq import ChatGroq

# .env file मधील environment variables load करण्यासाठी import करतो
from dotenv import load_dotenv

# .env file मधील variables load करतो
load_dotenv()

# Groq वरील AI model initialize करतो
llm = ChatGroq(model="openai/gpt-oss-20b")

# AI ला कोणत्या topic वर report द्यायचा आहे
# आणि output कोणत्या format मध्ये हवा आहे, हे सांगणारा prompt तयार करतो
tmpl = "provide a short report on {topic} \n {format_instruction}"

# AI च्या output साठी JSON format च्या सूचना मिळवण्यासाठी
# JsonOutputParser चा object तयार करतो
parser = JsonOutputParser()

# PromptTemplate तयार करतो
prompt_obj = PromptTemplate(
    template=tmpl,

    # JSON output format च्या सूचना आधीच सेट करतो
    # त्यामुळे त्या invoke करताना पुन्हा द्याव्या लागत नाहीत
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

# Topic ची value देऊन पूर्ण prompt तयार करतो
final_prompt = prompt_obj.invoke({
    "topic": "climate change"
})

# तयार केलेल्या prompt मधील text query मध्ये store करतो
query = final_prompt.text

# Query AI model ला पाठवून response मिळवतो
result = llm.invoke(query)

# AI च्या response मधून content घेऊन JSON format मध्ये parse करतो
final_result = parser.invoke(result)

# अंतिम structured output स्क्रीनवर दाखवतो
print(final_result)
