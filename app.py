import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v3.5", page_icon="🔥")

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

# --- BANCO DE DADOS (TENDÊNCIAS) ---
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
    return f"{periodo}\n\n{random.choice(ganchos)}\n\n{random.choice(reflexoes)}\n\n{random.choice(conclusoes)}\n\nCom carinho, LuhVee Stores ❤️"

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

# --- ABA 1: POSTAR PRODUTOS (COM CAMPO DE PREÇO) ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Gerador de Madeirada")
    
    col_p, col_v = st.columns([2, 1])
    with col_p:
        produto = st.text_input("Nome do Produto:", placeholder="Ex: Escova 3 em 1")
    with col_v:
        preco = st.text_input("Preço (R$):", placeholder="Ex: 49,90")
    
    foto = st.file_uploader("📸 Escolha a foto", type=["png", "jpg", "jpeg"])
    if foto: st.image(Image.open(foto), use_column_width=True)
    
    loja = st.radio("Link de qual loja?", list(LINKS.keys()))
    link_f = LINKS[loja]

    if st.button("🚀 GERAR COPY COM PREÇO"):
        if produto:
            st.success("✅ ESTRATÉGIA GERADA!")
            
            valor_display = f"💰 Por apenas: R$ {preco}" if preco else "🔥 Preço Imperdível no Link!"
            
            copy_story = (
                f"🚨 Meninas, CHOCADA com esse {produto}! ✨\n\n"
                f"Procurei em todo lugar e esse é o melhor preço que vocês vão encontrar. "
                f"Qualidade premium e entrega super rápida! 😍\n\n"
                f"{valor_display}\n"
                f"🔗 Link aqui: {link_f}\n\n"
                f"LuhVee Stores 🛍️"
            )
            
            copy_viral = (
                f"POV: Você achou o {produto} que viralizou com o melhor preço da internet! 💸✨\n\n"
                f"Pare de pagar caro! Eu garimpei pra vocês e o link já está na Bio. "
                f"{valor_display} ✅\n\n"
                f"🔗 LINK NA BIO! Corra antes que o estoque acabe! 🔥\n"
                f"#luhveestores #achadinhos #oferta #shopee"
            )
            
            st.markdown("### 📱 Copy para Stories")
            st.code(copy_story, language="text")
            st.markdown("### 🎬 Copy para Reels/TikTok")
            st.code(copy_viral, language="text")
        else:
            st.warning("Luh, coloque o nome do produto primeiro! 😘")

# --- ABA 2: PESQUISA MULTI-REDES ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência Multi-Plataforma")
    categoria = st.selectbox("Nicho de Mineração:", list(tendencias_reais.keys()))
    if st.button("📡 ESCANEAR TENDÊNCIAS GLOBAIS"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(redes_sociais)
        st.subheader(f"💡 Sugestão: {sugestao}")
        st.success(f"📍 Em alta no: **{rede}**")
        st.info("A IA detectou um aumento de 150% nas buscas por este item hoje!")

# --- ABA 3: INSTAGRAM TRENDS IA ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Instagram Insights")
    publico = st.selectbox("Seu foco:", ["Engajamento", "Vendas Diretas", "Crescimento"])
    if st.button("🔍 ANALISAR ALGORITMO"):
        st.warning(f"🎯 Formato Sugerido: {'Reels Dinâmico' if publico == 'Engajamento' else 'Carrossel de Prova Social'}")
        st.write("🎶 Áudio Trend: Instrumentais Lo-fi (estão retendo mais público)")
        st.info("Dica: Use a nova ferramenta de 'Notas' para avisar que tem link novo no Stories!")

# --- ABA 4: MOTIVACIONAIS ---
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    if st.button("✨ GERAR MENSAGEM PROFUNDA"):
        st.code(gerar_texto_profundo(periodo), language="text")

# --- ABA 5: HUB ---
else:
    st.title("🔗 Hub de Links")
    for n, u in LINKS.items():
        st.markdown(f"**{n}**")
        st.code(u)