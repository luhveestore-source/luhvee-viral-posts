import streamlit as st
import random
import requests
from bs4 import BeautifulSoup
import re

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="LuhVee AI ULTRA PRO", layout="wide")

# Banco de dados de frases para gerar variações infinitas
COMPONENTES = {
    "aberturas": ["🚨 OFERTA RELÂMPAGO! 🚨", "😱 OLHA O QUE EU ACHEI!", "🔥 PREÇO BAIXOU AGORA!", "💎 ACHADINHO DE MILHÕES!", "✨ O QUERIDINHO CHEGOU!"],
    "corpo": ["O {produto} está com um preço absurdo hoje.", "Sério, esse {produto} é o que faltava no seu dia a dia.", "Encontrei o {produto} no menor preço dos últimos tempos!"],
    "gatilhos": ["Restam poucas unidades nesse valor! ⏳", "O estoque está acabando rápido demais! 🏃‍♂️", "De R${preco_orig} por APENAS R${preco_promo}! 💸"],
    "ctas": ["👉 Garanta o seu aqui: {link}", "🛍️ Link direto para o desconto: {link}", "🔗 Aproveite antes que suba: {link}"]
}

# --- FUNÇÃO DE CAPTURA REAL ---
def extrair_dados(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        # 1. Segue o redirecionamento (importante para links meli.la)
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 2. Tenta pegar o título (ML usa h1 com essa classe)
        titulo_tag = soup.find("h1", {"class": "ui-pdp-title"})
        titulo = titulo_tag.get_text() if titulo_tag else "Produto Identificado"

        # 3. Tenta pegar o preço original (meta tag é mais confiável)
        preco_tag = soup.find("meta", {"itemprop": "price"})
        preco = float(preco_tag['content']) if preco_tag else 0.0

        return titulo, preco
    except:
        return None, None

# --- INTERFACE ---
st.title("👑 LuhVee AI: Sales Master Pro")

with st.sidebar:
    st.header("🛒 Captura de Link")
    url_input = st.text_input("Cole o Link (Mercado Livre, etc)")
    
    if st.button("🔍 PUXAR DADOS DO PRODUTO"):
        if url_input:
            with st.spinner("IA buscando informações..."):
                nome, preco = extrair_dados(url_input)
                if nome:
                    st.session_state['nome_prod'] = nome
                    st.session_state['preco_orig'] = preco
                    st.success("Dados Capturados!")
                else:
                    st.error("Site bloqueou a captura. Digite manualmente abaixo.")

    st.divider()
    # Campos que recebem os dados da captura
    prod_nome = st.text_input("Nome do Produto", value=st.session_state.get('nome_prod', ""))
    p_orig = st.number_input("Preço Original", value=float(st.session_state.get('preco_orig', 0.0)))
    p_promo = st.number_input("Preço de Venda (Promo)", value=p_orig * 0.85)

# --- BOTÃO DE GERAR COPIES ---
if st.button("🔥 GERAR COPIES INFINITAS"):
    if prod_nome:
        cols = st.columns(2)
        for i in range(4):
            with cols[i % 2]:
                # A mágica acontece aqui: sorteio aleatório de componentes
                texto = f"{random.choice(COMPONENTES['aberturas'])}\n\n" \
                        f"{random.choice(COMPONENTES['corpo']).format(produto=prod_nome)}\n\n" \
                        f"{random.choice(COMPONENTES['gatilhos']).format(preco_orig=p_orig, preco_promo=p_promo)}\n\n" \
                        f"{random.choice(COMPONENTES['ctas']).format(link=url_input)}"
                
                st.subheader(f"Opção {i+1}")
                st.code(texto, language="text")
    else:
        st.warning("Primeiro capture ou digite o nome do produto.")
