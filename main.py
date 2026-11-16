from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

CAMINHO_DB = 'db'

prompt_templet = """
Responda a pergunta do usuário:
{pergunta}

com base nessas informações:

{base_conhecimento}

Se você não encontrar a rersposta para a pergunta do usuário nessas informações,
responda não sei te dizer isso"""

def perguntar():
    pergunta = input("Escreva sua pergunta: ")
