from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini"
)

parser = StrOutputParser()


prompt = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

def work_count(text):
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt, model, parser)

parellel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    # 'word_count': RunnableLambda(work_count)
    'word_count': RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain, parellel_chain)

result = final_chain.invoke({
    'topic': 'AI'
})

print(result)