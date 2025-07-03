# we can send only one string in model.invoke OR 
# chat_hostory or list of string to model.invoke so that model could have the knowledge of prev msges


# but chat history te ektar por ekta msg dhukaite thakle pore ai model bujhbe na kon chat ta kar, konta ai er konta human er 

# ejonno langchain a amra system message, human message , ai message 3 type er msg banaite pari jkono take,
# mane amdr query hbe human msg, ai er reply hbe ai msg,
# and system message is a special type of message that sets the behavior or context for the AI model , jemon eta bole "You’re a helpful assistant" etc

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

chat_history = [
    SystemMessage(content='You are a helpful AI assistant'),   
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history) # full history disi
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)
