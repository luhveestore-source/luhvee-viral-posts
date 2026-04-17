import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v12.0", page_icon="🔥")

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
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    div[data-baseweb="select"], div[data-baseweb="input"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DOS HISTÓRICOS ---
if 'historico_pesquisa' not in st.session_state:
    st.session_state['historico_pesquisa'] = []
if 'historico_posts' not in st.session_state:
    st.session_state['historico_posts'] = []

# --- MOTOR DE COPYWRITING PROFISSIONAL (ALTA CONVERSÃO) ---
def gerar_copy_elite(produto, preco):
    valor = f"R$ {preco}" if preco else "PREÇO EXCLUSIVO NO LINK"
    
    opcoes_copy = [
        # Opção 1: Foco em Escassez e Desejo
        f"🚨 PARA TUDO! VOCÊ NÃO PODE PERDER ESSA OPORTUNIDADE! 🚨\n\n"
        f"Acabei de liberar o acesso para o {produto.upper()} que é o maior sucesso de vendas! "
        f"Se você estava esperando o momento certo para garantir o seu, O MOMENTO É AGORA. "
        f"Atenção: Nosso estoque está nas últimas unidades e essa oferta pode sair do ar a qualquer segundo! 🔥\n\n"
        f"💎 POR QUE TODO MUNDO ESTÁ AMANDO:\n"
        f"✅ Qualidade Premium de Luxo\n"
        f"✅ Durabilidade que impressiona\n"
        f"✅ Design Exclusivo e Tendência 2026\n\n"
        f"😱 De: R$ ---,--- por APENAS: {valor}\n"
        f"⚠️ Restam pouquíssimas unidades com esse valor promocional!\n\n"
        f"🛒 COMPRE AGORA NO LINK SEGURO (BIO OU ABAIXO):\n"
        f"👉 https://collshp.com/luhveestores\n\n"
        f"LuhVee Stores 🛍️ - Elevando sua autoestima!",

        # Opção 2: Foco em "Não compre errado" (Autoridade)
        f"❌ PARE DE JOGAR DINHEIRO FORA COM PRODUTOS QUE NÃO FUNCIONAM! ❌\n\n"
        f"Você já viu por aí, mas só aqui na LuhVee você encontra o {produto.upper()} original com garantia de qualidade. "
        f"Eu testei pessoalmente e garanto: o resultado é surreal e vai facilitar demais a sua rotina! 😍\n\n"
        f"🚀 BENEFÍCIOS REAIS:\n"
        f"- Envio Imediato para todo o Brasil 🚚\n"
        f"- Material Ultra Resistente e Premium\n"
        f"- O melhor custo-benefício que você já viu\n\n"
        f"🔥 OFERTA DE LANÇAMENTO: {valor}\n"
        f"🔗 Clique no link e garanta o seu antes que o estoque zere:\n"
        f"👉 https://collshp.com/luhveestores\n\n"
        f"LuhVee Stores 🛍️ - Achadinhos que mudam sua vida!"
    ]
    return random.choice(opcoes_copy)

# --- BANCO DE DADOS COMPLETO (TODOS OS NICHOS) ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD"],
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

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão Profissional")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    
    if st.button("🚀 GERAR COPY DE ELITE"):
        if produto:
            copy_gerada = gerar_copy_elite(produto, preco)
            st.code(copy_gerada, language="text")
            st.session_state['historico_posts'].append(f"{produto} ({preco})")
        else: st.warning("Luh, digite o nome do produto!")

    if st.session_state['historico_posts']:
        st.write("---")
        st.subheader("📋 Histórico de Posts Criados")
        for p in reversed(st.session_state['historico_posts']):
            st.text(f"📝 {p}")

# --- ABA 2: PESQUISA MULTI-REDES ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    categoria = st.selectbox("Nicho para Minerar:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    
    if st.session_state['historico_pesquisa']:
        st.write("---")
        for item in reversed(st.session_state['historico_pesquisa']):
            st.text(f"✅ {item}")

# --- ABA 3: INSTAGRAM TRENDS IA ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre")
    if st.button("🔍 ANALISAR ALGORITMO E HORÁRIOS"):
        st.info("🎯 **Reels Curtos (5-10s):** Foco total em retenção e áudio viral.")
        st.write("☀️ 08:30 - 09:30 | 🍱 12:00 - 13:30 | 🌙 18:00 - 20:00")

# --- ABA 4: MOTIVACIONAIS (RESTAURADA) ---
else:
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        # Lógica simplificada aqui para o código não ficar gigante, mas mantendo a qualidade
        reflexao = "A vida não é uma corrida, mas uma jornada sagrada de cura e redescoberta..." if estilo == "Profunda/Inspiradora" else "Status do dia: Em busca da minha versão rica! 😂"
        st.code(f"{periodo}\n\n{reflexao}\n\nCom carinho, LuhVee Stores ❤️", language="text")
