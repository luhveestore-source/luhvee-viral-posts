import streamlit as st
import random
import json
import os
from datetime import datetime
from itertools import cycle

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="👑 LuhVee Vendas PRO", layout="wide")

# 🔗 SEUS LINKS
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# Arquivo de histórico
ARQUIVO_HISTORICO = "luhvee_posts_historico.json"

st.title("👑 LuhVee Vendas PRO - Multicanal + Histórico")
st.markdown("Gerador de copies + Radar de Trending + Histórico Inteligente 🎯🚀")

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

def baixar_historico():
    """Prepara arquivo para download"""
    historico = carregar_historico()
    return json.dumps(historico, ensure_ascii=False, indent=2)

# ===== PRODUTOS TRENDING (Dados Simulados + Web) =====

produtos_trending = {
    "Shopee": [
        {"nome": "Bolsa De Ombro Premium", "preco": "89.90", "categoria": "Moda", "tendencia": "⬆️ +45%"},
        {"nome": "Luminária RGB Smart", "preco": "129.90", "categoria": "Tech", "tendencia": "⬆️ +62%"},
        {"nome": "Almofada De Pescoço", "preco": "39.90", "categoria": "Casa", "tendencia": "⬆️ +38%"},
        {"nome": "Sérum Facial Retinol", "preco": "49.90", "categoria": "Beleza", "tendencia": "⬆️ +71%"},
        {"nome": "Coleira GPS Pet", "preco": "159.90", "categoria": "Pet", "tendencia": "⬆️ +55%"},
    ],
    "Mercado Livre": [
        {"nome": "Carregador Rápido 65W", "preco": "79.90", "categoria": "Tech", "tendencia": "⬆️ +48%"},
        {"nome": "Protetor Solar Facial", "preco": "59.90", "categoria": "Beleza", "tendencia": "⬆️ +64%"},
        {"nome": "Tapete Antiderrapante", "preco": "69.90", "categoria": "Casa", "tendencia": "⬆️ +42%"},
        {"nome": "Brinquedo Interativo Pet", "preco": "44.90", "categoria": "Pet", "tendencia": "⬆️ +51%"},
        {"nome": "Bolsa Executiva", "preco": "199.90", "categoria": "Moda", "tendencia": "⬆️ +39%"},
    ],
    "Trending Geral": [
        {"nome": "iPhone 15 Case", "preco": "89.90", "categoria": "Tech", "tendencia": "⬆️ +78%"},
        {"nome": "Delineador Líquido", "preco": "29.90", "categoria": "Beleza", "tendencia": "⬆️ +85%"},
        {"nome": "Difusor Aromas", "preco": "99.90", "categoria": "Casa", "tendencia": "⬆️ +72%"},
        {"nome": "Cama Aquecida Pet", "preco": "179.90", "categoria": "Pet", "tendencia": "⬆️ +81%"},
        {"nome": "Bota Inverno 2024", "preco": "249.90", "categoria": "Moda", "tendencia": "⬆️ +76%"},
    ]
}

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

# ===== ESTRATÉGIAS DE VENDAS =====

# ESTRATÉGIA 1: URGÊNCIA
urgencia_whatsapp = [
    "🚨 PROMOÇÃO RELÂMPAGO! {produto} com DESCONTO ABSURDO!\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n⏰ *TÁ ACABANDO!*\n\n{link}\n\nLuhvee Stores ❤️",
    "⚡ ATENÇÃO! {produto} saiu na nossa loja!\n\nR${preco_promocional} (Era R${preco_original})\n\n⏳ Estoque LIMITADO!\n\n{link}\n\nLuhvee Stores ❤️",
]

urgencia_instagram = [
    "🚨 ALERTA DE OFERTA URGENTE! 🚨\n\n{produto} QUEBRANDO PREÇO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 😱\n\n⏰ Tá saindo rápido!\n\n🛒 {link}\n\n#ofertas #promoção",
    "🔥 GRITANDO AQUI! {produto} em PROMOÇÃO DOIDA!\n\n💰 R${preco_promocional}!\n\n⚡ Depois dessa preço volta ao normal!\n\n👉 {link}\n\n#achadinhos #desconto",
]

