import streamlit as st
import random
import datetime

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Máquina de vendas automática")

# ===== ESTADO =====
if "historico" not in st.session_state:
    st.session_state.historico = []

# ===== INPUT =====
produto = st.text_input("📦 Produto")
preco = st.text_input("💰 Preço")
link = st.text_input("🔗 Link")

angulo = st.selectbox("🎯 Ângulo de venda", [
    "Viral",
    "Barato",
    "Problema/Solução",
    "Luxo",
])

# ===== FUNÇÕES =====
def gerar_copies(produto, preco, link, angulo):

    hooks = {
        "Viral": ["😳 ISSO TÁ EM TODO LUGAR", "🔥 TODO MUNDO COMPRANDO"],
        "Barato": ["💣 PREÇO RIDÍCULO", "😱 BARATO DEMAIS"],
        "Problema/Solução": ["🤯 RESOLVE ISSO EM SEGUNDOS", "⚠️ ACABOU SEU PROBLEMA"],
        "Luxo": ["✨ ISSO AQUI É OUTRO NÍVEL", "💎 PRODUTO PREMIUM"]
    }

    base = random.choice(hooks[angulo])

    copies = []
    for i in range(5):
        copy = f"""{base}

🔥 {produto}
💰 R$ {preco}

👉 {link}

⚠️ pode acabar hoje
"""
        copies.append(copy)

    return copies

def gerar_titulo(produto):
    return random.choice([
        f"😳 {produto} MUITO BARATO",
        f"🔥 {produto} tá viral",
        f"🚨 ninguém tá falando disso",
    ])

def gerar_hashtags():
    return "#achadinhos #promoção #oferta #shopee #viral"

def gerar_roteiro(produto):
    return f"""
🎬 ROTEIRO:

1. “olha isso aqui…”
2. mostra {produto}
3. “muito barato”
4. CTA: link na bio
"""

# ===== BOTÃO =====
if st.button("⚡ GERAR MODO ABSURDO"):
    if produto and preco and link:

        copies = gerar_copies(produto, preco, link, angulo)
        titulo = gerar_titulo(produto)
        roteiro = gerar_roteiro(produto)
        hashtags = gerar_hashtags()

        st.session_state.historico.append({
            "produto": produto,
            "hora": datetime.datetime.now().strftime("%H:%M"),
            "copies": copies
        })

        st.success("🔥 Máquina ativada!")

        st.subheader("🎯 Título")
        st.code(titulo)

        st.subheader("📱 Hashtags")
        st.code(hashtags)

        st.subheader("🎬 Roteiro")
        st.code(roteiro)

        st.subheader("📋 Copies")
        for c in copies:
            st.code(c)

    else:
        st.warning("Preencha tudo!")

# ===== HISTÓRICO =====
st.markdown("---")
st.subheader("📜 Histórico")

for item in reversed(st.session_state.historico):
    st.markdown(f"**{item['produto']} - {item['hora']}**")