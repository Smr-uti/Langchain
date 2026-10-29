# Import Groq LLM to use a language model
from langchain_groq import ChatGroq

# Import PromptTemplate to create dynamic prompts
from langchain_core.prompts import PromptTemplate

# Import StrOutputParser to convert the LLM response into a string
from langchain_core.output_parsers import StrOutputParser

# Import load_dotenv to load environment variables from the .env file
from dotenv import load_dotenv

# Load environment variables, such as the Groq API key
load_dotenv()

# Initialize the Groq LLM with the specified model
llm = ChatGroq(model="openai/gpt-oss-20b")

# Create the first prompt to generate a detailed report on a given topic
prompt_obj1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]  # Variable required by the first prompt
)

# Initialize the output parser
parser_obj = StrOutputParser()

# Create the second prompt to generate a five-point summary from the report
prompt_obj2 = PromptTemplate(
    template="Generate a 5-point summary from the following text:\n{text}",
    input_variables=["text"]  # Variable containing the detailed report
)

# Connect all components sequentially using the LCEL pipe operator
# Step 1: Generate a prompt
# Step 2: Generate a detailed report using the LLM
# Step 3: Convert the report into a string
# Step 4: Create a summary prompt using that report
# Step 5: Generate the summary and convert it into a string
chain = prompt_obj1 | llm | parser_obj | prompt_obj2 | llm | parser_obj

# Execute the complete chain by providing the topic as input
result = chain.invoke({
    "topic": "climate change"
})

# Display the final five-point summary
print(result)

# Display the chain workflow as an ASCII graph
chain.get_graph().print_ascii()