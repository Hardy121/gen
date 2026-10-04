from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda


load_dotenv()


model = ChatOpenAI(
    model="gpt-4o-mini"
)

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the wonderful of the feedback.")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template="Classify the sentiments of the following feedback text into positive or negative. \n {feedback} \n {formate_instruction}",
    input_variables=['feedback'],
    partial_variables={'formate_instruction' : parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback': 'This is a terrible smartphone.'})

# print(result.sentiment)

positive_prompt = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback'],
)

negative_prompt = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback'],
)


branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive" , positive_prompt | model | parser ),
    (lambda x:x.sentiment == "negative" , negative_prompt | model | parser),
    RunnableLambda(lambda x:"could not find sentiments")
)


chain = classifier_chain | branch_chain

result = chain.invoke({"feedback":'This is a wonderful smartphone'})

print(result)
chain.get_graph().print_ascii()