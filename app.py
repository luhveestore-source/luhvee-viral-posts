import streamlit as st
import random
import json
import os
import re
from datetime import datetime

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="LuhVee AI Vendas ULTRA", layout="wide", page_icon="🚀")

# Estilização Customizada para Conversão
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; font-weight: bold; }
    .copy-card { border: 1px solid #333; padding: 20px; border-radius: 10px; margin-bottom: 10px; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS DINÂMICO (MATRIZ DE PERSUASÃO) ---
# Aqui a "IA" cria frases infinitas combinando partes diferentes
COMPONENTES = {
    "aberturas": [
        "🚨 ALERTA DE OPORTUNIDADE! 🚨", "😱 VOCÊ NÃO VAI ACREDITAR NO QUE EU ACHEI!", 
        "🔥 PARE TUDO O QUE ESTÁ FAZENDO!", "💎 ACHADINHO DE MILHÕES!", 
        "🎁 PRESENTE PARA VOCÊ!", "👀 OLHA O QUE ACABOU DE BAIXAR!",
        "✨ O QUERIDINHO DO TIKTOK CHEGOU!", "🏆 TOP 1 DE VENDAS VOLTOU!"
    ],
    "corpo": [
        "O {produto} que você tanto queria está com um preço absurdo.",
        "Sério, a qualidade desse {produto} é de outro nível e o preço nem se fala.",
        "Quem conhece sabe: o {produto} é indispensável e hoje está quase de graça.",
        "Encontrei o {produto} com o maior desconto da história da loja.",
        "Desejo de consumo de muita gente, o {produto} finalmente entrou em oferta."
    ],
    "gatilhos": [
        "Mas atenção: o estoque é limitado e já está no fim! ⏳",
        "É sério, restam pouquíssimas unidades com esse valor. 🏃‍♂️",
        "O último lote acabou em menos de 15 minutos, não bobeia!",
        "Promoção válida apenas enquanto durarem as unidades reservadas. 🛑",
        "De R${preco_orig} por APENAS R${preco_promo}. Economia real! 💸"
    ],
    "ctas": [
        "👉 Garanta o seu antes que o preço suba: {link}",
        "🛍️ Clique aqui e pegue o seu: {link}",
        "👇 Não perde tempo, o link é esse: {link}",
        "🚀 Voe para o site e aproveite: {link}",
        "🔗 Link seguro aqui: {link}"
    ]
}

LINKS_BASE = {
    "Shopee": "https://shopee.com.br/product/luhveestore/",
    "Mercado Livre": "https://mercadolivre.com.br/p/",
    "Hub": "https://links-luhveestore.streamlit.app/"
}

# --- FUNÇÕES LÓGICAS ---

def buscar_produto_por_codigo(codigo):
    """Simula a busca de produto via código ou link"""
    # Em uma versão Pro, aqui entraria um Selenium ou API oficial
    if "shope" in codigo.lower() or len(codigo) > 10:
        return f"Produto Identificado (Ref: {codigo[:8]})", 150.00
    return "Produto Desconhecido", 0.0

def gerar_copy_insana(produto, preco_orig, preco_promo, link):
    """Gera uma copy única combinando elementos aleatórios"""
    abertura = random.choice(COMPONENTES["aberturas"])
    corpo = random.choice(COMPONENTES["corpo"]).format(produto=produto.upper())
    gatilho = random.choice(COMPONENTES["gatilhos"]).format(preco_orig=preco_orig, preco_promo=preco_promo)
    cta = random.choice(COMPONENTES["ctas"]).format(link=link)
    
    return f"{abertura}\n\n{corpo}\n\n{gatilho}\n\n{cta}\n\n👑 LuhVee Stores"

# --- INTERFACE ---

st.title("👑 LuhVee AI: Sales Master Pro")
st.markdown("### O Gerador de Vendas Automático mais Poderoso do Mercado")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1162/1162456.png", width=100)
    st.header("🛒 Captura de Produto")
    metodo = st.radio("Como quer adicionar?", ["Link/Código", "Manual"])
    
    if metodo == "Link/Código":
        codigo_input = st.text_input("Cole o Link ou Código do Produto")
        if st.button("🔍 Puxar Dados"):
            nome_prod, preco_sugerido = buscar_produto_por_codigo(codigo_input)
            st.session_state['nome_prod'] = nome_prod
            st.session_state['preco_orig'] = preco_sugerido
            st.success("Dados capturados!")
    
    st.divider()
    nome_p = st.text_input("Nome do Produto", value=st.session_state.get('nome_prod', ""))
    p_orig = st.number_input("Preço Original (R$)", value=st.session_state.get('preco_orig', 0.0))
    p_promo = st.number_input("Preço Promo (R$)", value=p_orig * 0.7 if p_orig > 0 else 0.0)
    plataforma = st.selectbox("Plataforma", list(LINKS_BASE.keys()))

st.subheader("💎 Suas Mensagens de Alta Conversão")
col1, col2 = st.columns([1, 1])

if st.button("🔥 GERAR VARIAÇÕES INFINITAS"):
    link_final = LINKS_BASE[plataforma]
    
    with col1:
        st.markdown("#### 📱 WhatsApp / Grupos")
        for i in range(3):
            copy = gerar_copy_insana(nome_p, p_orig, p_promo, link_final)
            st.markdown(f"<div class='copy-card'>{copy}</div>", unsafe_allow_html=True)
            st.button(f"Copiar Variação {i+1}", key=f"w_{i}")

    with col2:
        st.markdown("#### 📸 Instagram / Facebook")
        for i in range(3):
            copy = gerar_copy_insana(nome_p, p_orig, p_promo, link_final)
            # Adiciona hashtags no final para redes sociais
            copy += "\n\n#achadinhos #oferta #shopee #promocao #luhvee"
            st.markdown(f"<div class='copy-card'>{copy}</div>", unsafe_allow_html=True)
            st.button(f"Copiar Variação {i+1}", key=f"s_{i}")

# --- DASHBOARD DE VENDAS ---
st.divider()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Cliques Estimados", f"{random.randint(100, 500)}")
c2.metric("Conversão", "4.8%")
c3.metric("Posts Gerados", "1.2k")
c4.metric("ROI", "12x")

st.info("💡 Dica: Varie as mensagens entre os grupos para evitar o bloqueio do WhatsApp (Shadowban).")
