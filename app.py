import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v10.0", page_icon="🔥")

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

# --- MOTOR DE DIVERSIDADE DE COPYWRITING ---
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
        f"Não adianta economizar comprando réplica que estraga em uma semana. Aqui você tem a garantia do produto original que viralizou na gringa. Durabilidade e estilo em um só lugar."
    ]
    chamada = [f"😱 De: R$ ---,--- por APENAS: {valor}\n\n🛒 COMPRE AGORA NO LINK SEGURO:\n👉 https://collshp.com/luhveestores"]
    return f"{random.choice(ganchos)}\n\n{random.choice(corpo)}\n\n{random.choice(chamada)}\n\nLuhVee Stores 🛍️"

# --- FUNÇÃO DE MENSAGENS LONGAS ---
def gerar_mensagem_luhvee_completa(tipo, periodo):
    if tipo == "Profunda/Inspiradora":
        gancho = "Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos. Pare um segundo. Respire fundo."
        reflexao = "A vida não é uma corrida contra o tempo, mas uma jornada sagrada de cura. Cada cicatriz que você carrega é um mapa de uma batalha que você venceu em silêncio. Valorize os pequenos passos, pois são eles que constroem os grandes destinos."
        conclusao = "Você é rara, preciosa e digna de tudo o que é bom. O seu momento de florescer é hoje!"
    else:
        gancho = "Status do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre! 😂"
        reflexao = "Dizem que o dinheiro não traz felicidade, mas eu preferia chorar em Paris do que na fila do pão! A vida é curta demais para não comprar aquele achadinho que você amou. Lembre-se: boletos a gente paga, mas o brilho no olho de um produtinho novo não tem preço!"
        conclusao = "Foca no objetivo e não esquece o café! Sorria, as rugas de preocupação saem caro para botocar depois!"
    return f"{periodo}\n\n{gancho}\n\n{reflexao}\n\n{conclusao}\n\nCom carinho, LuhVee Stores ❤️"

# --- BANCO DE DADOS DE TENDÊNCIAS ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade", "Almofada Amamentação", "Kit Saída Maternidade"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Elásticos", "Massageador Muscular"],
    "🌎 Internacional": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
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
    if st.button("🚀 GERAR NOVA COPY EXCLUSIVA"):
        if produto:
            copy_gerada = gerar_copy_venda_agressiva(produto, preco)
            st.code(copy_gerada, language="text")
            st.session_state['historico_posts'].append(f"{produto} ({preco})")
        else: st.warning("Digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    categoria = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")

# --- ABA 3: INSTAGRAM TRENDS IA (ATUALIZADA COM HORÁRIOS E EXPLICAÇÕES) ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre para Instagram")
    st.markdown("### Clique no botão para analisar o algoritmo de hoje:")
    
    if st.button("🔍 ANALISAR ALGORITMO E HORÁRIOS"):
        st.write("---")
        
        # 1. Sugestão de Formato
        st.subheader("1. Sugestão de Formato (O que postar?)")
        st.info("🎯 **Reels Curtos (5 a 10 segundos):** O Instagram está entregando muito mais vídeos rápidos que vão direto ao ponto. Use cortes secos e rápidos.")
        
        # 2. Tendência de Áudio
        st.subheader("2. Tendência de Áudio")
        st.success("🎶 **Áudios Virais com 'Setinha':** Procure músicas que estão subindo. Isso coloca o seu post na aba de 'Explorar' de novas clientes em potencial.")
        
        # 3. Gancho de Retenção
        st.subheader("3. Gancho de Retenção")
        st.warning("👀 **Legenda no Centro:** Coloque o título do produto bem no meio da tela nos primeiros 3 segundos. Isso impede que a pessoa 'arraste' para cima antes de ver sua oferta.")
        
        # 4. Horários de Ouro
        st.subheader("⏰ Horários de Ouro (Maior Conversão)")
        st.markdown("""
        * **Manhã (08:30 - 09:30):** Ótimo para Stories de 'Bom dia' e mostrar o uso do produto.
        * **Almoço (12:00 - 13:30):** Pico de visualizações. Poste o Reels da 'Madeirada' aqui.
        * **Noite (18:00 - 20:00):** Momento de maior venda. As pessoas estão relaxadas e mais propensas a clicar no link da Bio.
        """)
        
        st.info("💡 **Dica da LuhVee:** Poste um Story com uma enquete 30 minutos antes do seu Reels para 'aquecer' o algoritmo!")

# --- ABA 4: MOTIVACIONAIS ---
else:
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo da Mensagem:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        msg = gerar_mensagem_luhvee_completa(estilo, periodo)
        st.code(msg, language="text")