urgencia_facebook = [
    "🚨 PROMOÇÃO FLASH AGORA! 🚨\n\n{produto} COM DESCONTO BRUTAL!\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n⏰ ESTOQUE LIMITADO!\n\n✅ Compra Segura | ✅ Entrega Rápida\n\n{link}\n\nLuhvee Stores ❤️",
]

# ESTRATÉGIA 2: FOMO
fomo_whatsapp = [
    "😱 ENQUANTO VOCÊ LÊ, ALGUÉM JÁ PEGOU!\n\n{produto} está SUMINDO!\n\nR${preco_promocional} (Era R${preco_original})\n\n{link}\n\nLuhvee Stores ❤️",
    "👀 VIU? MAIS UM COMPROU {produto}!\n\nTodos estão descobrindo essa oferta!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
]

fomo_instagram = [
    "👀 VIRA ESSA VOLTA!\n\n{produto} VIRALIZOU! 😱\n\nTodos estão falando!\n\n💰 R${preco_promocional}\n\n🔗 {link}\n\n#viral #trending #luhveestores",
    "😭 NÃO SEJA A ÚLTIMA!\n\n{produto} está na boca de todos!\n\n🛍️ R${preco_promocional}\n\n👉 {link}\n\n#luhvee #imperdível",
]

fomo_facebook = [
    "😱 OLHA SÓ! {produto} ESTÁ NA BOCA DE TODOS!\n\nTodos estão comprando!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
]

# ESTRATÉGIA 3: DESCONTO
desconto_whatsapp = [
    "💰 ACHADO DEMAIS! {produto} em PROMOÇÃO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 🎉\n\n{link}\n\nLuhvee Stores ❤️",
    "🤑 GRANA GUARDADA! {produto} está barato!\n\nDe R${preco_original} por R${preco_promocional}!\n\n{link}\n\nLuhvee Stores ❤️",
]

desconto_instagram = [
    "💰 ECONOMIZA PRA CARAMBA! {produto}\n\nR${preco_promocional} (ANTES R${preco_original}!) 😱\n\n✨ Qualidade + Preço!\n\n👉 {link}\n\n#desconto #promoção #luhvee",
]

desconto_facebook = [
    "💰 ECONOMIZA DEMAIS! {produto}\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n✅ Qualidade Garantida | ✅ Preço Imbatível\n\n{link}\n\nLuhvee Stores ❤️",
]

# ESTRATÉGIA 4: SOCIAL PROOF
social_whatsapp = [
    "⭐ TODO MUNDO AMANDO! {produto} é QUERIDINHO!\n\nJá tem CENTENAS aprovando!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
]

social_instagram = [
    "⭐ APROVADO POR TODOS! {produto}\n\n💯 Centenas de clientes satisfeitos!\n\n💰 R${preco_promocional}\n\n🛒 {link}\n\n#recomendação #luhveestores",
]

social_facebook = [
    "⭐ APROVADO E RECOMENDADO! {produto}\n\n✅ Centenas SATISFEITOS! ✅ Reviews INCRÍVEIS!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
]

# ESTRATÉGIA 5: EXCLUSIVIDADE
exclusivo_whatsapp = [
    "👑 ACESSO EXCLUSIVO! {produto} é RARIDADE!\n\nR${preco_promocional} só pra você!\n\n{link}\n\nLuhvee Stores ❤️",
]

exclusivo_instagram = [
    "👑 EXCLUSIVO! {produto}\n\n✨ Selecionado pra quem tem bom gosto!\n\n💳 R${preco_promocional}\n\n{link}\n\n#exclusive #premium #luhveestores",
]

exclusivo_facebook = [
    "👑 SELEÇÃO ESPECIAL! {produto}\n\n✨ Pra você que tem BOM GOSTO!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
]

