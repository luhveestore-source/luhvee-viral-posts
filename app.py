import streamlit as st
import random
import datetime
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import tempfile

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Máquina automática de conteúdo + criativo")

# ===== LINKS AFILIADOS =====
LINK_AFILIADO_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_AFILIADO_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# ===== ESTADO =====
if "historico" not in st.session_state:
    st.session_state.historico = []

# ===== LINK AFILIADO =====
def gerar_link_afiliado(link):
    link_lower = link.lower()
    if "shopee" in link_lower:
        return LINK_AFILIADO_SHOPEE
    elif "mercadolivre" in link_lower:
        return LINK_AFILIADO_ML
    return link

# ===== SCRAPING =====
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

# ===== COPY =====
def gerar_copies(produto, preco, link, angulo):
    hooks = {
        "Viral": ["😳 ISSO TÁ EM TODO LUGAR", "🔥 TODO MUNDO COMPRANDO"],
        "Barato": ["💣 PREÇO RIDÍCULO", "😱 BARATO DEMAIS"],
        "Problema": ["🤯 RESOLVE ISSO EM SEGUNDOS", "⚠️ ACABOU SEU PROBLEMA"],
        "Luxo": ["✨ OUTRO NÍVEL", "💎 PREMIUM"]
    }

    base = random.choice(hooks[angulo])

    return [
        f"""{base}

🔥 {produto}
💰 R$ {preco}

👉 {link}

⚠️ pode acabar hoje
"""
        for _ in range(5)
    ]

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

# ===== CRIATIVO (IMAGEM) =====
def gerar_imagem(produto, preco, imagem_url):
    try:
        response = requests.get(imagem_url)
        img_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img_temp.write(response.content)
        img_temp.close()

        img = Image.open(img_temp.name).convert("RGB")
        draw = ImageDraw.Draw(img)

        texto = f"{produto}\nR$ {preco}"

        draw.text((20, 20), texto, fill="white")

        img_final = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img.save(img_final.name)

        return img_final.name

    except:
        return None

# ===== INPUT =====
link = st.text_input("🔗 Cole o link do produto")

produto = ""
preco = ""
imagem = ""

if st.button("🤖 PUXAR DADOS"):
    if link:
        produto, preco, imagem = extrair_dados(link)
        st.success("Dados carregados!")
    else:
        st.warning("Cole o link")

produto = st.text_input("📦 Produto", value=produto)
preco = st.text_input("💰 Preço", value=preco)

angulo = st.selectbox("🎯 Ângulo", ["Viral","Barato","Problema","Luxo"])

# ===== GERAR =====
if st.button("⚡ GERAR CONTEÚDO"):
    if produto and preco and link:

        link_final = gerar_link_afiliado(link)

        copies = gerar_copies(produto, preco, link_final, angulo)
        titulo = gerar_titulo(produto)
        hashtags = gerar_hashtags()
        roteiro = gerar_roteiro(produto)

        st.success("🔥 Conteúdo pronto!")

        if imagem:
            st.image(imagem, width=200)

        st.subheader("🔗 Link afiliado")
        st.code(link_final)

        st.subheader("🎯 Título")
        st.code(titulo)

        st.subheader("📱 Hashtags")
        st.code(hashtags)

        st.subheader("🎬 Roteiro")
        st.code(roteiro)

        st.subheader("📋 Copies")
        for c in copies:
            st.code(c)

        # ===== GERAR IMAGEM =====
        if imagem:
            if st.button("🖼 GERAR CRIATIVO"):
                img = gerar_imagem(produto, preco, imagem)

                if img:
                    st.image(img)
                    with open(img, "rb") as f:
                        st.download_button("📥 Baixar imagem", f, file_name="criativo.jpg")
                else:
                    st.error("Erro ao gerar imagem")

        st.session_state.historico.append({
            "produto": produto,
            "hora": datetime.datetime.now().strftime("%H:%M")
        })

    else:
        st.warning("Preencha tudo!")

# ===== HISTÓRICO =====
st.markdown("---")
st.subheader("📜 Histórico")

for item in reversed(st.session_state.historico):
    st.write(f"{item['produto']} - {item['hora']}")