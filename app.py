import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v13.0", page_icon="🔥")

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
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DOS HISTÓRICOS ---
if 'historico_pesquisa' not in st.session_state:
    st.session_state['historico_pesquisa'] = []
if 'historico_posts' not in st.session_state:
    st.session_state['historico_posts'] = []

# --- MOTOR DE INTELIGÊNCIA DE COPYWRITING (ABORDAGEM AGRESSIVA 500+ LETRAS) ---
def gerar_copy_agressiva_ia(produto, preco):
    valor = f"R$ {preco}" if preco else "PREÇO EXCLUSIVO"
    
    # Simulação de motor OpenAI com estruturas de alta conversão
    ganchos = [
        f"🚨 ALERTA DE ESTOQUE: VOCÊ VAI DEIXAR O {produto.upper()} ESCAPAR? 🚨",
        f"🔥 O SEGREDO FOI REVELADO: POR QUE TODO MUNDO QUER O {produto.upper()}? 🔥",
        f"👑 EXCLUSIVIDADE LUHVEE STORES: O {produto.upper()} QUE VOCÊ MERECE! 👑"
    ]
    
    desenvolvimento = [
        f"Se você está cansada de produtos que prometem muito e não entregam nada, o {produto} veio para mudar o seu jogo. Eu testei pessoalmente e a qualidade é algo que nunca vi antes. Não é apenas mais um item no seu carrinho, é um investimento na sua autoestima e praticidade. O acabamento premium e a durabilidade fazem deste produto o desejo número 1 das redes sociais neste momento.",
        f"Atenção: O mercado está saturado de réplicas baratas, mas aqui na LuhVee nós prezamos pela sua satisfação real. O {produto} que você está vendo agora é o original, aquele que viralizou na gringa e que todas as influencers estão usando. Ele resolve o seu problema de forma rápida, elegante e com o melhor custo-benefício que você já encontrou em toda a internet."
    ]
    
    urgencia = [
        f"⚠️AVISO IMPORTANTE: Nosso estoque é limitado e as unidades com preço promocional estão voando. Não adianta me mandar mensagem depois pedindo desconto se você perder essa oportunidade agora. O link abaixo é seguro e direto da loja oficial. Garanta o seu antes que o botão mude para 'Esgotado'!",
        f"⏰ O TEMPO ESTÁ CORRENDO: Esta oferta é válida apenas enquanto durarem os nossos estoques físicos. O {produto} é o item mais pedido da semana e a demanda está surreal. Clique no link agora, garanta o seu e receba no conforto da sua casa com envio prioritário e nota fiscal."
    ]
    
    # Montagem do texto para atingir o volume de letras solicitado
    texto_final = (
        f"{random.choice(ganchos)}\n\n"
        f"{random.choice(desenvolvimento)}\n\n"
        f"💎 DIFERENCIAIS QUE VOCÊ SÓ ENCONTRA AQUI:\n"
        f"✅ Qualidade Premium Testada\n"
        f"✅ Design Exclusivo Tendência 2026\n"
        f"✅ Envio Imediato e Seguro\n\n"
        f"😱 DE: R$ ---,--- | POR APENAS: {valor}\n\n"
        f"{random.choice(urgencia)}\n\n"
        f"🛒 COMPRE AGORA NO LINK ABAIXO:\n"
        f"👉 https://collshp.com/luhveestores\n\n"
        f"LuhVee Stores 🛍️ - Onde a sua satisfação é a nossa prioridade!"
    )
    return texto_final

# --- BANCO DE DADOS COMPLETO ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade", "Almofada Amamentação", "Kit Saída Maternidade"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Elásticos", "Massageador Turbo"],
    "🌎 Internacional": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS (INTELIGÊNCIA RESTAURADA) ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão IA")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    
    if st.button("🚀 GERAR COPY DE ALTA CONVERSÃO"):
        if produto:
            copy = gerar_copy_agressiva_ia(produto, preco)
            st.code(copy, language="text")
            st.session_state['historico_posts'].append(f"{produto} ({preco})")
        else: st.warning("Digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES ---
elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    categoria = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    
    if st.session_state['historico_pesquisa']:
        st.write("---")
        for item in reversed(st.session_state['historico_pesquisa']): st.text(f"✅ {item}")

# --- ABA 3: INSTAGRAM TRENDS IA ---
elif aba == "📸 Instagram Trends IA":
    st.title("📸 Estratégia de Mestre")
    if st.button("🔍 ANALISAR ALGORITMO"):
        st.info("🎯 **Reels Curtos (5-10s):** Foco em retenção.")
        st.write("☀️ 08:30 - 09:30 | 🍱 12:00 - 13:30 | 🌙 18:00 - 20:00")

# --- ABA 4: MOTIVACIONAIS (MENSAGENS DE 500+ LETRAS) ---
else:
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        if estilo == "Profunda/Inspiradora":
            msg = f"{periodo}\n\nA vida não é uma corrida desenfreada contra o tempo, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é um mapa de uma batalha que você venceu em silêncio. Não se compare com o palco de ninguém enquanto você ainda está nos seus bastidores. O seu brilho é único e a sua essência é o que faz o mundo ser um lugar mais bonito de se viver. Valorize os pequenos passos, pois são eles que constroem os grandes destinos. Você é rara, preciosa e digna de tudo o que é bom. O seu momento de florescer é hoje! ✨\n\nCom carinho, LuhVee Stores ❤️"
        else:
            msg = f"{periodo}\n\nStatus do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre! 😂 Dizem que o dinheiro não traz felicidade, mas eu preferia chorar em Paris do que na fila do pão! A vida é curta demais para não comprar aquele achadinho que você amou. Lembre-se: boletos a gente paga, mas o brilho no olho de um produtinho novo chegando em casa não tem preço! Foca no objetivo e não esquece o café! Sorria, as rugas de preocupação saem caro para botocar depois! 💅\n\nCom carinho, LuhVee Stores ❤️"
        st.code(msg, language="text")
