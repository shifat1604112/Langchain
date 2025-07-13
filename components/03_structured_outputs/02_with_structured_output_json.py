from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# schema -> pydantic er moto same jinish, just json format a likha,
# ei json format a default values and automatic conversation support kore na pydantic er moto

json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by GG
""")

#print(result)

# First, print the type of the result to know if it's a list or dict
print("Type of result:", type(result))
print("Raw result:", result)

if isinstance(result, list) and len(result) > 0:
    item = result[0]
    args = item.get("args", {})
    
    print("Summary:", args.get("summary", "[summary not found]"))
    print("Sentiment:", args.get("sentiment", "[sentiment not found]"))
    print("Pros:", args.get("pros", "[pros not found]"))

# Edge case: unexpected format
else:
    print("Unexpected result format. Cannot extract fields.")



# when we write :

#json_schema = {
 # "title": "Review",
  #"type": "object",
  #"properties": { ... },
  #"required": [ ... ]
#}

# structured_model = model.with_structured_output(json_schema)

#under the hood LangChain treats this JSON schema as a function-like tool definition, and transforms it into something like:

#{
 # "name": "Review",
  #"description": "...",
  #"parameters": {
   # "type": "object",
    #"properties": { ... }
  #}
#}

# and Then, when Gemini responds, it wraps the result as:

#[
 # {
  #  "type": "Review",
   # "args": {
    #  "summary": "...",
     # "sentiment": "pos",
      #...
    #}
  #}
#]

# ejonno 

# item = result[0] -> model ekta response pathacche only
# args = item.get("args", {}) evabe args use krsi