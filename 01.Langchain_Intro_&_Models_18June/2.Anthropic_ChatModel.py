from dotenv import load_dotenv
import os
load_dotenv()

from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model = "claude-sonnet-4-6")

query = "What is the capital of india?"
result = llm.invoke(query)

print(result)