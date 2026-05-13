import streamlit as st
import google.generativeai as genai

# --- 1. IDENTIDADE VISUAL (Estilo Luhvee Stores) ---
st.set_page_config(page_title="Central Luhvees Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Segurança via Secrets) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Busca automática de modelo para evitar erro NotFound
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")
    st.stop()

# --- 3. BANCO DE LINKS OFICIAIS (Atualizados) ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Hub": "https://links-luhveestore.streamlit.app/",
    "Shopintegra": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "@luhveestore"
}

# --- 4. NAVEGAÇÃO ---
aba = st.sidebar.radio("Selecione o que postar:", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "🏠 Minha Loja"])

# --- PILAR 1: CALÇADOS (Modelo 'Cansado de Procurar') ---
if aba == "👠 Calçados (Shoes)":
    st.subheader("👟 Gerador Luhvee Shoes")
    nome_calca = st.text_input("Nome do Produto / REF.")
    valor_calca = st.text_input("Preço (R$)")
    desc_calca = st.text_area("Descrição Técnica (Cole aqui os detalhes de material, solado, etc.)")

    if st.button("🚀 GERAR POST DE CALÇADOS"):
        if nome_calca and valor_calca:
            copy_shoes = f"""😤 CANSADO DE PROCURAR?

{nome_calca.upper()} ORIGINAL está AQUI! 👈

Sem fake, sem enganação! ✅

{desc_calca}

💰 R$ {valor_calca}

Fim da busca! 🎉

🛒 COMPRE AGORA:
🏪 Catálogo: {LINKS['Shopintegra']}

💬 WhatsApp: {LINKS['WhatsApp']}

💳 Formas de Pagamento:
✅ Cartão de Crédito
✅ Link de Pagamento
✅ PIX

📲 Instagram: {LINKS['Instagram']}
🔗 Mais Links: {LINKS['Hub']}"""
            st.text_area("Pronto para copiar:", copy_shoes, height=450)
        else:
            st.warning("Preencha o Nome e o Valor.")

# --- PILAR 2: ACHADINHOS (Instagram e WhatsApp) ---
elif aba == "🎁 Achadinhos":
    st.subheader("🎁 Gerador de Achadinhos Viral")
    prod_achado = st.text_input("Nome do Produto")
    preco_achado = st.text_input("Preço")
    loja = st.selectbox("Escolha a Loja:", ["Shopee", "Shein", "Mercado Livre"])

    if st.button("🚀 GERAR MENSAGENS"):
        if prod_achado and preco_achado:
            with st.spinner("IA criando suas copies..."):
                prompt = f"Crie um post viral para {prod_achado} por R$ {preco_achado}. Gere uma versão para Instagram e uma versão curta para WhatsApp."
                response = model.generate_content(prompt)
                
                final_achado = f"{response.text}\n\n🔗 COMPRE AQUI: {LINKS[loja]}\n🔥 Grupo VIP: {LINKS['WhatsApp']}\n🌐 Hub: {LINKS['Hub']}"
                st.text_area("Copies Geradas:", final_achado, height=400)
        else:
            st.warning("Preencha o produto e o preço.")

# --- PILAR 3: MINHA LOJA ---
else:
    st.subheader("🏠 Postagem: Minha Loja")
    st.info("Espaço reservado para o lançamento de amanhã!")
    item_loja = st.text_input("Produto da Loja")
    vlr_loja = st.text_input("Valor")
    
    if st.button("🚀 GERAR POST DA LOJA"):
        prompt_loja = f"Crie uma legenda elegante para vender {item_loja} por {vlr_loja} no meu site oficial."
        res_loja = model.generate_content(prompt_loja)
        st.text_area("Copy da Loja:", f"{res_loja.text}\n\n🔗 SITE: {LINKS['Hub']}\n📱 Whats: {LINKS['WhatsApp']}", height=400)
