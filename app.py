import streamlit as st
import random
import json
import os
from datetime import datetime
import time

try:
    from pytrends.request import TrendReq
    TRENDS_DISPONIVEL = True
except ImportError:
    TRENDS_DISPONIVEL = False

st.set_page_config(page_title="👑 LuhVee Vendas PRO - Google Trends", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

ARQUIVO_HISTORICO = "luhvee_posts_historico.json"
CACHE_TRENDING = "trending_cache.json"

st.title("👑 LuhVee Vendas PRO - Com Google Trends Real")
st.markdown("Gerador de copies + Radar com Google Trends em TEMPO REAL! 🎯📊")

@st.cache_data(ttl=3600)
def obter_trending_google():
    """Obtém dados reais do Google Trends com delays aumentados"""
    if not TRENDS_DISPONIVEL:
        st.warning("⚠️ Google Trends não instalado.")
        return None
    
    try:
        pytrends = TrendReq(hl='pt-BR', tz=360, timeout=(15, 25))
        
        palavras_chave = {
            "Moda": ["bolsa", "tenis", "bota"],
            "Beleza": ["serum", "delineador", "protetor"],
            "Tech": ["carregador", "fone", "case"],
            "Casa": ["almofada", "difusor", "luminaria"],
            "Pet": ["coleira", "cama", "brinquedo"]
        }
        
        trending_data = {}
        
        for categoria, palavras in palavras_chave.items():
            trending_data[categoria] = []
            
            for palavra in palavras:
                try:
                    time.sleep(4)
                    pytrends.build_payload([palavra], timeframe='today 7-d', geo='BR')
                    df = pytrends.interest_over_time()
                    
                    if not df.empty and len(df) > 1:
                        interesse_atual = int(df[palavra].iloc[-1])
                        interesse_anterior = int(df[palavra].iloc[0])
                        
                        if interesse_anterior > 0:
                            percentual = int(((interesse_atual - interesse_anterior) / interesse_anterior) * 100)
                        else:
                            percentual = 0
                        
                        if interesse_atual > 5:
                            trending_data[categoria].append({
                                "nome": palavra.title(),
                                "interesse": interesse_atual,
                                "tendencia": f"⬆️ +{percentual}%" if percentual > 0 else f"⬇️ {percentual}%",
                                "percentual_raw": percentual
                            })
                    
                except Exception as e:
                    time.sleep(2)
                    continue
        
        if any(trending_data.values()):
            salvar_trending_cache(trending_data)
            return trending_data
        else:
            return None
    
    except Exception as e:
        return None

def carregar_trending_cache():
    if os.path.exists(CACHE_TRENDING):
        try:
            with open(CACHE_TRENDING, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    return None

def salvar_trending_cache(dados):
    try:
        with open(CACHE_TRENDING, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    except:
        pass

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
        "copies": copies,
        "views": 0,
        "cliques": 0,
        "vendas": 0
    }
    historico.append(novo_post)
    salvar_historico(historico)
    return novo_post

urgencia_wa = ["🚨 PROMOÇÃO RELÂMPAGO! {produto} com DESCONTO ABSURDO!\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n⏰ *TÁ ACABANDO!*\n\n{link}\n\nLuhvee Stores ❤️"]
urgencia_ig = ["🚨 ALERTA DE OFERTA URGENTE! 🚨\n\n{produto} QUEBRANDO PREÇO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 😱\n\n⏰ Tá saindo rápido!\n\n🛒 {link}\n\n#ofertas #promoção #shopeebrasil"]
urgencia_fb = ["🚨 PROMOÇÃO FLASH AGORA! 🚨\n\n{produto} COM DESCONTO BRUTAL!\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n⏰ ESTOQUE LIMITADO!\n\n{link}\n\nLuhvee Stores ❤️"]

fomo_wa = ["😱 ENQUANTO VOCÊ LÊ, ALGUÉM JÁ PEGOU!\n\n{produto} está SUMINDO!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
fomo_ig = ["👀 VIRA ESSA VOLTA!\n\n{produto} VIRALIZOU! 😱\n\nTodos estão falando!\n\n💰 R${preco_promocional}\n\n🔗 {link}\n\n#viral #trending #luhveestores"]
fomo_fb = ["😱 OLHA SÓ! {produto} ESTÁ NA BOCA DE TODOS!\n\nTodos estão comprando!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

desconto_wa = ["💰 ACHADO DEMAIS! {produto} em PROMOÇÃO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 🎉\n\n{link}\n\nLuhvee Stores ❤️"]
desconto_ig = ["💰 ECONOMIZA PRA CARAMBA! {produto}\n\nR${preco_promocional} (ANTES R${preco_original}!) 😱\n\n✨ Qualidade + Preço!\n\n👉 {link}\n\n#desconto #promoção #luhvee"]
desconto_fb = ["💰 ECONOMIZA DEMAIS! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]

social_wa = ["⭐ TODO MUNDO AMANDO! {produto} é QUERIDINHO!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
social_ig = ["⭐ APROVADO POR TODOS! {produto}\n\n💯 Centenas de clientes satisfeitos!\n\n💰 R${preco_promocional}\n\n{link}\n\n#recomendação #luhveestores"]
social_fb = ["⭐ APROVADO E RECOMENDADO! {produto}\n\n✅ Centenas SATISFEITOS!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

exclusivo_wa = ["👑 ACESSO EXCLUSIVO! {produto}\n\nR${preco_promocional} só pra você!\n\n{link}\n\nLuhvee Stores ❤️"]
exclusivo_ig = ["👑 EXCLUSIVO! {produto}\n\n✨ Pra quem tem bom gosto!\n\n💳 R${preco_promocional}\n\n{link}\n\n#exclusive #luhveestores"]
exclusivo_fb = ["👑 SELEÇÃO ESPECIAL! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

curiosidade_wa = ["🤔 ADIVINHA O QUÊ? {produto} CHEGOU!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
curiosidade_ig = ["🤔 ACHEI ALGO QUE VOCÊ VAI AMAR!\n\n{produto} é perfeito!\n\n💰 R${preco_promocional}\n\n{link}\n\n#achado #descoberta"]
curiosidade_fb = ["🤔 OLHA O QUE EU ENCONTREI! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

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
    copies_geradas = []
    for template in templates:
        copy = template.format(
            produto=produto,
            preco_original=preco_original,
            preco_promocional=preco_promo,
            link=link
        )
        copies_geradas.append(copy)
    return copies_geradas

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Gerar Copies", "🌐 Google Trends", "📊 Histórico", "📥 Importar", "ℹ️ Info"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ Dados do Produto")
        nome_produto = st.text_input("Nome do Produto", placeholder="Ex: Bolsa De Ombro")
        categoria = st.selectbox("Categoria", ["Casa", "Beleza", "Tech", "Pet", "Moda"])
    with col2:
        st.subheader("💰 Preços")
        preco_promo = st.text_input("Preço Promocional", placeholder="R$ XX,XX")
        preco_original = st.text_input("Preço Original", placeholder="R$ XX,XX")
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("🎯 Estratégia")
        estrategia = st.selectbox("Escolha a estratégia:", list(ESTRATEGIAS.keys()))
    with col4:
        st.subheader("🛒 Plataforma")
        plataforma = st.radio("Onde vai vender?", ["Shopee", "Mercado Livre", "Hub"], horizontal=True)
    
    link_selecionado = {"Shopee": LINK_SHOPEE, "Mercado Livre": LINK_ML, "Hub": LINK_HUB}[plataforma]
    
    if st.button("✨ GERAR COPIES", use_container_width=True, type="primary"):
        if nome_produto and preco_promo:
            copies_wa = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "whatsapp", link_selecionado)
            copies_ig = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "instagram", link_selecionado)
            copies_fb = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "facebook", link_selecionado)
            
            novo_post = adicionar_ao_historico(nome_produto, preco_promo, preco_original, estrategia, {
                "whatsapp": copies_wa,
                "instagram": copies_ig,
                "facebook": copies_fb
            })
            
            st.success(f"✅ Post #{novo_post['id']} salvo!")
            
            tab_w, tab_i, tab_f = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
            with tab_w:
                st.subheader("Estilo para Grupos/Canais")
                for i, copy in enumerate(copies_wa, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            with tab_i:
                st.subheader("Estilo para Feed/Stories")
                for i, copy in enumerate(copies_ig, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            with tab_f:
                st.subheader("Estilo para Grupos/Timeline")
                for i, copy in enumerate(copies_fb, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()

with tab2:
    st.subheader("🌐 Google Trends - Produtos em ALTA Agora")
    st.info("Dados em TEMPO REAL do Google Trends Brasil! Atualiza a cada 1 hora.")
    
    if st.button("🔄 Buscar Tendências (Google Trends)", use_container_width=True, type="primary"):
        with st.spinner("Buscando tendências no Google Trends... ⏳"):
            trending_google = obter_trending_google()
        
        if trending_google:
            st.success("✅ Tendências atualizadas!")
            
            for categoria, produtos in trending_google.items():
                if produtos:
                    st.subheader(f"📊 {categoria}")
                    
                    produtos_ordenados = sorted(produtos, key=lambda x: x['percentual_raw'], reverse=True)
                    
                    for idx, produto in enumerate(produtos_ordenados, 1):
                        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                        
                        with col1:
                            st.markdown(f"**{idx}. {produto['nome']}**")
                        
                        with col2:
                            st.metric("Interesse", produto['interesse'])
                        
                        with col3:
                            st.markdown(f"**{produto['tendencia']}**")
                        
                        with col4:
                            if st.button(f"Usar", key=f"usar_trend_{categoria}_{produto['nome']}"):
                                st.session_state.nome_produto = produto['nome']
                                st.session_state.categoria = categoria
                                st.success("✅ Produto carregado! Vá para 'Gerar Copies'")
                        
                        st.divider()
        
        else:
            st.warning("⚠️ Não consegui buscar Google Trends. Tentando cache local...")
            trending_cache = carregar_trending_cache()
            
            if trending_cache:
                st.info("📦 Mostrando dados em cache")
                for categoria, produtos in trending_cache.items():
                    if produtos:
                        st.subheader(f"📊 {categoria} (Cache)")
                        for idx, produto in enumerate(produtos[:3], 1):
                            st.markdown(f"**{idx}. {produto['nome']}** - Interesse: {produto['interesse']} {produto['tendencia']}")
            else:
                st.error("❌ Instale: pip install pytrends")

with tab3:
    st.subheader("📊 Histórico de Posts")
    
    historico = carregar_historico()
    
    if historico:
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        with col_stats1:
            st.metric("Total de Posts", len(historico))
        with col_stats2:
            total_views = sum(p.get("views", 0) for p in historico)
            st.metric("Total Views", total_views)
        with col_stats3:
            total_vendas = sum(p.get("vendas", 0) for p in historico)
            st.metric("Total Vendas", total_vendas)
        
        st.divider()
        
        for post in reversed(historico):
            with st.expander(f"#{post['id']} - {post['produto']} ({post['data']})"):
                col_info1, col_info2, col_info3 = st.columns(3)
                
                with col_info1:
                    st.metric("Preço", f"R$ {post['preco_promocional']}")
                
                with col_info2:
                    st.metric("Estratégia", post['estrategia'])
                
                with col_info3:
                    st.metric("Vendas", post.get('vendas', 0))
                
                st.markdown("**Copies Salvos:**")
                tab_h_w, tab_h_i, tab_h_f = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
                
                with tab_h_w:
                    for copy in post['copies'].get('whatsapp', []):
                        st.code(copy, language="text")
                
                with tab_h_i:
                    for copy in post['copies'].get('instagram', []):
                        st.code(copy, language="text")
                
                with tab_h_f:
                    for copy in post['copies'].get('facebook', []):
                        st.code(copy, language="text")
                
                col_op1, col_op2 = st.columns(2)
                with col_op1:
                    if st.button(f"📋 Copiar #{post['id']}", key=f"copiar_{post['id']}"):
                        st.info("Copies copiadas! Cole onde precisa.")
                
                with col_op2:
                    if st.button(f"🗑️ Deletar #{post['id']}", key=f"deletar_{post['id']}"):
                        historico.remove(post)
                        salvar_historico(historico)
                        st.success("Post deletado!")
                        st.rerun()
        
        st.divider()
        
        st.subheader("📥 Exportar Histórico")
        json_str = json.dumps(historico, ensure_ascii=False, indent=2)
        st.download_button(
            label="📥 Baixar Histórico (JSON)",
            data=json_str,
            file_name=f"luhvee_posts_{datetime.now().strftime('%d_%m_%Y')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    else:
        st.warning("Ainda não há posts no histórico!")

with tab4:
    st.subheader("📥 Importar Posts Salvos")
    
    arquivo_upload = st.file_uploader("Escolha um arquivo JSON", type=["json"])
    
    if arquivo_upload:
        try:
            dados_importados = json.load(arquivo_upload)
            
            if isinstance(dados_importados, list):
                st.success(f"✅ Arquivo válido! {len(dados_importados)} posts encontrados.")
                
                if st.button("➕ Adicionar ao Histórico Atual", use_container_width=True, type="primary"):
                    historico_atual = carregar_historico()
                    proximo_id = max([p['id'] for p in historico_atual], default=0) + 1
                    for post in dados_importados:
                        post['id'] = proximo_id
                        proximo_id += 1
                    
                    historico_atual.extend(dados_importados)
                    salvar_historico(historico_atual)
                    
                    st.success(f"✅ {len(dados_importados)} posts importados!")
            else:
                st.error("Formato de arquivo inválido!")
        
        except json.JSONDecodeError:
            st.error("Arquivo JSON inválido!")

with tab5:
    st.subheader("ℹ️ Sobre LuhVee Vendas PRO")
    
    st.markdown("""
    ### 🎯 Versão com Google Trends
    
    Esta versão usa **dados REAIS** do Google Trends Brasil para descobrir:
    - ✅ O que tá viralizando AGORA
    - ✅ % de crescimento de busca
    - ✅ Tendências por categoria
    - ✅ Produtos em alta demanda
    
    ### 🔧 Instalação
    ```bash
    pip install pytrends
    ```
    
    ### 📊 Como Funciona
    1. Busca **7 últimos dias** do Google
    2. Calcula **% de crescimento**
    3. Mostra **interesse atual**
    4. **1-click** para usar no copy
    
    ### 💡 Dicas
    - Refresh a cada 1 hora (cache)
    - Produtos com +50% = SUPER trending
    - Use produtos trending com Urgência/FOMO
    - Sempre acompanhe as tendências!
    
    ### 🎁 Recursos
    - ✅ 6 estratégias de venda
    - ✅ Google Trends integrado
    - ✅ Multicanal (3 plataformas)
    - ✅ Histórico completo
    - ✅ Backup em JSON
    - ✅ Todos seus links
    
    ### 📞 Suporte
    Leia a documentação completa em GitHub!
    """)

st.divider()
st.caption("👑 LuhVee Vendas PRO com Google Trends | Luhvee Stores ❤️")
