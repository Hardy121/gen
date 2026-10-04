from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI(
    model="gpt-4o-mini"
)

model2 = ChatOpenAI(
    model="gpt-4o-mini"
)

prompt1 = PromptTemplate(
    template="Generate Short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate a short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into single document \n notes -> {notes} and quize -> quiz {quiz}",
    input_variables=['notes', 'quiz']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz':  prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """

Act as an expert study assistant. Based on the text provided below, generate two things:

1. Short and simple notes summarizing the key points using bullet points.
2. Short question and answer pairs (Q&A) covering the most important concepts for quick revision.
On kubernetes
    """

result = parallel_chain.invoke({
    'text': text
})

print(result)
chain.get_graph().print_ascii()

