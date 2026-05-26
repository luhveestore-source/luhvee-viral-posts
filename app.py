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
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")
    st.stop()

# --- 3. BANCO DE LINKS OFICIAIS LUHVEES ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Hub": "https://links-luhveestore.streamlit.app/",
    "Shopintegra": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "@luhveestore"
}

# --- 4. NAVEGAÇÃO LATERAL ---
aba = st.sidebar.radio("Selecione o que postar:", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "💬 Mensagens de Grupo"])

# --- PILAR 1: CALÇADOS ---
if aba == "👠 Calçados (Shoes)":
    st.subheader("👟 Gerador Luhvee Shoes - Neurocopy Ativada")
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

# --- PILAR 2: ACHADINHOS (Atualizado com seu novo padrão visual e links) ---
elif aba == "🎁 Achadinhos":
    st.subheader("🎁 Gerador de Achadinhos Sem Rodeios")
    prod_achado = st.text_input("Nome do Produto", placeholder="Ex: Roupão Plush Ultra Macio")
    preco_achado = st.text_input("Preço (R$)", placeholder="69,90")
    loja_principal = st.selectbox("Escolha a Loja Principal do Link:", ["Shopee", "Shein"])

    if st.button("🚀 GERAR MENSAGENS"):
        if prod_achado and preco_achado:
            with st.spinner("IA aplicando gatilhos subconscientes de compra..."):
                prompt = f"""
                Atue como copywriter especialista em Neuromarketing e Neurocopy para e-commerce.
                Crie textos EXTREMAMENTE CURTOS, DIRETOS E SEM ENROLAÇÃO para o produto: '{prod_achado}' pelo valor de R$ {preco_achado}.
                
                Use gatilhos de:
                - Curiosidade e Desejo Visual
                - Oportunidade e Urgência imperdível
                
                Forneça o texto estruturado exatamente assim:
                
                📸 **INSTAGRAM:**
                [Texto curto, focado no desejo estético do produto + Emojis]
                
                💬 **WHATSAPP / TELEGRAM:**
                [Mensagem rápida de um clique, gerando urgência de estoque + Emojis]
                
                📱 **STATUS / STORIES:**
                [Uma frase matadora de no máximo 2 linhas para gerar o clique por impulso]
                """
                response = model.generate_content(prompt)
                
                # Montagem do rodapé fixo exatamente com as alterações que você pediu
                rodapie_personalizado = (
                    f"\n\n🛒 **LINK PARA COMPRAR ({loja_principal.upper()}):**\n"
                    f"🔗 {LINKS[loja_principal]}\n\n"
                    f"🛍️ **COMPRAR NO MERCADO LIVRE:**\n"
                    f"🔗 {LINKS['Mercado Livre']}\n\n"
                    f"🌐 **VEJA TODOS OS ACHADINHOS:**\n"
                    f"👉 {LINKS['Hub']}\n\n"
                    f"Boas compras 🛍️ bjs da Luh ❤️"
                )
                
                st.text_area("Copies com Alta Conversão:", f"{response.text}{rodapie_personalizado}", height=550)
        else:
            st.warning("Preencha o produto e o preço.")

# --- PILAR 3: MENSAGENS DE GRUPO ---
elif aba == "💬 Mensagens de Grupo":
    st.subheader("💬 Máquina de Engajamento
