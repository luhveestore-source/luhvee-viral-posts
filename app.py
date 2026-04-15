import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL (Igual às fotos) ---
st.set_page_config(page_title="LuhVee Viral Machine", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'sans serif'; }
    .stButton>button {
        background-color: #ff69b4 !important; color: white !important; 
        border: 2px solid #ffd700 !important; border-radius: 10px; width: 100%;
        font-weight: bold; font-size: 18px;
    }
    .stCode { background-color: #1e1e1e !important; border: 1px solid #ff69b4 !important; color: #00ff00 !important; }
    div[data-baseweb="select"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS DA IA DE PESQUISA (A VOLTA DA IA!) ---
tendencias_reais = {
    "Beleza": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "Casa": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "Moda": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "Internacional": ["ProDentim (Saúde Bucal)", "Suplemento BioFit", "Renovador Facial Digistore"]
}

# --- LINKS DAS VITRINES ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "ProDentim": "https://luhvee-store.systeme.io/prodentim-special",
    "Whats": "https://wa.me/5511948021428",
    "Telegram": "https://t.me/luhveestores",
    "Grupo Whats": "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Viral IA", "✨ Frases Motivacionais", "🔗 Vitrines & Hub"])

# ==========================================
# ABA 1: GERADOR DE MADEIRADA (IGUAL À FOTO)
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Gerador de Madeirada")
    
    produto = st.text_input("Nome do Produto:", placeholder="Ex: Escova 3 em 1")
    
    foto = st.file_uploader("📸 Escolha a foto", type=["png", "jpg", "jpeg"])
    if foto: 
        st.image(Image.open(foto), use_column_width=True)
    
    loja = st.radio("Link de qual loja?", ["Shopee", "Mercado Livre", "ProDentim"])
    link_f = LINKS[loja]

    if st.button("🚀 GERAR POSTS COMPLETO"):
        if produto:
            st.success("✅ TEXTOS GERADOS!")
            st.markdown("### Status/Stories")
            st.code(f"Apenas CHOCADA com esse {produto}! ✨\nLink aqui: {link_f}\nLuhVee Stores 🛍️❤️", language="text")
            
            st.markdown("### TikTok/Reels")
            st.code(f"POV: Você encontrou o {produto} que viralizou! ✨💖\n🔗 Link na BIO!\n#luhveestores #achadinhos", language="text")
        else:
            st.warning("Luh, digite o nome do produto primeiro! 😘")

# ==========================================
# ABA 2: PESQUISA VIRAL IA (TURBINADA)
# ==========================================
elif aba == "🔎 Pesquisa Viral IA":
    st.title("🔎 Inteligência de Mercado")
    st.subheader("O que está bombando nas redes?")
    
    categoria = st.selectbox("Escolha um nicho:", list(tendencias_reais.keys()))
    
    if st.button("🔥 BUSCAR PRODUTO VIRAL"):
        sugestao = random.choice(tendencias_reais[categoria])
        st.write("---")
        st.header(f"💡 Sugestão: {sugestao}")
        st.info(f"Dica LuhVee: Este produto está com alto engajamento no TikTok hoje. Ótimo para a 'madeirada'!")

# ==========================================
# ABA 3: MOTIVACIONAIS
# ==========================================
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Escolha o momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    
    frases_longas = [
        "Que seu dia seja tão brilhante quanto o seu sorriso! Você nasceu para conquistar o mundo. ✨🌸",
        "Pausa para um café e para lembrar: você é uma mulher poderosa e merece o melhor! ☕👑",
        "Missão cumprida! Agora descanse a mente, renove as energias e sonhe alto. 🌙⭐"
    ]
    
    if st.button("✨ GERAR MENSAGEM COM CARINHO"):
        st.code(f"{periodo}\n\n{random.choice(frases_longas)}\n\nCom carinho,\nLuhVee Stores ❤️", language="text")

# ==========================================
# ABA 4: VITRINES & HUB (SEUS LINKS)
# ==========================================
else:
    st.title("🔗 Minhas Vitrines Oficiais")
    st.markdown("### Clique para copiar ou conferir seus links:")
    
    for nome, url in LINKS.items():
        st.markdown(f"**{nome}**")
        st.code(url, language="text")