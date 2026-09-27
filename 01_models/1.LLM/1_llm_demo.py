from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4o-mini")


result = llm.invoke("Write a short poem about the beauty of nature.")


print(result)