from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

class  Person(BaseModel):
    name: str
    age: int

parser = PydanticOutputParser(pydantic_object=Person)

llm = ChatOpenAI(model_name="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Please provide a person's name and age in JSON format."),
])

chain = prompt | llm | parser

result = chain.invoke({})

print(result)