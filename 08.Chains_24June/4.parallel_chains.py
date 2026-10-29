# Step 1: Groq LLM import करणे
from langchain_groq import ChatGroq

# Step 2: Prompt तयार करण्यासाठी PromptTemplate import करणे
from langchain_core.prompts import PromptTemplate

# Step 3: LLM च्या output ला string मध्ये convert करण्यासाठी parser
from langchain_core.output_parsers import StrOutputParser

# Step 4: दोन independent chains parallel execute करण्यासाठी
from langchain_core.runnables import RunnableParallel

# Step 5: .env file मधील environment variables load करण्यासाठी
from dotenv import load_dotenv


# Step 6: .env file मधील API key load करणे
load_dotenv()


# Step 7: Groq model initialize करणे
# हा model notes आणि quiz generate करेल
llm = ChatGroq(model="openai/gpt-oss-20b")


# Step 8: पहिला prompt तयार करणे
# दिलेल्या text मधून short आणि simple notes तयार होतील
prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text:\n{text}",
    input_variables=["text"]
)


# Step 9: दुसरा prompt तयार करणे
# दिलेल्या text मधून 5 short question-answer तयार होतील
prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text:\n{text}",
    input_variables=["text"]
)


# Step 10: LLM च्या output ला plain string मध्ये convert करणे
parser_obj = StrOutputParser()


# Step 11: Notes आणि quiz एकाच document मध्ये merge करण्यासाठी prompt
# याला notes आणि quiz या दोन inputs ची आवश्यकता आहे
prompt3 = PromptTemplate(
    template=(
        "Merge the provided notes and quiz into a single document.\n"
        "Notes:\n{notes}\n\n"
        "Quiz:\n{quiz}"
    ),
    input_variables=["notes", "quiz"]
)


# Step 12: Parallel chain तयार करणे
# दोन्ही branches एकाच वेळी स्वतंत्रपणे काम करतील
parallel_chain = RunnableParallel(
    {
        # Branch 1: Text घेणे → Prompt तयार करणे → LLM → String output
        "notes": prompt1 | llm | parser_obj,

        # Branch 2: Text घेणे → Prompt तयार करणे → LLM → String output
        "quiz": prompt2 | llm | parser_obj
    }
)


# Step 13: Final chain तयार करणे
# आधी parallel_chain notes आणि quiz तयार करेल
# नंतर prompt3 दोन्ही outputs merge करण्यासाठी वापरला जाईल
# शेवटी LLM merged document तयार करेल आणि parser string देईल
chain = parallel_chain | prompt3 | llm | parser_obj


# Step 14: Input text
# हाच text notes आणि quiz या दोन्ही branches ला दिला जाईल
text = """
Technology Brief: The State of Generative AI (GenAI)

Generative AI (GenAI) is a subset of artificial intelligence
that relies on deep learning models to create original content,
including text, images, video, audio, or software code.

Global Market Adoption & Implementation:

Approximately 54% of global organizations actively deploy GenAI,
and up to 86% maintain active budgets for the technology.

Roughly 80% of organizations have piloted basic productivity
assistants. However, only 5% of customized enterprise systems
successfully reach full production.

Telecommunications, banking, insurance, and retail lead
operational deployment. North America leads in deep enterprise
integration, while APAC and China focus on corporate usage
frameworks and compliance preparation.
"""


# Step 15: पूर्ण chain execute करणे
# "text" हे input_variables मधील key आहे
# invoke() संपूर्ण chain चालवून final output परत करतो
result = chain.invoke({
    "text": text
})


# Step 16: Final merged output print करणे
# यात notes आणि quiz एकाच document मध्ये असतील
print(result)


# Step 17: Chain चा execution graph print करणे
# कोणते components कोणत्या क्रमाने जोडले आहेत ते पाहता येईल
chain.get_graph().print_ascii()