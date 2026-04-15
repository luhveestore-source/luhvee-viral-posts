import streamlit as st
import random
from PIL import Image
from datetime import datetime

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

# --- INICIALIZAR HISTÓRICO ---
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# --- LINKS OFICIAIS ---
LINK_SHOPEE = "https://collshp.com/luhveestores"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- MENU LATERAL ---
st.sidebar.title("Menu LuhVee")
aba = st.sidebar.radio("Escolha o que fazer:", ["🛍️ Postar Produtos", "✨ Frases Motivacionais", "📋 Meus Posts Salvos"])

# ==========================================
# ABA 1: PRODUTOS
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 LuhVee Viral Machine")
    
    tendencias = {
        "Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Escova 3 em 1"],
        "Casa": ["MOP Giratório Inox", "Organizador Luxo", "Mini Processador"],
        "Moda": ["Conjunto Alfaiataria", "Salto Scarpin", "Lingerie Renda"]
    }

    if st.button("🔎 IA: SUGERIR PRODUTO"):
        cat = random.choice(list(tendencias.keys()))
        st.session_state['prod'] = random.choice(tendencias[cat])

    produto = st.text_input("Nome do Produto:", value=st.session_state.get('prod', ""))
    foto = st.file_uploader("📸 Foto do Produto", type=["png", "jpg", "jpeg", "webp"])
    
    loja = st.radio("Destino:", ["Shopee", "Mercado Livre", "Outro"])
    link_final = LINK_SHOPEE if loja == "Shopee" else LINK_ML if loja == "Mercado Livre" else st.text_input("Cole o link:")

    if st.button("🚀 GERAR POSTS"):
        if produto and link_final:
            st.session_state['ultimo_post'] = {
                "produto": produto,
                "link": link_final,
                "data": datetime.now().strftime("%d/%m - %H:%M"),
                "texto": f"🔥 *ACHADINHO DA LUHVEE!* 🔥\n\nMeninas, olhem esse *{produto}*! 😱✨\n\n🛒 *Garanta aqui:* {link_final}\n\nLuhVee Stores 🛍️"
            }
            st.success("✅ Gerado! Veja abaixo:")
            st.code(st.session_state['ultimo_post']['texto'], language="text")
            
            if st.button("💾 SALVAR NO HISTÓRICO"):
                st.session_state['historico'].append(st.session_state['ultimo_post'])
                st.toast("Post guardado no histórico! 📋")
        else:
            st.error("Preencha o nome e o link! 😉")

# ==========================================
# ABA 2: MOTIVACIONAIS
# ==========================================
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee Stores")
    # (Lógica das frases que já temos...)
    st.info("Escolha o período e gere sua mensagem de carinho!")

# ==========================================
# ABA 3: HISTÓRICO (A NOVIDADE!)
# ==========================================
else:
    st.title("📋 Histórico de Postagens")
    if not st.session_state['historico']:
        st.warning("Seu histórico está vazio. Comece a salvar seus posts!")
    else:
        if st.button("🗑️ Limpar Todo Histórico"):
            st.session_state['historico'] = []
            st.rerun()

        for idx, item in enumerate(reversed(st.session_state['historico'])):
            with st.expander(f"📦 {item['produto']} ({item['data']})"):
                st.code(item['texto'], language="text")
                st.write(f"🔗 Link: {item['link']}")
                if st.button(f"Remover {idx}", key=f"del_{idx}"):
                    st.session_state['historico'].pop(-(idx+1))
                    st.rerun()
