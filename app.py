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

# --- MENU DE NAVEGAÇÃO ---
aba = st.sidebar.selectbox("O que vamos fazer?", ["Fábrica de Posts (Produtos)", "Mensagens Motivacionais"])

if aba == "Fábrica de Posts (Produtos)":
    st.title("🔥 LuhVee Viral Machine")
    st.subheader("Copywriting para Todas as Redes")

    # Banco de Dados
    tendencias = {
        "Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Escova 3 em 1"],
        "Casa": ["MOP Giratório", "Organizador Luxo", "Mini Processador"],
        "Moda": ["Conjunto Alfaiataria", "Salto Scarpin", "Lingerie Renda"]
    }

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
        st.image(img, caption="Sua foto pronta!", use_column_width=True)

    st.write("---")
    st.markdown("### 🔗 Passo 2: Escolha o Link")
    loja = st.radio("Destino:", ["Shopee", "Mercado Livre", "Outro"])
    link_final = LINK_SHOPEE if loja == "Shopee" else LINK_ML if loja == "Mercado Livre" else st.text_input("Cole o link:")

    if st.button("🚀 GERAR POSTS PARA TODAS AS REDES"):
        if produto and link_final:
            st.success("✅ TEXTOS GERADOS!")
            st.code(f"Apenas CHOCADA com esse {produto}! ✨\nLink aqui: {link_final}\nLuhVee Stores 🛍️", language="text")
            st.code(f"POV: Você encontrou o {produto} que viralizou! ✨💖\n🔗 Link na BIO!\n#luhveestores", language="text")
        else:
            st.error("Luh, preencha tudo! 😘")

# ==========================================
# ✨ ABA NOVA: MENSAGENS MOTIVACIONAIS
# ==========================================
else:
    st.title("✨ Vibes LuhVee Stores")
    st.subheader("Mensagens para encantar suas clientes")

    periodo = st.radio("Qual o momento do dia?", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])

    frases_bom_dia = [
        "Que seu dia seja tão radiante quanto o seu sorriso! Comece hoje com a certeza de que o melhor está por vir. ✨",
        "Acorde, respire fundo e conquiste o mundo! Você é capaz de coisas incríveis hoje. 💪🌸",
        "Um café quente e uma dose extra de amor-próprio. Que seu dia seja produtivo e abençoado! ☕❤️"
    ]
    
    frases_boa_tarde = [
        "Passando para te desejar uma tarde cheia de energia positiva e conquistas! 🌟",
        "Que a sua tarde seja leve, produtiva e repleta de motivos para sorrir. Você merece! 🌸",
        "Pausa para um café e para lembrar: você está fazendo o seu melhor. Continue firme! ✨"
    ]

    frases_boa_noite = [
        "Hora de descansar a mente e renovar as energias. Amanhã é uma nova chance de brilhar! 🌙✨",
        "Que sua noite seja de paz e sonhos lindos. Descanse, rainha! 👑💖",
        "Gratidão pelo dia de hoje. Que o sono seja leve e o despertar seja alegre. Durma bem! 😴⭐"
    ]

    if st.button("✨ GERAR MENSAGEM DO MOMENTO"):
        if "Bom Dia" in periodo:
            texto = random.choice(frases_bom_dia)
        elif "Boa Tarde" in periodo:
            texto = random.choice(frases_boa_tarde)
        else:
            texto = random.choice(frases_boa_noite)
        
        st.write("---")
        st.markdown("#### ✅ Copie e poste com uma foto linda:")
        mensagem_final = f"{periodo}\n\n{texto}\n\nCom carinho,\n*LuhVee Stores ❤️*"
        st.code(mensagem_final, language="text")
        st.info("💡 DICA: Poste essa mensagem com uma foto sua tomando café, ou uma paisagem bem bonita, antes de começar as ofertas!")
