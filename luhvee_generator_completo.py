import streamlit as st
import random

st.set_page_config(page_title="👑 LuhVee Gerador Completo", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

st.title("👑 LuhVee - Gerador Completo")
st.markdown("Gerador simples e rápido de cópias de vendas! 🚀")

templates = {
    "🚨 Urgência": "🚨 PROMOÇÃO! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n⏰ TÁ ACABANDO!\n\n{link}\n\nLuhvee Stores ❤️",
    "😱 FOMO": "😱 {produto} ESTÁ VIRALIZANDO!\n\nTodos estão querendo!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
    "💰 Desconto": "💰 SUPER DESCONTO!\n\n{produto}: De R${preco_original} por APENAS R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️",
    "⭐ Social Proof": "⭐ APROVADO POR TODOS!\n\n{produto} - R${preco_promocional}\n\nCentenas de pessoas amando!\n\n{link}\n\nLuhvee Stores ❤️",
    "👑 Exclusividade": "👑 EXCLUSIVO!\n\n{produto}\n\nSelecionado a dedo para você!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
    "🤔 Curiosidade": "🤔 ACHEI ALGO ESPECIAL!\n\n{produto}\n\nVocê vai AMAR!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"
}

col1, col2 = st.columns(2)
with col1:
    st.subheader("📝 Dados")
    produto = st.text_input("Produto", placeholder="Bolsa De Ombro")
    preco_promo = st.text_input("Preço Promo", placeholder="89.90")
with col2:
    st.subheader("⚙️ Configuração")
    preco_original = st.text_input("Preço Original", placeholder="150.00")
    estrategia = st.selectbox("Estratégia", list(templates.keys()))

loja = st.radio("Loja", ["Shopee", "Mercado Livre", "Hub"], horizontal=True)
link = {"Shopee": LINK_SHOPEE, "Mercado Livre": LINK_ML, "Hub": LINK_HUB}[loja]

if st.button("✨ GERAR CÓPIA", use_container_width=True, type="primary"):
    if produto and preco_promo:
        copy = templates[estrategia].format(
            produto=produto,
            preco_original=preco_original,
            preco_promocional=preco_promo,
            link=link
        )
        st.success("✅ Cópia gerada!")
        st.code(copy, language="text")
    else:
        st.error("Preencha produto e preço!")

st.divider()
st.caption("👑 LuhVee - Gerador Completo | Luhvee Stores ❤️")