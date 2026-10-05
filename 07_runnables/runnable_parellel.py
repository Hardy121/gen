from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini"
)

parser = StrOutputParser()


prompt = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post tweet about {topic}",
    input_variables=["topic"]
)

parellel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parellel_chain.invoke({
    "topic": "AI"
})

print(result)