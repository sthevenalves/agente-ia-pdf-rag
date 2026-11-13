    # carregar_documentos
    # dividir os documentos em pedaços de texto(chunks)
    # vetorizar os chunks com o processo de embedding

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


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

def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size = 2000, 
        chunk_overlap = 500,
        length_function = len,
        add_start_index = True
    )
    Chunks = separador_documentos.split_documents(documentos)
    return Chunks

criar_db()