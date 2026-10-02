from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


model = ChatOpenAI(model_name="gpt-4o-mini")


template =  PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]

)

template1 =  PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]

)

prompt1 = template.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)
print(result.content)
prompt2 = template1.invoke({'text': result.content})

result1 = model.invoke(prompt2)

print(result1.content)