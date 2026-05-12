import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (Estilo Luhvee Stores) ---
st.set_page_config(page_title="Radar Viral Luhvees 2026", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stMetric { background-color: #1a1a1a; border-left: 5px solid #ff69b4; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Segurança via Secrets) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Busca o modelo disponível para evitar Erro 404
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
except Exception as e:
    st.error("Erro: Verifique a GEMINI_API_KEY nos Secrets do Streamlit.")

# --- 3. BANCO DE LINKS INEGOCIÁVEIS (Seus contatos fixos) ---
CONTATOS = {
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "https://instagram.com/luhveestore",
    "Grupo VIP": "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
}

LINKS_VENDA = {
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Luhvee Shoes": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes"
}

# --- 4. FUNÇÕES DE INTELIGÊNCIA ---
def analisar_nicho(produto):
    p = produto.lower()
    if any(k in p for k in ['sapato', 'tenis', 'salto', 'bota', 'sandalia']):
        return "Calçados Femininos", "Elegância e Conforto"
    return "Achadinhos Gerais", "Praticidade e Estilo"

def minerar_tendencia(termo):
    try:
        url = f"https://news.google.com/rss/search?q={termo}+brasil+2026&hl=pt-BR"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        return [item.title.text.split(" - ")[0] for item in soup.find_all('item', limit=3)]
    except:
        return []

# --- 5. INTERFACE ---
st.title("🛍️ Radar Viral & Gerador de Afiliados")
produto = st.text_input("Qual o produto do momento?", placeholder="Ex: Sandália Lilás")

if produto:
    nicho, gatilho = analisar_nicho(produto)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Nicho Identificado", nicho)
    with col_b:
        st.write("**O que está em alta:**")
        noticias = minerar_tendencia(produto)
        for n in noticias: st.write(f"✅ {n}")

    st.markdown("---")
    
    st.write("### 🔗 Selecione os Links de Afiliada")
    selecionados = []
    c1, c2, c3, c4 = st.columns(4)
    if c1.checkbox("Shopee"): selecionados.append(f"🔸 Shopee: {LINKS_VENDA['Shopee']}")
    if c2.checkbox("Mercado Livre"): selecionados.append(f"🔹 ML: {LINKS_VENDA['Mercado Livre']}")
    if c3.checkbox("Shein"): selecionados.append(f"👠 Shein: {LINKS_VENDA['Shein']}")
    if c4.checkbox("Shoes"): selecionados.append(f"👟 Shoes: {LINKS_VENDA['Luhvee Shoes']}")

    if st.button("🚀 GERAR POST COMPLETO"):
        with st.spinner("Criando sua copy matadora..."):
            prompt = f"Crie uma legenda curta e viral para vender {produto}. Use gatilhos de {gatilho}. Foco em 2026."
            response = model.generate_content(prompt)
            
            # Montagem Final
            texto_venda = "\n".join(selecionados)
            rodape = f"\n\n---\n🔥 Grupo VIP: {CONTATOS['Grupo VIP']}\n📱 Whats: {CONTATOS['WhatsApp']}\n📸 Insta: {CONTATOS['Instagram']}"
            
            st.success("Tudo pronto para postar!")
            st.text_area("Resultado:", response.text + "\n\n📌 ADQUIRA AQUI:\n" + texto_venda + rodape, height=400)
