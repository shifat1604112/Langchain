# we are using the api to talk with the model

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1", # from hf goto models, then take a model for text generation, goto that model, copy the path
    task="text-generation" # need to specify the task of the model
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is langchain")

print(result.content)