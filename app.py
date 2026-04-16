import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v4.5", page_icon="🔥")

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
    div[data-baseweb="select"], div[data-baseweb="input"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DO HISTÓRICO ---
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# --- BANCO DE DADOS DE TENDÊNCIAS (TODOS OS NICHOS) ---
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

# --- FUNÇÃO DE MENSAGENS LONGAS (VOLTOU!) ---
def gerar_mensagem_luhvee(tipo, periodo):
    if tipo == "Profunda/Inspiradora":
        ganchos = ["Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos.", "Pare um segundo. Respire fundo. Olhe ao seu redor."]
        reflexoes = [
            "A vida não é uma corrida desenfreada contra o tempo, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é um mapa de uma batalha que você venceu em silêncio. Não se compare com o palco de ninguém enquanto você ainda está nos seus bastidores. O seu brilho é único e a sua essência é o que faz o mundo ser um lugar mais bonito. Valorize os pequenos passos, pois são eles que constroem os grandes destinos.",
            "Muitas vezes depositamos a nossa felicidade no 'quando eu chegar lá'. Mas a verdade é que a vida acontece agora, neste exato fôlego. Ser uma mulher forte não significa não cansar, mas sim ter a sabedoria de descansar sem desistir. Você é o projeto mais importante da sua vida. Cuide-se com o mesmo amor que dedica aos outros, pois o seu coração é o seu templo mais sagrado e ele precisa de luz."
        ]
        conclusoes = ["Você é rara e preciosa.", "O seu momento de florescer é hoje."]
    else: # Engraçada/Vibes
        ganchos = ["Status do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre! 😂", "Acordei com uma vontade de vencer na vida, mas a vontade de voltar a dormir era maior."]
        reflexoes = [
            "Dizem que o dinheiro não traz felicidade, mas eu preferia chorar em Paris do que chorar na fila do pão, não é mesmo? A vida é curta demais para não comprar aquele achadinho que você amou. Se você está em dúvida entre o certo e o errado, escolha o que te faz feliz (e o que parcela em 12x na Shopee!). Lembre-se: boleto a gente paga, mas o brilho no olho de um produtinho novo chegando em casa não tem preço!",
            "Fui procurar o equilíbrio emocional e acabei encontrando um carrinho cheio de compras. Minha terapia é o rastreio do correio dizendo 'saiu para entrega'. Ser adulta é basicamente esperar encomendas e fingir que sabemos o que estamos fazendo. Sorria, afinal, as rugas de preocupação saem caro para botocar depois, então é melhor rir de tudo e seguir plena!"
        ]
        conclusoes = ["Foca no objetivo e não esquece o café!", "Plena e pronta para o próximo recebido! 💅"]

    return f"{periodo}\n\n{random.choice(ganchos)}\n\n{random.choice(reflexoes)}\n\n{random.choice(conclusoes)}\n\nCom carinho, LuhVee Stores ❤️"

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais", "🔗 Vitrines & Hub"])

# --- ABA 1: POSTAR PRODUTOS (COPY AGRESSIVA) ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Vendas")
    produto = st.text_input("Nome do Produto:")
    preco = st.text_input("Preço (R$):")
    if st.button("🚀 GERAR COPY AGRESSIVA"):
        if produto:
            valor = f"POR APENAS R$ {preco}" if preco else "PREÇO DE OPORTUNIDADE"
            st.code(f"🚨 ÚLTIMO AVISO: {produto.upper()}! 🚨\n\nEstoque voando! Qualidade premium por {valor}.\n🔗 Link: https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️", language="text")

# --- ABA 2: PESQUISA MULTI-REDES + HISTÓRICO ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Mineração de Ouro")
    categoria = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Ads Library 📢"])
        info = f"PRODUTO: {sugestao} | REDE: {rede}"
        st.session_state['historico'].append(info)
        st.success(f"💡 {sugestao} está bombando no {rede}!")
    
    if st.session_state['historico']:
        st.write("---")
        st.subheader("📋 Histórico de Hoje")
        for item in reversed(st.session_state['historico']):
            st.text(f"✅ {item}")

# --- ABA 3: INSTAGRAM TRENDS ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Insights do Insta")
    if st.button("🔍 ANALISAR"):
        st.warning("🎯 Reels de 7 seg com áudio instrumental está em alta!")

# --- ABA 4: MOTIVACIONAIS (COMPLETAS!) ---
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo da Mensagem:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        msg = gerar_mensagem_luhvee(estilo, periodo)
        st.code(msg, language="text")

# --- ABA 5: HUB ---
else:
    st.title("🔗 Seus Links")
    st.code("https://collshp.com/luhveestores")
