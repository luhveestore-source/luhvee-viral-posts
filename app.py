import streamlit as st
import google.generativeai as genai

# --- 1. ESTILO VISUAL (Luhvees) ---
st.set_page_config(page_title="Radar Viral Luhvees 2026", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stMetric { background-color: #1a1a1a; border-left: 5px solid #ff69b4; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Busca nos Secrets) ---
# MÉTODO EDUCATIVO: O comando st.secrets busca a chave no painel do Streamlit Cloud, não no código.
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Seleciona o modelo disponível
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
    else:
        st.error("🚨 Chave não encontrada nos Secrets do Streamlit!")
        st.stop()
except Exception as e:
    st.error(f"Erro técnico: {e}")
    st.stop()

# --- 3. BANCO DE LINKS ---
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
        with st.spinner("IA processando sua nova chave..."):
            try:
                prompt = f"Crie uma legenda curta e viral para vender {produto}. Use gatilhos de urgência e foco em 2026."
                response = model.generate_content(prompt)
                
                links_texto = "\n".join(selecionados)
                rodape = "\n\n---\n🔥 WhatsApp: https://wa.me/5511948021428\n📸 Insta: @luhveestore"
                
                st.success("Tudo pronto!")
                st.text_area("Resultado:", response.text + "\n\n📌 ADQUIRA AQUI:\n" + links_texto + rodape, height=350)
            except Exception as e:
                st.error(f"Erro ao gerar: {e}")
