import streamlit as st
import random
import datetime
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Máquina automática de conteúdo para afiliados")

# ===== ESTADO =====
if "historico" not in st.session_state:
    st.session_state.historico = []

# ===== FUNÇÃO SCRAPING =====
def extrair_dados(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        titulo = soup.title.string if soup.title else "Produto"

        preco = ""
        for span in soup.find_all("span"):
            if "R$" in span.text:
                preco = span.text.strip()
                break

        imagem = ""
        img = soup.find("img")
        if img and img.get("src"):
            imagem = img["src"]

        return titulo[:80], preco, imagem

    except:
        return "", "", ""

# ===== COPY ENGINE =====
def gerar_copies(produto, preco, link, angulo):
    hooks = {
        "Viral": ["😳 ISSO TÁ EM TODO LUGAR", "🔥 TODO MUNDO COMPRANDO"],
        "Barato": ["💣 PREÇO RIDÍCULO", "😱 BARATO DEMAIS"],
        "Problema": ["🤯 RESOLVE ISSO EM SEGUNDOS", "⚠️ ACABOU SEU PROBLEMA"],
        "Luxo": ["✨ OUTRO NÍVEL", "💎 PREMIUM"]
    }

    base = random.choice(hooks[angulo])

    copies = []
    for _ in range(5):
        copies.append(f"""{base}

🔥 {produto}
💰 R$ {preco}

👉 {link}

⚠️ pode acabar hoje
""")
    return copies

def gerar_titulo(produto):
    return random.choice([
        f"😳 {produto} MUITO BARATO",
        f"🔥 {produto} tá viral",
        f"🚨 ninguém tá falando disso"
    ])

def gerar_hashtags():
    return "#achadinhos #promoção #oferta #viral #shopee #mercadolivre"

def gerar_roteiro(produto):
    return f"""🎬 ROTEIRO:

1. “olha isso aqui…”
2. mostra {produto}
3. “muito barato”
4. CTA: link na bio
"""

# ===== INPUTS =====
link = st.text_input("🔗 Cole o link do produto")

produto = ""
preco = ""
imagem = ""

if st.button("🤖 PUXAR DADOS"):
    if link:
        produto, preco, imagem = extrair_dados(link)
        st.success("Dados carregados! (confira)")
    else:
        st.warning("Cole o link primeiro")

produto = st.text_input("📦 Produto", value=produto)
preco = st.text_input("💰 Preço", value=preco)

angulo = st.selectbox("🎯 Ângulo de venda", ["Viral","Barato","Problema","Luxo"])

# ===== GERAR =====
if st.button("⚡ GERAR MODO ABSURDO"):
    if produto and preco and link:

        copies = gerar_copies(produto, preco, link, angulo)
        titulo = gerar_titulo(produto)
        hashtags = gerar_hashtags()
        roteiro = gerar_roteiro(produto)

        st.success("🔥 Conteúdo pronto!")

        if imagem:
            st.image(imagem, width=200)

        st.subheader("🎯 Título")
        st.code(titulo)

        st.subheader("📱 Hashtags")
        st.code(hashtags)

        st.subheader("🎬 Roteiro")
        st.code(roteiro)

        st.subheader("📋 Copies")
        for c in copies:
            st.code(c)

        # salvar histórico
        st.session_state.historico.append({
            "produto": produto,
            "hora": datetime.datetime.now().strftime("%H:%M")
        })

        # download
        conteudo = f"{titulo}\n\n{hashtags}\n\n{roteiro}\n\n" + "\n\n".join(copies)
        st.download_button("📥 Baixar conteúdo", conteudo, file_name="conteudo.txt")

    else:
        st.warning("Preencha tudo!")

# ===== HISTÓRICO =====
st.markdown("---")
st.subheader("📜 Histórico")

for item in reversed(st.session_state.historico):
    st.write(f"{item['produto']} - {item['hora']}")

# ===== LOTE =====
st.markdown("---")
st.subheader("🚀 Modo Lote")

lote = st.text_area("Cole vários links (1 por linha)")

if st.button("🔥 GERAR LOTE"):
    links = lote.split("\n")

    resultado = ""

    for l in links:
        if l.strip():
            nome, preco_l, _ = extrair_dados(l)

            if not nome:
                nome = "Produto"

            if not preco_l:
                preco_l = "??"

            copies = gerar_copies(nome, preco_l, l, "Viral")

            bloco = f"\n\n===== {nome} =====\n"
            bloco += "\n".join(copies)

            resultado += bloco

    st.code(resultado)
    st.download_button("📥 Baixar lote", resultado, file_name="lote.txt")