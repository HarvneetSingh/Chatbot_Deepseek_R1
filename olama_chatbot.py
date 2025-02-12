from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

##prompt  Template
prompt = ChatPromptTemplate.from_messages([("system","You are a helpful assistant."),
                                           ("user","Questions:{Queries}")])

#streamlit framework
st.title('langchain Deepseek r1 chatbot')
input_text = st.text_input("search the topic u want")

#calling the llama2 LLm
llm = Ollama(model="deepseek-r1")
output_parser = StrOutputParser()

chain = LLMChain(prompt = prompt,llm = llm, output_parser = output_parser)

if input_text:
    st.write(chain.invoke({'Queries':input_text}))
