import streamlit as st
import random
import json
import os
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup

try:
    from pytrends.request import TrendReq
    TRENDS_DISPONIVEL = True
except ImportError:
    TRENDS_DISPONIVEL = False

st.set_page_config(page_title="👑 LuhVee Vendas PRO - Com Busca de Produtos", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

ARQUIVO_HISTORICO = "luhvee_posts_historico.json"
CACHE_TRENDING = "trending_cache.json"

st.title("👑 LuhVee Vendas PRO - Com Busca de Produtos")
st.markdown("Gere copies inteligentes + Pesquise produtos por LINK! 🎯📊")

# ===== FUNÇÕES DE WEB SCRAPING =====

def extrair_mercado_livre(url):
    """Extrai dados do produto do Mercado Livre"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrai nome do produto
        titulo = soup.find('h1', class_='ui-pdp-title')
        nome = titulo.text.strip() if titulo else "Produto"
        
        # Extrai preço atual
        preco_atual = soup.find('span', class_='andes-money-amount__fraction')
        preco_promo = preco_atual.text.strip() if preco_atual else ""
        
        # Extrai preço original (se houver desconto)
        preco_original_tag = soup.find('s', class_='andes-money-amount')
        preco_original = ""
        if preco_original_tag:
            preco_original = preco_original_tag.text.strip()
        else:
            preco_original = preco_promo
        
        return {
            "sucesso": True,
            "nome": nome[:50],  # Limita a 50 caracteres
            "preco_original": preco_original.replace("R$", "").replace(",", ".").strip(),
            "preco_promocional": preco_promo.replace("R$", "").replace(",", ".").strip(),
            "plataforma": "Mercado Livre"
        }
    
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}

def extrair_shopee(url):
    """Extrai dados do produto do Shopee"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrai nome
        nome_tag = soup.find('span', class_='shopee-page-title')
        nome = nome_tag.text.strip() if nome_tag else "Produto"
        
        # Extrai preço
        preco_tag = soup.find('span', class_='shopee-price-display')
        preco_promo = preco_tag.text.strip() if preco_tag else ""
        
        return {
            "sucesso": True,
            "nome": nome[:50],
            "preco_original": preco_promo.replace("R$", "").replace(",", ".").strip(),
            "preco_promocional": preco_promo.replace("R$", "").replace(",", ".").strip(),
            "plataforma": "Shopee"
        }
    
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}

def buscar_produto_por_link(link):
    """Identifica plataforma e extrai dados"""
    if "mercadolivre" in link.lower() or "mercado-livre" in link.lower():
        return extrair_mercado_livre(link)
    elif "shopee" in link.lower():
        return extrair_shopee(link)
    else:
        return {"sucesso": False, "erro": "Plataforma não suportada. Use Mercado Livre ou Shopee."}

# ===== RESTO DO CÓDIGO (IGUAL AO ANTERIOR) =====

@st.cache_data(ttl=3600)
def obter_trending_google():
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

