import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("ERRO: variável GROQ_API_KEY não encontrada no .env")
    exit(1)

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "Você é um assistente que explica programação de forma clara, simples e com exemplos curtos quando necessário."
)

def perguntar(prompt):
    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500,
    )
    return chat.choices[0].message.content

def main():
    print("=== Assistente de Estudos IA ===\n")

    while True:
        pergunta = input("Pergunte sobre programação (ou digite 'sair' para encerrar):\n> ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break

        resposta = perguntar(pergunta)
        print("\n🤖 Assistente:\n")
        print(resposta + "\n")

if __name__ == "__main__":
    main()
