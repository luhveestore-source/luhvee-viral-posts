import streamlit as st
import random
import datetime

st.set_page_config(page_title="LuhVee PRO", layout="centered")

st.title("🔥 Robô LuhVee PRO")
st.caption("Automação de vendas para afiliados 🚀")

# ===== ESTADOS =====
if "historico" not in st.session_state:
    st.session_state.historico = []

if "favoritos" not in st.session_state:
    st.session_state.favoritos = []

# ===== INPUTS =====
produto = st.text_input("📦 Nome do Produto")
preco = st.text_input("💰 Preço")
link = st.text_input("🔗 Link do Produto")

plataforma = st.selectbox("🌍 Plataforma", ["Shopee", "Mercado Livre"])
modo = st.selectbox("🔥 Tipo de Copy", ["Agressiva", "Moderada"])

# ===== FUNÇÕES =====
def gerar_copy(produto, preco, link, modo):
    gatilhos = [
        "🚨 ÚLTIMAS UNIDADES!",
        "🔥 TODO MUNDO COMPRANDO!",
        "⚠️ ESTOQUE ACABANDO!",
        "💣 PREÇO IMPERDÍVEL!"
    ]

    calls = [
        "CORRE AGORA!",
        "ACABA HOJE!",
        "VOCÊ VAI PERDER!",
        "CLICA E GARANTE!"
    ] if modo == "Agressiva" else [
        "Vale a pena conferir",
        "Recomendo muito",
        "Olha isso 👀"
    ]

    base = f"""{random.choice(gatilhos)}

🔥 {produto}
💰 R$ {preco}

👉 {link}

{random.choice(calls)}
"""

    return [base, base