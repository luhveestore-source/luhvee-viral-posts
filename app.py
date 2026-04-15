import streamlit as st
import random

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
    .stCode { background-color: #1e1e1e !important; border: 1px solid #ff69b4 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LINKS OFICIAIS ---
LINK_SHOPEE = "https://collshp.com/luhveestores"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

st.title("🔥 LuhVee Viral Machine")
st.subheader("Gerador de Postagens Grátis com Sua Foto")

# --- BANCO DE DADOS DE PRODUTOS ---
tendencias = {
    "Perfumaria e Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Kit Rapunzel Lola"],
    "Achadinhos de Casa": ["MOP Limpeza Prática", "Organizador de Geladeira", "Mini Processador"],
    "Moda/Acessórios": ["Conjunto Alfaiataria", "Óculos Retrô", "Bolsa Baguete"],
    "Eletrônicos": ["Smartwatch Série 9", "Fone Bluetooth Pro", "Projetor Astronauta"]
}

# --- BOTÃO PESQUISAR ---
if st.button("🔎 IA: SUGERIR PRODUTO DO DIA"):
    cat_sorteada = random.choice(list(tendencias.keys()))
    prod_sorteado = random.choice(tendencias[cat_sorteada])
    st.session_state['produto_sugerido'] = prod_sorteado
    st.session_state['categoria_sugerida'] = cat_sorteada
    st.success(f"✅ Sugestão: {prod_sorteado}")

# --- CAMPOS ---
produto = st.text_input("Nome do Produto:", value=st.session_state.get('produto_sugerido', ""))

# ==========================================
# 📸 CAMPO DE FOTO (UPLOAD GRÁTIS)
# ==========================================
st.write("---")
st.markdown("### 📸 Passo 1: Coloque a foto do produto")
foto_carregada = st.file_uploader("Arraste ou escolha a foto que você baixou", type=["png", "jpg", "jpeg"])

if foto_carregada:
    st.image(foto_carregada, caption="Imagem do seu post", width=300)

st.write("---")
# --- ESCOLHA DA LOJA ---
st.markdown("### 🔗 Passo 2: Escolha o destino")
loja_escolhida = st.radio("Onde você vai vender?", ["Shopee", "Mercado Livre", "Outro Link"])

if loja_escolhida == "Shopee":
    link_usar = LINK_SHOPEE
elif loja_escolhida == "Mercado Livre":
    link_usar = LINK_ML
else:
    link_usar = st.text_input("Cole o link aqui:", "")

# --- GERADOR ---
if st.button("🚀 Passo 3: GERAR TEXTO PARA O POST"):
    if produto and link_usar:
        st.write("---")
        st.markdown("#### ✅ SEU POST ESTÁ PRONTO!")
        
        copy_whats = f"""🔥 *ACHADINHO DA LUHVEE!* 🔥\n\nMeninas, olhem que perfeição esse *{produto}*! 😱✨\n\nAcabei de subir na minha vitrine do {loja_escolhida} com um preço especial para vocês.\n\n👇 *Garanta o seu aqui:*\n{link_usar}\n\nEntrega rápida e segura! 🏃‍♀️💨"""
        st.code(copy_whats, language="text")
        
        st.info("💡 Como postar: Copie o texto acima, abra seu WhatsApp, escolha a foto que você baixou e cole o texto na legenda!")
    else:
        st.error("Luh, preencha o nome do produto e o link! 😉")