# ESTRATÉGIA 6: CURIOSIDADE
curiosidade_whatsapp = [
    "🤔 ADIVINHA O QUÊ? {produto} CHEGOU!\n\nAquele que você queria! 🎉\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
]

curiosidade_instagram = [
    "🤔 ACHEI ALGO QUE VOCÊ VAI AMAR!\n\n{produto} é perfeito!\n\n💰 R${preco_promocional}\n\n👉 {link}\n\n#achado #descoberta #luhveestores",
]

curiosidade_facebook = [
    "🤔 OLHA O QUE EU ENCONTREI! {produto}\n\n✨ Você ia procurar por isso!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️",
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

# Abas principais
tab1, tab2, tab3, tab4 = st.tabs(["📝 Gerar Copies", "🎯 Radar Trending", "📊 Histórico", "📥 Importar Posts"])

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
            # Gera copies
            copies_whatsapp = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "whatsapp", link_selecionado)
            copies_instagram = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "instagram", link_selecionado)
            copies_facebook = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "facebook", link_selecionado)
            
            # Salva no histórico
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
            
            # Abas por canal
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
            
            # Stats
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

# ========== TAB 2: RADAR TRENDING ==========
with tab2:
    st.subheader("🎯 Radar de Produtos Virais")
    st.info("Produtos mais buscados e vendidos no mercado! Use esses nomes para gerar seus copies.")
    
    radar_col = st.columns(3)
    
    plataformas_radar = ["Shopee", "Mercado Livre", "Trending Geral"]
    
    for idx, plat in enumerate(plataformas_radar):
        with radar_col[idx]:
            st.markdown(f"### 🔥 {plat}")
            
            for produto in produtos_trending[plat]:
                col_nome, col_tend = st.columns([3, 1])
                
                with col_nome:
                    st.markdown(f"**{produto['nome']}**")
                    st.caption(f"R$ {produto['preco']} • {produto['categoria']}")
                
                with col_tend:
                    st.markdown(f"{produto['tendencia']}")
                
                # Botão para usar
                if st.button(f"Usar → {produto['nome']}", key=f"usar_{plat}_{produto['nome']}"):
                    st.session_state.nome_produto = produto['nome']
                    st.session_state.categoria = produto['categoria']
                    st.session_state.preco_base = produto['preco']
                    st.success(f"✅ Produto {produto['nome']} carregado! Vá para 'Gerar Copies'")
                
                st.divider()

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
        
        # Filtro
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
        
        # Filtra histórico
        historico_filtrado = historico
        if filtro_estrategia != "Todas":
            historico_filtrado = [p for p in historico_filtrado if p["estrategia"] == filtro_estrategia]
        
        # Mostra posts
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
                
                # Opções
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
        
        # Download
        st.subheader("📥 Exportar Histórico")
        col_down1, col_down2 = st.columns(2)
        
        with col_down1:
            json_str = baixar_historico()
            st.download_button(
                label="📥 Baixar Histórico (JSON)",
                data=json_str,
                file_name=f"luhvee_posts_{datetime.now().strftime('%d_%m_%Y')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col_down2:
            if st.button("🗑️ Limpar Histórico Completo", use_container_width=True):
                if st.checkbox("Tenho certeza que quero deletar TUDO"):
                    salvar_historico([])
                    st.success("Histórico limpo!")
                    st.rerun()
    
    else:
        st.warning("Ainda não há posts no histórico. Gere alguns para começar!")

# ========== TAB 4: IMPORTAR ==========
with tab4:
    st.subheader("📥 Importar Posts Salvos")
    
    arquivo_upload = st.file_uploader("Escolha um arquivo JSON", type=["json"])
    
    if arquivo_upload:
        try:
            dados_importados = json.load(arquivo_upload)
            
            if isinstance(dados_importados, list):
                st.success(f"✅ Arquivo válido! {len(dados_importados)} posts encontrados.")
                
  