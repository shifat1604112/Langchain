# majhe majhe emon hoy j customer chatbot er sathe kotha boltese,
# then porer din eshe abr query korle chatbot er ager history o thakte hbe
# naile correctly ans krte parbena, ei kaj ta message place holder diye kora jabe

# suppose ager chat history chat_history.txt te save ase
# now user will query again jeta agertar upor dependent o



from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), # <<<MessagesPlaceholder
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt) ## made a dynamic prompt using MessagePlaceholder and ChatPromptTemplate
