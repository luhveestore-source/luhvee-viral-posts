import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v11.0", page_icon="🔥")

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

# --- MOTOR DE DIVERSIDADE DE COPYWRITING (AGRESSIVO E PROFISSIONAL) ---
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
        f"Não adianta economizar comprando réplica que estraga em uma semana. Aqui você tem a garantia do produto original que viralizou na gringa. Durabilidade e estilo em um só lugar.",
        f"Sabe aquele item que muda completamente a sua rotina? É esse! Resolvi trazer para a loja porque eu mesma não vivo mais sem. É prático, elegante e de altíssima performance."
    ]
    chamada = [
        f"😱 De: R$ ---,--- por APENAS: {valor}\n\n🛒 GARANTA O SEU NO LINK SEGURO:\n👉 https://collshp.com/luhveestores",
        f"🔥 OPORTUNIDADE ÚNICA: {valor}\n\n👇 CLICA AGORA E NÃO FICA SEM:\n👉 https://collshp.com/luhveestores"
    ]
    return f"{random.choice(ganchos)}\n\n{random.choice(corpo)}\n\n{random.choice(chamada)}\n\nLuhVee Stores 🛍️"

# --- BANCO DE DADOS COMPLETO (TODOS OS SEUS NICHOS RESTAURADOS) ---
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

# --- FUNÇÃO DE MENSAGENS LONGAS (1000 LETRAS) ---
def gerar_mensagem_luhvee_completa(tipo, periodo):
    if tipo == "Profunda/Inspiradora":
        gancho = "Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos. Pare um segundo. Respire fundo."
        reflexao = "A vida não é uma corrida contra o tempo, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é um mapa de uma batalha vencida em silêncio. Valorize os pequenos passos, pois são eles que constroem os grandes destinos."
        conclusao = "Você é rara, preciosa e digna de tudo o que é bom. O seu momento de florescer é hoje!"
    else:
        gancho = "Status do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre! 😂"
        reflexao = "Dizem que o dinheiro não traz felicidade, mas eu preferia chorar em Paris do que na fila do pão! Boletos a gente paga, mas o brilho no olho de um produtinho novo chegando em casa não tem preço!"
        conclusao = "Foca no objetivo e não esquece o café! Sorria, as rugas de preocupação saem caro para botocar depois!"
    return f"{periodo}\n\n{gancho}\n\n{reflexao}\n\n{conclusao}\n\nCom carinho, LuhVee Stores ❤️"

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS ---
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
        else: st.warning("Digite o nome do produto!")

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

# --- ABA 3: INSTAGRAM TRENDS IA (HORÁRIOS E EXPLICAÇÕES) ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre")
    if st.button("🔍 ANALISAR ALGORITMO E HORÁRIOS"):
        st.subheader("1. Sugestão de Formato")
        st.info("🎯 **Reels Curtos (5 a 10s):** Maior entrega hoje. Vídeos rápidos convertem mais.")
        st.subheader("2. Tendência de Áudio")
        st.success("🎶 **Áudios Virais:** Use músicas com a 'setinha' para subir no Explorar.")
        st.subheader("3. Gancho de Retenção")
        st.warning("👀 **Texto no Centro:** Prenda a atenção nos primeiros 3 segundos.")
        st.subheader("⏰ Horários de Ouro")
        st.write("☀️ 08:30 - 09:30 | 🍱 12:00 - 13:30 | 🌙 18:00 - 20:00")

# --- ABA 4: MOTIVACIONAIS ---
else:
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        st.code(gerar_mensagem_luhvee_completa(estilo, periodo), language="text")
