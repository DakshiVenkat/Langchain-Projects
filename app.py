from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server",
    path="/openai"
)

llm=Ollama(model="qwen2:0.5b")


prompt2=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")


add_routes(
    app,
    prompt2|llm,
    path='/essay'
)

if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000)
