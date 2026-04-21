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

# --- LINKS ---
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- NICHOS ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Luminária Pôr do Sol", "Projetor Astronauta"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Mini Projetor Portátil", "Smartwatch Ultra"]
}

# --- MOTOR MÁQUINA DE VENDAS ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace, rede):

    link_venda = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML

    preco_formatado = f"R$ {preco.replace('R$', '').strip()}"
    parcela_txt = f"\n💳 {parcelas}" if parcelas else ""

    hooks = [
        f"🚨 {produto.upper()} TÁ VIRALIZANDO AGORA",
        f"😳 COMO ISSO FICOU TÃO BARATO?",
        f"🔥 TODO MUNDO TÁ COMPRANDO ISSO",
        f"💥 ISSO AQUI EXPLODIU DO NADA",
        f"⚠️ VOCÊ PRECISA VER ISSO"
    ]

    dores = [
        "se você ainda não tem isso, tá perdendo tempo todo dia",
        "isso resolve algo que muita gente sofre sem perceber",
        "a maioria das pessoas ainda não descobriu isso"
    ]

    desejos = [
        "facilita sua rotina absurdamente",
        "deixa tudo mais prático e rápido",
        "você vai usar isso todo dia"
    ]

    provas = [
        "tá entre os mais vendidos",
        "todo mundo que compra recomenda",
        "explodiu nos vídeos essa semana"
    ]

    urgencias = [
        "⚠️ pode acabar a qualquer momento",
        "🔥 estoque limitado",
        "🚨 preço pode subir"
    ]

    ctas = [
        "👉 garante o seu agora",
        "👉 clica e aproveita",
        "👉 corre enquanto dá tempo"
    ]

    intensidades = ["leve", "medio", "agressivo"]

    copies = []

    for _ in range(5):

        nivel = random.choice(intensidades)

        if nivel == "leve":
            copy = f"""{random.choice(hooks)}

{produto}

💡 {random.choice(desejos)}

💰 {preco_formatado}{parcela_txt}

👉 {link_venda}
"""

        elif nivel == "medio":
            copy = f"""{random.choice(hooks)}

{random.choice(dores)}

🔥 {produto}

💡 {random.choice(desejos)}

😳 {random.choice(provas)}

💰 {preco_formatado}{parcela_txt}

👉 {link_venda}

{random.choice(urgencias)}
"""

        else:
            copy = f"""{random.choice(hooks)}

{random.choice(dores).upper()}

🔥 {produto.upper()}

💥 {random.choice(desejos).upper()}

😱 {random.choice(provas).upper()}

💰 {preco_formatado}{parcela_txt}

👉 {link_venda}

{random.choice(urgencias)}
{random.choice(ctas)}
"""

        copies.append(copy)

    estrategias = {
        "Instagram 📸": "💡 STORY + CTA forte",
        "TikTok 📱": "💡 Hook nos 3 primeiros segundos",
        "WhatsApp 💬": "💡 Envie nos grupos agora"
    }

    return copies, estrategias[rede]

# --- MENSAGENS ---
def gerar_mensagem_unica(periodo):
    return f"{periodo} 💖 Nunca desista!\n\n👉 {LINK_HUB}"

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Navegação:", ["🛍️ Postar Produtos", "🔎 Minerador", "💖 Mensagens"])

if aba == "🛍️ Postar Produtos":

    st.title("🔥 Máquina de Vendas")

    col1, col2 = st.columns(2)

    with col1:
        mkt = st.selectbox("Marketplace:", ["Shopee 🛍️", "Mercado Livre 📦"])
        rede_sel = st.selectbox("Rede:", ["Instagram 📸", "TikTok 📱", "WhatsApp 💬"])

    with col2:
        prod = st.text_input("Produto")
        prc = st.text_input("Preço")
        parc = st.text_input("Parcelamento")

    if st.button("🚀 GERAR COPYS INSANAS"):

        if prod and prc:

            random.seed(time.time())

            copies, dica = motor_maquina_vendas(prod, prc, parc, mkt, rede_sel)

            for i, c in enumerate(copies):
                st.text_area(f"📋 Copy {i+1}", c, height=250)

            st.success(dica)

        else:
            st.warning("Preencha tudo")

elif aba == "🔎 Minerador":

    st.title("🔎 Minerador de Produtos")

    nicho = st.selectbox("Nicho", list(nichos_completos.keys()))

    if st.button("📡 MINERAR"):
        st.success(random.choice(nichos_completos[nicho]))

else:

    st.title("💖 Mensagens")

    periodo = st.selectbox("Período", ["Bom dia", "Boa tarde", "Boa noite"])

    if st.button("✨ GERAR"):
        st.text_area("Mensagem", gerar_mensagem_unica(periodo), height=200)