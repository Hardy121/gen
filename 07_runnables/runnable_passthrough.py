from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini"
)

parser = StrOutputParser()


prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="explain the joke {text}",
    input_variables=["text"]
)


joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2, model, parser) 
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({
    'topic' : 'AI'
})

print(result)