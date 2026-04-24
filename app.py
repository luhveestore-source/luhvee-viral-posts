import streamlit as st
import random
import json
import os
from datetime import datetime
from itertools import cycle
import time

# Google Trends
try:
    from pytrends.request import TrendReq
    TRENDS_DISPONIVEL = True
except ImportError:
    TRENDS_DISPONIVEL = False

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="👑 LuhVee Vendas PRO com Google Trends", layout="wide")

# 🔗 SEUS LINKS
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# Arquivo de histórico
ARQUIVO_HISTORICO = "luhvee_posts_historico.json"

# Cache para Google Trends
CACHE_TRENDING = "trending_cache.json"

st.title("👑 LuhVee Vendas PRO - Com Google Trends Real")
st.markdown("Gerador de copies + Radar com Google Trends em TEMPO REAL! 🎯📊")

# ===== GOOGLE TRENDS =====

@st.cache_data(ttl=3600)  # Cache por 1 hora
def obter_trending_google():
    """Obtém dados reais do Google Trends com fallback seguro"""
    if not TRENDS_DISPONIVEL:
        st.warning("⚠️ Google Trends não instalado.")
        return None
    
    try:
        # Usa timeout e retry automático
        pytrends = TrendReq(hl='pt-BR', tz=360, timeout=(10, 15))
        
        # Palavras-chave por categoria - MAIS GENÉRICAS pra evitar erro 400
        palavras_chave = {
            "Moda": ["bolsa", "tênis", "bota"],
            "Beleza": ["sérum", "delineador", "protetor"],
            "Tech": ["carregador", "fone", "case"],
            "Casa": ["almofada", "difusor", "luminária"],
            "Pet": ["coleira", "cama pet", "brinquedo"]
        }
        
        trending_data = {}
        
        for categoria, palavras in palavras_chave.items():
            trending_data[categoria] = []
            
            for palavra in palavras:
                try:
                    # Delay maior pra evitar throttling
                    time.sleep(2)  # 2 segundos entre requisições
                    
                    # Busca interesse nos últimos 7 dias
                    pytrends.build_payload([palavra], timeframe='today 7-d', geo='BR')
                    df = pytrends.interest_over_time()
                    
                    if not df.empty and len(df) > 1:
                        interesse_atual = int(df[palavra].iloc[-1])
                        interesse_anterior = int(df[palavra].iloc[0])
                        
                        if interesse_anterior > 0:
                            percentual = int(((interesse_atual - interesse_anterior) / interesse_anterior) * 100)
                        else:
                            percentual = 0
                        
                        # Só adiciona se tiver interesse
                        if interesse_atual > 10:
                            trending_data[categoria].append({
                                "nome": palavra.title(),
                                "interesse": interesse_atual,
                                "tendencia": f"⬆️ +{percentual}%" if percentual > 0 else f"⬇️ {percentual}%",
                                "percentual_raw": percentual
                            })
                    
                except Exception as e:
                    # Silencioso - não mostra erro, continua
                    continue
        
        # Se conseguiu dados, salva cache
        if any(trending_data.values()):
            salvar_trending_cache(trending_data)
            return trending_data
        else:
            return None
    
    except Exception as e:
        return None

