import streamlit as st
import random
import time
import io
import textwrap

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --- CONFIG ---
st.set_page_config(page_title="LuhVee Viral Machine ELITE", page_icon="👑", layout="wide")

# --- STYLE ---
st.markdown("""
<style>
.stApp { background-color: #050505; }
h1, h2 { color: #ff69b4 !important; }
.stButton>button {
    background: linear-gradient(135deg, #ff69b4, #ff1493);
    color: white; border-radius: 12px;
    font-weight: bold; height: 55px;
}
</style>
""", unsafe_allow_html=True)

# --- LINKS ---
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- GERADOR DE IMAGEM PROFISSIONAL ---
def criar_post_elite(nome_prod, preco, foto_file, logo_file):

    base = Image.new('RGB', (1080, 1920), (10,10,10))

    # Fundo blur
    if foto_file:
        try:
            bg = Image.open(foto_file).convert("RGB")
            bg = bg.resize((1080,1920))
            bg = bg.filter(ImageFilter.GaussianBlur(25))
            base = bg
        except:
            pass

    overlay = Image.new('RGBA', (1080,1920), (0,0,0,160))
    base = Image.alpha_composite(base.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(base)

    # Produto central
    if foto_file:
        try:
            prod = Image.open(foto_file).convert("RGBA")
            prod.thumbnail((800,900))
            pos = ((1080-prod.size[0])//2, (1920-prod.size[1])//2 - 100)
            base.paste(prod, pos, prod)
        except:
            pass

    # Fontes
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 90)
        font_price = ImageFont.truetype("arialbd.ttf", 130)
        font_small = ImageFont.truetype("arial.ttf", 50)
    except:
        font_title = font_price = font_small = ImageFont.load_default()

    # Nome
    nome = textwrap.fill(nome_prod.upper(), 18)
    y = 120
    for linha in nome.split("\n"):
        draw.text((540,y), linha, fill="white", font=font_title, anchor="mm")
        y += 100

    # Preço
    preco_txt = f"R$ {preco}"
    draw.text((544,1554), preco_txt, font=font_price, fill=(0,0,0), anchor="mm")
    draw.text((540,1550), preco_txt, font=font_price, fill=(255,105,180), anchor="mm")

    # CTA
    draw.text((540,1680), "🔥 GARANTA AGORA 🔥", font=font_small, fill="white", anchor="mm")

    # Sticker
    draw.rounded_rectangle((700,50,1050,150), 30, fill=(255,20,147))
    draw.text((875,100), "LINK NA BIO", font=font_small, fill="white", anchor="mm")

    # Logo
    if logo_file:
        try:
            logo = Image.open(logo_file).convert("RGBA")
            logo.thumbnail((200,200))
            base.paste(logo, (30,30), logo)
        except:
            pass

    return base.convert("RGB")

# --- MOTOR MÁQUINA DE VENDAS ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace):

    link = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML

    hooks = [
        "🚨 ISSO TÁ VIRALIZANDO",
        "🔥 TODO MUNDO COMPRANDO",
        "💥 EXPLODIU DO NADA",
        "😱 OLHA ISSO"
    ]

    desejos = [
        "facilita sua vida",
        "qualidade absurda",
        "todo mundo quer",
        "você vai usar todo dia"
    ]

    urgencia = [
        "⚠️ pode acabar hoje",
        "🔥 estoque limitado",
        "🚨 corre antes que suba"
    ]

    copies = []

    for _ in range(5):
        copy = f"""{random.choice(hooks)}

🔥 {produto}

💡 {random.choice(desejos)}

💰 R$ {preco}
{parcelas if parcelas else ""}

👉 {link}

{random.choice(urgencia)}
"""
        copies.append(copy)

    return copies

# --- UI ---
st.title("👑 LuhVee Máquina de Vendas")

col1, col2 = st.columns(2)

with col1:
    logo = st.file_uploader("Logo", type=["png"])
    foto = st.file_uploader("Produto", type=["png","jpg","jpeg"])

with col2:
    produto = st.text_input("Nome do Produto")
    preco = st.text_input("Preço")
    parcelas = st.text_input("Parcelamento")
    mkt = st.selectbox("Marketplace", ["Shopee 🛍️", "Mercado Livre 📦"])

if st.button("🚀 GERAR TUDO"):

    if produto and preco and foto:

        # Imagem
        img = criar_post_elite(produto, preco, foto, logo)
        st.image(img, use_container_width=True)

        buf = io.BytesIO()
        img.save(buf, format="PNG")

        st.download_button("📥 Baixar Imagem", buf.getvalue(), "post.png")

        # Copies
        st.subheader("📋 Copies de Venda")
        cps = motor_maquina_vendas(produto, preco, parcelas, mkt)

        for i, c in enumerate(cps):
            st.text_area(f"Copy {i+1}", c, height=200)

    else:
        st.warning("Preencha tudo!")