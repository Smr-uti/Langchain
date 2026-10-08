from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

bot = ChatGroq(model="openai/gpt-oss-20b")

SYSTEM_ROLE = "You are a helpful AI Tutor, Provide answer in one liner only"

dialogue = [SystemMessage(content=SYSTEM_ROLE)]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    dialogue.append(HumanMessage(content=user_input))
    response = bot.invoke(dialogue)
    ai_text = response.content
    dialogue.append(AIMessage(content=ai_text))
    print(f"AI: {ai_text}")