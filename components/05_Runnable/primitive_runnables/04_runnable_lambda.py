from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Runnable is like lego block, input runnable ouput o ekta runnable,
# so that we can attach any runnable to other runnables
# suppose amra ekta pain output pacchi, but sheta runnable er sathe mananor jonno we need to make that plain into Runnable
# that when RunnableLambda becomes handy eg :  following example we are using word_count Int output, and we are making
# the Int into runnable by using 'word_count': RunnableLambda(word_count)


def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)