urgencia_wa = ["🚨 PROMOÇÃO RELÂMPAGO! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n⏰ *TÁ ACABANDO!*\n\n{link}\n\nLuhvee Stores ❤️"]
urgencia_ig = ["🚨 ALERTA DE OFERTA! {produto}\n\nDe R${preco_original} por R${preco_promocional}!\n\n⏰ Tá saindo rápido!\n\n{link}\n\n#ofertas #promoção"]
urgencia_fb = ["🚨 PROMOÇÃO FLASH! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]

fomo_wa = ["😱 ENQUANTO VOCÊ LÊ, ALGUÉM JÁ PEGOU!\n\n{produto} está SUMINDO!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
fomo_ig = ["👀 {produto} VIRALIZOU!\n\nTodos estão falando!\n\nR${preco_promocional}\n\n{link}\n\n#viral #trending"]
fomo_fb = ["😱 {produto} ESTÁ NA BOCA DE TODOS!\n\nTodos estão comprando!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

desconto_wa = ["💰 ACHADO DEMAIS! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]
desconto_ig = ["💰 ECONOMIZA! {produto}\n\nR${preco_promocional} (ANTES R${preco_original}!)\n\n{link}\n\n#desconto"]
desconto_fb = ["💰 DESCONTO DEMAIS!\n\n{produto}: De R${preco_original} por R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️"]

social_wa = ["⭐ TODO MUNDO AMANDO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
social_ig = ["⭐ APROVADO POR TODOS! {produto}\n\nR${preco_promocional}\n\n{link}\n\n#recomendado"]
social_fb = ["⭐ APROVADO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

exclusivo_wa = ["👑 ACESSO EXCLUSIVO! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
exclusivo_ig = ["👑 EXCLUSIVO! {produto}\n\nR${preco_promocional}\n\n{link}\n\n#exclusive"]
exclusivo_fb = ["👑 SELEÇÃO ESPECIAL! {produto}\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]

curiosidade_wa = ["🤔 ADIVINHA O QUÊ? {produto} CHEGOU!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"]
curiosidade_ig = ["🤔 ACHEI ALGO QUE VOCÊ VAI AMAR! {produto}\n\nR${preco_promocional}\n\n{link}\n\n#achado"]
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
        copy = template.format(produto=produto, preco_original=preco_original, preco_promocional=preco_promo, link=link)
        copies_geradas.append(copy)
    return copies_geradas

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Gerar Copies", "🌐 Google Trends", "📊 Histórico", "📥 Importar", "ℹ️ Info"])

with tab1:
    st.subheader("🔍 OPÇÃO 1: Buscar por LINK")
    
    col_busca1, col_busca2 = st.columns([3, 1])
    with col_busca1:
        link_produto = st.text_input("Cole o LINK do produto (Mercado Livre ou Shopee)", 
                                     placeholder="https://mercadolivre.com.br/... ou https://shopee.com.br/...")
    with col_busca2:
        if st.button("🔍 Buscar Produto", use_container_width=True):
            if link_produto:
                with st.spinner("Buscando dados do produto..."):
                    resultado = buscar_produto_por_link(link_produto)
                
                if resultado["sucesso"]:
                    st.success("✅ Produto encontrado!")
                    st.session_state.nome_produto = resultado["nome"]
                    st.session_state.preco_original = resultado["preco_original"]
                    st.session_state.preco_promocional = resultado["preco_promocional"]
                    st.info(f"📦 {resultado['nome']}\n\nDe R${resultado['preco_original']} por R${resultado['preco_promocional']}")
                else:
                    st.error(f"❌ Erro: {resultado.get('erro', 'Não consegui extrair os dados')}")
    
    st.divider()
    st.subheader("✏️ OPÇÃO 2: Preencher Manualmente")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ Dados do Produto")
        nome_produto = st.text_input("Nome do Produto", 
                                     value=st.session_state.get("nome_produto", ""),
                                     placeholder="Ex: Bolsa De Ombro")
        categoria = st.selectbox("Categoria", ["Casa", "Beleza", "Tech", "Pet", "Moda"])
    with col2:
        st.subheader("💰 Preços")
        preco_promo = st.text_input("Preço Promocional", 
                                    value=st.session_state.get("preco_promocional", ""),
                                    placeholder="89.90")
        preco_original = st.text_input("Preço Original", 
                                       value=st.session_state.get("preco_original", ""),
                                       placeholder="150.00")
    
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
                "whatsapp": copies_wa, "instagram": copies_ig, "facebook": copies_fb
            })
            
            st.success(f"✅ Post #{novo_post['id']} salvo!")
            
            tab_w, tab_i, tab_f = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
            with tab_w:
                for i, copy in enumerate(copies_wa, 1):
                    st.code(copy, language="text")
                    st.divider()
            with tab_i:
                for i, copy in enumerate(copies_ig, 1):
                    st.code(copy, language="text")
                    st.divider()
            with tab_f:
                for i, copy in enumerate(copies_fb, 1):
                    st.code(copy, language="text")
                    st.divider()

with tab2:
    st.subheader("🌐 Google Trends")
    if st.button("🔄 Buscar Tendências", use_container_width=True, type="primary"):
        with st.spinner("Buscando..."):
            trending = obter_trending_google()
        if trending:
            st.success("✅ Atualizado!")
            for categoria, produtos in trending.items():
                if produtos:
                    st.subheader(f"📊 {categoria}")
                    for idx, p in enumerate(sorted(produtos, key=lambda x: x['percentual_raw'], reverse=True), 1):
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.markdown(f"**{idx}. {p['nome']}**")
                        with col2:
                            st.metric("Interesse", p['interesse'])
                        with col3:
                            st.markdown(f"**{p['tendencia']}**")
                        st.divider()

with tab3:
    st.subheader("📊 Histórico")
    historico = carregar_historico()
    if historico:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Posts", len(historico))
        with col2:
            st.metric("Total Views", sum(p.get("views", 0) for p in historico))
        with col3:
            st.metric("Total Vendas", sum(p.get("vendas", 0) for p in historico))
        
        for post in reversed(historico):
            with st.expander(f"#{post['id']} - {post['produto']}"):
                st.metric("Preço", f"R$ {post['preco_promocional']}")
                if st.button(f"🗑️ Deletar #{post['id']}", key=f"del_{post['id']}"):
                    historico.remove(post)
                    salvar_historico(historico)
                    st.rerun()

with tab4:
    st.subheader("📥 Importar")
    arquivo = st.file_uploader("Escolha um arquivo JSON", type=["json"])
    if arquivo:
        try:
            dados = json.load(arquivo)
            if isinstance(dados, list):
                st.success(f"✅ {len(dados)} posts!")
                if st.button("➕ Adicionar", use_container_width=True, type="primary"):
                    hist = carregar_historico()
                    prox_id = max([p['id'] for p in hist], default=0) + 1
                    for p in dados:
                        p['id'] = prox_id
                        prox_id += 1
                    hist.extend(dados)
                    salvar_historico(hist)
                    st.success(f"✅ {len(dados)} importados!")
        except:
            st.error("Inválido!")

with tab5:
    st.markdown("""
    ### 👑 LuhVee Vendas PRO
    ✅ Busca por LINK (Mercado Livre + Shopee)
    ✅ Google Trends
    ✅ 6 Estratégias
    ✅ Histórico
    ✅ Multicanal
    """)

st.divider()
st.caption("👑 LuhVee Vendas PRO | Luhvee Stores ❤️")
