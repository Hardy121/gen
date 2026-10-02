from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini")


schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 fact about the topic:{topic}. \n {formate_instructions}",
    input_variables=["topic"],
    partial_variables={'formate_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({"topic": "black hole"})

# result = model.invoke(prompt)

# # print(result)

# final_result = parser.parse(result.content)

# print(final_result)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

final_result = parser.parse(result.content)
print(final_result)
