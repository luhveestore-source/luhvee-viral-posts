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
    .stTextArea>div>div>textarea { background-color: #1a1a1a !important; color: #ff69b4 !important; border: 1px solid #ff69b4 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LINKS OFICIAIS ---
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- BANCO DE NICHOS COMPLETO ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Kit de Pincéis Profissional", "Máscara de LED Facial", "Removedor de Cravos a Vácuo", "Organizador de Maquiagem Giratório"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Projetor Astronauta", "Fita LED RGB Inteligente", "Umidificador de Ar Retrô", "Aspirador Robô Inteligente"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro", "Óculos de Sol Luxury", "Relógio Feminino Rose Gold", "Cinto Corrente Trend"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico", "Aquecedor de Mamadeira USB", "Monitor de Bebê Wi-Fi", "Tapete de Atividades"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital", "Tablet LCD para Desenho", "Escavadeira de Controle", "Kit de Miçangas DIY", "Lousa Mágica Colorida", "Mini Drone Sensor"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica", "Brinquedo Interativo com Petiscos", "Coleira com LED", "Lançador de Bolinhas", "Rede para Gatos de Janela"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Carregador Magsafe", "Mini Projetor Portátil", "Smartwatch Ultra Series", "Teclado Mecânico RGB", "Suporte Articulado para Monitor", "Power Bank Indução"],
    "🚗 Acessórios Automotivos": ["Suporte Celular Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon App", "Polidor de Farol", "Câmera de Ré Visão Noturna", "Organizador de Banco Couro"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras Empilháveis", "Sacos de Vácuo para Roupas", "Mini Aspirador de Mesa", "Suporte de Vassouras Adesivo", "Dispenser de Sabão Automático"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda Profissional", "Regador Automático Solar", "Vaso de Auto-irrigação", "Parafusadeira Viral sem Fio", "Lanterna Tática Militar", "Kit de Ferramentas Rosa"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento Refletiva", "Kit Meias Performance", "Carteira Slim Antifurto", "Pulseira de Couro Masculina"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro Ortopédica", "Bota Adventure Impermeável", "Tênis de Academia Knit"],
    "💪 Produtos de Academia": ["Garrafa de Água Motivacional", "Kit de Faixas Elásticas", "Massageador Muscular Turbo", "Corda de Pular Digital", "Tapete de Yoga Antiderrapante", "Rolo de Liberação Miofascial"],
    "🌎 Internacional (High Ticket)": ["ProDentim Original", "Suplemento BioFit", "Renovador Facial 24k", "Redutor de Medidas Viral", "Sérum Anti-Idade Suíço"]
}

# --- MOTOR DE VENDAS AGRESSIVO (MAX 300 LETRAS) ---
def motor_vendas_curto(produto, preco, marketplace, rede):
    link_venda = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML
    estrategias = {
        "Instagram 📸": "💡 STORY: Use sticker de link!",
        "TikTok 📱": "💡 TIKTOK: Áudio viral + Link Bio!",
        "WhatsApp 💬": "💡 WHATS: Poste no Status agora!"
    }

    copy = f"""🚨 VIRALIZOU: {produto.upper()} 🚨

O segredo que as blogueiras escondem finalmente revelado! Qualidade premium e preço que cabe no seu bolso. 🔥

✅ Original & Testado
✅ Design de Luxo
✅ Praticidade Total

😱 APENAS: R$ {preco}

🛒 COMPRE AQUI:
👉 {link_venda}

🎁 MEU HUB DE OFERTAS:
👉 {LINK_HUB}

---
{estrategias[rede]}
Bjs da Luhvee Stores 🛍️"""
    return copy

# --- MOTOR DE MENSAGENS INFINITAS (SUA LÓGICA LIMPA) ---
aberturas = ["✨ Hoje é um novo começo!", "💖 Ei, não esquece:", "🌸 Um lembrete importante:", "🔥 Acorda pra vida que você merece!", "💫 Você nasceu pra brilhar!"]
meios = ["você merece coisas incríveis", "seu esforço vai valer a pena", "coisas boas estão chegando", "seu momento está mais perto", "você é mais forte do que pensa"]
fechamentos = ["💖 Confia no processo", "✨ Vai dar certo", "🔥 Bora pra cima", "🌸 Você consegue", "💫 Nunca desista"]

def gerar_mensagem_unica(periodo):
    s = "☀️ Bom dia!" if periodo == "Bom Dia" else "🌤️ Boa tarde!" if periodo == "Boa Tarde" else "🌙 Boa noite!"
    # Montagem sem pontos extras no final das frases do meio
    msg = f"{s}\n\n{random.choice(aberturas)}\n{random.choice(meios)}.\n{random.choice(fechamentos)}!"
    links = f"\n\n🌐 Hub: {LINK_HUB}"
    assinatura = "\n\nBjs da Luhvee Stores ❤️"
    return msg + links + assinatura

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Navegação:", ["🛍️ Postar Produtos", "🔎 Minerador de Ouro", "💖 Mensagens Infinitas"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada Curta & Lucrativa")
    col1, col2 = st.columns(2)
    with col1:
        mkt = st.selectbox("Marketplace:", ["Shopee 🛍️", "Mercado Livre 📦"])
        rede_sel = st.selectbox("Rede Social:", ["Instagram 📸", "TikTok 📱", "WhatsApp 💬"])
    with col2:
        prod = st.text_input("📦 Produto:", placeholder="Ex: Escova 5 em 1")
        prc = st.text_input("💰 Preço:", placeholder="Ex: 89,90")
        
    if st.button("🚀 GERAR COPY AGRESSIVA"):
        if prod and prc:
            resultado_venda = motor_vendas_curto(prod, prc, mkt, rede_sel)
            st.text_area("📋 Copy Pronta:", resultado_venda, height=300)
        else:
            st.warning("Preencha o nome e o preço!")

elif aba == "🔎 Minerador de Ouro":
    st.title("🔎 Minerador Profissional")
    nicho = st.selectbox("Selecione o Nicho:", list(nichos_completos.keys()))
    if st.button("📡 MINERAR"):
        st.success(f"💎 Sugestão Viral: **{random.choice(nichos_completos[nicho])}**")

else:
    st.title("💖 Gerador de Mensagens Infinitas")
    per = st.selectbox("Período:", ["Bom Dia", "Boa Tarde", "Boa Noite"])
    qtd = st.slider("Quantidade:", 1, 500, 20)
    if st.button("✨ GERAR AGORA"):
        random.seed(time.time())
        mensagens = [gerar_mensagem_unica(per) for _ in range(qtd)]
        st.text_area("📋 Lista de Mensagens:", "\n\n---\n\n".join(mensagens), height=500)
        st.balloons()
