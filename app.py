import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v5.0", page_icon="🔥")

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
        font-family: 'monospace';
    }
    div[data-baseweb="select"], div[data-baseweb="input"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DO HISTÓRICO ---
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# --- BANCO DE DADOS DE TENDÊNCIAS ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD"],
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

# --- FUNÇÃO DE MENSAGENS LONGAS ---
def gerar_mensagem_luhvee(tipo, periodo):
    if tipo == "Profunda/Inspiradora":
        gancho = "Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos. Pare um segundo. Respire fundo. Olhe ao seu redor e perceba o quanto você já caminhou até este momento."
        reflexao = "A vida não é uma corrida desenfreada contra o tempo, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é um mapa de uma batalha que você venceu em silêncio. Não se compare com o palco de ninguém enquanto você ainda está nos seus bastidores. O seu brilho é único e a sua essência é o que faz o mundo ser um lugar mais bonito de se viver. Valorize os pequenos passos, pois são eles que constroem os grandes destinos."
        conclusao = "Você é rara, preciosa e digna de tudo o que é bom. O seu momento de florescer é hoje!"
    else:
        gancho = "Status do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre! 😂 Acordei com uma vontade de vencer na vida, mas a vontade de voltar a dormir era maior."
        reflexao = "Dizem que o dinheiro não traz felicidade, mas eu preferia chorar em Paris do que na fila do pão! A vida é curta demais para não comprar aquele achadinho que você amou. Se está em dúvida, escolha o que te faz feliz (e o que parcela no cartão!). Lembre-se: boleto a gente paga, mas o brilho de um produtinho novo chegando em casa não tem preço!"
        conclusao = "Foca no objetivo, gata! Sorria, as rugas de preocupação saem mais caro depois!"
    
    return f"{periodo}\n\n{gancho}\n\n{reflexao}\n\n{conclusao}\n\nCom carinho, LuhVee Stores ❤️"

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais", "🔗 Vitrines & Hub"])

# ==========================================
# ABA 1: GERADOR DE MADEIRADA (ATUALIZADO AGRESSIVO)
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        produto = st.text_input("Nome do Produto:", placeholder="Ex: Camisa Linho Premium")
    with col2:
        preco = st.text_input("Preço (R$):", placeholder="Ex: 86,90")
    
    loja = st.radio("Link de qual loja?", ["Shopee", "Mercado Livre", "Site Oficial"])
    link_f = "https://collshp.com/luhveestores" # Link padrão conforme sua imagem

    if st.button("🚀 GERAR COPY AGRESSIVA"):
        if produto:
            st.success("✅ ESTRATÉGIA GERADA!")
            valor_final = f"R$ {preco}" if preco else "PREÇO DE OPORTUNIDADE"
            
            # --- COPY PARA GRUPOS E STORIES (MUITO AGRESSIVA) ---
            copy_agressiva = (
                f"🚨 PARA TUDO! VOCÊ VAI PERDER ESSA? 🚨\n\n"
                f"Acabei de liberar o link do {produto.upper()} que vocês tanto pediram! "
                f"Atenção: O estoque da loja está no fim e quem não boletar agora vai ficar sem. "
                f"É a melhor qualidade que eu já testei, tecido premium e caimento impecável. 🔥\n\n"
                f"💎 Diferenciais:\n"
                f"✅ Qualidade Superior (Não desbota)\n"
                f"✅ Entrega Garantida e Rápida\n"
                f"✅ O queridinho das redes sociais\n\n"
                f"😱 De: R$ ---,--- por APENAS: {valor_final}\n\n"
                f"🛒 COMPRE AGORA (Link Seguro):\n"
                f"👉 {link_f}\n\n"
                f"LuhVee Stores 🛍️ - Só trabalhamos com o que é tendência!"
            )
            
            # --- COPY PARA REELS/TIKTOK (GANCHO DE RETENÇÃO) ---
            copy_viral = (
                f"PARE DE COMPRAR ERRADO! ❌ Esse é o {produto} original!\n\n"
                f"Você já viu todo mundo usando, mas só aqui você encontra o preço de fábrica com qualidade real. "
                f"Não adianta economizar 10 reais e receber um produto que estraga na primeira lavagem. 💸\n\n"
                f"🔥 OFERTA EXCLUSIVA: {valor_final}\n"
                f"🚚 Frete Grátis disponível no link!\n\n"
                f"🔗 LINK NA BIO! Ou comenta 'EU QUERO' que eu te mando o desconto no Direct agora! 🚀\n\n"
                f"#luhveestores #achadinhos #moda #viral #shopeebrasil"
            )
            
            st.markdown("### 📱 Copy para WhatsApp / Stories / Grupos")
            st.code(copy_agressiva, language="text")
            
            st.markdown("### 🎬 Copy para Legenda de Vídeos (Instagram/TikTok)")
            st.code(copy_viral, language="text")
        else:
            st.warning("Luh, coloque o nome do produto primeiro! 😘")

# --- AS OUTRAS ABAS CONTINUAM IGUAIS PARA MANTER O HISTÓRICO E MENSAGENS ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Mineração de Ouro")
    categoria = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Ads Library 📢"])
        st.session_state['historico'].append(f"PRODUTO: {sugestao} | REDE: {rede}")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    if st.session_state['historico']:
        st.write("---")
        st.subheader("📋 Histórico")
        for item in reversed(st.session_state['historico']): st.text(f"✅ {item}")

elif aba == "📸 Instagram Trends IA":
    st.title("📸 Insights do Insta")
    if st.button("🔍 ANALISAR"): st.warning("🎯 Reels curtos e dinâmicos hoje!")

elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM"):
        st.code(gerar_mensagem_luhvee(estilo, periodo), language="text")

else:
    st.title("🔗 Seus Links")
    st.code("https://collshp.com/luhveestores")
