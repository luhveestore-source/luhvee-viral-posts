import streamlit as st
import random
import requests
from bs4 import BeautifulSoup
import re

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="LuhVee AI ULTRA PRO", layout="wide", page_icon="🚀")

# Estilização
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; }
    .copy-card { border: 1px solid #333; padding: 15px; border-radius: 10px; background-color: #161b22; color: #fff; margin-bottom: 10px;}
    </style>
    """, unsafe_allow_html=True)

# --- MATRIZ DE PERSUASÃO INFINITA ---
COMPONENTES = {
    "aberturas": ["🚨 OFERTA RELÂMPAGO! 🚨", "😱 OLHA O QUE EU ACHEI!", "🔥 PREÇO BAIXOU AGORA!", "💎 ACHADINHO EXCLUSIVO!", "✨ TREND DO MOMENTO!"],
    "corpo": ["O {produto} está com um desconto bizarro hoje.", "Sério, esse {produto} é o que faltava no seu dia a dia.", "Encontrei o {produto} no menor preço dos últimos 30 dias!"],
    "gatilhos": ["Restam poucas unidades nesse valor! ⏳", "O estoque está acabando rápido demais! 🏃‍♂️", "De R${preco_orig} por APENAS R${preco_promo}! 💸"],
    "ctas": ["👉 Garanta o seu aqui: {link}", "🛍️ Link direto para o desconto: {link}", "🔗 Aproveite antes que suba: {link}"]
}

# --- FUNÇÃO REAL DE CAPTURA (WEB SCRAPING) ---
def extrair_dados_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        titulo = ""
        preco = 0.0

        # Lógica para Mercado Livre
        if "mercadolivre" in url or "meli.la" in url:
            # Busca o título
            titulo_tag = soup.find("h1", {"class": "ui-pdp-title"})
            titulo = titulo_tag.get_text() if titulo_tag else "Produto Mercado Livre"
            
            # Busca o preço
            preco_tag = soup.find("meta", {"itemprop": "price"})
            if preco_tag:
                preco = float(preco_tag['content'])
            else:
                # Tenta outra forma de achar o preço no ML
                preco_span = soup.find("span", {"class": "andes-money-amount__fraction"})
                if preco_span:
                    preco = float(preco_span.get_text().replace('.', '').replace(',', '.'))

        # Lógica para Shopee (Shopee é mais difícil pois usa JavaScript, mas tentamos o básico)
        elif "shopee" in url:
            titulo = "Produto da Shopee (Confira no Link)"
            # Shopee geralmente bloqueia scrapers simples, o ideal seria API oficial
            # Mas vamos deixar o campo aberto para o usuário ajustar se falhar
            
        return titulo, preco
    except Exception as e:
        return None, None

# --- INTERFACE ---
st.title("👑 LuhVee AI: Sales Master Pro")

with st.sidebar:
    st.header("🛒 Captura Inteligente")
    url_input = st.text_input("Cole o Link (Mercado Livre, Shopee, etc)")
    
    if st.button("🔍 EXTRAIR DADOS AGORA"):
        if url_input:
            with st.spinner("Acessando plataforma..."):
                nome_extraido, preco_extraido = extrair_dados_url(url_input)
                if nome_extraido:
                    st.session_state['nome_prod'] = nome_extraido
                    st.session_state['preco_orig'] = preco_extraido
                    st.success("Dados capturados com sucesso!")
                else:
                    st.error("Não consegui ler o site automaticamente. Digite abaixo:")
        else:
            st.warning("Cole um link válido!")

    st.divider()
    # Campos que recebem os dados capturados
    nome_final = st.text_input("Nome do Produto", value=st.session_state.get('nome_prod', ""))
    p_orig = st.number_input("Preço Original (R$)", value=float(st.session_state.get('preco_orig', 0.0)))
    p_promo = st.number_input("Preço com Desconto (R$)", value=p_orig * 0.8)
    link_venda = st.text_input("Seu Link de Afiliado", value=url_input)

# --- GERAÇÃO DE COPIES ---
if st.button("🔥 GERAR VARIAÇÕES INFINITAS PARA VENDER"):
    if nome_final and link_venda:
        cols = st.columns(2)
        for i in range(4): # Gera 4 variações
            canal = "WhatsApp" if i < 2 else "Instagram"
            with cols[0 if i < 2 else 1]:
                abertura = random.choice(COMPONENTES["aberturas"])
                corpo = random.choice(COMPONENTES["corpo"]).format(produto=nome_final)
                gatilho = random.choice(COMPONENTES["gatilhos"]).format(preco_orig=p_orig, preco_promo=p_promo)
                cta = random.choice(COMPONENTES["ctas"]).format(link=link_venda)
                
                texto_final = f"{abertura}\n\n{corpo}\n\n{gatilho}\n\n{cta}"
                st.markdown(f"**Variação {i+1} ({canal})**")
                st.code(texto_final, language="text")
    else:
        st.error("Preencha o nome do produto e o link!")

# Dashboard fake para valorizar o software
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Poder de Conversão", "Alta", "98%")
c2.metric("Variações Disponíveis", "Infinitas")
c3.metric("Status da IA", "Online", "Turbo")
