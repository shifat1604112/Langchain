# close source model usage

# close source models -> provider give api and have to communicate through it, eg : gemini,openAI

# open source models ->  can be downloaded and then can be used / or can be used by higgingface api key
# nothing to upload on the provider server,so secured, eg : LLaMA, Falcon, Bloom
# but if run locally need very good HW :(, need setup, lack of RLHF(not fine tuned with human feedbacks for better response), limited multimodal ability :(


#https://python.langchain.com/api_reference/google_genai/chat_models/langchain_google_genai.chat_models.ChatGoogleGenerativeAI.html#langchain_google_genai.chat_models.ChatGoogleGenerativeAI

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
# other param need to be checked, eg : temperature(if it is 0 then o/p always same for same i/p, if more than 0 depending on the value o/p will vary every time we invoke)

result = model.invoke('what is langchain')

print(result.content)