from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template = "generate 5 sentence of {topic}",
    input_variables=["topic"]  
)

model = ChatOpenAI(
    model="gpt-4o-mini"
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "Kubernetes"
})

print(result)
chain.get_graph().print_ascii()