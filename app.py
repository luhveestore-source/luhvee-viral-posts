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

# --- 2. INTELIGÊNCIA E IA (Segurança via Secrets) ---
try:
    # Busca a chave configurada no painel do Streamlit
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Método educativo: lista modelos para garantir que o app não quebre (evita Erro 404)
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel('models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0])
except Exception as e:
    st.error("Erro: Verifique a GEMINI_API_KEY nos Secrets do Streamlit.")

# --- 3. LINKS INEGOCIÁVEIS (Contatos e Afiliados) ---
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

# --- 4. FUNÇÕES DE MINERAÇÃO ---
def buscar_tendencias(termo):
    try:
        url = f"https://news.google.com/rss/search?q={termo}+2026+tendencia&hl=pt-BR"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        # Retorna os 3 títulos mais relevantes
        return [item.title.text.split(" - ")[0] for item in soup.find_all('item', limit=3)]
    except:
        return ["Tendência em alta para 2026 confirmada!"]

# --- 5. INTERFACE DO RADAR ---
st.title("🔥 Radar Viral Luhvee Stores")
produto_input = st.text_input("O que vamos minerar hoje?", placeholder="Ex: Sandália de Salto, Sérum Facial...")

if produto_input:
    # Mineração e Análise
    st.markdown("---")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("🌐 Radar de Tendências")
        tendencias = buscar_tendencias(produto_input)
        for t in tendencias:
            st.write(f"✅ {t}")

    with col_b:
        st.subheader("🔗 Gerador de Links de Afiliada")
        selecionados = []
        if st.checkbox("Shopee"): selecionados.append(f"🔸 Shopee: {LINKS_VENDA['Shopee']}")
        if st.checkbox("Mercado Livre"): selecionados.append(f"🔹 ML: {LINKS_VENDA['Mercado Livre']}")
        if st.checkbox("Shein"): selecionados.append(f"👠 Shein: {LINKS_VENDA['Shein']}")
        if st.checkbox("Luhvee Shoes"): selecionados.append(f"👟 Shoes: {LINKS_VENDA['Luhvee Shoes']}")

    # --- 6. GERAÇÃO DA COPY FINAL ---
    if st.button("🚀 GERAR POST COMPLETO"):
        with st.spinner("IA processando a melhor estratégia..."):
            prompt = f"Atue como expert em marketing. Crie uma legenda curta e viral para vender {produto_input}. Foco em urgência e no ano de 2026."
            response = model.generate_content(prompt)
            
            # Montagem Final
            bloco_links = "\n".join(selecionados)
            rodape = f"\n\n---\n🔥 Grupo VIP: {CONTATOS['Grupo VIP']}\n📱 WhatsApp: {CONTATOS['WhatsApp']}\n📸 Instagram: {CONTATOS['Instagram']}"
            
            st.success("Tudo pronto para postar!")
            st.text_area("Copy Final:", response.text + "\n\n📌 ADQUIRA AQUI:\n" + bloco_links + rodape, height=400)
else:
    st.info("Digite um produto acima para começar a inteligência de mercado.")
