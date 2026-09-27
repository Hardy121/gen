from langchain import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=1.8,
    max_output_tokens=10,    
)

result = model.invoke("Write a short poem about the beauty of nature.")

print(result)


