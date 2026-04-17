import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v21.0", page_icon="🔥")

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

# --- INICIALIZAÇÃO DE HISTÓRICO ---
if 'historico_pesquisa' not in st.session_state:
    st.session_state['historico_pesquisa'] = []

# --- MOTOR IA: DIVERSIDADE DE COPY AGRESSIVA (MÚLTIPLAS OPÇÕES) ---
def gerar_copy_agressiva_ia(produto, preco):
    valor = f"R$ {preco}" if preco else "OFERTA EXCLUSIVA"
    prod_u = produto.upper()
    
    opcoes_copy = [
        # Opção 1: Gatilho de Escassez e Status
        f"🚨 ALERTA DE TENDÊNCIA: O {prod_u} CHEGOU! 🚨\n\nQualidade surreal e testada por mim! Se você cansou de produtos que prometem e não entregam, esse veio para mudar o jogo. Acabamento premium e desejo número 1 das redes sociais hoje.\n\n😱 POR APENAS: {valor}\n\n⏰ O TEMPO ESTÁ CORRENDO: Estoque físico nas últimas unidades! Garanta o seu agora ou aceite pagar o dobro depois!\n\n🛒 LINK SEGURO:\n👉 https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️",
        
        # Opção 2: Gatilho de Autoridade e Prova Social
        f"👑 EXCLUSIVIDADE: O {prod_u} QUE AS BLOGUEIRAS ESCONDEM! 👑\n\nO segredo foi revelado! O original que viralizou na gringa finalmente disponível aqui. Esqueça réplicas que duram uma semana. Aqui você tem qualidade real e estilo para sua rotina.\n\n🔥 OFERTA ÚNICA: {valor}\n\n⚠️ AVISO: Sem previsão de reposição com esse valor promocional. Proteja seu bolso e sua autoestima!\n\n🛒 COMPRE AGORA NO LINK:\n👉 https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️",
        
        # Opção 3: Gatilho de Medo de Perder (FOMO)
        f"😱 NÃO COMPRE O {prod_u} ANTES DE VER ISSO! ❌\n\nVocê merece o melhor! O {prod_u} resolve sua rotina com elegância e praticidade. É o investimento que faltava para você se sentir plena e moderna hoje. Não aceite menos!\n\n💸 PREÇO IMBATÍVEL: {valor}\n\n🚀 CORRE PRO LINK ANTES QUE ESGOTE! A demanda está surreal e o botão vai sair do ar!\n\n🛒 GARANTA O SEU AQUI:\n👉 https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️"
    ]
    return random.choice(opcoes_copy)

# --- MOTOR IA: MENSAGENS MOTIVACIONAIS (ATÉ 300 LETRAS) ---
def gerar_motivacional_ia(estilo, periodo):
    if estilo == "Profunda/Inspiradora":
        msgs = [
            f"{periodo}\n\nA jornada não é corrida, é renovação. Valorize seus passos e sua essência. Você é rara e seu momento de florescer é hoje! Confie na sua luz e nunca pare. ✨\n\nLuhVee Stores ❤️",
            f"{periodo}\n\nRespire fundo. Olhe o quanto você já caminhou. Cada cicatriz é uma vitória silenciosa. Você é o milagre que tanto procurava. Mantenha a fé e brilhe! 🌸\n\nLuhVee Stores ❤️"
        ]
    else:
        msgs = [
            f"{periodo}\n\nStatus: Em busca da versão rica, porque a linda cansou de boletos! 😂 Chorar em Paris é melhor que na fila do pão. Foca no café forte e no brilho! 💅\n\nLuhVee Stores ❤️",
            f"{periodo}\n\nMinha terapia é o rastreio dizendo 'saiu para entrega'. Boletos a gente paga, mas produtinho novo não tem preço! Sorria sempre, botox tá caro! ☕✨\n\nLuhVee Stores ❤️"
        ]
    return random.choice(msgs)

# --- BANCO DE DADOS DE NICHOS (TODOS RESTAURADOS) ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade", "Almofada Amamentação", "Canguru Ergonômico"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Elásticos", "Massageador Turbo"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento"],
    "👟 Calçados Masculinos": ["Tênis Nuvem", "Sapato Social Flex", "Bota Adventure"],
    "🌎 Internacional": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Ferramentas:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS (COPY + ROTEIRO) ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão IA")
    col1, col2 = st.columns([2, 1])
    with col1: prod = st.text_input("Nome do Produto:")
    with col2: prc = st.text_input("Preço (R$):")
    
    if st.button("🚀 GERAR COPY PROFISSIONAL"):
        if prod:
            st.success("✅ DIVERSIDADE IA: NOVA COPY GERADA!")
            st.code(gerar_copy_agressiva_ia(prod, prc), language="text")
            
            st.markdown("### 🗺️ Roteiro Estratégico de Postagem:")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("**📸 Instagram**")
                st.caption("Stories: 3 fotos (detalhe/uso/prova). Reels: 7s com áudio viral.")
            with c2:
                st.write("**📱 TikTok**")
                st.caption("Gancho inicial 3s + Link na Bio.")
            with c3:
                st.write("**💬 WhatsApp**")
                st.caption("Grupos: Copy completa. Status: Foto com preço em destaque.")
        else: st.warning("Digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES + HISTÓRICO ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    cat = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[cat])
        rede = random.choice(["TikTok", "Pinterest", "Instagram"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    
    if st.session_state['historico_pesquisa']:
        st.write("---")
        st.subheader("📋 Histórico de Mineração")
        for i in reversed(st.session_state['historico_pesquisa']): st.text(f"✅ {i}")

# --- ABA 3: INSTAGRAM TRENDS IA ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre")
    if st.button("🔍 ANALISAR ALGORITMO"):
        st.info("🎯 **Reels Curtos (5-10s):** Foco em retenção.")
        st.write("☀️ 08:30-09:30 | 🍱 12:00-13:30 | 🌙 18:00-20:00")

# --- ABA 4: MOTIVACIONAIS IA (300 LETRAS) ---
else:
    st.title("✨ Vibes LuhVee Stores")
    per = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    est = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM IA"):
        st.code(gerar_motivacional_ia(est, per), language="text")
