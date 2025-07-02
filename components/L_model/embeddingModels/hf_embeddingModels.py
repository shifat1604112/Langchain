# embedding models generate embeddings for the given sequence input

#Currently, LangChain does not provide a built-in wrapper to use Hugging Face remote inference API for embeddings directly

# so need to download locally and get the embeddings

import os
from langchain_huggingface import HuggingFaceEmbeddings

# Set the custom cache directory before loading the model --- it will create a folder like : /Users/shifat/Personal/ML_AI_DL/GENAI/Langchain/models/sentence-transformers/
os.environ["TRANSFORMERS_CACHE"] = "/Users/shifat/Personal/ML_AI_DL/GENAI/Langchain/models"

# Load the embedding model (this will download into your custom path)
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Name of my country is bangladesh",
    "Dhaka is capital of bangladesh",
    "Chattogram is the best city of Bangladesh"
]

vector = embedding.embed_documents(documents)

#if want to get embedding for single line
# text = "Dhaka is capital of bangladesh"
# vector = embedding.embed_query(text)

print(str(vector))