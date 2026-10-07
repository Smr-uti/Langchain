# load_prompt is used to load a saved PromptTemplate from a file
from langchain_core.prompts import load_prompt

# ChatGroq is used to connect with Groq LLM
from langchain_groq import ChatGroq

# load_dotenv is used to load API keys from .env file
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Load the saved prompt template from JSON file
loaded_prompt = load_prompt("report_template.json")


# Print the loaded prompt template
print(loaded_prompt)


# Take subject input from the user
subject = input("Provide a subject: ")


# Take mood/tone input from the user
tone = input("Provide a mood/tone: ")


# Take number of lines from the user
# int() converts the input from string to integer
lines = int(input("Enter lines of the poem to create: "))


# Fill the prompt template with user-provided values
complete_prompt = loaded_prompt.invoke({
    "subject": subject,
    "tone": tone,
    "lines": lines
})


# Extract the actual text prompt from PromptValue
final_prompt = complete_prompt.text


# Create the Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


# Send the final prompt to the LLM
result = llm.invoke(final_prompt)


# Print the LLM-generated response
print(result.content)