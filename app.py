import streamlit as st
import random
import time
import io
import textwrap
import requests
from bs4 import BeautifulSoup

from PIL import Image, ImageDraw, ImageFont

# --- CONFIG ---
st.set_page_config(page_title="LuhVee Viral Machine ELITE", page_icon="👑", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.stApp { background-color: #050505; }
h1, h2, h3 { color: #ff69b4 !important; }
.stButton>button {
    background: linear-gradient(135deg, #ff69b4, #ff1493);
    color: white !important;
    border-radius: 12px;
    font-weight: bold;
    height: 55px;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- LINKS ---
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"
LINK_HUB = "https://links-luhveestore.streamlit.app/"

# --- SESSION ---
if "produtos_salvos" not in st.session_state:
    st.session_state.produtos_salvos = []

# --- FORMATAR PREÇO ---
def formatar_preco(preco):
    preco = preco.replace("R$", "").strip()
    return f"R$ {preco}"

# --- EXTRAIR PRODUTO ---
def extrair_produto(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(link, headers=headers, timeout=5)

        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.text, "html.parser")

        if soup.title:
            return soup.title.text.strip()[:80]

        return None
    except:
        return None

# --- GERAR IMAGEM ---
def criar_post_elite(nome_prod, preco, foto_file):

    base = Image.new('RGB', (1080, 1920), (0, 0, 0))
    draw = ImageDraw.Draw(base)

    img = Image.open(foto_file).convert("RGBA")

    ratio = min(900/img.width, 1000/img.height)
    new_size = (int(img.width * ratio), int(img.height * ratio))
    img = img.resize(new_size)

    pos = ((1080 - new_size[0])//2, (1920 - new_size[1])//2 - 150)
    base.paste(img, pos, img)

    def get_font(size):
        try:
            return ImageFont.truetype("arialbd.ttf", size)
        except:
            return ImageFont.load_default()

    font_titulo = get_font(90)
    font_preco = get_font(120)
    font_sticker = get_font(50)

    nome = nome_prod.upper()
    linhas = textwrap.wrap(nome, width=15)

    y = 120
    for linha in linhas:
        draw.text((540, y), linha, fill="white", font=font_titulo, anchor="mm")
        y += 100

    preco = formatar_preco(preco)
    draw.text((540, 1700), preco, fill=(255,105,180), font=font_preco, anchor="mm")

    draw.rounded_rectangle([650,50,1030,180], radius=30, fill=(255,20,147))
    draw.text((840,115), "LINK NA BIO 🔗", fill="white", font=font_sticker, anchor="mm")

    return base

# --- COPY ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace):

    link = LINK_SHOPEE if "Shopee" in marketplace else LINK_ML
    preco = formatar_preco(preco)

    hooks = ["🚨 VIRALIZOU", "🔥 TODO MUNDO COMPRANDO", "⚠️ ACABANDO"]
    desejos = ["qualidade absurda", "nível premium", "resultado imediato"]

    copies = []

    for _ in range(3):
        copy = f"""{random.choice(hooks)}

🔥 {produto}
💎 {random.choice(desejos)}

💰 {preco}
{parcelas if parcelas else ""}

⚠️ pode acabar hoje

👉 {link}

❤️ LuhVee Stores
"""
        copies.append(copy)

    return copies

# --- MENSAGENS ---
def gerar_mensagens(qtd, banco):

    aberturas = ["🚨 OLHA ISSO", "🔥 VIRAL", "⚠️ NÃO IGNORA"]
    gatilhos = ["estoque acabando", "preço baixo", "todo mundo comprando"]
    acoes = ["👉 corre ver", "👉 aproveita", "👉 link aqui"]

    msgs = []

    for _ in range(qtd):
        msg = f"""{random.choice(aberturas)}

🔥 {random.choice(banco)}

💣 {random.choice(gatilhos)}

{random.choice(acoes)}

🌐 {LINK_HUB}
"""
        msgs.append(msg)

    return msgs

# --- SIDEBAR ---
st.sidebar.title("👑 LuhVee ELITE")

# SALVAR PRODUTO
novo = st.sidebar.text_input("💾 Salvar produto")

if st.sidebar.button("Salvar"):
    if novo:
        st.session_state.produtos_salvos.append(novo)
        st.sidebar.success("Salvo!")

# RADAR VIRAL
banco_base = [
    "Mini Seladora", "LED TikTok", "Fone Bluetooth",
    "Carregador Turbo", "Umidificador", "Projetor Astronauta"
]

banco_total = banco_base + st.session_state.produtos_salvos

if st.sidebar.button("📡 Produto viral"):
    st.sidebar.success(random.choice(banco_total))

# MENU
aba = st.sidebar.radio("Menu:", ["🛍️ Criar Post", "💬 Mensagens"])

# --- ABA POST ---
if aba == "🛍️ Criar Post":

    st.title("🔥 Criador de Post")

    link = st.text_input("🔗 Cole link produto")

    if st.button("🔎 Puxar nome"):
        nome = extrair_produto(link)
        if nome:
            st.session_state["produto"] = nome
            st.success(nome)

    produto = st.text_input("Produto", value=st.session_state.get("produto", ""))
    preco = st.text_input("Preço")
    parcelas = st.text_input("Parcelas")
    marketplace = st.selectbox("Plataforma", ["Shopee 🛍️", "Mercado Livre 📦"])

    foto = st.file_uploader("Foto produto", type=["png","jpg","jpeg"])

    if st.button("🚀 GERAR POST"):

        if produto and preco and foto:

            img = criar_post_elite(produto, preco, foto)
            st.image(img)

            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.download_button("Baixar imagem", buf.getvalue(), "post.png")

            copies = motor_maquina_vendas(produto, preco, parcelas, marketplace)

            for i, c in enumerate(copies):
                st.text_area(f"Copy {i+1}", c, height=200)

        else:
            st.warning("Preencha tudo")

# --- ABA MENSAGENS ---
else:

    st.title("💬 Máquina de Mensagens")

    qtd = st.slider("Quantidade", 1, 200, 20)

    if st.button("🔥 GERAR"):

        msgs = gerar_mensagens(qtd, banco_total)

        st.text_area("Copiar:", "\n\n---\n\n".join(msgs), height=400)