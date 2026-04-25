import streamlit as st
import random
import json
import os
from datetime import datetime

st.set_page_config(page_title="👑 LuhVee Vendas PRO", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

ARQUIVO_HISTORICO = "luhvee_posts_historico.json"

st.title("👑 LuhVee Vendas PRO")

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_historico(posts):
    with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

def adicionar_ao_historico(produto, preco_promo, preco_original, estrategia, copies):
    historico = carregar_historico()
    novo_post = {
        "id": len(historico) + 1,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "produto": produto,
        "preco_promocional": preco_promo,
        "preco_original": preco_original,
        "estrategia": estrategia,
        "copies": copies
    }
    historico.append(novo_post)
    salvar_historico(historico)
    return novo_post

urgencia = ["🚨 PROMOÇÃO! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
fomo = ["😱 {produto} está SUMINDO!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
desconto = ["💰 DESCONTO! {produto}\n\nDe R${preco_original} por R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]
social = ["⭐ APROVADO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

ESTRATEGIAS = {
    "🚨 Urgência": urgencia,
    "😱 FOMO": fomo,
    "💰 Desconto": desconto,
    "⭐ Social Proof": social,
}

col1, col2 = st.columns(2)
with col1:
    produto = st.text_input("Produto", placeholder="Bolsa De Ombro")
    preco_promo = st.text_input("Preço Promo", placeholder="89.90")
with col2:
    preco_original = st.text_input("Preço Original", placeholder="150.00")
    estrategia = st.selectbox("Estratégia", list(ESTRATEGIAS.keys()))

loja = st.radio("Loja", ["Shopee", "Mercado Livre", "Hub"], horizontal=True)
link = {"Shopee": LINK_SHOPEE, "Mercado Livre": LINK_ML, "Hub": LINK_HUB}[loja]

if st.button("✨ GERAR", use_container_width=True, type="primary"):
    if produto and preco_promo:
        template = random.choice(ESTRATEGIAS[estrategia])
        copy = template.format(produto=produto, preco_original=preco_original, preco_promocional=preco_promo, link=link)
        
        novo_post = adicionar_ao_historico(produto, preco_promo, preco_original, estrategia, [copy])
        
        st.success(f"✅ Post #{novo_post['id']} salvo!")
        st.code(copy, language="text")

st.divider()
st.caption("👑 LuhVee Vendas PRO | Luhvee Stores ❤️")