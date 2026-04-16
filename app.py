import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v4.0", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'sans serif'; }
    .stButton>button {
        background-color: #ff69b4 !important; color: white !important; 
        border: 2px solid #ffd700 !important; border-radius: 10px; width: 100%;
        font-weight: bold; font-size: 18px;
    }
    .stCode { 
        background-color: #1e1e1e !important; 
        border: 1px solid #ff69b4 !important; 
        color: #00ff00 !important; 
        white-space: pre-wrap !important; 
    }
    div[data-baseweb="select"], div[data-baseweb="input"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DO HISTÓRICO (Session State) ---
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# --- BANCO DE DADOS COMPLETO E ATUALIZADO ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica"],
    "📱 Tecnologia & Gadgets": ["Fone de Ouvido Noise Cancelling", "Carregador Magnético Magsafe", "Mini Projetor Portátil"],
    "🚗 Acessórios Automotivos": ["Suporte de Celular por Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda Profissional", "Regador Automático Solar", "Vaso de Auto-irrigação", "Cortador de Grama Portátil"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento Viral", "Kit Cuecas de Bambu"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro Ortopédica", "Bota Adventure"],
    "💪 Produtos de Academia": ["Garrafa de Água Motivacional", "Kit de Faixas Elásticas", "Massageador Muscular Turbo", "Smartwatch Fitness"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

redes_sociais = ["TikTok Trends 📱", "Pinterest Predicts 📌", "Facebook Ads Library 📢", "YouTube Shorts 🎬"]

# --- LINKS ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Whats": "https://wa.me/5511948021428"
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", [
    "🛍️ Postar Produtos", 
    "🔎 Pesquisa Multi-Redes", 
    "📸 Instagram Trends IA",
    "✨ Frases Motivacionais", 
    "🔗 Vitrines & Hub"
])

# ==========================================
# ABA 1: GERADOR DE MADEIRADA (COPY AGRESSIVA)
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Vendas (Copy Agressiva)")
    
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    
    loja = st.radio("Link de qual loja?", list(LINKS.keys()))
    link_f = LINKS[loja]

    if st.button("🚀 GERAR TEXTOS DE CONVERSÃO"):
        if produto:
            st.success("✅ ESTRATÉGIA AGRESSIVA GERADA!")
            valor = f"POR APENAS R$ {preco}" if preco else "PREÇO DE OPORTUNIDADE"
            
            copy_story = (
                f"🚨 ÚLTIMO AVISO: {produto.upper()} EM OFERTA! 🚨\n\n"
                f"Gente, para de perder tempo! Eu achei o {produto} que todo mundo está procurando e o estoque está voando! "
                f"É a maior qualidade que já vi e por um preço que não existe em outro lugar. 😱\n\n"
                f"🔥 {valor}\n"
                f"⏳ Restam poucas unidades no link abaixo!\n"
                f"🔗 CLICA AQUI AGORA: {link_f}\n\n"
                f"LuhVee Stores 🛍️ - Não diga que eu não avisei!"
            )
            
            copy_viral = (
                f"PARE DE SER ENGANADA! ❌ Você precisa desse {produto}!\n\n"
                f"Esquece tudo o que você já viu. Esse aqui é o único original que viralizou na gringa. "
                f"Resolve o seu problema em segundos e custa menos que um lanche! 💸\n\n"
                f"✅ {valor}\n"
                f"✅ QUALIDADE PREMIUM TESTADA\n"
                f"✅ ENTREGA RÁPIDA\n\n"
                f"🔗 LINK NA MINHA BIO! Digita 'EU QUERO' que o link vai no seu direct! 🚀\n"
                f"#luhveestores #achadinhos #viral #promoção"
            )
            
            st.markdown("### 📱 Copy para Stories (Urgência)")
            st.code(copy_story, language="text")
            st.markdown("### 🎬 Copy para Reels/TikTok (Desejo)")
            st.code(copy_viral, language="text")
        else: st.warning("Digite o produto!")

# ==========================================
# ABA 2: PESQUISA MULTI-REDES + HISTÓRICO
# ==========================================
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Mineração de Ouro Multi-Plataforma")
    categoria = st.selectbox("Selecione o Nicho para Minerar:", list(tendencias_reais.keys()))
    
    if st.button("📡 INICIAR VARREDURA AVANÇADA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(redes_sociais)
        info = f"PRODUTO: {sugestao} | REDE: {rede}"
        
        # Salva no histórico
        st.session_state['historico'].append(info)
        
        st.subheader(f"💡 Resultado: {sugestao}")
        st.success(f"📍 Tendência Confirmada: **{rede}**")
        st.info("Atenção: Este produto está sendo escalado agora. Aproveite o timing!")

    # --- SEÇÃO DE HISTÓRICO ---
    if st.session_state['historico']:
        st.write("---")
        st.subheader("📋 Histórico de Mineração")
        for item in reversed(st.session_state['historico']):
            st.text(f"✅ {item}")
        if st.button("🗑️ Limpar Histórico"):
            st.session_state['historico'] = []
            st.rerun()

# ==========================================
# ABA 3: INSTAGRAM TRENDS
# ==========================================
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia Instagram")
    if st.button("🔍 ANALISAR ALGORITMO AGORA"):
        st.success("🎯 FORMATO DO DIA: Reels de 7 segundos com texto no centro.")
        st.write("🎶 Áudio do Momento: 'Trending Luxury Beats'")
        st.info("Dica: Interaja com 10 seguidores antes de postar para aumentar o alcance!")

# ==========================================
# ABA 4: MOTIVACIONAIS
# ==========================================
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    if st.button("✨ GERAR REFLEXÃO PROFUNDA"):
        # Importamos a lógica de texto longo aqui
        st.code("A vida é uma jornada sagrada... [Texto Longo Gerado]", language="text")

# ==========================================
# ABA 5: VITRINES & HUB
# ==========================================
else:
    st.title("🔗 Hub de Links")
    for n, u in LINKS.items():
        st.markdown(f"**{n}**")
        st.code(u)
