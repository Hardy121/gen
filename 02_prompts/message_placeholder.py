from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate


# chat_template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('user', '{input}')
])

# load chat history
chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({'chat_history': chat_history, 'input': 'What is the capital of France?'})

print(prompt)

