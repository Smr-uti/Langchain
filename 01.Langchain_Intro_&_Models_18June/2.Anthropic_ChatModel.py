from dotenv import load_dotenv
import os
load_dotenv()

from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model = "claude-haiku-4-5-2025-1001")

query = "What is the capital of india?"
result = llm.invoke(query)

print(result)