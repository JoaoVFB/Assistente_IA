# 🤖 Assistente de Estudos (Groq + Llama 3.1)

Este projeto implementa um assistente de estudos focado em programação, utilizando a **Groq API** para inferência de modelos de linguagem de grande escala (LLMs) com alta velocidade. O assistente pode ser executado tanto via linha de comando (`main.py`) quanto como uma aplicação web interativa, utilizando o **Streamlit** (`streamlit_app.py`).

O modelo de linguagem utilizado é o **Llama 3.1 8B Instant**, conhecido por seu excelente desempenho e otimização para a arquitetura Groq.

## ✨ Funcionalidades

*   **Resposta Rápida:** Utiliza a Groq API para obter respostas em tempo real.
*   **Modelo Otimizado:** Implementado com o modelo `llama-3.1-8b-instant`.
*   **Interface Dupla:**
    *   **CLI (`main.py`):** Interface simples via terminal para testes rápidos.
    *   **Web App (`streamlit_app.py`):** Interface gráfica interativa construída com Streamlit.
*   **Assistente de Programação:** Configurado com um *system prompt* para explicar conceitos de programação de forma clara e com exemplos.

## 🛠️ Pré-requisitos

Certifique-se de ter o Python 3.9+ instalado em seu sistema.

## ⚙️ Instalação

1.  **Clone o repositório** (ou descompacte o arquivo do projeto).
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Assistente_ia_hf
    ```
3.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

## 🔑 Configuração da API Key

O projeto utiliza a biblioteca `python-dotenv` para gerenciar a chave de API de forma segura.

1.  **Obtenha sua chave de API** no console da Groq.
2.  **Crie o arquivo `.env`:** Copie o arquivo `.env.example` e renomeie a cópia para `.env`.
    ```bash
    cp .env.example .env
    ```
3.  **Edite o arquivo `.env`** e insira sua chave de API:
    ```
    GROQ_API_KEY=gsk_SUA_CHAVE_AQUI
    ```

## 🚀 Como Executar

Você tem duas opções para rodar o assistente:

### 1. Via Linha de Comando (CLI)

Execute o arquivo `main.py` no seu terminal:

```bash
python main.py
```

O programa entrará em um loop de perguntas e respostas. Digite `sair` para encerrar.

### 2. Via Aplicação Web (Streamlit)

Execute o arquivo `streamlit_app.py` usando o Streamlit:

```bash
streamlit run streamlit_app.py
```

O Streamlit iniciará um servidor local e abrirá a aplicação no seu navegador (geralmente em `http://localhost:8501`).

## 📂 Estrutura do Projeto

```
Assistente_ia_hf/
├── .env.example
├── .gitignore
├── main.py             # Versão CLI do assistente
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do Python
└── streamlit_app.py    # Versão Web (Streamlit) do assistente
```

## ⚠️ Solução de Problemas (Troubleshooting)

Se você estiver migrando de uma versão anterior ou encontrou erros de execução, as seguintes correções foram aplicadas:

| Problema Original | Causa | Solução Aplicada |
| :--- | :--- | :--- |
| `groq.BadRequestError: ... gemma2-9b-it has been decommissioned` | O modelo `gemma2-9b-it` foi descontinuado pela Groq. | Substituído pelo modelo **`llama-3.1-8b-instant`**. |
| `TypeError: 'ChatCompletionMessage' object is not subscriptable` | Tentativa de acessar o conteúdo da mensagem como um dicionário. | Alterado o acesso para a sintaxe de objeto: `chat.choices[0].message.content`. |

Certifique-se de que seus arquivos `main.py` e `streamlit_app.py` contenham o modelo e a sintaxe de acesso à resposta atualizados.
