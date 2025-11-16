import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.title('🤖 Assistente de Estudos IA')

if not GROQ_API_KEY:
    st.error('GROQ_API_KEY não encontrada. Copie .env.example para .env e cole sua chave.')
else:
    client = Groq(api_key=GROQ_API_KEY)

    pergunta = st.text_area('Digite sua dúvida sobre programação', height=120)

    if st.button('Perguntar') and pergunta.strip():
        with st.spinner('Consultando o modelo...'):
            chat = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "Explique programação de forma simples, com exemplos."},
                    {"role": "user", "content": pergunta}
                ],
                temperature=0.2,
                max_tokens=500
            )
            resposta = chat.choices[0].message.content
            st.markdown("**Resposta:**")
            st.write(resposta)
