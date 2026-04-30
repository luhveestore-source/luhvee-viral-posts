import streamlit as st
import random
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="LuhVee AI ULTRA PRO", layout="wide", page_icon="👑")

ARQUIVO_HISTORICO = "historico_vendas_luhvee.json"

# Seus Links Oficiais
LINKS_VITRINE = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Hub de Links": "https://links-luhveestore.streamlit.app/"
}

# --- FUNÇÕES DE HISTÓRICO ---
def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return []
    return []

def salvar_no_historico(produto, preco_promo, plataforma, link_final):
    hist = carregar_historico()
    novo_item = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "produto": produto,
        "preco": f"R$ {preco_promo:.2f}",
        "plataforma": plataforma,
        "link": link_final
    }
    hist.append(novo_item)
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(hist, f, ensure_ascii=False, indent=4)

# --- ENGINE DE COPYWRITING ---
ESTRUTURA = {
    "aberturas": ["🚨 OFERTA RELÂMPAGO! 🚨", "😱 OLHA O QUE EU ACHEI!", "🔥 PREÇO BAIXOU AGORA!", "💎 ACHADINHO VIP!", "✨ TREND DO MOMENTO!"],
    "corpo": ["O {produto} está com um desconto bizarro hoje.", "Sério, esse {produto} é o que faltava no seu dia a dia.", "Encontrei o {produto} no menor preço dos últimos tempos!"],
    "urgencia": ["Restam poucas unidades nesse valor! ⏳", "O estoque está acabando rápido demais! 🏃‍♂️", "De R${p_orig} por APENAS R${p_promo}! 💸"],
    "fechamento": ["👉 Garanta o seu aqui: {link}", "🛍️ Link direto para o desconto: {link}", "🔗 Aproveite antes que suba: {link}", "🚀 Voe para o site: {link}"]
}

# --- SCRAPER ---
def buscar_dados_v3(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        # Tenta pegar título de várias formas
        titulo = "Produto Selecionado"
        if soup.find("h1"):
            titulo = soup.find("h1").get_text().strip()
        elif soup.find("title"):
            titulo = soup.find("title").get_text().strip()
        return titulo[:50], 0.0
    except:
        return None, None

# --- INTERFACE ---
st.title("👑 LuhVee AI: Sales Master Pro 3.0")

aba_gerador, aba_historico = st.tabs(["🚀 Gerador de Vendas", "📊 Histórico de Posts"])

with aba_gerador:
    col_link, col_btn = st.columns([3, 1])
    with col_link:
        url_produto_real = st.text_input("1. Cole o Link do Produto (para a IA ler):", placeholder="https://...")
    with col_btn:
        st.write("")
        btn_puxar = st.button("🔍 PUXAR DADOS")

    if btn_puxar and url_produto_real:
        with st.spinner("IA Lendo Produto..."):
            nome, valor = buscar_dados_v3(url_produto_real)
            if nome:
                st.session_state.p_nome = nome
                st.success("Dados Capturados!")

    st.divider()
    
    # Seleção de Plataforma de Destino
    c_plat, c_nome = st.columns([1, 2])
    with c_plat:
        plataforma_sel = st.selectbox("2. Plataforma de Venda:", list(LINKS_VITRINE.keys()))
    with c_nome:
        nome_prod = st.text_input("3. Nome do Produto:", value=st.session_state.get('p_nome', ""))

    c1, c2 = st.columns(2)
    v_orig = c1.number_input("Preço Original (R$):", value=0.0)
    v_promo = c2.number_input("Preço com Desconto (R$):", value=0.0)

    if st.button("🔥 GERAR COPIES E SALVAR"):
        if nome_prod:
            # O link que vai na mensagem é o da sua vitrine
            link_final = LINKS_VITRINE[plataforma_sel]
            
            # Salva no Histórico
            salvar_no_historico(nome_prod, v_promo, plataforma_sel, link_final)
            
            st.subheader(f"✅ Copies Geradas para {plataforma_sel}:")
            cols = st.columns(2)
            for i in range(4):
                with cols[i % 2]:
                    txt = f"{random.choice(ESTRUTURA['aberturas'])}\n\n" \
                          f"{random.choice(ESTRUTURA['corpo']).format(produto=nome_prod.upper())}\n\n" \
                          f"{random.choice(ESTRUTURA['urgencia']).format(p_orig=v_orig, p_promo=v_promo)}\n\n" \
                          f"{random.choice(ESTRUTURA['fechamento']).format(link=link_final)}"
                    
                    st.markdown(f"**Variação {i+1}**")
                    st.code(txt, language="text")
        else:
            st.error("Por favor, identifique o produto primeiro!")

with aba_historico:
    st.header("📋 Histórico de Divulgação")
    dados_hist = carregar_historico()
    
    if dados_hist:
        st.table(dados_hist[::-1])
        if st.button("🗑️ Limpar Tudo"):
            if os.path.exists(ARQUIVO_HISTORICO):
                os.remove(ARQUIVO_HISTORICO)
                st.rerun()
    else:
        st.info("Ainda não há nada no histórico.")
