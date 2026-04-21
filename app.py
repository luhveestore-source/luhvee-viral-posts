import streamlit as st
import random
import time
import io
import textwrap
from PIL import Image, ImageDraw, ImageFont

# =========================
# CONFIG LuhVee
# =========================
st.set_page_config(page_title="👑 LuhVee GOD MODE", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# =========================
# HISTÓRICO
# =========================
if "historico" not in st.session_state:
    st.session_state.historico = []

# =========================
# BANCO VIRAL (NICHOS)
# =========================
nichos = {
    "🔥 Viral Geral": ["Mini Seladora", "LED TikTok", "Carregador Turbo", "Fone Bluetooth"],
    "💄 Beleza": ["Sérum Facial", "Escova 3 em 1", "Máscara LED", "Gloss Labial"],
    "🏠 Casa": ["Mop Giratório", "Organizador", "Aspirador Portátil", "Umidificador"],
    "📱 Tech": ["Smartwatch", "Mini Projetor", "Power Bank", "Teclado RGB"],
    "🐶 Pet": ["Cama Pet Nuvem", "Fonte de Água", "Escova Tira Pelo"]
}

# =========================
# FORMATAR PREÇO
# =========================
def preco_formatado(p):
    return f"R$ {p.replace('R$','').strip()}"

# =========================
# IMAGEM SEM DISTORÇÃO
# =========================
def criar_imagem(produto, preco, foto):

    base = Image.new("RGB", (1080,1920), (0,0,0))
    draw = ImageDraw.Draw(base)

    img = Image.open(foto).convert("RGBA")

    ratio = min(900/img.width, 1000/img.height)
    img = img.resize((int(img.width*ratio), int(img.height*ratio)))

    base.paste(img, ((1080-img.width)//2, 500), img)

    try:
        font = ImageFont.truetype("arialbd.ttf", 90)
    except:
        font = ImageFont.load_default()

    draw.text((540,200), produto.upper(), fill="white", anchor="mm", font=font)

    try:
        font2 = ImageFont.truetype("arialbd.ttf", 120)
    except:
        font2 = ImageFont.load_default()

    draw.text((540,1700), preco_formatado(preco), fill=(255,105,180), anchor="mm", font=font2)

    return base

# =========================
# COPY INSANA (AGRESSIVA)
# =========================
def gerar_copy(produto, preco, parcelas, mkt):

    link = LINK_SHOPEE if "Shopee" in mkt else LINK_ML

    hooks = [
        f"🚨 {produto.upper()} TÁ VIRALIZANDO AGORA!",
        f"🔥 TODO MUNDO CORRENDO PRA COMPRAR ISSO!",
        f"⚠️ ISSO VAI ESGOTAR HOJE!"
    ]

    dores = [
        "Você ainda tá perdendo dinheiro comprando errado?",
        "Cansado de produto ruim?",
        "Isso aqui resolve de verdade!"
    ]

    desejos = [
        "qualidade absurda",
        "resultado imediato",
        "nível premium de verdade"
    ]

    finais = [
        "👉 corre antes que acabe",
        "👉 aproveita agora",
        "👉 já garanti o meu"
    ]

    copy = f"""{random.choice(hooks)}

{random.choice(dores)}

🔥 {produto}
💎 {random.choice(desejos)}

💰 {preco_formatado(preco)}
{parcelas if parcelas else ""}

⚠️ Estoque limitado

🛒 COMPRE AQUI:
{link}

🎁 Meu HUB:
{LINK_HUB}

{random.choice(finais)}

❤️ LuhVee Stores
"""

    return copy

# =========================
# MENSAGENS MOTIVACIONAIS + VENDA
# =========================
def gerar_mensagens(qtd):

    msgs = []

    for _ in range(qtd):

        msg = f"""✨ Bom dia!

Você merece coisas incríveis 💖
E hoje pode ser o dia da sua virada.

🔥 Aproveita essas ofertas:
👉 {LINK_HUB}

🚀 Não deixa pra depois!
"""

        msgs.append(msg)

    return msgs

# =========================
# INTERFACE
# =========================
st.sidebar.title("👑 LuhVee GOD")

aba = st.sidebar.radio("Menu", [
    "🛍️ Criar Post",
    "🔎 Minerador Viral",
    "💬 Mensagens",
    "📜 Histórico"
])

# =========================
# CRIAR POST
# =========================
if aba == "🛍️ Criar Post":

    st.title("🔥 Criador LuhVee")

    produto = st.text_input("Produto")
    preco = st.text_input("Preço")
    parcelas = st.text_input("Parcelas")
    mkt = st.selectbox("Plataforma", ["Shopee", "Mercado Livre"])
    foto = st.file_uploader("Foto")

    if st.button("🚀 GERAR"):

        if produto and preco and foto:

            img = criar_imagem(produto, preco, foto)
            st.image(img)

            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.download_button("Baixar imagem", buf.getvalue())

            copy = gerar_copy(produto, preco, parcelas, mkt)

            st.text_area("Copy", copy, height=300)

            st.session_state.historico.append(copy)

# =========================
# MINERADOR
# =========================
elif aba == "🔎 Minerador Viral":

    st.title("💎 Produtos Virais")

    nicho = st.selectbox("Escolha nicho", list(nichos.keys()))

    if st.button("📡 MINERAR"):

        produto = random.choice(nichos[nicho])
        st.success(f"🔥 {produto}")

# =========================
# MENSAGENS
# =========================
elif aba == "💬 Mensagens":

    st.title("💖 Mensagens LuhVee")

    qtd = st.slider("Quantidade",1,100,10)

    if st.button("✨ GERAR"):

        msgs = gerar_mensagens(qtd)

        st.text_area("Copiar", "\n\n---\n\n".join(msgs), height=400)

# =========================
# HISTÓRICO
# =========================
else:

    st.title("📜 Histórico")

    for h in reversed(st.session_state.historico):
        st.text_area("Copy gerada", h, height=200)