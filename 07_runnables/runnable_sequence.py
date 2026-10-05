from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI(
    model="gpt-4o-mini"
)

parser = StrOutputParser()


prompt2 = PromptTemplate(
    template="explain the joke {text}",
    input_variables=["text"]
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "Web development"})

print(result)