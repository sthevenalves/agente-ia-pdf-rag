from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

CAMINHO_DB = 'db'

prompt_templet = """
Responda a pergunta do usuário:
{pergunta}

com base nessas informações abaixo:

{base_conhecimento}"""

def perguntar():
    pergunta = input("Escreva sua pergunta: ")

    # carregar o banco de dados
    funcao_embedding = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview"
    )

    db = Chroma(
        persist_directory=CAMINHO_DB,
        embedding_function=funcao_embedding
    )

    # comparar a pergunta do usuario (embedding) com o meu banco de dados
    resultados = db.similarity_search_with_relevance_scores(pergunta, k=3)  
    if len(resultados) == 0 or resultados[0][1] < 0.4:
        print("Nao encontrou informação relevante")
        return

    textos_resultados = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultados.append(texto)
        
    base_conhecimento = "\n\n----\n\n".join(textos_resultados)
    prompt = ChatPromptTemplate.from_template(prompt_templet)
    prompt = prompt.invoke({"pergunta": pergunta, 
                            "base_conhecimento": base_conhecimento})
    
    modelo = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2
)
    texto_resposta = modelo.invoke(prompt).content
    print("Resposta IA: ", texto_resposta)
    
    
perguntar()