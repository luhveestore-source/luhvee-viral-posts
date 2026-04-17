import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v17.0", page_icon="🔥")

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

# --- MOTOR IA: COPYWRITING PROFISSIONAL ---
def gerar_copy_venda_ia(produto, preco):
    valor = f"R$ {preco}" if preco else "PREÇO EXCLUSIVO"
    gancho = f"🚨 ALERTA DE TENDÊNCIA: O {produto.upper()} CHEGOU! 🚨"
    corpo = f"A qualidade deste {produto} é surreal. Testado e aprovado! Se você está cansada de investir em produtos que não entregam nada, este item veio para mudar o seu jogo. O acabamento premium e o design impecável fazem deste produto o desejo número 1 das redes sociais."
    urgencia = f"⏰ O TEMPO ESTÁ CORRENDO: Esta oferta exclusiva é válida apenas enquanto durarem os nossos estoques. Clique no link agora e garanta o seu!"
    return f"{gancho}\n\n{corpo}\n\n😱 POR APENAS: {valor}\n\n{urgencia}\n\n🛒 LINK SEGURO:\n👉 https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️"

# --- BANCO DE DADOS COMPLETO ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Faixas Elásticas", "Massageador Muscular Turbo"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão IA")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    if st.button("🚀 GERAR COPY PROFISSIONAL"):
        if produto:
            res = gerar_copy_venda_ia(produto, preco)
            st.code(res, language="text")
            st.session_state['historico_posts'].append(f"POST: {produto} - R$ {preco}")
        else: st.warning("Digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES + ROTEIRO IA ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Caçador de Tendências + Roteiro IA")
    cat = st.selectbox("Nicho para Minerar:", list(tendencias_reais.keys()))
    
    if st.button("📡 INICIAR MINERAÇÃO E CRIAR ROTEIRO"):
        sugestao = random.choice(tendencias_reais[cat])
        rede_origem = random.choice(["TikTok", "Pinterest", "Instagram"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede_origem})")
        
        st.write("---")
        st.header(f"💎 Produto Encontrado: {sugestao}")
        st.success(f"📍 Este item está explodindo no **{rede_origem}**")
        
        st.markdown("### 🗺️ Roteiro de Postagem Estratégica:")
        
        col_inst, col_tik, col_whats = st.columns(3)
        
        with col_inst:
            st.subheader("📸 Instagram")
            st.write("**Stories:** Fazer 3 fotos (1 detalhe, 1 uso, 1 prova social).")
            st.write("**Reels:** Vídeo de 7s com corte seco no áudio viral.")
            st.code("#achadinhos #estilo #shopee #viralreels", language="text")
            
        with col_tik:
            st.subheader("📱 TikTok")
            st.write("**Vídeo:** Iniciar com gancho 'Você não vai acreditar!'.")
            st.write("**Legenda:** Usar copy agressiva + CTA para a Bio.")
            st.code("#tiktokmadeit #achados #luhveestores #foryou", language="text")
            
        with col_whats:
            st.subheader("💬 WhatsApp")
            st.write("**Grupos:** Mandar a copy completa + o link direto.")
            st.write("**Status:** Foto chamativa com o preço em destaque.")
            st.write("Dica: Use emojis de urgência (🚨, 🔥).")

    if st.session_state['historico_pesquisa']:
        st.write("---")
        st.subheader("📋 Histórico de Mineração")
        for item in reversed(st.session_state['historico_pesquisa']): st.text(f"✅ {item}")

# --- ABA 3: INSTAGRAM TRENDS IA ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre")
    if st.button("🔍 ANALISAR ALGORITMO"):
        st.info("🎯 **Reels Curtos (5-10s):** Foco em retenção.")
        st.write("☀️ 08:30-09:30 | 🍱 12:00-13:30 | 🌙 18:00-20:00")

# --- ABA 4: MOTIVACIONAIS ---
else:
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        if estilo == "Profunda/Inspiradora":
            msg = f"{periodo}\n\nA vida é uma jornada sagrada... [Texto IA de 1000 Letras]\n\nLuhVee Stores ❤️"
        else:
            msg = f"{periodo}\n\nStatus: Em busca da riqueza! 😂 [Texto IA de 1000 Letras]\n\nLuhVee Stores ❤️"
        st.code(msg, language="text")
