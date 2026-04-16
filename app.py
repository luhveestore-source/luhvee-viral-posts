import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL (PRETO, ROSA E DOURADO) ---
st.set_page_config(page_title="LuhVee Viral Machine", page_icon="🔥")

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
    div[data-baseweb="select"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS DE PRODUTOS ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Máscara LED Facial"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "📱 Tecnologia & Gadgets": ["Fone de Ouvido Noise Cancelling", "Carregador Magnético Magsafe", "Mini Projetor Portátil"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- LINKS FIXOS ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Whats": "https://wa.me/5511948021428"
}

# --- MENU LATERAL (REMOVIDO O HUB) ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", [
    "🚀 Venda Agressiva (Postar)", 
    "🔎 Pesquisa Multi-Redes", 
    "📸 Instagram Estratégico",
    "✨ Mensagens que Tocam o Coração"
])

# ==========================================
# ABA 1: VENDA AGRESSIVA (COPYWRITING LONGO)
# ==========================================
if aba == "🚀 Venda Agressiva (Postar)":
    st.title("🔥 Gerador de Venda Agressiva")
    produto = st.text_input("Nome do Produto:", placeholder="Ex: Escova Para Cabelo Cacheado")
    loja = st.radio("Onde está o link?", list(LINKS.keys()))
    link_f = LINKS[loja]

    if st.button("🚀 GERAR TEXTOS DE ALTA CONVERSÃO"):
        if produto:
            st.success("✅ ESTRATÉGIA DE VENDA GERADA!")
            
            # COPY LONGA E AGRESSIVA
            copy_agressiva = (
                f"🚨 ALERTA DE OPORTUNIDADE: VOCÊ NÃO PODE MAIS IGNORAR ISSO! 🚨\n\n"
                f"Meninas, parem tudo! Se vocês sofrem com o tempo perdido ou com produtos que prometem e não cumprem, "
                f"o {produto} chegou para mudar o jogo. Não é apenas mais um 'achadinho', é a solução que vai transformar a sua rotina! ✨\n\n"
                f"Por que você PRECISA dele agora?\n"
                f"✅ Tecnologia exclusiva que você não encontra em qualquer lugar.\n"
                f"✅ Design premium que traz praticidade e elegância.\n"
                f"✅ Viral absoluto: quem comprou, não troca por nada!\n\n"
                f"O estoque está voando e eu não sei até quando consigo manter esse preço. "
                f"A decisão é sua: continuar passando sufoco ou garantir o seu {produto} agora mesmo com a garantia da LuhVee Stores. 🛍️\n\n"
                f"👇 NÃO DEIXE PARA DEPOIS, O LINK ESTÁ AQUI:\n"
                f"🔗 {link_f}\n\n"
                f"LuhVee Stores ❤️ — Sua autoestima em primeiro lugar!"
            )
            
            st.markdown("### 📱 Copy para Stories/Status (Toque e segure para copiar)")
            st.code(copy_agressiva, language="text")
            
            copy_reels = (
                f"POV: Você finalmente encontrou o segredo das blogueiras: {produto}! 😍🔥\n\n"
                f"Chega de gastar com o que não funciona. Este é o investimento que você merece. "
                f"Se você quer facilidade, brilho e resultados reais, esse vídeo é o seu sinal! 🎀\n\n"
                f"Diga 'EU QUERO' nos comentários que eu te mando o link direto no seu direct! 📥\n\n"
                f"🔗 Link na BIO também!\n#luhveestores #achadinhos #vendasonline #viral"
            )
            st.markdown("### 🎬 Copy para Reels/TikTok")
            st.code(copy_reels, language="text")
        else:
            st.warning("Luh, escreva o nome do produto primeiro! 😘")

# ==========================================
# ABA 2: PESQUISA MULTI-REDES
# ==========================================
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência Global de Mercado")
    categoria = st.selectbox("Escolha o Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 MINERAR TENDÊNCIAS"):
        prod = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Facebook Ads 📢"])
        st.subheader(f"💡 Sugestão Viral: {prod}")
        st.info(f"Este item está explodindo no **{rede}** hoje. Ótima oportunidade de postagem!")

# ==========================================
# ABA 3: INSTAGRAM ESTRATÉGICO
# ==========================================
elif aba == "📸 Instagram Estratégico":
    st.title("📸 O que postar hoje?")
    foco = st.selectbox("Qual seu objetivo?", ["Vender Muito", "Ganhar Seguidores", "Engajar/Ganhar Likes"])
    
    if st.button("🔍 GERAR PLANO DE AÇÃO"):
        if foco == "Vender Muito":
            st.warning("🎯 **Ação:** Faça 3 Stories mostrando a dor do cliente e finalize com o seu link (Madeirada!).")
        elif foco == "Ganhar Seguidores":
            st.info("🎯 **Ação:** Poste um Reels de 'Achadinho Útil' com áudio em alta. Use cortes rápidos.")
        else:
            st.success("🎯 **Ação:** Poste uma frase motivacional profunda no Feed ou Stories e peça para compartilharem.")
        
        st.write("**Hashtags do dia:** #luhveestores #achadinhos #viral #lifestyle")

# ==========================================
# ABA 4: MENSAGENS PROFUNDAS (1000 LETRAS)
# ==========================================
elif aba == "✨ Mensagens que Tocam o Coração":
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    
    if st.button("✨ GERAR REFLEXÃO PROFUNDA"):
        # Lógica de texto longo restaurada
        texto_longo = (
            f"{periodo}\n\n"
            "Às vezes, a correria nos faz esquecer de olhar para dentro. Você já parou para pensar no quanto você é incrível? "
            "A vida não é apenas pagar contas e correr contra o relógio, é sobre os momentos que fazem o coração vibrar. "
            "Você é uma mulher guerreira, cheia de luz, e cada desafio que você enfrenta só prova a sua força incomum. "
            "Não se compare com ninguém, pois o seu brilho é único e ninguém pode apagá-lo. "
            "Que hoje você se priorize, se ame e entenda que você merece o melhor do mundo, inclusive os pequenos mimos que trazem alegria ao seu dia. "
            "Siga com fé, pois o melhor ainda está por vir e você está apenas começando a florescer nesta jornada linda chamada vida.\n\n"
            "Com todo carinho do mundo,\nLuhVee Stores 🛍️❤️"
        )
        st.code(texto_longo, language="text")
