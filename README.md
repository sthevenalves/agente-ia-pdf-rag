# Agente de IA com Python — RAG com LangChain

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=langchain&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-FF6F00)
![RAG](https://img.shields.io/badge/Architecture-RAG-6A5ACD)
![PyPDF](https://img.shields.io/badge/PDF-PyPDF-DC143C)
![License](https://img.shields.io/badge/license-MIT-green)

Projeto de um agente de Inteligência Artificial capaz de consultar documentos PDF e responder perguntas com base nas informações encontradas neles. A aplicação utiliza a arquitetura **RAG (Retrieval-Augmented Generation)**, integrando LangChain, Google Gemini e ChromaDB.

## Objetivo

Desenvolver uma aplicação que permita ao usuário fazer perguntas sobre documentos PDF, recuperando informações relevantes e utilizando um modelo de linguagem para elaborar respostas contextualizadas.

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **LangChain:** integração e organização do fluxo de processamento com modelos de linguagem.
- **Google Gemini:** geração de respostas e criação de embeddings.
- **ChromaDB:** armazenamento e recuperação de vetores.
- **PyPDF:** extração de conteúdo dos arquivos PDF.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

## Como funciona

O projeto é dividido em duas etapas principais:

### 1. Criação do banco vetorial (`criar_db.py`)

Responsável pelo processamento dos documentos e armazenamento das informações.

1. Carregamento dos arquivos PDF presentes na pasta `base`.
2. Extração do conteúdo dos documentos.
3. Divisão do conteúdo em pequenos trechos (*chunks*).
4. Geração de embeddings utilizando o Google Gemini.
5. Armazenamento dos vetores no ChromaDB.

Configurações utilizadas na divisão dos documentos:

- `chunk_size`: 2000 caracteres.
- `chunk_overlap`: 500 caracteres.

### 2. Consulta aos documentos (`main.py`)

Responsável pela recuperação das informações e geração das respostas.

1. Recebe uma pergunta do usuário.
2. Converte a pergunta em embedding.
3. Realiza uma busca por similaridade no ChromaDB.
4. Recupera os três trechos mais relevantes.
5. Aplica um filtro de relevância mínima de 0.4.
6. Organiza os trechos recuperados em um contexto.
7. Utiliza `ChatPromptTemplate` para estruturar o prompt.
8. Envia a pergunta e o contexto ao Google Gemini.
9. Exibe a resposta gerada pela IA.

## Estrutura do projeto

```text
agente-ia-pdf-rag/
│
├── base/
│   └── documentos.pdf
│
├── db/
│   └── banco vetorial
│
├── .venv/
│
├── .env
├── .gitignore
├── requirements.txt
├── criar_db.py
└── main.py
```

## Instalação e configuração

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd agente-ia-pdf-rag
```

### 2. Crie e ative o ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_API_KEY=sua_chave_api
```

A chave pode ser obtida no [Google AI Studio](https://aistudio.google.com/api-keys).

**Importante:** não compartilhe sua chave de API nem envie o arquivo `.env` para o GitHub.

### 5. Adicione os documentos PDF

Coloque os arquivos PDF que deseja consultar dentro da pasta `base/`.

### 6. Crie o banco vetorial

Execute:

```bash
python criar_db.py
```

Esse processo irá carregar os documentos, dividi-los em chunks, gerar os embeddings e armazená-los no ChromaDB.

### 7. Execute o agente

Após a criação do banco, execute:

```bash
python main.py
```

Digite sua pergunta no terminal para receber uma resposta baseada nos documentos processados.

## Variáveis e configurações

| Configuração | Descrição |
|---|---|
| `CAMINHO_DB` | Diretório do banco vetorial |
| `PASTA_BASE` | Diretório dos documentos PDF |
| `chunk_size` | Quantidade máxima de caracteres por trecho |
| `chunk_overlap` | Sobreposição entre os trechos |
| `k=3` | Quantidade de documentos recuperados |
| `0.4` | Limite mínimo de relevância configurado |

## Conceitos aplicados

- Recuperação aumentada por geração (RAG).
- Embeddings e representação vetorial.
- Busca por similaridade semântica.
- Processamento e divisão de documentos.
- Engenharia de prompts.
- Integração com modelos de linguagem (LLMs).
- Banco de dados vetorial.
