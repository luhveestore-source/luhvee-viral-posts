import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v9.5", page_icon="🔥")

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

# --- FUNÇÃO DE MENSAGENS LONGAS (RESTAURADA TOTALMENTE) ---
def gerar_mensagem_luhvee_completa(tipo, periodo):
    if tipo == "Profunda/Inspiradora":
        ganchos = [
            "Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos e do que viemos fazer aqui nesta terra.",
            "Pare um segundo. Respire fundo. Olhe ao seu redor e perceba o quanto você já caminhou até este exato momento.",
            "O sucesso não é apenas sobre os números na conta, mas sobre a paz que você sente ao deitar a cabeça no travesseiro."
        ]
        reflexoes = [
            "A vida não é uma corrida desenfreada contra o tempo ou contra os outros, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é, na verdade, um mapa detalhado de uma batalha que você venceu em silêncio. Não se compare com o palco de ninguém enquanto você ainda está nos seus bastidores. O seu brilho é único, singular, e a sua essência é exatamente o que faz o mundo ser um lugar mais bonito de se viver. Valorize os pequenos passos, cada respiração, pois são eles que constroem os grandes destinos e as histórias que valem a pena ser contadas ao longo dos anos. Você é o milagre que tanto procurava.",
            "Muitas vezes depositamos a nossa felicidade no 'quando eu tiver' ou 'quando eu chegar lá'. Mas a verdade nua e crua é que a vida acontece agora, neste exato fôlego, nesta exata batida de coração. Ser uma mulher forte não significa não cansar ou nunca chorar, mas sim ter a sabedoria divina de descansar sem jamais desistir do que te faz vibrar. Você é o projeto mais importante e urgente da sua vida. Cuide-se com o mesmo amor e dedicação que você dedica aos outros, pois o seu coração é o seu templo mais sagrado e ele precisa de luz para continuar iluminando quem está ao seu redor."
        ]
        conclusoes = [
            "Que este momento seja o início de uma nova perspectiva na sua vida. Você é rara, preciosa e digna de tudo o que é bom.",
            "Lembre-se sempre: você é o milagre. Siga com fé, cabeça erguida e muita coragem. O mundo espera por você."
        ]
    else: # Engraçada/Vibes
        ganchos = [
            "Status do dia: Em busca da minha versão rica, porque a versão linda já cansou de ser pobre e carregar sacolas! 😂",
            "Acordei com uma vontade imensa de vencer na vida e conquistar o mundo, mas a vontade de voltar a dormir era um pouco maior.",
            "Se a vida te der limões, faça uma limonada, mas se ela te der um cartão sem limite, faça compras na LuhVee Stores!"
        ]
        reflexoes = [
            "Dizem por aí que o dinheiro não traz felicidade, mas eu sinceramente preferia muito mais estar chorando em Paris ou Maldivas do que chorar na fila do pão às seis da manhã, não é mesmo? A vida é curta demais para a gente não comprar aquele achadinho que amou de primeira vista. Se você está em dúvida entre o que é certo e o que te faz feliz, escolha o que te faz sorrir (e o que parcela no cartão em 12 vezes sem juros!). Lembre-se: boletos a gente paga com o suor do rosto, mas o brilho no olho de ver o rastreio dizendo 'saiu para entrega' não tem preço que pague nesta vida!",
            "Fui procurar o meu equilíbrio emocional hoje cedo e acabei encontrando um carrinho cheio de compras e um cupom de desconto. Minha terapia favorita é o barulho da notificação do banco dizendo que a compra foi aprovada. Ser adulta é basicamente viver esperando encomendas e fingir que sabemos exatamente o que estamos fazendo da vida enquanto tomamos um café gelado. Sorria sempre, gata! Afinal, as rugas de preocupação e estresse saem muito mais caro para botocar depois, então é melhor rir de tudo, manter a elegância e seguir plena para o próximo recebido!"
        ]
        conclusoes = [
            "Foca no objetivo, não esquece o café e mantém o brilho! Plena e pronta para o que der e vier!",
            "Seja o caos ou seja o brilho, mas seja você! Agora vai lá e arrasa porque os boletos não se pagam sozinhos!"
        ]

    return f"{periodo}\n\n{random.choice(ganchos)}\n\n{random.choice(reflexoes)}\n\n{random.choice(conclusoes)}\n\nCom todo carinho do mundo,\nLuhVee Stores ❤️"

# --- O RESTANTE DO CÓDIGO (MADEIRADA E PESQUISA) ---

tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade", "Almofada Amamentação", "Kit Saída Maternidade"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Elásticos", "Massageador Turbo"],
    "🌎 Internacional": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "📸 Instagram Trends IA", "✨ Frases Motivacionais"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Vendas")
    col1, col2 = st.columns([2, 1])
    with col1: produto = st.text_input("Nome do Produto:")
    with col2: preco = st.text_input("Preço (R$):")
    if st.button("🚀 GERAR COPY AGRESSIVA"):
        if produto:
            valor = f"R$ {preco}" if preco else "PREÇO ESPECIAL"
            copy = f"🚨 PARA TUDO! 🚨\n\nO {produto.upper()} chegou! Qualidade premium e estoque no fim! 🔥\n\n😱 Por APENAS: {valor}\n👉 https://collshp.com/luhveestores\n\nLuhVee Stores 🛍️"
            st.code(copy, language="text")
            st.session_state['historico_posts'].append(f"{produto} ({valor})")

elif aba == "🔎 Pesquisa Multi-Redes":
    st.title("🔎 Inteligência de Mercado")
    categoria = st.selectbox("Nicho:", list(tendencias_reais.keys()))
    if st.button("📡 VARREDURA"):
        sugestao = random.choice(tendencias_reais[categoria])
        rede = random.choice(["TikTok 📱", "Pinterest 📌", "Instagram 📸", "Facebook Ads 📢"])
        st.session_state['historico_pesquisa'].append(f"{sugestao} ({rede})")
        st.success(f"💡 {sugestao} em alta no {rede}!")
    if st.session_state['historico_pesquisa']:
        st.write("---")
        for item in reversed(st.session_state['historico_pesquisa']): st.text(f"✅ {item}")

elif aba == "📸 Instagram Trends IA":
    st.title("📸 Insights Instagram")
    if st.button("🔍 ANALISAR"): st.warning("🎯 Reels curtos com áudio viral hoje!")

elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee")
    periodo = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    estilo = st.radio("Estilo da Mensagem:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM COMPLETA"):
        msg = gerar_mensagem_luhvee_completa(estilo, periodo)
        st.code(msg, language="text")
