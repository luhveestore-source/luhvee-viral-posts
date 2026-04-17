import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v16.0", page_icon="🔥")

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

# --- INICIALIZAÇÃO DOS HISTÓRICOS ---
if 'historico_pesquisa' not in st.session_state:
    st.session_state['historico_pesquisa'] = []
if 'historico_posts' not in st.session_state:
    st.session_state['historico_posts'] = []

# --- MOTOR IA: COPYWRITING PROFISSIONAL (OPENAI STYLE) ---
def gerar_copy_venda_ia(produto, preco):
    valor = f"R$ {preco}" if preco else "PREÇO EXCLUSIVO"
    
    gancho = random.choice([
        f"🚨 ALERTA DE TENDÊNCIA: O {produto.upper()} CHEGOU PARA MUDAR TUDO! 🚨",
        f"🔥 PARA TUDO! Se você estava esperando um sinal para garantir o seu {produto.upper()}, O SINAL É ESSE! 🔥",
        f"😱 NÃO COMPRE o {produto.upper()} em qualquer lugar antes de ler isso aqui até o final!",
        f"👑 EXCLUSIVIDADE LUHVEE STORES: O {produto.upper()} que as blogueiras não querem que você descubra!"
    ])
    
    corpo = random.choice([
        f"A qualidade deste {produto} é simplesmente surreal e superou todas as nossas expectativas nos testes de curadoria. Se você está cansada de investir em produtos que prometem muito e não entregam nada, este item veio para mudar o seu jogo definitivamente. Não é apenas mais um item no seu carrinho de compras, é um investimento real na sua autoestima, na sua praticidade e no seu bem-estar diário. O acabamento premium, a durabilidade extrema e o design impecável fazem deste produto o desejo número 1 das redes sociais neste exato momento em todo o Brasil. Você merece o melhor e nós trouxemos exatamente isso.",
        f"Atenção: O mercado está inundado de réplicas que decepcionam, mas aqui na LuhVee Stores nós só trabalhamos com a elite dos achadinhos virais. O {produto} que você está vendo agora é o original, aquele que viralizou na gringa e que todas as grandes influencers estão usando em segredo para facilitar a rotina. Ele resolve o seu problema de forma rápida, elegante e com um custo-benefício que parece erro de sistema. É a união perfeita entre tecnologia, estilo e a confiança que só a nossa marca oferece. Não aceite imitações quando você pode ter o topo da categoria."
    ])
    
    urgencia = random.choice([
        f"⚠️ AVISO DE ÚLTIMA HORA: Nosso estoque físico está nas últimas unidades devido ao sucesso estrondoso nas redes vizinhas. Se você quer o {produto} com esse valor promocional exclusivo, a hora de agir é agora. O botão de compra pode mudar para 'Esgotado' a qualquer segundo e não temos previsão de reposição com este preço. Proteja o seu investimento, garanta a sua unidade agora mesmo e faça parte do grupo seleto de mulheres que não aceitam nada menos que o melhor para si mesmas.",
        f"⏰ O TEMPO ESTÁ CORRENDO: Esta oferta exclusiva é válida apenas enquanto durarem os nossos estoques. O {produto} é, sem dúvida, o item mais pedido da semana e a demanda está simplesmente surreal. Não adianta me mandar mensagem no direct depois pedindo cupom se você perder essa oportunidade única. Clique no link agora, garanta o seu e receba no conforto da sua casa com envio prioritário, rastreio em tempo real e nota fiscal garantida."
    ])

    return f"{gancho}\n\n{corpo}\n\n💎 DIFERENCIAIS:\n✅ Qualidade Premium Testada\n✅ Design Tendência 2026\n✅ Envio Imediato e Seguro\n\n😱 POR APENAS: {valor}\n\n{urgencia}\n\n🛒 LINK SEGURO:\n👉 https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️"

# --- BANCO DE DADOS COMPLETO (TODOS OS NICHOS) ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade", "Canguru Ergonômico"],
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

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão IA")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    if st.button("🚀 GERAR COPY PROFISSIONAL"):
        if produto:
            res = gerar_copy_venda_ia(produto, preco)
            st.code(res, language="text")
            st.session_state['historico_posts'].append(f"POST: {produto} - R$ {preco}")
        else: st.warning("Digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES + HISTÓRICO ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    cat = st.selectbox("Nicho para Minerar:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[cat])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    if st.session_state['historico_pesquisa']:
        st.write("---")
        st.subheader("📋 Histórico de Mineração")
        for item in reversed(st.session_state['historico_pesquisa']): st.text(f"✅ {item}")

# --- ABA 3: INSTAGRAM TRENDS IA (EXPLICAÇÕES + HORÁRIOS) ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre")
    if st.button("🔍 ANALISAR ALGORITMO E HORÁRIOS"):
        st.subheader("1. Sugestão de Formato")
        st.info("🎯 **Reels Curtos (5 a 10 segundos):** O Instagram está entregando muito mais vídeos rápidos que vão direto ao ponto. Use cortes secos e rápidos.")
        st.subheader("2. Tendência de Áudio")
        st.success("🎶 **Áudios Virais com 'Setinha':** Use músicas que estão subindo para entrar no Explorar automaticamente.")
        st.subheader("3. Gancho de Retenção")
        st.warning("👀 **Texto no Centro da Tela:** Coloque o título do produto bem no meio da tela nos primeiros 3 segundos para prender a atenção.")
        st.subheader("⏰ Horários de Ouro (Maior Conversão)")
        st.write("☀️ **Manhã:** 08:30 - 09:30 | 🍱 **Almoço:** 12:00 - 13:30 | 🌙 **Noite:** 18:00 - 20:00")

# --- ABA 4: MOTIVACIONAIS (TEXTO LONGO 1000 LETRAS) ---
else:
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        if estilo == "Profunda/Inspiradora":
            msg = f"{periodo}\n\nÀs vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos. Pare um segundo. Respire fundo. Olhe ao seu redor e perceba o quanto você já caminhou até este exato momento. A vida não é uma corrida desenfreada contra o tempo, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é um mapa de uma batalha vencida em silêncio. Valorize os pequenos passos, pois são eles que constroem os grandes destinos. Você é rara e preciosa.\n\nO seu momento de florescer é hoje! ✨\n\nCom carinho, LuhVee Stores ❤️"
        else:
            msg = f"{periodo}\n\nStatus do dia: Em busca da minha versão rica! 😂 Dizem que o dinheiro não traz felicidade, mas eu preferia muito mais estar chorando em Paris do que na fila do pão! A vida é curta demais para a gente não comprar aquele achadinho que amou de primeira vista. Lembre-se: boletos a gente paga, mas o brilho no olho de ver o produto chegando em casa não tem preço! Sorria, as rugas de preocupação saem caro para botocar depois!\n\n💅 Plena e pronta para o próximo recebido!\n\nCom carinho, LuhVee Stores ❤️"
        st.code(msg, language="text")
