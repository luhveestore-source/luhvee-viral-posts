import streamlit as st
import random
import io
from PIL import Image, ImageDraw, ImageFont

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="👑 LuhVee MULTICANAL", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# Banco de dados expandido para IA de texto simples
dados_produtos = {
    "Casa": ["Praticidade total!", "Sua casa merece esse cuidado. ✨", "O queridinho das donas de casa."],
    "Beleza": ["Fique ainda mais linda! 💄", "Resultado de salão em casa.", "O segredo das blogueiras."],
    "Tech": ["Tecnologia que facilita a vida. ⚡", "Gadget indispensável!", "Alta performance e estilo."],
    "Pet": ["Seu pet vai amar! 🐾", "Conforto máximo para seu melhor amigo.", "Cuidado que eles merecem."]
}

# --- FUNÇÕES DE GERAÇÃO DE TEXTO ---

def gerar_v2_whatsapp(produto, p_atual, p_antigo, link):
    return f"""*{produto.upper()}* Tudo o que você precisa em segundos! Reutilizável e prático. ♻️✨

*POR R${p_atual}*
~Custa R${p_antigo}~

*COMPRE AQUI*
{link}

O que você achou dessa oferta? Reage aqui 👍❤️😳"""

def gerar_v2_instagram(produto, p_atual, link):
    return f"""🚨 ALERTA DE OFERTA: {produto.upper()}! 🚨

Desejo de consumo que acabou de baixar o preço! 😱 
Ideal para quem busca qualidade e preço baixo em um só lugar.

💰 APENAS: R${p_atual}

🔗 Link na BIO ou peça nos comentários que eu te envio!
🎁 Catálogo Completo: {LINK_HUB}

#achadinhos #promoção #shopeebrasil #mercadolivre #ofertas #luhvee #estilo"""

def gerar_v2_facebook(produto, p_atual, p_antigo, link):
    return f"""🔥 OPORTUNIDADE ÚNICA NO {produto.upper()}! 🔥

Gente, olha o que acabei de encontrar! Esse produto é excelente e está com um desconto real. De R${p_antigo} por APENAS R${p_atual}.

✅ Compra 100% Segura
✅ Entrega Rápida

Confira os detalhes e garanta o seu aqui: {link}

Dúvidas? Pode chamar! 👇"""

# --- INTERFACE ---
st.title("👑 LuhVee Turbo - Postagem Multicanal")
st.info("Gere copies otimizadas para todas as suas redes sociais de uma vez só!")

with st.sidebar:
    st.header("⚙️ Dados da Oferta")
    nome = st.text_input("Produto")
    cat = st.selectbox("Nicho", list(dados_produtos.keys()))
    p_off = st.text_input("Preço Promo")
    p_real = st.text_input("Preço Original")
    mkt = st.radio("Plataforma", ["Shopee", "Mercado Livre"])
    foto = st.file_uploader("Upload da Imagem", type=["jpg", "png"])

if st.button("🚀 GERAR TODAS AS POSTAGENS"):
    if nome and p_off:
        link_f = LINK_SHOPEE if mkt == "Shopee" else LINK_ML
        
        # Criando as abas para organizar
        tab1, tab2, tab3 = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
        
        with tab1:
            st.subheader("Estilo Canal/Grupo")
            copy_w = gerar_v2_whatsapp(nome, p_off, p_real, link_f)
            st.code(copy_w, language="text")
            
        with tab2:
            st.subheader("Estilo Feed/Stories")
            copy_i = gerar_v2_instagram(nome, p_off, link_f)
            st.code(copy_i, language="text")
            
        with tab3:
            st.subheader("Estilo Grupos de Venda")
            copy_f = gerar_v2_facebook(nome, p_off, p_real, link_f)
            st.code(copy_f, language="text")
            
        if foto:
            st.divider()
            st.image(foto, caption="Preview da Imagem", width=400)
    else:
        st.error("Preencha o nome e o preço promocional!")
