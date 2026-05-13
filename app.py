import streamlit as st
import google.generativeai as genai

# --- 1. IDENTIDADE VISUAL (Estilo Luhvees) ---
st.set_page_config(page_title="Central Luhvee Stores Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Correção do Erro NotFound) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Busca automática do modelo disponível para evitar erros de versão
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")
    st.stop()

# --- 3. BANCO DE LINKS E CONTATOS ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Luhvee Shoes": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "Minha Loja": "https://luhveestores.com.br",
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "@luhveestore"
}

# --- 4. NAVEGAÇÃO LATERAL ---
aba = st.sidebar.radio("Selecione o Pilar de Venda:", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "🏠 Minha Loja"])

# --- PILAR 1: CALÇADOS (Versão Simplificada com 3 campos) ---
if aba == "👠 Calçados (Shoes)":
    st.subheader("Gerador Luhvee Shoes (Simplificado)")
    nome_calçado = st.text_input("Nome do Produto / REF.")
    valor_calçado = st.text_input("Preço (R$)")
    desc_tecnica = st.text_area("Descrição Técnica (Material, Palmilha, Solado, etc.)")

    if st.button("🚀 GERAR POST DE CALÇADOS"):
        if nome_calçado and valor_calçado:
            copy_shoes = f"""😤 CANSADO DE PROCURAR?

{nome_calçado.upper()} ORIGINAL está AQUI! 👈

Sem fake, sem enganação! ✅

{desc_tecnica}

💰 R$ {valor_calçado}

Fim da busca! 🎉

🛒 COMPRE AGORA:
🏪 Catálogo: {LINKS['Luhvee Shoes']}

💬 WhatsApp: {LINKS['WhatsApp']}

💳 Formas de Pagamento:
✅ Cartão de Crédito
✅ Link de Pagamento
✅ PIX

📲 Instagram: {LINKS['Instagram']}"""
            st.text_area("Copie sua mensagem de Calçados:", copy_shoes, height=450)
        else:
            st.warning("Preencha o Nome e o Valor.")

# --- PILAR 2: ACHADINHOS (Correção do Erro de IA) ---
elif aba == "🎁 Achadinhos":
    st.subheader("Gerador de Achadinhos Viral")
    produto = st.text_input("Qual o achadinho?")
    preco = st.text_input("Preço")
    loja_selecionada = st.selectbox("Escolha a Loja:", ["Shopee", "Mercado Livre", "Shein"])

    if st.button("🚀 GERAR MENSAGENS (INSTA E WHATS)"):
        if produto and preco:
            with st.spinner("IA criando as versões..."):
                prompt = f"Crie um post viral para {produto} por R$ {preco}. Gere uma versão engajadora para Instagram e uma versão curta para WhatsApp."
                response = model.generate_content(prompt)
                
                final_text = f"{response.text}\n\n🔗 COMPRE AQUI: {LINKS[loja_selecionada]}\n🔥 Grupo VIP: {LINKS['WhatsApp']}"
                st.text_area("Copiáveis (Instagram e WhatsApp):", final_text, height=400)
        else:
            st.warning("Preencha o produto e o preço.")

# --- PILAR 3: MINHA LOJA ---
else:
    st.subheader("🏠 Postagem: Minha Loja Própria")
    item_loja = st.text_input("Produto")
    vlr_loja = st.text_input("Valor")

    if st.button("🚀 GERAR POST DA LOJA"):
        with st.spinner("Gerando copy para a nova loja..."):
            prompt_loja = f"Crie uma legenda de luxo para vender {item_loja} por {vlr_loja} na minha loja própria."
            res_loja = model.generate_content(prompt_loja)
            st.text_area("Copy da Loja:", f"{res_loja.text}\n\n🌐 SITE OFICIAL: {LINKS['Minha Loja']}\n📱 Suporte: {LINKS['WhatsApp']}", height=400)
