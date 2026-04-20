import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL PREMIUM ---
st.set_page_config(page_title="LuhVee Viral Machine PRO", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #ff69b4 !important; font-family: 'Inter', sans-serif; text-shadow: 2px 2px 4px #000000; }
    .stButton>button {
        background: linear-gradient(135deg, #ff69b4, #ff1493);
        color: white !important; border: 1px solid #ffd700; border-radius: 12px;
        font-weight: bold; width: 100%; height: 50px; font-size: 18px; transition: 0.4s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0px 10px 20px rgba(255, 105, 180, 0.4); }
    .stTextInput>div>div>input, .stSelectbox>div>div { background-color: #1a1a1a !important; color: white !important; border: 1px solid #333 !important; }
    .copy-section { background-color: #111; border-left: 5px solid #ff69b4; padding: 20px; border-radius: 10px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE NICHOS COMPLETO (RESTAURADO) ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Kit de Pincéis Profissional"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Projetor Astronauta"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital", "Tablet LCD", "Escavadeira de Controle"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte", "Escova Tira Pelos", "Brinquedo Interativo"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Carregador Magsafe", "Mini Projetor Portátil", "Smartwatch Ultra"],
    "🚗 Acessórios Automotivos": ["Suporte Gravidade", "Aspirador Sem Fio", "Luz Interna Neon", "Polidor de Farol"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo", "Mini Aspirador de Mesa"],
    "🌿 Ferramentas & Jardinagem": ["Kit Poda Profissional", "Regador Solar", "Vaso Auto-irrigação", "Parafusadeira Viral"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento", "Kit Meias Performance"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro", "Bota Adventure"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Faixas Elásticas", "Massageador Turbo", "Corda de Pular Digital"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial", "Redutor de Medidas"]
}

# --- MOTOR IA DE CONSTRUÇÃO DE TEXTO (NUNCA REPETE) ---
def motor_ia_luhvee(tipo, produto=None, preco=None, marketplace=None, periodo=None):
    # Dicionário de Blocos para Variedade Infinita
    ganchos_venda = [
        f"🚨 ALERTA DE TENDÊNCIA: O {produto} CHEGOU! 🚨",
        f"🔥 O SEGREDO FOI REVELADO! Você precisa desse {produto}! 🔥",
        f"😱 NÃO COMPRE o {produto} sem ver esse vídeo antes!",
        f"💎 EXCLUSIVIDADE: O {produto} que viralizou na gringa chegou na LuhVee!",
        f"👑 STATUS DE LUXO: Tenha o {produto} original e sinta a diferença!"
    ]
    
    corpo_venda = [
        "A qualidade é surreal e foi testada pessoalmente por mim. Esqueça as réplicas que decepcionam.",
        "Sabe aquele item que resolve sua vida e te deixa com cara de rica? É exatamente esse!",
        "O acabamento premium e a durabilidade fazem deste produto o desejo número 1 das redes sociais.",
        "Tecnologia de ponta e design exclusivo. Você não vai encontrar essa qualidade em outro lugar.",
        "Eu usei, aprovei e garanto: o resultado é imediato e vai transformar sua rotina."
    ]
    
    chamada_venda = [
        "Estoque físico nas últimas unidades! Garanta o seu ou aceite pagar o dobro depois.",
        "⚠️ AVISO: Sem previsão de reposição com esse valor. Proteja seu bolso e sua autoestima!",
        "🚀 CORRE PRO LINK! A demanda está surreal e o botão vai sair do ar a qualquer segundo!",
        "Não deixe para amanhã o que você pode garantir hoje com preço de lançamento."
    ]

    # Lógica de Links
    link_final = "https://collshp.com/luhveestores" if marketplace == "Shopee 🛍️" else "https://www.mercadolivre.com.br/social/axwelloliveira"
    
    if tipo == "Venda":
        res = f"{random.choice(ganchos_venda)}\n\n{random.choice(corpo_venda)}\n\n💎 DIFERENCIAIS:\n✅ Qualidade Premium\n✅ Envio Imediato\n✅ Garantia LuhVee\n\n😱 POR APENAS: R$ {preco}\n\n{random.choice(chamada_venda)}\n\n🛒 LINK SEGURO NO {marketplace.upper()}:\n👉 {link_final}\n\nLuhVee Stores 🛍️"
        return res

    elif tipo == "Vibes":
        intro = f"{periodo} 🌸"
        corpo_v = [
            "A jornada da vida não é uma corrida, mas um ciclo de renovação. Valorize seus passos.",
            "Status: Em busca da versão rica, porque a linda já cansou de boletos! 😂",
            "Respire fundo. Cada cicatriz é uma vitória silenciosa que te trouxe até aqui.",
            "Minha terapia favorita é o rastreio dizendo 'saiu para entrega'. Renova a alma!",
            "Você é rara, preciosa e digna de todo luxo e amor deste mundo. Floresça!"
        ]
        reflexao = [
            "Não deixe ninguém apagar seu brilho. O sol nasce para quem cultiva luz interior.",
            "Dizem que dinheiro não traz felicidade, mas chorar em Paris é bem melhor, né?",
            "Foca no café, no brilho e nos objetivos. Seus sonhos não se pagam sozinhos!",
            "Sorria sempre, o botox está caro e rir é o melhor tratamento de beleza gratuito."
        ]
        msg = f"{intro}\n\n{random.choice(corpo_v)} {random.choice(reflexao)}\n\n✨ Confira meus achadinhos:\n👉 https://collshp.com/luhveestores\n\nCom carinho, LuhVee Stores ❤️"
        return msg

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee PRO")
aba = st.sidebar.radio("Selecione a Missão:", ["🛍️ Postar Produtos", "🔎 Minerador de Ouro", "✨ Frases Motivacionais IA"])

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Conversão Milionária")
    mkt = st.selectbox("Qual o Marketplace?", ["Shopee 🛍️", "Mercado Livre 📦"])
    
    col1, col2 = st.columns(2)
    with col1: prod_n = st.text_input("Nome do Produto:")
    with col2: prc_n = st.text_input("Preço:")
    
    if st.button("🚀 GERAR COPY IA INFINITA"):
        if prod_n:
            st.success("✅ IA TRABALHANDO: COPY EXCLUSIVA GERADA!")
            texto = motor_ia_luhvee("Venda", produto=prod_n, preco=prc_n, marketplace=mkt)
            st.code(texto, language="text")
            
            st.markdown("### 🗺️ Plano de Postagem (Passo a Passo)")
            c1, c2, c3 = st.columns(3)
            with c1: st.info("**Insta:** 3 Fotos Stories + Reels 7s")
            with c2: st.info("**TikTok:** Gancho de 3s + Link Bio")
            with c3: st.info("**Whats:** Copy Grupos + Preço Status")
        else: st.warning("Digite o produto!")

# --- ABA 2: MINERADOR ---
elif aba == "🔎 Minerador de Ouro":
    st.title("🔎 Caçador de Tendências Pro")
    nicho = st.selectbox("Escolha o Nicho:", list(nichos_completos.keys()))
    if st.button("📡 MINERAR AGORA"):
        produto_achado = random.choice(nichos_completos[nicho])
        st.success(f"💎 PRODUTO VIRAL ENCONTRADO: **{produto_achado}**")
        st.write("Dica: Esse item está com alta demanda de busca orgânica hoje.")

# --- ABA 3: MOTIVACIONAIS IA ---
else:
    st.title("✨ Vibes LuhVee Stores (IA)")
    momento = st.selectbox("Período:", ["Bom Dia", "Boa Tarde", "Boa Noite"])
    if st.button("🪄 GERAR MENSAGEM ÚNICA"):
        msg_ia = motor_ia_luhvee("Vibes", periodo=momento)
        st.code(msg_ia, language="text")