def carregar_trending_cache():
    """Carrega cache local se Google Trends falhar"""
    if os.path.exists(CACHE_TRENDING):
        try:
            with open(CACHE_TRENDING, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    return None

def salvar_trending_cache(dados):
    """Salva cache local"""
    try:
        with open(CACHE_TRENDING, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    except:
        pass

# ===== FUNÇÕES DE HISTÓRICO =====

def carregar_historico():
    """Carrega o histórico de posts"""
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_historico(posts):
    """Salva o histórico de posts"""
    with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

def adicionar_ao_historico(produto, preco_promo, preco_original, estrategia, copies):
    """Adiciona um novo post ao histórico"""
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

# ===== BANCO DE DADOS DE PRODUTOS =====

descricoes_categoria = {
    "Casa": {
        "adjetivos": ["prático", "funcional", "moderno", "elegante", "resistente"],
        "beneficios": ["economiza espaço", "facilita o dia a dia", "dura anos", "vale muito a pena", "muda sua rotina"]
    },
    "Beleza": {
        "adjetivos": ["poderoso", "eficaz", "natural", "profissional", "transformador"],
        "beneficios": ["deixa você mais linda", "resultado garantido", "pele impecável", "cabelo dos sonhos", "valor de salão"]
    },
    "Tech": {
        "adjetivos": ["inovador", "inteligente", "poderoso", "fácil de usar", "essencial"],
        "beneficios": ["facilita a vida", "aumenta produtividade", "super prático", "tecnologia pura", "vida mais fácil"]
    },
    "Pet": {
        "adjetivos": ["confortável", "seguro", "carinhoso", "prático", "especial"],
        "beneficios": ["pet ama", "conforto máximo", "saúde do seu pet", "qualidade premium", "amor e cuidado"]
    },
    "Moda": {
        "adjetivos": ["estiloso", "trendy", "elegante", "confortável", "versátil"],
        "beneficios": ["transforma o look", "combina com tudo", "estilo garantido", "trend do momento", "clássico sempre"]
    }
}

# ===== ESTRATÉGIAS DE VENDAS (REDUZIDO) =====

urgencia_whatsapp = [
    "🚨 PROMOÇÃO RELÂMPAGO! {produto} com DESCONTO ABSURDO!\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n⏰ *TÁ ACABANDO!*\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

urgencia_instagram = [
    "🚨 ALERTA DE OFERTA URGENTE! 🚨\n\n{produto} QUEBRANDO PREÇO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 😱\n\n⏰ Tá saindo rápido!\n\n🛒 {link}\n\n#ofertas #promoção #shopeebrasil",
]

urgencia_facebook = [
    "🚨 PROMOÇÃO FLASH AGORA! 🚨\n\n{produto} COM DESCONTO BRUTAL!\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n⏰ ESTOQUE LIMITADO!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

fomo_whatsapp = [
    "😱 ENQUANTO VOCÊ LÊ, ALGUÉM JÁ PEGOU!\n\n{produto} está SUMINDO!\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

fomo_instagram = [
    "👀 VIRA ESSA VOLTA!\n\n{produto} VIRALIZOU! 😱\n\nTodos estão falando!\n\n💰 R${preco_promocional}\n\n🔗 {link}\n\n#viral #trending #luhveestores",
]

fomo_facebook = [
    "😱 OLHA SÓ! {produto} ESTÁ NA BOCA DE TODOS!\n\nTodos estão comprando!\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

desconto_whatsapp = [
    "💰 ACHADO DEMAIS! {produto} em PROMOÇÃO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 🎉\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

desconto_instagram = [
    "💰 ECONOMIZA PRA CARAMBA! {produto}\n\nR${preco_promocional} (ANTES R${preco_original}!) 😱\n\n✨ Qualidade + Preço!\n\n👉 {link}\n\n#desconto #promoção #luhvee",
]

desconto_facebook = [
    "💰 ECONOMIZA DEMAIS! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

social_whatsapp = [
    "⭐ TODO MUNDO AMANDO! {produto} é QUERIDINHO!\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

social_instagram = [
    "⭐ APROVADO POR TODOS! {produto}\n\n💯 Centenas satisfeitos!\n\n💰 R${preco_promocional}\n\n{link}\n\n#recomendação #luhveestores",
]

social_facebook = [
    "⭐ APROVADO E RECOMENDADO! {produto}\n\n✅ Centenas SATISFEITOS!\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

exclusivo_whatsapp = [
    "👑 ACESSO EXCLUSIVO! {produto}\n\nR${preco_promocional} só pra você!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

exclusivo_instagram = [
    "👑 EXCLUSIVO! {produto}\n\n✨ Pra quem tem bom gosto!\n\n💳 R${preco_promocional}\n\n{link}\n\n#exclusive #luhveestores",
]

exclusivo_facebook = [
    "👑 SELEÇÃO ESPECIAL! {produto}\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

curiosidade_whatsapp = [
    "🤔 ADIVINHA O QUÊ? {produto} CHEGOU!\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

curiosidade_instagram = [
    "🤔 ACHEI ALGO QUE VOCÊ VAI AMAR!\n\n{produto} é perfeito!\n\n💰 R${preco_promocional}\n\n👉 {link}\n\n#achado #descoberta",
]

curiosidade_facebook = [
    "🤔 OLHA O QUE EU ENCONTREI! {produto}\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

ESTRATEGIAS = {
    "🚨 Urgência": {
        "whatsapp": urgencia_whatsapp,
        "instagram": urgencia_instagram,
        "facebook": urgencia_facebook
    },
    "😱 FOMO": {
        "whatsapp": fomo_whatsapp,
        "instagram": fomo_instagram,
        "facebook": fomo_facebook
    },
    "💰 Desconto": {
        "whatsapp": desconto_whatsapp,
        "instagram": desconto_instagram,
        "facebook": desconto_facebook
    },
    "⭐ Social Proof": {
        "whatsapp": social_whatsapp,
        "instagram": social_instagram,
        "facebook": social_facebook
    },
    "👑 Exclusividade": {
        "whatsapp": exclusivo_whatsapp,
        "instagram": exclusivo_instagram,
        "facebook": exclusivo_facebook
    },
    "🤔 Curiosidade": {
        "whatsapp": curiosidade_whatsapp,
        "instagram": curiosidade_instagram,
        "facebook": curiosidade_facebook
    }
}

# ===== FUNÇÕES =====

def gerar_copies(produto, preco_promo, preco_original, estrategia, plataforma, link):
    """Gera copies usando a estratégia escolhida"""
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

# ===== INTERFACE PRINCIPAL =====

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Gerar Copies", "🌐 Google Trends", "📊 Histórico", "📥 Importar", "ℹ️ Info"])

# ========== TAB 1: GERAR COPIES ==========
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚙️ Dados do Produto")
        nome_produto = st.text_input("Nome do Produto", placeholder="Ex: Bolsa De Ombro")
        categoria = st.selectbox("Categoria", list(descricoes_categoria.keys()))
        
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
            copies_whatsapp = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "whatsapp", link_selecionado)
            copies_instagram = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "instagram", link_selecionado)
            copies_facebook = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "facebook", link_selecionado)
            
            novo_post = adicionar_ao_historico(
                nome_produto,
                preco_promo,
                preco_original,
                estrategia,
                {
                    "whatsapp": copies_whatsapp,
                    "instagram": copies_instagram,
                    "facebook": copies_facebook
                }
            )
            
            st.success(f"✅ Post #{novo_post['id']} salvo no histórico!")
            
            tab_w, tab_i, tab_f = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
            
            with tab_w:
                st.subheader("Estilo para Grupos/Canais")
                for i, copy in enumerate(copies_whatsapp, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            
            with tab_i:
                st.subheader("Estilo para Feed/Stories")
                for i, copy in enumerate(copies_instagram, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            
            with tab_f:
                st.subheader("Estilo para Grupos/Timeline")
                for i, copy in enumerate(copies_facebook, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            
            st.divider()
            col_s1, col_s2, col_s3, col_s4 = st.columns(4)
            with col_s1:
                st.metric("Produto", nome_produto)
            with col_s2:
                st.metric("Estratégia", estrategia.split()[1])
            with col_s3:
                st.metric("Post ID", f"#{novo_post['id']}")
            with col_s4:
                st.metric("Data", novo_post['data'])
        
        else:
            st.error("Preencha o produto e preço!")

# ========== TAB 2: GOOGLE TRENDS ==========
with tab2:
    st.subheader("🌐 Google Trends - Produtos em ALTA Agora")
    st.info("Dados em TEMPO REAL do Google Trends Brasil! Atualiza a cada 1 hora.")
    
    if st.button("🔄 Buscar Tendências (Google Trends)", use_container_width=True, type="primary"):
        with st.spinner("Buscando tendências no Google Trends... ⏳"):
            trending_google = obter_trending_google()
        
        if trending_google:
            # Salva cache
            salvar_trending_cache(trending_google)
            st.success("✅ Tendências atualizadas!")
            
            # Exibe por categoria
            for categoria, produtos in trending_google.items():
                if produtos:
                    st.subheader(f"📊 {categoria}")
                    
                    # Ordena por percentual
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
                            if st.button(f"Usar", key=f"cache_{categoria}_{produto['nome']}"):
                                st.session_state.nome_produto = produto['nome']
                                st.session_state.categoria = categoria
                                st.success("✅ Produto carregado!")
            else:
                st.error("❌ Não foi possível buscar tendências. Instale: pip install pytrends")
    
    else:
        st.markdown("### Como Usar")
        st.markdown("""
        1. Clique no botão acima
        2. Aguarde buscar dados do Google
        3. Veja produtos em ALTA agora
        4. Clique 'Usar' no que quiser
        5. Automático carrega em 'Gerar Copies'
        
        **Dica:** Quanto maior o Interesse, mais as pessoas estão buscando! 🔥
        """)

# ========== TAB 3: HISTÓRICO ==========
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
        
        col_filtro1, col_filtro2 = st.columns(2)
        with col_filtro1:
            filtro_estrategia = st.selectbox(
                "Filtrar por Estratégia:",
                ["Todas"] + list(ESTRATEGIAS.keys()),
                key="filtro_estrat"
            )
        with col_filtro2:
            filtro_categoria = st.selectbox(
                "Filtrar por Categoria:",
                ["Todas"] + list(descricoes_categoria.keys()),
                key="filtro_cat"
            )
        
        historico_filtrado = historico
        if filtro_estrategia != "Todas":
            historico_filtrado = [p for p in historico_filtrado if p["estrategia"] == filtro_estrategia]
        
        for post in reversed(historico_filtrado):
            with st.expander(f"#{post['id']} - {post['produto']} ({post['data']})"):
                col_info1, col_info2, col_info3 = st.columns(3)
                
                with col_info1:
                    st.metric("Preço", f"R$ {post['preco_promocional']}")
                
                with col_info2:
                    st.metric("Estratégia", post['estrategia'].split()[1])
                
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

# ========== TAB 4: IMPORTAR ==========
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

# ========== TAB 5: INFO ==========
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

# ========== FOOTER ==========
st.divider()
st.caption("👑 LuhVee Vendas PRO com Google Trends | Trending REAL + Histórico Inteligente | Bjs da Luh da LuhVee ❤️")
