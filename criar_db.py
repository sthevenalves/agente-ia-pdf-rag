    # carregar_documentos
    # dividir os documentos em pedaços de texto(chunks)
    # vetorizar os chunks com o processo de embedding

from langchain_community.document_loaders import PyPDFDirectoryLoader

PASTA_BASE = 'base'

def criar_db():
    documentos = carregar_documentos()
    # chunks = dividir_chunks(documentos)
    # vetorizar_chunks(chunks)
    print(documentos)


def carregar_documentos():
    carregador = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = carregador.load()
    return documentos

    

criar_db()