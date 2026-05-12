import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (Identidade Luhvees) ---
st.set_page_config(page_title="Radar Viral & Vendas 2026", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stMetric { background-color: #1a1a1a; border-left: 5px solid #ff69b4; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Segurança via Secrets) ---
try:
    # O código busca a chave salva no painel do Streamlit
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Busca automática do modelo disponível (evita Erro 404)
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
except Exception as e:
    st.error("Erro: A GEMINI_API_KEY não foi encontrada nos Secrets do Streamlit.")

# --- 3. LINKS INEGOCIÁVEIS (Luhvee Stores) ---
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

# --- 4. INTERFACE ---
st.title("🛍️ Radar Viral Luhvee Stores")
produto = st.text_input("O que vamos minerar hoje?", placeholder="Ex: Sandália Lilás")

if produto:
    st.markdown("---")
    col_links = st.columns(3)
    selecionados = []
    
    with col_links[0]:
        if st.checkbox("Shopee"): selecionados.append(f"🔸 Shopee: {LINKS_VENDA['Shopee']}")
    with col_links[1]:
        if st.checkbox("Mercado Livre"): selecionados.append(f"🔹 ML: {LINKS_VENDA['Mercado Livre']}")
    with col_links[2]:
        if st.checkbox("Shein"): selecionados.append(f"👠 Shein: {LINKS_VENDA['Shein']}")

    if st.button("🚀 GERAR POST COMPLETO"):
        with st.spinner("IA processando a melhor estratégia..."):
            try:
                prompt = f"Crie uma legenda curta e viral para vender {produto}. Use gatilhos de urgência."
                response = model.generate_content(prompt)
                
                # Montagem Final
                bloco_links = "\n".join(selecionados)
                rodape = f"\n\n---\n🔥 Grupo VIP: {CONTATOS['Grupo VIP']}\n📱 WhatsApp: {CONTATOS['WhatsApp']}\n📸 Instagram: {CONTATOS['Instagram']}"
                
                st.success("Tudo pronto!")
                st.text_area("Resultado:", response.text + "\n\n📌 ADQUIRA AQUI:\n" + bloco_links + rodape, height=400)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
