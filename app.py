import streamlit as st
import random
from PIL import Image

# --- 1. CONFIGURAÇÃO (A CARA DA SUA MARCA) ---
st.set_page_config(page_title="Hub LuhVee Stores", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p { color: #ffffff !important; text-align: center; }
    /* Botões do Hub para o Cliente */
    .hub-button {
        display: block; width: 100%; padding: 16px; margin: 12px 0;
        text-align: center; color: white !important; 
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        border: 2px solid #ffd700; border-radius: 50px; 
        text-decoration: none; font-weight: bold; font-size: 18px;
    }
    /* Estilo dos botões do seu Robô */
    .stButton>button { background-color: #1e1e1e !important; color: #ff69b4 !important; border: 1px solid #ff69b4 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SEU ESTOQUE DE LINKS (ESTÃO SALVOS AQUI) ---
LINK_SHOPEE = "https://collshp.com/luhveestores"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"
LINK_GRUPO_WHATS = "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
LINK_TELEGRAM = "https://t.me/luhveestores"
LINK_PRODENTIM = "https://luhvee-store.systeme.io/prodentim-special"
LINK_INSTA = "https://instagram.com/luhveestore"
LINK_TIKTOK = "https://www.tiktok.com/@luhvee.stores"
LINK_WHATS_MEU = "https://wa.me/5511948021428"

# --- 3. MENU LATERAL (SEU ESCRITÓRIO SECRETO) ---
with st.sidebar:
    st.markdown("### 👑 Painel da Luh")
    aba = st.radio("Mudar visão:", ["🏠 HUB CLIENTE (Público)", "🔎 PESQUISA & ROBÔ (Privado)"])
    st.write("---")
    st.caption("Aba Privada: Só você usa para criar os posts!")

# ==========================================
# VISÃO DO CLIENTE (O QUE APARECE NO LINK DA BIO)
# ==========================================
if aba == "🏠 HUB CLIENTE (Público)":
    st.markdown("# 🛍️ HUB LUHVEE STORES")
    st.markdown("#### Os melhores achadinhos em um só lugar! ✨")
    
    st.markdown(f'<a href="{LINK_SHOPEE}" class="hub-button">🛍️ Vitrine Oficial Shopee</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{LINK_ML}" class="hub-button">📦 Loja Mercado Livre</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{LINK_PRODENTIM}" class="hub-button">🦷 ProDentim (Saúde Bucal Premium)</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{LINK_GRUPO_WHATS}" class="hub-button">🟢 Grupo de Ofertas WhatsApp</a>', unsafe_allow_html=True)
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1: st.markdown(f'<a href="{LINK_INSTA}" class="hub-button">📸 Instagram</a>', unsafe_allow_html=True)
    with col2: st.markdown(f'<a href="{LINK_TIKTOK}" class="hub-button">📱 TikTok</a>', unsafe_allow_html=True)
    
    st.markdown(f'<a href="{LINK_WHATS_MEU}" class="hub-button">💬 Fale Comigo no WhatsApp</a>', unsafe_allow_html=True)

# ==========================================
# SEU ESCRITÓRIO (ROBÔ E PESQUISA)
# ==========================================
else:
    st.title("🤖 Seu Escritório de Vendas")
    
    # --- PARTE DA PESQUISA ---
    st.subheader("🔎 Pesquisar Tendências")
    if st.button("🔥 O QUE ESTÁ VIRALIZANDO AGORA?"):
        ideias = ["MOP de Limpeza Triangular", "Protetor Solar Coreano em Stick", "Organizador de Maquiagem Giratório", "Mini Selador de Embalagens", "Conjunto Canelado Confort"]
        st.success(f"Dica da IA: Tente postar sobre '{random.choice(ideias)}' hoje!")

    st.write("---")
    
    # --- PARTE DO GERADOR DE POSTS ---
    st.subheader("🚀 Gerar Posts (A Madeirada!)")
    prod_nome = st.text_input("Nome do Produto:")
    loja_escolhida = st.selectbox("Para qual loja?", ["Shopee", "Mercado Livre", "ProDentim"])
    link_final = LINK_SHOPEE if loja_escolhida == "Shopee" else LINK_ML if loja_escolhida == "Mercado Livre" else LINK_PRODENTIM

    if st.button("GERAR TEXTO PARA STATUS"):
        if prod_nome:
            texto = f"Meninas, olha esse {prod_nome}! ✨😱\nFiquei chocada com a qualidade! Já garanti o meu.\n\n🛒 Link para comprar: {link_final}\n\nLuhVee Stores ❤️"
            st.code(texto)
        else:
            st.error("Luh, escreva o nome do produto primeiro! 😘")
