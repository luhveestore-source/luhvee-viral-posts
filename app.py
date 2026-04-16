import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v7.0", page_icon="🔥")

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

# --- INICIALIZAÇÃO DO HISTÓRICO ---
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# --- BANCO DE DADOS COMPLETO ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica"],
    "📱 Tecnologia & Gadgets": ["Fone de Ouvido Noise Cancelling", "Carregador Magnético Magsafe", "Mini Projetor Portátil"],
    "🚗 Acessórios Automotivos": ["Suporte de Celular por Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda Profissional", "Regador Automático Solar", "Vaso de Auto-irrigação"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento Viral"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro Ortopédica"],
    "💪 Produtos de Academia": ["Garrafa de Água Motivacional", "Kit de Faixas Elásticas", "Massageador Muscular Turbo"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- FUNÇÃO DE MENSAGENS LONGAS (1000 LETRAS) ---
def gerar_mensagem_luhvee(tipo, periodo):
    if tipo == "Profunda/Inspiradora":
        gancho = "Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos. Pare um segundo. Respire fundo. Olhe ao seu redor e perceba o quanto você já caminhou até este momento."
        reflexao = "A vida não é uma corrida desenfreada contra o tempo, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é um mapa de uma batalha que você venceu em silêncio. Não se compare com o palco de ninguém enquanto você ainda está nos seus bastidores. O seu brilho é único e a sua essência é o que faz o mundo ser um lugar mais bonito de se viver. Valorize os pequenos passos, pois são eles que constroem os grandes destinos."
        conclusao = "Você é rara, preciosa e digna de tudo o que é bom. O seu momento de florescer é hoje!"
    else:
        gancho = "Status do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre! 😂 Acordei com uma vontade de vencer na vida, mas a vontade de voltar a dormir era maior."
        reflexao = "Dizem que o dinheiro não traz felicidade, mas eu preferia chorar em Paris do que na fila do pão! A vida é curta demais para não comprar aquele achadinho que você amou. Se está em dúvida, escolha o que te faz feliz (e o que parcela no cartão!). Lembre-se: boleto a gente paga, mas o brilho de um produtinho novo chegando em casa não tem preço!"
        conclusao = "Foca no objetivo e não esquece o café! Sorria, afinal, as rugas de preocupação saem caro para botocar depois!"
    
    return f"{periodo}\n\n{gancho}\n\n{reflexao}\n\n{conclusao}\n\nCom carinho, LuhVee Stores ❤️"

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais", "🔗 Vitrines & Hub"])

# --- ABA 1: POSTAR PRODUTOS (COPY PROFISSIONAL AGRESSIVA) ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão Profissional")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    
    if st.button("🚀 GERAR COPY AGRESSIVA"):
        if produto:
            valor_final = f"R$ {preco}" if preco else "PREÇO DE OPORTUNIDADE"
            # Copy Profissional com gatilhos reais para WhatsApp/Instagram/TikTok
            copy_completa = (
                f"🚨 PARA TUDO! VOCÊ VAI PERDER ESSA OPORTUNIDADE? 🚨\n\n"
                f"Acabei de liberar o link do {produto.upper()} que viralizou na gringa e finalmente chegou para nós! "
                f"Atenção: Esse é o estoque exclusivo e quem não garantir agora vai ficar na mão. "
                f"Qualidade premium testada e aprovada por mim. 🔥\n\n"
                f"💎 POR QUE VOCÊ PRECISA DISSO:\n"
                f"✅ Qualidade Superior (Acabamento de Luxo)\n"
                f"✅ Resultado Imediato e Prático\n"
                f"✅ O queridinho das redes sociais\n\n"
                f"😱 De: R$ ---,--- por APENAS: {valor_final}\n"
                f"⚠️ O link expira em breve devido à alta demanda!\n\n"
                f"🛒 COMPRE AGORA NO LINK SEGURO:\n"
                f"👉 https://collshp.com/luhveestores\n\n"
                f"LuhVee Stores 🛍️ - Sua dose diária de tendência e autoestima!"
            )
            st.code(copy_completa, language="text")
            st.info("💡 Copy estruturada com gatilhos de Escassez, Urgência e Autoridade.")
        else: st.warning("Luh, digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES + HISTÓRICO ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado + Histórico")
    categoria = st.selectbox("Nicho para Minerar:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        # Salva no histórico da sessão
        st.session_state['historico'].append(f"{sugestao} (Encontrado no {rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    
    if st.session_state['historico']:
        st.write("---")
        st.subheader("📋 Histórico de Pesquisas")
        for item in reversed(st.session_state['historico']):
            st.text(f"✅ {item}")
        if st.button("🗑️ Limpar Tudo"):
            st.session_state['historico'] = []
            st.rerun()

# --- ABA 3: INSTAGRAM TRENDS ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Insights Instagram")
    if st.button("🔍 ANALISAR ALGORITMO"):
        st.warning("🎯 Reels curtos (7-10 seg) com áudio instrumental e legenda no centro estão bombando!")

# --- ABA 4: MOTIVACIONAIS ---
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM"):
        st.code(gerar_mensagem_luhvee(estilo, periodo), language="text")

# --- ABA 5: HUB ---
else:
    st.title("🔗 Seus Links Oficiais")
    st.code("https://collshp.com/luhveestores")
