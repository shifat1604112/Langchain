from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# RunnablePassthrough buffer er moto input tai output a diye de
# so when we need it? suppose amra duita model use krtesi , first er ta details bole, then 2nd
# model details theke summary bole, ekhn amdr main o/p summary ta, so sequntial model kaj ta kore felbe,
# but what if amra details taw print korte chaitesi, amra tokhn RunnableParallel
# a ekta side a RunnablePassthrough onno side a amdr baki summary er kaj ta krbo


prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))