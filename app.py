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
        font-weight: bold; font-size: 18px;
    }
    .stCode { background-color: #1e1e1e !important; border: 1px solid #ff69b4 !important; color: #00ff00 !important; }
    div[data-baseweb="select"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS DA IA DE PESQUISA (TODOS OS NICHOS - SEM COMIDA/BEBIDA) ---
tendencias_reais = {
    "✨ Beleza & Autocuidado": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Kit de Pincéis Luxo", "Máscara LED Facial"],
    "🏠 Casa & Organização": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Prateleira Adesiva Banheiro", "Cesto de Roupa Dobrável"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador", "Bolsa Corrente Ouro", "Óculos Retrô VIP", "Relógio Minimalista"],
    "🐶 Pet Shop": ["Cama Nuvem Relaxante", "Bebedouro Fonte USB", "Escova Tira Pelos Mágica", "Brinquedo Inteligente Interativo"],
    "🛠️ Ferramentas & Utilidades": ["Parafusadeira Sem Fio Pink", "Kit Reparo Rápido", "Lanterna Tática Potente", "Fita Dupla Face Nano"],
    "🎧 Eletrônicos & Tech": ["Fone Bluetooth Estojo Digital", "Smartwatch Série Luxo", "Mini Projetor Portátil", "Suporte Celular Articulado"],
    "🧸 Infantil & Kids": ["Projetor Galáxia Astronauta", "Lousa Mágica Digital", "Kit Miçangas VIP", "Brinquedo Educativo Montessori"],
    "🌍 Internacional (Digistore24)": ["ProDentim (Saúde Bucal)", "Cortexi (Audição)", "Prodentim Pre-sell", "E-book Digital Premium"]
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
# ABA 1: GERADOR DE MADEIRADA
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Gerador de Madeirada")
    produto = st.text_input("Nome do Produto:", placeholder="Ex: MOP Giratório")
    foto = st.file_uploader("📸 Escolha a foto", type=["png", "jpg", "jpeg"])
    if foto: st.image(Image.open(foto), use_column_width=True)
    loja = st.radio("Link de qual loja?", ["Shopee", "Mercado Livre", "ProDentim"])
    link_f = LINKS[loja]
    if st.button("🚀 GERAR POSTS COMPLETO"):
        if produto:
            st.success("✅ TEXTO GERADO!")
            st.code(f"Apenas CHOCADA com esse {produto}! ✨\nLink aqui: {link_f}\nLuhVee Stores 🛍️❤️", language="text")
        else:
            st.warning("Luh, digite o nome do produto! 😘")

# ==========================================
# ABA 2: PESQUISA VIRAL IA (COM TODOS OS NICHOS)
# ==========================================
elif aba == "🔎 Pesquisa Viral IA":
    st.title("🔎 Inteligência de Mercado")
    st.subheader("O que as blogueiras estão postando hoje?")
    
    # Menu com todos os seus nichos
    categoria = st.selectbox("Escolha um nicho para minerar:", list(tendencias_reais.keys()))
    
    if st.button("🔥 BUSCAR PRODUTO VIRAL NO NICHO"):
        sugestao = random.choice(tendencias_reais[categoria])
        st.write("---")
        st.header(f"💡 Sugestão: {sugestao}")
        st.info(f"Dica Estratégica: Esse item de '{categoria}' está com alta busca. Procure o vídeo dele no TikTok para usar de inspiração!")

# ==========================================
# ABA 3: MOTIVACIONAIS
# ==========================================
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee Stores")
    # ... (Lógica das frases de bom dia/tarde/noite)
    st.info("Gere mensagens para conectar com suas clientes antes de vender!")

# ==========================================
# ABA 4: VITRINES & HUB
# ==========================================
else:
    st.title("🔗 Meus Links Oficiais")
    for nome, url in LINKS.items():
        st.markdown(f"**{nome}**")
        st.code(url, language="text")
