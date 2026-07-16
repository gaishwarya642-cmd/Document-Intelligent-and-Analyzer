import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.9
)

def explain_text(text):
    return llm.invoke("Explain the following text:\n" + text).content

def summarize_text(text):
    return llm.invoke("Summarize the following text:\n" + text).content

def generate_questions(text):
    return llm.invoke(
        "Generate 5 important questions from the following text:\n" + text
    ).content