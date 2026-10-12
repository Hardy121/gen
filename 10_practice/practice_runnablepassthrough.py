from dotenv import load_dotenv

# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()


# --------------------------------------------------
# 1. Model
# --------------------------------------------------

model = ChatOpenAI(
    model="gpt-4o-mini"
)


# --------------------------------------------------
# 2. Fake Retriever
# --------------------------------------------------

documents = {
    "kubernetes": """
    Kubernetes is a container orchestration platform.
    It is used to deploy, manage, scale, and monitor
    containerized applications.
    """,

    "docker": """
    Docker is a platform used to package applications
    and their dependencies into containers.
    """,

    "jenkins": """
    Jenkins is an automation server commonly used for
    CI/CD pipelines.
    """
}


def retriever(question):
    """
    Very simple fake retriever.

    In a real RAG application this would be:
        Vector Database
            ↓
        Similarity Search
            ↓
        Documents
    """

    question = question.lower()

    if "kubernetes" in question:
        return documents["kubernetes"]

    elif "docker" in question:
        return documents["docker"]

    elif "jenkins" in question:
        return documents["jenkins"]

    return "No relevant document found."


# --------------------------------------------------
# 3. Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template("""
You are a helpful technical assistant.

Answer the user's question using the provided context.

Context:
{context}

Question:
{question}

Give a simple and accurate answer.
""")


# --------------------------------------------------
# 4. Parser
# --------------------------------------------------

parser = StrOutputParser()


# --------------------------------------------------
# 5. Create the Chain
# --------------------------------------------------

chain = (
    {
        "question": RunnablePassthrough(),
        "context": retriever
    }
    | prompt
    | model
    | parser
)


# --------------------------------------------------
# 6. Invoke the Chain
# --------------------------------------------------

question = "What is CI/CD?"

response = chain.invoke(question)

print("\nFinal Answer:")
print(response)