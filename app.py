import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-baseweb="select"], input { background-color: #ffffff !important; color: #000000 !important; }
    .stButton>button {
        background-color: #ff69b4 !important; color: white !important; 
        border: 2px solid #ffd700 !important; border-radius: 10px;
        width: 100%; font-weight: bold; height: 50px; margin-top: 10px;
    }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'sans serif'; }
    .stCode { background-color: #1e1e1e !important; border: 1px solid #ff69b4 !important; color: #00ff00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LINKS OFICIAIS ---
LINK_SHOPEE = "https://collshp.com/luhveestores"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

st.title("🔥 LuhVee Viral Machine")
st.subheader("Copywriting para Todas as Redes")

# --- BANCO DE DADOS AMPLIADO ---
tendencias = {
    "Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Escova 3 em 1"],
    "Casa": ["MOP Giratório", "Organizador Luxo", "Mini Processador"],
    "Moda": ["Conjunto Alfaiataria", "Salto Scarpin", "Lingerie Renda"]
}

# Botão de Sugestão
if st.button("🔎 IA: SUGERIR PRODUTO VIRA"):
    cat = random.choice(list(tendencias.keys()))
    st.session_state['prod'] = random.choice(tendencias[cat])
    st.session_state['cat'] = cat

produto = st.text_input("Nome do Produto:", value=st.session_state.get('prod', ""))

st.write("---")
st.markdown("### 📸 Passo 1: Imagem do Produto")
foto = st.file_uploader("Escolha a foto (Print ou Original)", type=["png", "jpg", "jpeg", "webp"])

if foto:
    img = Image.open(foto)
    # Mostra a imagem centralizada
    st.image(img, caption="Sua foto pronta para o post!", use_column_width=True)
    st.info("💡 Dica: Se for print, lembre de cortar as bordas no seu celular para vender mais!")

st.write("---")
st.markdown("### 🔗 Passo 2: Escolha o Link")
loja = st.radio("Destino:", ["Shopee", "Mercado Livre", "Outro"])
link_final = LINK_SHOPEE if loja == "Shopee" else LINK_ML if loja == "Mercado Livre" else st.text_input("Cole o link:")

# --- GERAÇÃO DOS POSTS ---
if st.button("🚀 GERAR POSTS PARA TODAS AS REDES"):
    if produto and link_final:
        st.success("✅ TEXTOS GERADOS COM SUCESSO! COPIE ABAIXO:")
        
        # WHATSAPP STATUS / INSTA STORIES (Gatilho de Curiosidade)
        st.markdown("#### 🟢 WHATSAPP STATUS / STORIES")
        st.code(f"Apenas CHOCADA com esse {produto}! ✨\n\nQuem mais amou? Restam poucas unidades na promoção. 😱\n\nLink aqui: {link_final}\n\nLuhVee Stores 🛍️", language="text")

        # TIKTOK / REELS (Gatilho POV e Viral)
        st.markdown("#### 🎬 TIKTOK / REELS / SHORTS")
        st.code(f"POV: Você encontrou o {produto} que viralizou e não vive mais sem! ✨💖\n\nO segredo das blogueiras agora na LuhVee Stores.\n\n🔗 Link na BIO ou comente 'EU QUERO'!\n#achadinhos #viral #compras #shopee #luhveestores", language="text")

        # TELEGRAM / GRUPOS (Gatilho de Oferta)
        st.markdown("#### 🔵 TELEGRAM / GRUPOS DE OFERTAS")
        st.code(f"🔥 OFERTA DO DIA NA LUHVEE STORES! 🔥\n\n✅ {produto}\n\nDeixe sua rotina mais prática e elegante com esse achadinho. 🏆\n\n🛒 Compre agora: {link_final}\nEntrega garantida para todo Brasil! 🏃‍♀️💨", language="text")
    else:
        st.error("Luh, preencha o nome do produto e coloque uma foto! 😘")
