from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)


prompt1 = ChatPromptTemplate.from_template(
    """
    Explain {topic} in technical terms.
    """
)


prompt2 = ChatPromptTemplate.from_template(
    """
    Convert this explanation into beginner-friendly language:

    {explanation}
    """
)


def create_explanation_input(text):
    return {
        "explanation": text
    }


chain = (
    prompt1
    | model
    | StrOutputParser()
    | RunnableLambda(create_explanation_input)
    | prompt2
    | model
    | StrOutputParser()
)


result = chain.invoke({
    "topic": "Kubernetes"
})

print(result)

# RunnableLambda converts the normal python functions into langchain chain/function 