
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm_obj = HuggingFaceEndpoint(repo_id="Qwen/Qwen3-8B")

chat = ChatHuggingFace(llm=llm_obj)

response = chat.invoke("What is the capital of shrilanka?")
print(response.content)