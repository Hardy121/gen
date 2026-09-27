from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


chat_template = ChatPromptTemplate([
    # SystemMessage(content="You are a helpful assistant of {company_name}."),
    # HumanMessage(content="What is the current status of my order {order_id}?")

    ('system', "You are a helpful assistant of {company_name}."),
    ('human', "What is the current status of my order {order_id}?")
])

prompt = chat_template.invoke({
    "company_name": "Acme Corp",
    "order_id": "12345"
})

print(prompt)