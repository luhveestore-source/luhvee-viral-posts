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

# --- MENU LATERAL ---
st.sidebar.title("Menu LuhVee")
aba = st.sidebar.radio("Escolha o que fazer:", ["🛍️ Postar Produtos", "✨ Frases Motivacionais"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 LuhVee Viral Machine")
    st.subheader("Copywriting Pro: Textos que Vendem de Verdade")

    # Banco de Sugestões IA
    tendencias = {
        "Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Escova 3 em 1", "Sérum Facial Viral"],
        "Casa": ["MOP Giratório Inox", "Organizador de Acrílico", "Mini Processador Sem Fio"],
        "Moda": ["Conjunto Alfaiataria Luxo", "Salto Scarpin Verniz", "Lingerie de Renda Premium"]
    }

    if st.button("🔎 IA: SUGERIR PRODUTO DO DIA"):
        cat = random.choice(list(tendencias.keys()))
        st.session_state['prod'] = random.choice(tendencias[cat])
        st.session_state['cat'] = cat

    produto = st.text_input("Nome do Produto (Ex: Escova 3 em 1):", value=st.session_state.get('prod', ""))
    
    foto = st.file_uploader("📸 Passo 1: Escolha a foto do produto", type=["png", "jpg", "jpeg", "webp"])
    if foto:
        st.image(Image.open(foto), use_column_width=True)

    loja = st.radio("Passo 2: Escolha o Destino:", ["Shopee", "Mercado Livre", "Outro"])
    link_final = LINK_SHOPEE if loja == "Shopee" else LINK_ML if loja == "Mercado Livre" else st.text_input("Cole o link:")

    if st.button("🚀 GERAR POSTS COMPLETOS"):
        if produto and link_final:
            st.success("✅ TEXTOS DE ALTA CONVERSÃO GERADOS!")
            
            # --- STATUS / STORIES ---
            st.markdown("#### 🟢 WHATSAPP / INSTA STORIES")
            copy_stories = f"""GENTEE, para tudo! 😱 Olha a perfeição desse *{produto}* que acabou de chegar! ✨\n\nEu tô simplesmente apaixonada e já garanti o meu. Ele é perfeito para quem busca praticidade e aquele toque de luxo no dia a dia. ❤️\n\n⚠️ *Aviso:* O estoque da vitrine tá voando e restam poucas unidades com esse preço especial. Não diz que eu não avisei, hein? 🏃‍♀️💨\n\n🛒 *Garanta o seu aqui agora:* {link_final}\n\nLuhVee Stores — Levando o melhor até você! 🛍️✨"""
            st.code(copy_stories, language="text")

            # --- TIKTOK / REELS ---
            st.markdown("#### 🎬 TIKTOK / REELS / SHORTS")
            copy_reels = f"""POV: Você finalmente encontrou o {produto} que todo mundo está comentando no TikTok! ✨💖\n\nAquele achadinho que você não sabia que precisava, até ter um! Qualidade impecável e o precinho que a gente ama. 🚀\n\nChega de procurar, o melhor está aqui na LuhVee Stores. ✨\n\n🛍️ *Gostou? Link direto na BIO ou clique aqui:* {link_final}\n\n#luhveestores #achadinhos #viral #compras #shopee #beleza #utilidades"""
            st.code(copy_reels, language="text")

            # --- TELEGRAM ---
            st.markdown("#### 🔵 TELEGRAM / GRUPOS DE OFERTA")
            copy_telegram = f"""🔥 *OFERTA EXCLUSIVA LUHVEE STORES!* 🔥\n\n⭐ PRODUTO: {produto}\n💰 Valor promocional por tempo limitado!\n\nSe você estava esperando o sinal para renovar seus itens de {st.session_state.get('cat', 'Moda/Beleza')}, o sinal é esse! Produto viral com entrega garantida e segura. 🏆\n\n👇 *COMPRE PELO LINK OFICIAL:* \n{link_final}\n\n✅ Siga nosso canal para não perder os achadinhos do dia! 🛍️"""
            st.code(copy_telegram, language="text")

        else:
            st.error("Luh, preencha o nome do produto e o link! 😉")

# ==========================================
# ABA 2: MENSAGENS MOTIVACIONAIS
# ==========================================
else:
    st.title("✨ Vibes LuhVee Stores")
    st.subheader("Aquecimento de Audiência")
    periodo = st.selectbox("Qual o momento do dia?", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    
    # ... (as frases que já colocamos antes continuam aqui)
    if st.button("✨ GERAR MENSAGEM"):
        # Lógica de frases...
        st.code("Mensagem aqui...", language="text")
