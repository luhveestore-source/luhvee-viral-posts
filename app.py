import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO E IDENTIDADE (Luhvees) ---
st.set_page_config(page_title="Gerador Luhvee Stores Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stMetric { background-color: #1a1a1a; border-left: 5px solid #ff69b4; padding: 15px; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONEXÃO COM A IA (Segurança Secrets) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error("Erro na Chave: Verifique os Secrets do Streamlit.")
    st.stop()

# --- 3. BANCO DE LINKS (Os 3 Pilares) ---
LINKS = {
    "Achadinhos": {
        "Shopee": "https://collshp.com/luhveestores?view=storefront",
        "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
        "Choice": "https://s.click.aliexpress.com/e/_DkazL" # Exemplo Choice
    },
    "Shoes": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "Minha Loja": "https://luhveestores.com.br" # Seu novo domínio de amanhã
}

# --- 4. INTERFACE DE USUÁRIO ---
st.title("🛍️ Central de Copy - Luhvee Stores")

col_input, col_config = st.columns([2, 1])

with col_input:
    nome_prod = st.text_input("Nome do Produto", placeholder="Ex: Blusa de Frio Ultra Quente")
    preco_prod = st.text_input("Preço do Produto", placeholder="Ex: R$ 89,90")
    desc_prod = st.text_area("Descrição/Destaque", placeholder="Ex: A blusa mais quentinha do Brasil, interior peluciado...")

with col_config:
    st.write("### 🎯 Destino da Oferta")
    pilar = st.radio("Escolha o Pilar:", ["Achadinhos", "Luhvee Shoes", "Minha Loja"])
    
    opcoes_links = []
    if pilar == "Achadinhos":
        if st.checkbox("Incluir Shopee"): opcoes_links.append(f"🔸 Shopee: {LINKS['Achadinhos']['Shopee']}")
        if st.checkbox("Incluir Mercado Livre"): opcoes_links.append(f"🔹 ML: {LINKS['Achadinhos']['Mercado Livre']}")
        if st.checkbox("Incluir Choice"): opcoes_links.append(f"📦 Choice: {LINKS['Achadinhos']['Choice']}")
    elif pilar == "Luhvee Shoes":
        opcoes_links.append(f"👟 Shoes: {LINKS['Shoes']}")
    else:
        opcoes_links.append(f"🏠 Minha Loja: {LINKS['Minha Loja']}")

# --- 5. GERAÇÃO E EXIBIÇÃO ---
if st.button("🚀 GERAR MENSAGENS PARA INSTAGRAM E WHATSAPP"):
    if nome_prod and preco_prod:
        with st.spinner("IA criando as melhores ofertas..."):
            # Prompt Pedagógico: Instruímos a IA a separar as redes
            prompt = f"""
            Atue como especialista em marketing para a marca Luhvee Stores. 
            Crie duas mensagens de venda para o produto: {nome_prod}.
            Preço: {preco_prod}. Detalhes: {desc_prod}.
            
            1. Versão Instagram: Use emojis, gatilhos de desejo e hashtags. Seja envolvente.
            2. Versão WhatsApp: Seja direta, use escassez (Estoque limitado) e chame para o clique.
            """
            
            response = model.generate_content(prompt)
            texto_gerado = response.text
            
            links_formatados = "\n".join(opcoes_links)
            rodape = "\n\n---\n📱 WhatsApp: https://wa.me/5511948021428\n📸 Insta: @luhveestore"

            st.divider()
            
            aba_insta, aba_whats = st.tabs(["📸 Versão Instagram", "💬 Versão WhatsApp"])
            
            with aba_insta:
                st.subheader("Copy para Instagram")
                st.text_area("Copie aqui:", f"{texto_gerado.split('2.')[0]}\n\n📌 ADQUIRA AQUI:\n{links_formatados}{rodape}", height=300)
                
            with aba_whats:
                st.subheader("Copy para WhatsApp")
                # Pegamos a segunda parte do texto gerado
                parte_whats = texto_gerado.split('2.')[1] if '2.' in texto_gerado else texto_gerado
                st.text_area("Copie aqui (WhatsApp):", f"{parte_whats}\n\n📌 COMPRE AGORA:\n{links_formatados}{rodape}", height=300)
    else:
        st.warning("Por favor, preencha o Nome e o Preço do produto!")
