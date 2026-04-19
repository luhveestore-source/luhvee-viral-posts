import streamlit as st
import random

st.set_page_config(page_title="LuhVee PRO", layout="centered")

st.title("🔥 Robô LuhVee PRO")

# ===== SEUS LINKS FIXOS =====
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"

# ===== PRODUTOS =====
produtos_virais = [
    {"nome": "Mini Seladora Portátil", "preco": "29,90"},
    {"nome": "Luz LED RGB TikTok", "preco": "49,90"},
    {"nome": "Escova Elétrica Facial", "preco": "39,90"},
    {"nome": "Suporte Celular Veicular", "preco": "24,90"},
    {"nome": "Organizador de Gaveta", "preco": "19,90"},
]

# ===== COPY =====
def gerar_copy(nome, preco, link):
    gatilhos = [
        "🚨 PROMOÇÃO RELÂMPAGO!",
        "🔥 TODO MUNDO COMPRANDO!",
        "⚠️ ESTOQUE ACABANDO!"
    ]

    call = [
        "Corre antes que acabe!",
        "Clica e garante o seu!",
        "Não perde essa chance!"
    ]

    return f"""{random.choice(gatilhos)}

🔥 {nome}
💰 R$ {preco}

👉 {link}

{random.choice(call)}
"""

# ===== ESCOLHA PLATAFORMA =====
plataforma = st.radio(
    "Escolha a plataforma:",
    ["Mercado Livre", "Shopee"]
)

link_base = LINK_ML if plataforma == "Mercado Livre" else LINK_SHOPEE

# ===== PRODUTOS =====
st.subheader("🔥 Produtos em Alta")

for p in produtos_virais:
    st.markdown(f"### {p['nome']}")
    st.write(f"💰 R$ {p['preco']}")

    if st.button(f"🚀 Gerar Copy - {p['nome']}"):
        copy = gerar_copy(p["nome"], p["preco"], link_base)
        st.code(copy)