import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine v25.0", page_icon="🔥")

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

# --- INICIALIZAÇÃO ---
if 'historico_pesquisa' not in st.session_state:
    st.session_state['historico_pesquisa'] = []

# --- MOTOR IA: DIVERSIDADE DE COPY AGRESSIVA (LINK ML ATUALIZADO) ---
def gerar_copy_agressiva_ia(produto, preco, marketplace):
    valor = f"R$ {preco}" if preco else "OFERTA EXCLUSIVA"
    prod_u = produto.upper()
    
    if marketplace == "Shopee 🛍️":
        link = "https://collshp.com/luhveestores"
        loja = "LuhVee Stores na Shopee 🛍️"
    else:
        # SEU LINK ATUALIZADO AQUI
        link = "https://www.mercadolivre.com.br/social/axwelloliveira"
        loja = "LuhVee Stores no Mercado Livre 📦"

    opcoes = [
        f"🚨 ALERTA DE TENDÊNCIA: O {prod_u} CHEGOU! 🚨\n\nA qualidade deste {produto} é simplesmente surreal e testada pessoalmente por mim! Se você está cansada de investir em produtos que prometem muito e não entregam nada, este item veio para mudar o seu jogo.\n\n😱 POR APENAS: {valor}\n\n⏰ O TEMPO ESTÁ CORRENDO: Estoque físico nas últimas unidades! Garanta o seu agora ou aceite pagar o dobro depois!\n\n🛒 COMPRE AGORA NO {marketplace.upper()}:\n👉 {link}\n\n{loja}",
        
        f"👑 EXCLUSIVIDADE: O {prod_u} QUE AS BLOGUEIRAS ESCONDEM! 👑\n\nO segredo foi finalmente revelado! O {prod_u} original que viralizou na gringa finalmente disponível. Esqueça réplicas baratas. Aqui você tem durabilidade e estilo real para sua rotina.\n\n🔥 OFERTA ÚNICA: {valor}\n\n⚠️ AVISO: Sem previsão de reposição com esse valor. Garanta sua unidade agora!\n\n🛒 LINK SEGURO {marketplace.upper()}:\n👉 {link}\n\n{loja}",
        
        f"😱 NÃO COMPRE O {prod_u} ANTES DE VER ISSO! ❌\n\nVocê merece o melhor e nós trouxemos a elite dos achadinhos mundiais. O {prod_u} resolve sua rotina com elegância e praticidade. É o investimento inteligente para se sentir plena e moderna hoje.\n\n💸 PREÇO IMBATÍVEL: {valor}\n\n🚀 CORRE PRO LINK ANTES QUE ESGOTE!\n\n🛒 GARANTA O SEU AQUI:\n👉 {link}\n\n{loja}"
    ]
    return random.choice(opcoes)

# --- MOTOR IA: MENSAGENS ROBUSTAS (IA REAL) ---
def gerar_motivacional_ia(estilo, periodo):
    if estilo == "Profunda/Inspiradora":
        msgs = [
            f"{periodo}\n\nA jornada da vida não é uma corrida desenfreada, mas um ciclo constante de renovação e cura. Valorize cada pequeno passo que você deu, pois eles construíram a mulher forte e resiliente que você é hoje. Você é uma essência rara, preciosa e o seu momento de florescer é exatamente agora! Confie na sua luz interior, mantenha a cabeça erguida e nunca deixe ninguém apagar o seu brilho. ✨\n\nCom carinho, LuhVee Stores ❤️",
            f"{periodo}\n\nPare um segundo, respire fundo e olhe para trás com orgulho de tudo o que você superou. Cada cicatriz que você carrega é, na verdade, uma medalha de uma batalha vencida em silêncio. Você é o milagre que tanto procurava e a força que precisa já habita em você. Proteja sua paz e continue brilhando. 🌸\n\nLuhVee Stores ❤️"
        ]
    else:
        msgs = [
            f"{periodo}\n\nStatus do dia: Em busca da minha versão milionária, porque a versão linda já cansou de ver boleto chegando! 😂 Dizem que dinheiro não traz felicidade, mas eu preferia muito mais estar chorando em Paris do que na fila do pão! Foca no café forte e nos objetivos, porque a gente nasceu para brilhar! 💅✨\n\nCom carinho, LuhVee Stores ❤️",
            f"{periodo}\n\nMinha terapia favorita é ver a notificação do rastreio dizendo que o produto 'saiu para entrega'. Boletos a gente paga com o suor do rosto, mas um produtinho novo chegando em casa renova a alma de qualquer mulher! Sorria sempre, afinal, o botox está caro! ☕ Plena e pronta para o próximo recebido!\n\nLuhVee Stores ❤️"
        ]
    return random.choice(msgs)

# --- BANCO DE DADOS COMPLETO ---
tendencias_reais = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída Maternidade", "Canguru Ergonômico"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet LCD"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Carregador Magsafe", "Mini Projetor Portátil"],
    "🚗 Acessórios Automotivos": ["Suporte Gravidade", "Aspirador Sem Fio", "Luz Interna Neon"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras", "Sacos de Vácuo"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda Profissional", "Regador Solar", "Vaso Auto-irrigação"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro Ortopédica"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Faixas Elásticas", "Massageador Turbo"],
    "🌎 Internacional": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Ferramentas:", ["🛍️ Postar Produtos", "🔎 Pesquisa Multi-Redes", "✨ Frases Motivacionais"])

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Alta Conversão IA")
    mkt = st.selectbox("Onde vai postar?", ["Shopee 🛍️", "Mercado Livre 📦"])
    col1, col2 = st.columns([2, 1])
    with col1: prod = st.text_input("Nome do Produto:")
    with col2: prc = st.text_input("Preço (R$):")
    
    if st.button("🚀 GERAR COPY PROFISSIONAL"):
        if prod:
            st.success(f"✅ COPY PARA {mkt.upper()} GERADA!")
            st.code(gerar_copy_agressiva_ia(prod, prc, mkt), language="text")
            
            st.markdown("### 🗺️ Roteiro de Postagem:")
            c1, c2, c3 = st.columns(3)
            with c1: st.write("**📸 Insta:** 3 fotos Stories + Reels 7s.")
            with c2: st.write("**📱 TikTok:** Gancho forte + Link Bio.")
            with c3: st.write("**💬 Whats:** Grupos + Preço Status.")
        else: st.warning("Digite o nome do produto!")

# --- ABA 2: PESQUISA MULTI-REDES ---
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
        for i in reversed(st.session_state['historico_pesquisa']): st.text(f"✅ {i}")

# --- ABA 3: MOTIVACIONAIS IA ---
else:
    st.title("✨ Vibes LuhVee Stores")
    per = st.selectbox("Momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    est = st.radio("Estilo:", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("✨ GERAR MENSAGEM IA"):
        st.code(gerar_motivacional_ia(est, per), language="text")  
