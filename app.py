import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (Estilo Luhvee Stores) ---
st.set_page_config(page_title="Radar Viral Luhvees 2026", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stMetric { background-color: #1a1a1a; border-left: 5px solid #ff69b4; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Método Educativo: Tratamento de Secrets) ---
# Tentamos buscar a chave. Se não existir, mostramos uma mensagem clara ao usuário.
if "GEMINI_API_KEY" not in st.secrets:
    st.error("🚨 ERRO: A chave 'GEMINI_API_KEY' não foi detectada nos Secrets.")
    st.info("💡 Siga o Passo a Passo abaixo para configurar no painel do Streamlit.")
    st.stop() # Interrompe a execução para evitar outros erros

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Busca automática de modelo para evitar Erro 404
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
except Exception as e:
    st.error(f"Erro técnico na IA: {e}")

# --- 3. LINKS DE VENDA ---
LINKS_VENDA = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825"
}

# --- 4. INTERFACE ---
st.title("🛍️ Radar Viral & Gerador Luhvees")
produto = st.text_input("Qual o produto para a copy?", placeholder="Ex: Sandália Lilás")

if produto:
    st.write("### 🔗 Selecione os Links de Afiliada")
    selecionados = []
    c1, c2, c3 = st.columns(3)
    if c1.checkbox("Shopee"): selecionados.append(f"🔸 Shopee: {LINKS_VENDA['Shopee']}")
    if c2.checkbox("Mercado Livre"): selecionados.append(f"🔹 ML: {LINKS_VENDA['Mercado Livre']}")
    if c3.checkbox("Shein"): selecionados.append(f"👠 Shein: {LINKS_VENDA['Shein']}")

    if st.button("🚀 GERAR POST COMPLETO"):
        with st.spinner("Criando sua copy matadora..."):
            prompt = f"Crie uma legenda curta e viral para vender {produto}. Use gatilhos de urgência."
            response = model.generate_content(prompt)
            
            links_texto = "\n".join(selecionados)
            rodape = "\n\n---\n🔥 WhatsApp: https://wa.me/5511948021428\n📸 Insta: @luhveestore"
            
            st.success("Tudo pronto!")
            st.text_area("Resultado:", response.text + "\n\n📌 ADQUIRA AQUI:\n" + links_texto + rodape, height=350)
