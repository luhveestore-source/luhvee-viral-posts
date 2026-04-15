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

# --- MENU DE NAVEGAÇÃO LATERAL ---
st.sidebar.title("Menu LuhVee")
aba = st.sidebar.radio("Escolha o que fazer:", ["🛍️ Postar Produtos", "✨ Frases Motivacionais"])

# ==========================================
# ABA 1: PRODUTOS
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 LuhVee Viral Machine")
    st.subheader("Copywriting para Todas as Redes")

    tendencias = {
        "Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Escova 3 em 1"],
        "Casa": ["MOP Giratório", "Organizador Luxo", "Mini Processador"],
        "Moda": ["Conjunto Alfaiataria", "Salto Scarpin", "Lingerie Renda"]
    }

    if st.button("🔎 IA: SUGERIR PRODUTO"):
        cat = random.choice(list(tendencias.keys()))
        st.session_state['prod'] = random.choice(tendencias[cat])
        st.session_state['cat'] = cat

    produto = st.text_input("Nome do Produto:", value=st.session_state.get('prod', ""))
    
    foto = st.file_uploader("📸 Escolha a foto do produto", type=["png", "jpg", "jpeg", "webp"])
    if foto:
        st.image(Image.open(foto), use_column_width=True)

    loja = st.radio("Destino:", ["Shopee", "Mercado Livre", "Outro"])
    link_final = LINK_SHOPEE if loja == "Shopee" else LINK_ML if loja == "Mercado Livre" else st.text_input("Cole o link:")

    if st.button("🚀 GERAR POSTS"):
        if produto and link_final:
            st.success("✅ TEXTOS GERADOS!")
            st.markdown("#### Status/Stories")
            st.code(f"Apenas CHOCADA com esse {produto}! ✨\nLink aqui: {link_final}\nLuhVee Stores 🛍️", language="text")
            st.markdown("#### TikTok/Reels")
            st.code(f"POV: Você encontrou o {produto} que viralizou! ✨💖\n🔗 Link na BIO!\n#luhveestores", language="text")
        else:
            st.error("Luh, preencha o nome do produto e o link! 😉")

# ==========================================
# ABA 2: MENSAGENS MOTIVACIONAIS
# ==========================================
else:
    st.title("✨ Vibes LuhVee Stores")
    st.subheader("Aquecimento de Audiência")

    periodo = st.selectbox("Qual o momento do dia?", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])

    # --- ONDE AS FRASES ESTÃO GUARDADAS ---
    frases_bom_dia = [
        "Oii! Que seu dia comece com um café quente e termine com uma meta batida! Você nasceu para brilhar. ✨☕",
        "Bom dia, rainha! Lembre-se: o seu único limite é a sua mente. Vamos conquistar o mundo hoje? 🌸💪",
        "Acorde e seja a sua melhor versão. A vida é curta demais para não usar aquele perfume maravilhoso! ✨💎",
        "Que a gratidão seja sua primeira oração e o sucesso seu único destino hoje. Bom dia! ✨🙌",
        "Um novo dia, uma nova chance de se apaixonar por você mesma. Vamos com tudo! 🌸❤️"
    ]
    
    frases_boa_tarde = [
        "Passando para te desejar uma tarde cheia de produtividade e boas notícias! 🌤️✨",
        "Pausa para o café e para lembrar: você é incrível e está fazendo um ótimo trabalho! 🌸☕",
        "Que o restante do seu dia seja leve e que a felicidade te encontre em cada detalhe. ✨🌟",
        "Tarde produtiva é aquela onde a gente foca nos sonhos. Falta pouco para o descanso, aguenta firme! 💪💖",
        "Energia positiva para a sua tarde! Que nada tire o seu brilho. ✨🌈"
    ]

    frases_boa_noite = [
        "Missão cumprida! Hora de descansar a mente e renovar a alma para brilhar amanhã. 🌙✨",
        "Durma com sonhos, acorde com planos. Que sua noite seja de profunda paz. 😴⭐",
        "Você venceu mais um dia! Descanse com a certeza de que você é uma mulher poderosa. 👑🌙",
        "Que o silêncio da noite traga o descanso que seu corpo merece. Até amanhã! ✨💤",
        "Gratidão por cada pequena vitória de hoje. Boa noite e bons sonhos! ❤️⭐"
    ]

    if st.button("✨ GERAR MENSAGEM DO MOMENTO"):
        if "Bom Dia" in periodo:
            texto = random.choice(frases_bom_dia)
        elif "Boa Tarde" in periodo:
            texto = random.choice(frases_boa_tarde)
        else:
            texto = random.choice(frases_boa_noite)
        
        st.write("---")
        mensagem_final = f"{periodo}\n\n{texto}\n\nCom carinho,\n*LuhVee Stores ❤️*"
        st.code(mensagem_final, language="text")
        st.success("Copiado? Agora posta com uma foto linda antes da 'madeirada'! 🔨✨")
