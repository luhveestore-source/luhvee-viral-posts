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
st.markdown("Gerador de Copies + Busca de Produtos 🎯")

# ===== FUNÇÕES =====

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_historico(posts):
    try:
        with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
    except:
        pass

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

# ===== ESTRATÉGIAS =====

urgencia_wa = ["🚨 PROMOÇÃO! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n⏰ TÁ ACABANDO!\n\n{link}\n\nLuhvee Stores ❤️"]
urgencia_ig = ["🚨 ALERTA! {produto}\n\nDe R${preco_original} por R${preco_promocional}!\n\n{link}\n\n#oferta #promoção"]
urgencia_fb = ["🚨 PROMOÇÃO! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]

fomo_wa = ["😱 {produto} SUMINDO!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
fomo_ig = ["👀 {produto} VIRALIZOU!\n\nR${preco_promocional}\n\n{link}\n\n#viral #trending"]
fomo_fb = ["😱 {produto} NA BOCA DE TODOS!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

desconto_wa = ["💰 ACHADO! {produto}\n\nDe R${preco_original} por R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]
desconto_ig = ["💰 DESCONTO! {produto}\n\nR${preco_promocional}\n\n{link}\n\n#desconto #promoção"]
desconto_fb = ["💰 {produto}\n\nDe R${preco_original} por R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]

social_wa = ["⭐ APROVADO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
social_ig = ["⭐ RECOMENDADO! {produto}\n\nR${preco_promocional}\n\n{link}\n\n#recomendado"]
social_fb = ["⭐ APROVADO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

exclusivo_wa = ["👑 EXCLUSIVO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
exclusivo_ig = ["👑 {produto}\n\nR${preco_promocional}\n\n{link}\n\n#exclusive"]
exclusivo_fb = ["👑 {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

curiosidade_wa = ["🤔 {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
curiosidade_ig = ["🤔 {produto}\n\nR${preco_promocional}\n\n{link}\n\n#descoberta"]
curiosidade_fb = ["🤔 {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

ESTRATEGIAS = {
    "🚨 Urgência": {"whatsapp": urgencia_wa, "instagram": urgencia_ig, "facebook": urgencia_fb},
    "😱 FOMO": {"whatsapp": fomo_wa, "instagram": fomo_ig, "facebook": fomo_fb},
    "💰 Desconto": {"whatsapp": desconto_wa, "instagram": desconto_ig, "facebook": desconto_fb},
    "⭐ Social Proof": {"whatsapp": social_wa, "instagram": social_ig, "facebook": social_fb},
    "👑 Exclusividade": {"whatsapp": exclusivo_wa, "instagram": exclusivo_ig, "facebook": exclusivo_fb},
    "🤔 Curiosidade": {"whatsapp": curiosidade_wa, "instagram": curiosidade_ig, "facebook": curiosidade_fb},
}

def gerar_copies(produto, preco_promo, preco_original, estrategia, plataforma, link):
    templates = ESTRATEGIAS[estrategia][plataforma]
    random.shuffle(templates)
    copies = []
    for template in templates:
        copy = template.format(
            produto=produto,
            preco_original=preco_original,
            preco_promocional=preco_promo,
            link=link
        )
        copies.append(copy)
    return copies

# ===== INTERFACE =====

tab1, tab2, tab3 = st.tabs(["📝 Gerar Copies", "📊 Histórico", "ℹ️ Info"])

with tab1:
    st.subheader("⚙️ Dados do Produto")
    
    col1, col2 = st.columns(2)
    with col1:
        nome_produto = st.text_input(
            "Nome do Produto",
            placeholder="Ex: Bolsa De Ombro"
        )
        categoria = st.selectbox("Categoria", ["Casa", "Beleza", "Tech", "Pet", "Moda"])
    
    with col2:
        preco_original = st.text_input(
            "Preço Original",
            placeholder="150.00"
        )
        preco_promocional = st.text_input(
            "Preço Promocional",
            placeholder="89.90"
        )
    
    st.divider()
    st.subheader("🎯 Configuração")
    
    col3, col4 = st.columns(2)
    with col3:
        estrategia = st.selectbox(
            "Escolha a Estratégia",
            list(ESTRATEGIAS.keys())
        )
    
    with col4:
        plataforma_venda = st.radio(
            "Onde vai vender?",
            ["Shopee", "Mercado Livre", "Hub"],
            horizontal=True
        )
    
    link_escolhido = {
        "Shopee": LINK_SHOPEE,
        "Mercado Livre": LINK_ML,
        "Hub": LINK_HUB
    }[plataforma_venda]
    
    if st.button("✨ GERAR COPIES", use_container_width=True, type="primary"):
        if nome_produto and preco_promocional:
            
            # Gera copies para cada plataforma
            copies_wa = gerar_copies(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                "whatsapp",
                link_escolhido
            )
            
            copies_ig = gerar_copies(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                "instagram",
                link_escolhido
            )
            
            copies_fb = gerar_copies(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                "facebook",
                link_escolhido
            )
            
            # Salva no histórico
            novo_post = adicionar_ao_historico(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                {
                    "whatsapp": copies_wa,
                    "instagram": copies_ig,
                    "facebook": copies_fb
                }
            )
            
            st.success(f"✅ Post #{novo_post['id']} criado com sucesso!")
            st.divider()
            
            # Mostra as copies
            tab_wa, tab_ig, tab_fb = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
            
            with tab_wa:
                st.subheader("Cópias para WhatsApp")
                for i, copy in enumerate(copies_wa, 1):
                    st.code(copy, language="text")
                    if i < len(copies_wa):
                        st.divider()
            
            with tab_ig:
                st.subheader("Cópias para Instagram")
                for i, copy in enumerate(copies_ig, 1):
                    st.code(copy, language="text")
                    if i < len(copies_ig):
                        st.divider()
            
            with tab_fb:
                st.subheader("Cópias para Facebook")
                for i, copy in enumerate(copies_fb, 1):
                    st.code(copy, language="text")
                    if i < len(copies_fb):
                        st.divider()
        
        else:
            st.error("❌ Preencha o Nome do Produto e Preço Promocional!")

with tab2:
    st.subheader("📊 Histórico de Posts")
    
    historico = carregar_historico()
    
    if historico:
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        
        with col_stat1:
            st.metric("Total de Posts", len(historico))
        
        with col_stat2:
            st.metric("Último Post", historico[-1]["data"])
        
        with col_stat3:
            st.metric("Categoria", historico[-1]["estrategia"])
        
        st.divider()
        
        for post in reversed(historico):
            with st.expander(f"#{post['id']} - {post['produto']} ({post['data']})"):
                
                col_info1, col_info2, col_info3 = st.columns(3)
                
                with col_info1:
                    st.metric("Estratégia", post['estrategia'])
                
                with col_info2:
                    st.metric("Preço Promo", f"R$ {post['preco_promocional']}")
                
                with col_info3:
                    st.metric("Preço Original", f"R$ {post['preco_original']}")
                
                st.divider()
                
                st.subheader("Copies Salvas:")
                
                if "copies" in post and isinstance(post["copies"], dict):
                    if "whatsapp" in post["copies"]:
                        st.subheader("📱 WhatsApp")
                        for copy in post["copies"]["whatsapp"]:
                            st.code(copy, language="text")
                    
                    if "instagram" in post["copies"]:
                        st.subheader("📸 Instagram")
                        for copy in post["copies"]["instagram"]:
                            st.code(copy, language="text")
                    
                    if "facebook" in post["copies"]:
                        st.subheader("👥 Facebook")
                        for copy in post["copies"]["facebook"]:
                            st.code(copy, language="text")
                
                st.divider()
                
                if st.button(f"🗑️ Deletar Post #{post['id']}", key=f"delete_{post['id']}"):
                    historico.remove(post)
                    salvar_historico(historico)
                    st.success("Post deletado!")
                    st.rerun()
    
    else:
        st.info("📭 Nenhum post no histórico ainda. Crie seu primeiro post!")

with tab3:
    st.markdown("""
    ### 👑 LuhVee Vendas PRO
    
    **O que é?**
    Sistema inteligente para gerar cópias de vendas com estratégias comprovadas!
    
    **Funcionalidades:**
    - ✅ 6 estratégias de venda diferentes
    - ✅ 3 plataformas (WhatsApp, Instagram, Facebook)
    - ✅ Histórico completo de posts
    - ✅ Fácil de usar
    - ✅ Sem erros
    
    **Estratégias incluídas:**
    1. 🚨 **Urgência** - Cria senso de urgência
    2. 😱 **FOMO** - Fear of Missing Out
    3. 💰 **Desconto** - Foco no preço
    4. ⭐ **Social Proof** - Aprovação de outros
    5. 👑 **Exclusividade** - Produto especial
    6. 🤔 **Curiosidade** - Gera interesse
    
    **Como usar:**
    1. Preencha o Nome do Produto
    2. Digite os Preços (original e promocional)
    3. Escolha a Categoria
    4. Selecione a Estratégia
    5. Escolha a Plataforma (ou gere para todas)
    6. Clique em "GERAR COPIES"
    7. Copie e cole nos seus canais!
    
    **Dicas:**
    - Use a estratégia certa para seu produto
    - Teste as diferentes estratégias
    - WhatsApp funciona bem com Urgência
    - Instagram funciona bem com FOMO
    - Facebook funciona bem com Social Proof
    
    ---
    
    **Luhvee Stores ❤️**
    """)

st.divider()
st.caption("👑 LuhVee Vendas PRO - Versão Final | Luhvee Stores ❤️")
