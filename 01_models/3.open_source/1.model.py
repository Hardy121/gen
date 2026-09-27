from langchain_huggingface import ChatHuggingFaceHub, HuggingFaceEndPoint
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndPoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"    
)

model = ChatHuggingFaceHub(
    llm=llm
)

result = model.invoke('Who is pm of india')

print(result.content )