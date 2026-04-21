import streamlit as st
import random
import time
import io
import textwrap

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    st.error("Instale: pip install Pillow")

# --- CONFIG ---
st.set_page_config(page_title="LuhVee Viral Machine ELITE", page_icon="👑", layout="wide")

# --- CSS MELHORADO ---
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

# --- FUNÇÃO AJUSTAR PREÇO ---
def formatar_preco(preco):
    preco = preco.replace("R$", "").strip()
    return f"R$ {preco}"

# --- IMAGEM ELITE CORRIGIDA ---
def criar_post_elite(nome_prod, preco, foto_file, logo_file):

    base = Image.new('RGB', (1080, 1920), (0, 0, 0))

    draw = ImageDraw.Draw(base)

    # --- FOTO PRODUTO (SEM DISTORCER) ---
    if foto_file:
        img = Image.open(foto_file).convert("RGBA")

        max_w, max_h = 900, 1000
        ratio = min(max_w/img.width, max_h/img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))

        img = img.resize(new_size, Image.Resampling.LANCZOS)

        pos = ((1080 - new_size[0])//2, (1920 - new_size[1])//2 - 150)
        base.paste(img, pos, img)

    # --- FONTES DINÂMICAS ---
    def get_font(size):
        try:
            return ImageFont.truetype("arialbd.ttf", size)
        except:
            return ImageFont.load_default()

    font_titulo = get_font(90)
    font_preco = get_font(120)
    font_sticker = get_font(50)

    # --- NOME PRODUTO (AUTO AJUSTE) ---
    nome = nome_prod.upper()
    linhas = textwrap.wrap(nome, width=15)

    y = 120
    for linha in linhas:
        draw.text((540, y), linha, fill="white", font=font_titulo, anchor="mm")
        y += 100

    # --- PREÇO ---
    preco = formatar_preco(preco)

    draw.text((540, 1700), preco, fill=(255,105,180), font=font_preco, anchor="mm")

    # --- BOTÃO LINK NA BIO ---
    x1, y1, x2, y2 = 650, 50, 1030, 180
    draw.rounded_rectangle([x1,y1,x2,y2], radius=30, fill=(255,20,147))

    draw.text(((x1+x2)//2, (y1+y2)//2), "LINK NA BIO 🔗", fill="white", font=font_sticker, anchor="mm")

    return base

# --- COPYS ELITE (MAIS LONGAS E DIFERENTES) ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace, rede):

    link = LINK_SHOPEE if "Shopee" in marketplace else LINK_ML
    preco = formatar_preco(preco)

    hooks = [
        f"🚨 {produto.upper()} VIRALIZOU AGORA!",
        f"🔥 TODO MUNDO TÁ COMPRANDO {produto.upper()}",
        f"⚠️ ISSO AQUI TÁ ESGOTANDO RÁPIDO!"
    ]

    dores = [
        "Cansado de produto ruim?",
        "Você merece algo melhor!",
        "Chega de gastar dinheiro à toa!"
    ]

    desejos = [
        "qualidade absurda",
        "resultado imediato",
        "nível premium de verdade"
    ]

    finais = [
        "👉 corre antes que acabe",
        "👉 aproveita enquanto tá barato",
        "👉 não deixa pra depois"
    ]

    copies = []

    for _ in range(3):
        copy = f"""{random.choice(hooks)}

{random.choice(dores)}

🔥 {produto}
💎 {random.choice(desejos)}

💰 {preco}
{parcelas if parcelas else ""}

⚠️ Estoque limitado

🛒 COMPRE AGORA:
{link}

{random.choice(finais)}

❤️ LuhVee Stores
"""
        copies.append(copy)

    return copies

# --- INTERFACE ---
st.sidebar.title("👑 LuhVee ELITE")
aba = st.sidebar.radio("Menu:", ["🛍️ Criar Post", "🔎 Ideias", "💬 Mensagens"])

# --- ABA 1 ---
if aba == "🛍️ Criar Post":

    st.title("🔥 Criador de Posts Profissionais")

    col1, col2 = st.columns(2)

    with col1:
        foto = st.file_uploader("📸 Foto Produto", type=['png','jpg','jpeg'])
        logo = st.file_uploader("🏷️ Logo", type=['png'])

    with col2:
        produto = st.text_input("📦 Produto")
        preco = st.text_input("💰 Preço")
        parcelas = st.text_input("💳 Parcelas")
        marketplace = st.selectbox("🌍 Plataforma", ["Shopee 🛍️", "Mercado Livre 📦"])
        rede = st.selectbox("📱 Rede", ["Instagram", "TikTok", "WhatsApp"])

    if st.button("🚀 GERAR POST ELITE"):

        if produto and preco and foto:

            img = criar_post_elite(produto, preco, foto, logo)
            st.image(img, use_container_width=True)

            buf = io.BytesIO()
            img.save(buf, format="PNG")

            st.download_button("📥 Baixar", buf.getvalue(), "post.png")

            st.subheader("📋 Copys")

            copies = motor_maquina_vendas(produto, preco, parcelas, marketplace, rede)

            for i, c in enumerate(copies):
                st.text_area(f"Copy {i+1}", c, height=200)

        else:
            st.warning("Preencha tudo!")

# --- ABA 2 ---
elif aba == "🔎 Ideias":

    ideias = ["Luz LED TikTok", "Escova Facial", "Mini Seladora", "Suporte Veicular"]

    if st.button("💡 Gerar Ideia"):
        st.success(random.choice(ideias))

# --- ABA 3 ---
else:

    if st.button("✨ Gerar Mensagem"):
        st.text_area("Mensagem", f"Você merece vencer! 💖\n👉 {LINK_HUB}")