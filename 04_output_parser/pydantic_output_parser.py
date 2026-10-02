from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini")


class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt= 18, description="Age of the person")
    city: str = Field(description="Name of the city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="""
        Generate the name, age, city of a fictional {place} person.
        {format_instruction}
    """,
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'place': 'indian'})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

final_result = chain.invoke({'place': 'indian'})

print(final_result)