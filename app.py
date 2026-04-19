import streamlit as st
import random
import datetime
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
import tempfile

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Gerador de conteúdo para afiliados")

# ===== LINKS AFILIADOS =====
LINK_AFILIADO_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_AFILIADO_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# ===== SESSION =====
if "produto" not in st.session_state:
    st.session_state.produto = ""

if "preco" not in st.session_state:
    st.session_state.preco = ""

if "imagem" not in st.session_state:
    st.session_state.imagem = ""

# ===== SCRAPING =====
def extrair_dados(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        titulo = soup.title.string if soup.title else "Produto"

        preco = "??"
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
        return "Produto", "??", ""

# ===== LINKS =====
def gerar_links(plataformas):
    lista = []
    if "Shopee" in plataformas:
        lista.append(("Shopee", LINK_AFILIADO_SHOPEE))
    if "Mercado Livre" in plataformas:
        lista.append(("Mercado Livre", LINK_AFILIADO_ML))
    return lista

# ===== COPIES DIFERENTES =====
def gerar_copies(produto, preco, link, angulo):
    hooks = {
        "Viral": [
            "😳 ISSO TÁ EM TODO LUGAR",
            "🔥 TODO MUNDO COMPRANDO",
            "🚨 ISSO EXPLODIU NA INTERNET",
            "😱 VOCÊ PRECISA VER ISSO",
            "💥 VIRALIZOU DO NADA"
        ],
        "Barato": [
            "💣 PREÇO RIDÍCULO",
            "😱 BARATO DEMAIS",
            "🔥 QUASE DE GRAÇA",
            "🚨 PROMOÇÃO INSANA",
            "💸 NEM ACREDITO NESSE PREÇO"
        ],
        "Problema": [
            "🤯 RESOLVE ISSO EM SEGUNDOS",
            "⚠️ ACABOU SEU PROBLEMA",
            "🔥 ISSO MUDA TUDO",
            "😳 VOCÊ PRECISA DISSO",
            "💡 SOLUÇÃO PERFEITA"
        ],
        "Luxo": [
            "✨ OUTRO NÍVEL",
            "💎 PREMIUM",
            "🔥 QUALIDADE TOP",
            "👑 NÍVEL ALTO",
            "💼 PRODUTO DIFERENCIADO"
        ]
    }

    copies = []
    for frase in hooks[angulo]:
        copy = f"""{frase}

🔥 {produto}
💰 R$ {preco}

👉 {link}

⚠️ pode acabar hoje
"""
        copies.append(copy)

    return copies

# ===== UTIL =====
def botao_copiar(texto, chave):
    st.text_area("Copiar conteúdo", texto, key=chave)

# ===== IMAGEM =====
def gerar_imagem(produto, preco, imagem_url):
    try:
        if not imagem_url:
            return None

        response = requests.get(imagem_url)
        img_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img_temp.write(response.content)
        img_temp.close()

        img = Image.open(img_temp.name).convert("RGB")
        draw = ImageDraw.Draw(img)

        draw.text((20, 20), f"{produto}\nR$ {preco}", fill="white")

        img_final = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img.save(img_final.name)

        return img_final.name

    except:
        return None

# ===== INPUT =====
link = st.text_input("🔗 Cole o link do produto")

if st.button("🤖 PUXAR DADOS"):
    if link:
        produto, preco, imagem = extrair_dados(link)
        st.session_state.produto = produto
        st.session_state.preco = preco
        st.session_state.imagem = imagem
        st.success("Dados carregados!")

produto = st.text_input("📦 Produto", value=st.session_state.produto)
preco = st.text_input("💰 Preço", value=st.session_state.preco)

plataformas = st.multiselect(
    "🌍 Onde quer gerar link?",
    ["Shopee", "Mercado Livre"],
    default=["Shopee"]
)

angulo = st.selectbox("🎯 Ângulo", ["Viral","Barato","Problema","Luxo"])

# ===== GERAR =====
if st.button("⚡ GERAR CONTEÚDO"):
    if produto and preco and plataformas:

        links = gerar_links(plataformas)

        for nome, link_final in links:

            st.markdown(f"## 🔗 {nome}")

            copies = gerar_copies(produto, preco, link_final, angulo)

            for i, c in enumerate(copies):
                botao_copiar(c, f"{nome}_{i}")

        if st.session_state.imagem:
            if st.button("🖼 GERAR CRIATIVO"):
                img = gerar_imagem(produto, preco, st.session_state.imagem)

                if img:
                    st.image(img)
                    with open(img, "rb") as f:
                        st.download_button("📥 Baixar imagem", f, file_name="criativo.jpg")

    else:
        st.warning("Preencha tudo!")