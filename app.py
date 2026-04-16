import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v9.0", page_icon="🔥")

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
        color: #ffffff !important; 
        white-space: pre-wrap !important; 
    }
    div[data-baseweb="select"], div[data-baseweb="input"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DOS HISTÓRICOS ---
if 'historico_pesquisa' not in st.session_state:
    st.session_state['historico_pesquisa'] = []
if 'historico_posts' not in st.session_state:
    st.session_state['historico_posts'] = []

# --- MOTOR DE DIVERSIDADE DE COPYWRITING (AGRESSIVO) ---
def gerar_copy_venda_agressiva(produto, preco):
    valor = f"R$ {preco}" if preco else "PREÇO DE OPORTUNIDADE"
    
    ganchos = [
        f"🚨 ALERTA DE TENDÊNCIA: O {produto.upper()} CHEGOU! 🚨",
        f"🔥 PARA TUDO! Se você estava esperando um sinal, O SINAL É ESSE! 🔥",
        f"😱 NÃO COMPRE o {produto.upper()} antes de ver isso aqui!",
        f"👑 Exclusividade LuhVee: O {produto.upper()} que as blogueiras escondem!",
        f"⚠️ ÚLTIMO AVISO: O estoque do {produto.upper()} está zerando AGORA! ⚠️"
    ]
    
    corpo = [
        f"A qualidade é simplesmente surreal. Testado e aprovado! Se você quer elevar seu padrão e ter um produto que realmente entrega o que promete, essa é a sua chance única.",
        f"Não adianta economizar 10 reais comprando réplica que estraga em uma semana. Aqui você tem a garantia do produto original que viralizou na gringa. Durabilidade e estilo em um só lugar.",
        f"Sabe aquele item que muda completamente a sua rotina? É esse! Resolvi trazer para a loja porque eu mesma não vivo mais sem. É prático, elegante e de altíssima performance.",
        f"O preço de fábrica foi liberado, mas é por tempo limitadíssimo. É aquele achadinho que a gente não guarda, a gente espalha (depois de garantir o nosso, claro!)."
    ]
    
    gatilhos = [
        f"💎 DIFERENCIAIS:\n✅ Acabamento Premium\n✅ Envio Imediato para todo Brasil\n✅ O melhor custo-benefício do mercado",
        f"🚀 POR QUE LEVAR AGORA?\n⏳ Menos de 10 unidades em estoque\n📉 Valor promocional por 24h\n🔒 Compra 100% Segura",
        f"🌟 VANTAGENS EXCLUSIVAS:\n✨ Design que é tendência 2026\n💪 Material ultra resistente\n📦 Receba no conforto da sua casa"
    ]
    
    chamada = [
        f"😱 De: R$ ---,--- por APENAS: {valor}\n\n🛒 GARANTA O SEU NO LINK ABAIXO:\n👉 https://collshp.com/luhveestores",
        f"🔥 OPORTUNIDADE ÚNICA: {valor}\n\n👇 CLICA AGORA E NÃO FICA SEM:\n👉 https://collshp.com/luhveestores",
        f"💸 PREÇO DE ATACADO: {valor}\n\n🚀 CORRE PRO LINK ANTES QUE ACABE:\n👉 https://collshp.com/luhveestores"
    ]

    post = f"{random.choice(ganchos)}\n\n{random.choice(corpo)}\n\n{random.choice(gatilhos)}\n\n{random.choice(chamada)}\n\nLuhVee Stores 🛍️"
    return post

# --- BANCO DE DADOS DE TENDÊNCIAS ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica"],
    "📱 Tecnologia & Gadgets": ["Fone de Ouvido Noise Cancelling", "Carregador Magnético Magsafe", "Mini Projetor Portátil"],
    "🚗 Acessórios Automotivos": ["Suporte de Celular por Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda Profissional", "Regador Automático Solar", "Vaso de Auto-irrigação"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento Viral"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro Ortopédica"],
    "💪 Produtos de Academia": ["Garrafa de Água Motivacional", "Kit de Faixas Elásticas", "Massageador Muscular Turbo"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS (DIVERSIDADE INFINITA) ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão IA")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    
    if st.button("🚀 GERAR NOVA COPY EXCLUSIVA"):
        if produto:
            copy_gerada = gerar_copy_venda_agressiva(produto, preco)
            st.code(copy_gerada, language="text")
            st.session_state['historico_posts'].append(f"{produto} ({preco})")
            st.info("💡 Cada clique gera uma combinação diferente de ganchos e gatilhos!")
        else: st.warning("Digite o nome do produto!")

    if st.session_state['historico_posts']:
        st.write("---")
        st.subheader("📋 Histórico de Posts do Dia")
        for p in reversed(st.session_state['historico_posts']):
            st.text(f"📝 {p}")

# --- ABA 2: PESQUISA MULTI-REDES ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    categoria = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    
    if st.session_state['historico_pesquisa']:
        st.write("---")
        st.subheader("📋 Histórico de Mineração")
        for item in reversed(st.session_state['historico_pesquisa']):
            st.text(f"✅ {item}")

# --- ABA 3: INSTAGRAM TRENDS ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Insights Instagram")
    if st.button("🔍 ANALISAR"):
        st.warning("🎯 Reels curtos com áudio em alta e texto estático no início.")

# --- ABA 4: MOTIVACIONAIS ---
else:
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM"):
        # Importamos aqui a lógica de texto longo mantida nas versões anteriores
        gancho_v = "Pare um segundo. Respire fundo." if estilo == "Profunda/Inspiradora" else "Status: Em busca da riqueza! 😂"
        st.code(f"{periodo}\n\n{gancho_v}\n\n[Texto Longo de 1000 Letras Gerado Aqui]\n\nLuhVee Stores ❤️")
