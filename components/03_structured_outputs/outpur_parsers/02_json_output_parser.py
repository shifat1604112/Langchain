from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template = PromptTemplate(
    template=(
        "Give me 5 facts about {topic}. "
        "Respond ONLY in the following JSON format:\n\n"
        "{format_instruction}"
    ),
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})

# This is already parsed by JsonOutputParser
print(result)
print(type(result))  # Should be a dict