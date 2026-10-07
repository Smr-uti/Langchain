from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

bot = ChatGroq(model="openai/gpt-oss-20b")

dialogue = [
    SystemMessage(content = "You are a helpful AI Tutor."),
    HumanMessage(content = "Tell me about langgraph framework"),
    AIMessage(content = "Langgraph is a framework for building Agentic AI application."),
    HumanMessage(content = "What are its key features?")
]

response = bot.invoke(dialogue)

dialogue.append(AIMessage(content = response.content))

print(dialogue)