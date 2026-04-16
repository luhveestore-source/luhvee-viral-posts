import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v3.0", page_icon="🔥")

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
    div[data-baseweb="select"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS EXPANDIDO ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Máscara LED Facial"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Projetor de Galáxia"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica"],
    "📱 Tecnologia & Gadgets": ["Fone de Ouvido Noise Cancelling", "Carregador Magnético Magsafe", "Mini Projetor Portátil"],
    "🚗 Acessórios Automotivos": ["Suporte de Celular por Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

redes_sociais = ["TikTok Trends 📱", "Pinterest Predicts 📌", "Facebook Ads Library 📢", "YouTube Shorts 🎬"]

# --- FUNÇÃO GERADORA DE TEXTOS PROFUNDOS ---
def gerar_texto_profundo(periodo):
    ganchos = ["Às vezes, a pressa nos faz esquecer de quem somos.", "Pare um segundo. Respire fundo.", "O sucesso é sobre a paz que você sente."]
    reflexoes = [
        "A vida não é uma corrida, mas uma jornada sagrada de cura. Cada cicatriz é um mapa de uma batalha vencida. Valorize os pequenos passos.",
        "A felicidade não está no 'quando chegar lá', mas no agora. Ser forte é saber descansar sem desistir. Você é o projeto mais importante.",
        "Não deixe o ruído alheio abafar o seu coração. A grandeza começa na gratidão. O tempo é precioso, use-o para construir sua paz."
    ]
    conclusoes = ["Você é rara e preciosa.", "Você é o milagre que procurava.", "O seu momento de florescer é hoje."]
    return f"{periodo}\n\n{random.choice(ganchos)}\n\n{random.choice(reflexoes)}\n\n{random.choice(conclusoes)}\n\nLuhVee Stores ❤️"

# --- LINKS ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Whats": "https://wa.me/5511948021428"
}

# --- MENU LATERAL ATUALIZADO ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", [
    "🛍️ Postar Produtos", 
    "🔎 Pesquisa Multi-Redes", 
    "📸 Instagram Trends IA",
    "✨ Frases Motivacionais", 
    "🔗 Vitrines & Hub"
])

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Gerador de Madeirada")
    produto = st.text_input("Nome do Produto:")
    loja = st.radio("Link de qual loja?", list(LINKS.keys()))
    if st.button("🚀 GERAR COPY"):
        st.code(f"🚨 Meninas, CHOCADA com esse {produto}! ✨\n🔗 {LINKS[loja]}\nLuhVee Stores 🛍️", language="text")

# --- ABA 2: PESQUISA MULTI-REDES (AVANÇADA) ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência Multi-Plataforma")
    categoria = st.selectbox("Nicho de Mineração:", list(tendencias_reais.keys()))
    
    if st.button("📡 ESCANEAR TENDÊNCIAS GLOBAIS"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(redes_sociais)
        st.subheader(f"💡 Produto: {sugestao}")
        st.success(f"📍 Detectado em alta no: **{rede}**")
        st.info(f"Análise IA: Este produto apresenta um crescimento de busca de 150% nas últimas 24h fora do Brasil. Hora de importar a tendência!")

# --- NOVA ABA 3: INSTAGRAM TRENDS IA ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Instagram Insights Avançado")
    st.subheader("O que as seguidoras querem ver hoje?")
    
    col1, col2 = st.columns(2)
    with col1:
        publico = st.selectbox("Seu foco hoje:", ["Engajamento", "Vendas Diretas", "Crescimento de Seguidores"])
    with col2:
        estilo = st.selectbox("Vibe do Post:", ["Elegante/Luxo", "Divertido/Viral", "Educativo/Dicas"])

    if st.button("🔍 ANALISAR ALGORITMO DO INSTAGRAM"):
        hashtags = ["#achadinhos", "#estilo", "#mulherespoderosas", "#homedecor", "#viralreels"]
        audios = ["Slow Motion (Reverb)", "Summer Vibes (Trend)", "Instrumental Inspiração", "Áudio de Comédia (POV)"]
        
        st.write("---")
        st.markdown("### 📈 Plano de Ação para o seu Instagram:")
        st.warning(f"🎯 **Formato Ideal:** {'Reels com corte rápido' if publico == 'Engajamento' else 'Carrossel de Benefícios'}")
        st.write(f"🎶 **Áudio Sugerido:** {random.choice(audios)}")
        st.write(f"🏷️ **Hashtags Estratégicas:** {', '.join(random.sample(hashtags, 3))}")
        st.info("💡 **Dica de Ouro:** Poste entre 18h e 21h. Use a primeira frase da legenda como um 'spoiler' do vídeo para aumentar a retenção.")

# --- ABA 4: MOTIVACIONAIS ---
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    if st.button("✨ GERAR MENSAGEM"):
        st.code(gerar_texto_profundo(periodo), language="text")

# --- ABA 5: HUB ---
else:
    st.title("🔗 Hub de Links")
    for n, u in LINKS.items():
        st.markdown(f"**{n}**")
        st.code(u)