from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage
)
from dotenv import load_dotenv


# 1. Load environment variables
load_dotenv()

# 2. Create the LLM
model = ChatOpenAI(
    model="gpt-4o-mini"
)

# 3. Define structured output
class BotResponse(BaseModel):
    answer: str = Field(
        description="The answer to the user's question."
    )
    topic: str = Field(
        description="The topic of the user's question."
    )
    confidence: str = Field(
        description="How confident the AI is: high, medium, or low"
    )

# 4. Tell the model to use structured output
structured_model = model.with_structured_output(
    BotResponse
)

# 5. Create ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages(
    [
    (
        "system",
        """
        You are a helpful GenAI and DevOps teacher.

        Rules:
        - Explain concepts clearly.
        - Prefer beginner-friendly explanations.
        - Give examples when useful.
        - If the user asks a technical question,
          explain the concept before giving code.
        """
    ),
    MessagesPlaceholder(
        variable_name="history"
    ),
    (
        "human",
        "{question}"
    )
])
print(chat_prompt)
# 6. Create chain

chain = chat_prompt | structured_model


# 7. History
history = []

# 8. Start chatbot
print("GenAI Bot started!")
print("Type 'exit' to stop.\n")


while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye")
        break

    # Send question + history to LLM

    response = chain.invoke({
        "history": history,
        "question": question
    })
 
    print(f"\nBot: {response.answer}")
    print(f"Topic: {response.topic}")
    print(f"Confidence: {response.confidence}\n")

    # Store conversation
    history.append(
        HumanMessage(
            content=question
        )
    )

    history.append(
        AIMessage(
            content=response.answer
        )
    )


print(history)