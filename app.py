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
    /* Estilo para a caixa de upload não sumir */
    .stFileUploader { background-color: #1e1e1e; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- LINKS OFICIAIS ---
LINK_SHOPEE = "https://collshp.com/luhveestores"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

st.title("🔥 LuhVee Viral Machine")
st.subheader("Gerador de Postagens Grátis")

# --- BANCO DE DADOS ---
# (Mantive as categorias que você pediu)
tendencias = {
    "Perfumaria e Beleza": ["Perfume Caviar Night", "Body Splash Melancia"],
    "Achadinhos de Casa": ["MOP Limpeza Prática", "Organizador de Geladeira"],
    "Móveis": ["Escrivaninha Compacta", "Puff Baú"],
    "Sapatos e Tênis": ["Tênis Chunky", "Salto Scarpin"]
}

if st.button("🔎 IA: SUGERIR PRODUTO DO DIA"):
    cat_sorteada = random.choice(list(tendencias.keys()))
    prod_sorteado = random.choice(tendencias[cat_sorteada])
    st.session_state['produto_sugerido'] = prod_sorteado
    st.session_state['categoria_sugerida'] = cat_sorteada

# --- CAMPOS ---
produto = st.text_input("Nome do Produto:", value=st.session_state.get('produto_sugerido', ""))

st.write("---")
st.markdown("### 📸 Passo 1: Coloque a foto do produto")

# AJUSTE AQUI: Aceitando mais formatos e limpando erro
foto_carregada = st.file_uploader("Arraste a foto ou clique para buscar", type=["png", "jpg", "jpeg", "webp"])

if foto_carregada is not None:
    try:
        st.image(foto_carregada, caption="✅ Imagem carregada com sucesso!", use_column_width=True)
    except:
        st.error("⚠️ Ops! Essa imagem está com um formato difícil. Tente tirar um PRINT da tela e subir o print!")

st.write("---")
st.markdown("### 🔗 Passo 2: Escolha o destino")
loja_escolhida = st.radio("Onde você vai vender?", ["Shopee", "Mercado Livre", "Outro Link"])

if loja_escolhida == "Shopee":
    link_usar = LINK_SHOPEE
elif loja_escolhida == "Mercado Livre":
    link_usar = LINK_ML
else:
    link_usar = st.text_input("Cole o link aqui:", "")

if st.button("🚀 Passo 3: GERAR TEXTO PARA O POST"):
    if produto and link_usar:
        st.write("---")
        st.markdown("#### ✅ SEU POST ESTÁ PRONTO!")
        
        copy_whats = f"""🔥 *ACHADINHO DA LUHVEE!* 🔥\n\nMeninas, olhem que perfeição esse *{produto}*! 😱✨\n\nAcabei de subir na minha vitrine do {loja_escolhida} com um preço especial para vocês.\n\n👇 *Garanta o seu aqui:*\n{link_usar}\n\nEntrega rápida e segura! 🏃‍♀️💨"""
        st.code(copy_whats, language="text")
        st.success("Copia o texto acima e posta com a foto! 🛍️")
