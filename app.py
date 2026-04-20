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
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- BANCO DE NICHOS ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Kit de Pincéis Profissional", "Máscara de LED Facial", "Removedor de Cravos a Vácuo", "Organizador de Maquiagem Giratório"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Projetor Astronauta", "Fita LED RGB Inteligente", "Umidificador de Ar Retrô", "Aspirador Robô Inteligente"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro", "Óculos de Sol Luxury", "Relógio Feminino Rose Gold", "Cinto Corrente Trend"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico", "Aquecedor de Mamadeira USB", "Monitor de Bebê Wi-Fi", "Tapete de Atividades"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital", "Tablet LCD para Desenho", "Escavadeira de Controle", "Kit de Miçangas DIY", "Lousa Mágica ColorColorida", "Mini Drone Sensor"],
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

# --- MOTOR DE VENDAS AGRESSIVO (LONGO E COMPLETO) ---
def motor_vendas_agressivo(produto, preco, marketplace, rede):
    link_venda = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML
    
    # Roteiro Anti-Flop por Rede
    estrategias = {
        "Instagram 📸": "💡 DICA ANTI-FLOP: Poste nos Stories com enquete antes. Use o link na bio e no sticker de link.",
        "TikTok 📱": "💡 DICA ANTI-FLOP: Use um áudio em alta no volume 3%. Legenda curta com 'Link na Bio'.",
        "WhatsApp 💬": "💡 DICA ANTI-FLOP: Poste no Status e envie individualmente para quem mais interage com você."
    }

    copy = f"""🚨 ALERTA DE PRODUTO VIRAL: {produto.upper()} 🚨

O segredo que as grandes blogueiras escondem finalmente foi revelado! Se você estava procurando por qualidade premium e um preço que cabe no seu bolso, sua busca termina AGORA.

✅ Por que você precisa do {produto}:
- Qualidade máxima testada e aprovada pela LuhVee.
- Design exclusivo que você não encontra em lojas comuns.
- Durabilidade garantida: não é descartável, é investimento!
- Praticidade que vai transformar sua rotina hoje mesmo.

⚠️ AVISO IMPORTANTE: O estoque está nas últimas unidades devido ao sucesso no TikTok. Quem deixar para amanhã vai perder o preço promocional!

💰 OFERTA EXCLUSIVA: R$ {preco}

🛒 COMPRE COM SEGURANÇA NOS LINKS ABAIXO:

🌐 MEU HUB DE OFERTAS: 
{LINK_HUB}

🛍️ LINK DIRETO DO PRODUTO ({marketplace.upper()}):
{link_venda}

🔍 CONSULTE OUTROS PRODUTOS:
{LINK_PESQUISA}

---
{estrategias[rede]}
Com carinho, LuhVee Stores ❤️"""
    return copy

# --- MOTOR INFINITO ---
aberturas = ["✨ Hoje pode ser o dia da sua virada...", "💖 Tem coisa boa chegando pra você...", "🌸 Não ignora isso aqui...", "🔥 Você merece muito mais...", "💫 Isso aqui pode mudar seu dia...", "✨ Hoje é um novo começo!", "💖 Ei, não esquece:", "🌸 Um lembrete importante:", "🔥 Acorda pra vida que você merece!", "💫 Você nasceu pra brilhar!"]
meios = ["imagine encontrar algo que combina com você", "coisas assim somem rápido", "muita gente já está aproveitando", "isso chama atenção de verdade", "você vai gostar disso", "você merece coisas incríveis", "seu esforço vai valer a pena", "coisas boas estão chegando", "seu momento está mais perto do que você imagina", "você é mais forte do que pensa"]
fechamentos = ["💖 Confia no processo.", "✨ Não deixa pra depois.", "🔥 Pode ser sua chance hoje.", "💫 Aproveita enquanto dá tempo.", "✨ Vai dar certo!", "🔥 Bora pra cima!", "🌸 Você consegue!", "💫 Nunca desista!"]

def gerar_mensagem_unica(periodo):
    s = "☀️ Bom dia!" if periodo == "Bom Dia" else "🌤️ Boa tarde!" if periodo == "Boa Tarde" else "🌙 Boa noite!"
    msg = f"{s}\n\n{random.choice(aberturas)} {random.choice(meios)}.\n{random.choice(fechamentos)}"
    links = f"\n\n🔍 Pesquisa: {LINK_PESQUISA}\n🌐 Hub: {LINK_HUB}"
    return msg + links

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Navegação:", ["🛍️ Postar Produtos", "🔎 Minerador de Ouro", "💖 Mensagens Infinitas"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Conversão Milionária")
    
    col1, col2 = st.columns(2)
    with col1:
        mkt = st.selectbox("Marketplace:", ["Shopee 🛍️", "Mercado Livre 📦"])
        rede_sel = st.selectbox("Onde vai postar?", ["Instagram 📸", "TikTok 📱", "WhatsApp 💬"])
    with col2:
        prod = st.text_input("📦 Nome do Produto:")
        prc = st.text_input("💰 Preço de Venda:")
        
    if st.button("🚀 GERAR COPY AGRESSIVA + ESTRATÉGIA"):
        if prod and prc:
            resultado_venda = motor_vendas_agressivo(prod, prc, mkt, rede_sel)
            st.text_area("📋 Copy Pronta para Uso:", resultado_venda, height=450)
        else:
            st.warning("Luh, preencha o nome e o preço do produto!")

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
        st.text_area("📋 Copie e poste:", "\n\n---\n\n".join(mensagens), height=500)
        st.balloons()
