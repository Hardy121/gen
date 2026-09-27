from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()

model = ChatAnthropic(
    model="claude-3.5-sonnet-20241022",
    temperature=1.8,
    max_output_tokens=10
) 

result = model.invoke("Write a short poem about the beauty of nature.")
print(result.content)
