import streamlit as st
import random
import time

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine ELITE", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #ff69b4 !important; font-family: 'Inter', sans-serif; text-shadow: 2px 2px 4px #000000; }
    .stButton>button {
        background: linear-gradient(135deg, #ff69b4, #ff1493);
        color: white !important; border: 1px solid #ffd700; border-radius: 12px;
        font-weight: bold; width: 100%; height: 55px; font-size: 20px; transition: 0.4s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0px 10px 20px rgba(255, 105, 180, 0.6); }
    .stTextInput>div>div>input, .stSelectbox>div>div { background-color: #1a1a1a !important; color: white !important; border: 1px solid #ff69b4 !important; }
    .stCode { background-color: #111 !important; border: 1px solid #ff69b4 !important; color: #ff69b4 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LINKS OFICIAIS ---
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- BANCO DE NICHOS ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Máscara de LED Facial", "Organizador Giratório"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Projetor Astronauta", "Aspirador Robô"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro", "Óculos Luxury"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada Amamentação", "Kit Saída Maternidade", "Canguru Ergonômico", "Monitor Wi-Fi"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital", "Tablet LCD", "Escavadeira Controle", "Mini Drone"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte", "Escova Mágica", "Brinquedo Interativo", "Rede de Janela"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Carregador Magsafe", "Mini Projetor", "Smartwatch Ultra", "Teclado RGB"],
    "🚗 Acessórios Automotivos": ["Suporte Gravidade", "Aspirador Sem Fio", "Luz Neon App", "Polidor Farol", "Câmera de Ré"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo", "Dispenser Automático"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda", "Regador Solar", "Vaso Auto-irrigação", "Parafusadeira Viral", "Lanterna Tática"],
    "👔 Moda Masculina": ["Camisa Linho", "Calça Jogger Tech", "Jaqueta Corta-Vento", "Carteira Antifurto"],
    "👟 Calçados Masculinos": ["Tênis Nuvem", "Sapato Social Flex", "Bota Adventure", "Tênis Academia"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Elásticos", "Massageador Turbo", "Corda Digital", "Tapete Yoga"],
    "🌎 Internacional (High Ticket)": ["ProDentim Original", "Suplemento BioFit", "Renovador Facial 24k", "Redutor de Medidas"]
}

# --- MOTOR DE INTELIGÊNCIA ARTIFICIAL (COPY DE PRODUTOS) ---
def gerar_copy_venda(produto, preco, marketplace):
    ganchos = ["🚨 ALERTA DE TENDÊNCIA: O {prod} CHEGOU! 🚨", "🔥 O SEGREDO FOI REVELADO! Você precisa desse {prod}! 🔥", "😱 PARE TUDO! Se você queria um sinal para ter seu {prod}, é esse!"]
    corpos = ["A qualidade é surreal e foi testada pessoalmente por mim. Esqueça réplicas.", "Sabe aquele item que resolve sua vida e te deixa com cara de rica? É esse!", "O design exclusivo faz deste produto o desejo número 1 das redes."]
    
    link = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML
    loja = "LuhVee Stores na Shopee" if marketplace == "Shopee 🛍️" else "LuhVee Stores no Mercado Livre"
    
    res = f"{random.choice(ganchos).format(prod=produto.upper())}\n\n{random.choice(corpos)}\n\n😱 POR APENAS: R$ {preco}\n\n🚀 CORRE PRO LINK! Estoque limitado!\n\n🛒 LINK SEGURO:\n👉 {link}\n\n{loja} 🛍️"
    return res

# --- MOTOR DE MENSAGENS INFINITAS (SUA LÓGICA INTEGRADA) ---
aberturas_inf = ["✨ Hoje pode ser o dia da sua virada...", "💖 Tem coisa boa chegando pra você...", "🌸 Não ignora isso aqui...", "🔥 Você merece muito mais...", "💫 Isso aqui pode mudar seu dia..."]
meio_inf = ["imagine encontrar algo que combina com você", "coisas assim somem rápido", "muita gente já está aproveitando", "isso chama atenção de verdade", "você vai gostar disso"]
fechamento_inf = ["💖 Confia no processo.", "✨ Não deixa pra depois.", "🔥 Pode ser sua chance hoje.", "💫 Aproveita enquanto dá tempo."]

def gerar_vibe_infinita(periodo):
    s = "☀️ Bom dia!" if periodo == "Bom Dia" else "🌤️ Boa tarde!" if periodo == "Boa Tarde" else "🌙 Boa noite!"
    base = f"{s}\n\n{random.choice(aberturas_inf)} {random.choice(meio_inf)}.\n{random.choice(fechamento_inf)}"
    links = f"\n\n🔍 Pesquisa: {LINK_PESQUISA}\n🌐 Hub: {LINK_HUB}"
    return base + links

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Selecione a Missão:", ["🛍️ Postar Produtos", "🔎 Minerador de Ouro", "✨ Mensagens Infinitas IA"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Conversão")
    mkt = st.selectbox("Marketplace:", ["Shopee 🛍️", "Mercado Livre 📦"])
    col1, col2 = st.columns(2)
    with col1: prod = st.text_input("📦 Nome do Produto:")
    with col2: prc = st.text_input("💰 Preço:")
    
    if st.button("🚀 GERAR COPY PROFISSIONAL"):
        if prod:
            st.code(gerar_copy_venda(prod, prc, mkt), language="text")
            st.info("📸 Insta: Stories + Reels | 📱 TikTok: Gancho 3s | 💬 Whats: Grupos")
        else: st.warning("Digite o nome do produto!")

elif aba == "🔎 Minerador de Ouro":
    st.title("🔎 Caçador de Tendências")
    nicho = st.selectbox("Nicho:", list(nichos_completos.keys()))
    if st.button("📡 MINERAR AGORA"):
        st.success(f"💎 PRODUTO VIRAL ENCONTRADO: **{random.choice(nichos_completos[nicho])}**")

else:
    st.title("💖 Mensagens Infinitas (Fábrica LuhVee)")
    per = st.selectbox("Tipo:", ["Bom Dia", "Boa Tarde", "Boa Noite"])
    qtd = st.slider("Quantidade de mensagens:", 1, 500, 20)
    
    if st.button("✨ GERAR 500 MENSAGENS AGORA"):
        random.seed(time.time())
        mensagens_lista = [gerar_vibe_infinita(per) for _ in range(qtd)]
        resultado_final = "\n\n---\n\n".join(mensagens_lista)
        st.text_area("📋 Copie e poste (Várias opções):", resultado_final, height=500)
        st.balloons()
