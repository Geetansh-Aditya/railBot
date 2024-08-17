from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are an Indian Railways complaint help assistant named Sahayak. "
         "Once sufficient information is collected, you will store the user prompt and reply to the user with a relieving message."),
        ("user", "Question:{question}")
    ]
)

llm = Ollama(model="llama3:8b")
output_parser = StrOutputParser()

def process_message(question: str) -> str:
    chain = prompt | llm | output_parser
    output = chain.invoke({'question': question})
    return output

class MessageRequest(BaseModel):
    message: str

@app.post("/chatbot/")
async def chatbot_endpoint(request: MessageRequest):
    user_message = request.message
    response = process_message(user_message)
    return {"reply": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
