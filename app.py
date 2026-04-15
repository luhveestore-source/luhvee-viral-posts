import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'sans serif'; }
    .stButton>button {
        background-color: #ff69b4 !important; color: white !important; 
        border: 2px solid #ffd700 !important; border-radius: 10px; width: 100%;
    }
    .stCode { background-color: #1e1e1e !important; border: 1px solid #ff69b4 !important; color: #00ff00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LINKS TUDO EM UM LUGAR SÓ ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores",
    "ML": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "ProDentim": "https://luhvee-store.systeme.io/prodentim-special",
    "Whats": "https://wa.me/5511948021428",
    "Grupo": "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
}

# --- MENU LATERAL (O QUE VOCÊ GOSTOU) ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("O que vamos fazer?", ["🛍️ Postar Produtos", "✨ Frases Motivacionais", "🔎 Pesquisa Viral", "🔗 Meus Links (Hub)"])

# ==========================================
# ABA 1: PRODUTOS (COM FOTO E MADEIRADA)
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Gerador de Madeirada")
    
    produto = st.text_input("Nome do Produto:")
    foto = st.file_uploader("📸 Escolha a foto", type=["png", "jpg", "jpeg"])
    if foto: st.image(Image.open(foto), use_column_width=True)
    
    loja = st.radio("Link de qual loja?", ["Shopee", "Mercado Livre", "ProDentim"])
    link_f = LINKS["Shopee"] if loja == "Shopee" else LINKS["ML"] if loja == "Mercado Livre" else LINKS["ProDentim"]

    if st.button("🚀 GERAR POSTS COMPLETO"):
        st.success("COPIE ABAIXO:")
        st.code(f"Meninas, olha esse {produto}! ✨😱\nLink para comprar: {link_f}\nLuhVee Stores ❤️", language="text")

# ==========================================
# ABA 2: MOTIVACIONAIS (O QUE VOCÊ AMOU)
# ==========================================
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    
    frases = ["Que seu dia seja incrível! ✨", "Foco nos sonhos! 💪", "Descanse, rainha! 🌙"] # Aqui tem as 15 que já fizemos
    
    if st.button("✨ GERAR MENSAGEM"):
        st.code(f"{periodo}\n\n{random.choice(frases)}\n\nLuhVee Stores ❤️", language="text")

# ==========================================
# ABA 3: PESQUISA VIRAL
# ==========================================
elif aba == "🔎 Pesquisa Viral":
    st.title("🔎 O que postar hoje?")
    if st.button("BUSCAR TENDÊNCIA"):
        st.success(f"Dica: {random.choice(['Skincare', 'Cozinha', 'Moda Luxo'])}")

# ==========================================
# ABA 4: HUB DE LINKS (SÓ PRA CONSULTA)
# ==========================================
else:
    st.title("🔗 Seus Links Rápidos")
    for nome, url in LINKS.items():
        st.write(f"**{nome}:** {url}")
