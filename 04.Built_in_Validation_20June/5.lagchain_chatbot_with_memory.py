from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

bot = ChatGroq(model="openai/gpt-oss-20b")

dialogue_logs = []

while True:
    user_msg = input("You:")
    if user_msg.lower() == "exit":
        break
    dialogue_logs.append(user_msg)
    print("logs----->", dialogue_logs)
    reply = bot.invoke(dialogue_logs)
    dialogue_logs.append(reply.content)
    print("logs----->", dialogue_logs)
    
