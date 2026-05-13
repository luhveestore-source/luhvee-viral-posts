import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (Identidade Luhvees) ---
st.set_page_config(page_title="Central de Vendas Luhvees", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Segurança via Secrets) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except:
    st.error("Erro: Verifique a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

# --- 3. BANCO DE LINKS E CONTATOS ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Luhvee Shoes": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "Minha Loja": "https://luhveestores.com.br", # Seu novo domínio de amanhã
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "@luhveestore"
}

# --- 4. INTERFACE DE NAVEGAÇÃO ---
st.title("🛍️ Central de Postagens Luhvee Stores")
aba_post = st.sidebar.radio("O que vamos postar hoje?", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "🏠 Minha Loja"])

# --- PILAR 1: CALÇADOS (O formato que você adorou) ---
if aba_post == "👠 Calçados (Shoes)":
    st.subheader("Gerador Técnico: Luhvee Shoes")
    c1, c2 = st.columns(2)
    with c1:
        ref = st.text_input("Nome/REF do Calçado")
        valor = st.text_input("Preço (R$)")
        mat = st.text_input("Material")
    with c2:
        enf = st.text_input("Enfeites")
        pal = st.text_input("Palmilha")
        forr = st.text_input("Forro")
        sol = st.text_input("Solado")

    if st.button("🚀 GERAR POST DE CALÇADOS"):
        copy_shoes = f"""😤 CANSADO DE PROCURAR?\n\n{ref.upper()} ORIGINAL está AQUI! 👈\n\nSem fake, sem enganação! ✅\n\n🔥 Material: {mat};\nEnfeites: {enf};\nPalmilha: {pal};\nForro: {forr};\nSolado {sol}.\n\n💰 R$ {valor}\n\nFim da busca! 🎉\n\n🛒 COMPRE AGORA:\n🏪 Catálogo: {LINKS['Luhvee Shoes']}\n\n💬 WhatsApp: {LINKS['WhatsApp']}\n\n💳 Pagamento: Cartão, Link ou PIX\n\n📲 Insta: {LINKS['Instagram']}"""
        st.text_area("Copie aqui:", copy_shoes, height=400)

# --- PILAR 2: ACHADINHOS (Mensagens Rápidas) ---
elif aba_post == "🎁 Achadinhos":
    st.subheader("Gerador de Achadinhos (Shopee, ML, Shein)")
    prod = st.text_input("Qual o achadinho?")
    preco_achado = st.text_input("Preço")
    loja = st.selectbox("Qual a loja?", ["Shopee", "Mercado Livre", "Shein"])
    
    if st.button("🚀 GERAR MENSAGENS RÁPIDAS"):
        prompt = f"Crie uma copy viral e curta para {prod} por {preco_achado}. Versão 1: Instagram (com emojis). Versão 2: WhatsApp (direta)."
        res = model.generate_content(prompt)
        
        st.info(f"Link de destino: {LINKS[loja]}")
        st.text_area("Posts Gerados:", f"{res.text}\n\n🔗 COMPRE AQUI: {LINKS[loja]}\n🔥 Grupo VIP: {LINKS['WhatsApp']}", height=400)

# --- PILAR 3: MINHA LOJA ---
else:
    st.subheader("🏠 Postagem: Minha Loja Própria")
    item = st.text_input("Produto da Loja")
    vlr = st.text_input("Preço")
    
    if st.button("🚀 GERAR POST DA LOJA"):
        prompt_loja = f"Crie um post elegante para a inauguração da minha loja própria vendendo {item} por {vlr}."
        res_loja = model.generate_content(prompt_loja)
        st.text_area("Copy da Loja:", f"{res_loja.text}\n\n🌐 SITE OFICIAL: {LINKS['Minha Loja']}\n📱 Suporte: {LINKS['WhatsApp']}", height=400)
