# chatbot1 a amra system message ta static banaisi age theke
# amra chaile dynamic banaite pari PromptTemplate er moto
# we will use ChatPromptTemplate class to create dynamic chat history

from langchain_core.prompts import ChatPromptTemplate

# instead of using 
# chat_template = ChatPromptTemplate([
  # SystemMessage(content="You are a helpful {domain} expert"),
  # HumanMessage(content="Explain in simple terms, what is {topic}")
#]

# we need to use like below tuple, SystemMessage er bodle system and HumanMessage er place a human use krte hbe as per documentation
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'}) # we can create dynamically chat history

print(prompt)

