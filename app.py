import streamlit as st
import random
import time

# --- CONFIGURAÇÃO VISUAL PREMIUM (BLACK & PINK) ---
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
    .copy-section { background-color: #111; border: 1px solid #333; padding: 25px; border-radius: 15px; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS GIGANTE DE NICHOS ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", "Kit de Pincéis Profissional", "Máscara de LED Facial", "Removedor de Cravos a Vácuo", "Organizador de Maquiagem Giratório"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol", "Projetor Astronauta", "Fita LED RGB Inteligente", "Umidificador de Ar Retrô", "Aspirador Robô Inteligente"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro", "Óculos de Sol Luxury", "Relógio Feminino Rose Gold", "Cinto Corrente Trend"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída Maternidade", "Canguru Ergonômico", "Aquecedor de Mamadeira USB", "Monitor de Bebê Wi-Fi", "Tapete de Atividades"],
    "🧸 Infantil & Brinquedos": ["Cacto Dançante", "Mini Câmera Digital", "Tablet LCD para Desenho", "Escavadeira de Controle", "Kit de Miçangas DIY", "Lousa Mágica ColorColorida", "Mini Drone Sensor"],
    "🐶 Mundo Pet": ["Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica", "Brinquedo Interativo com Petiscos", "Coleira com LED", "Lançador de Bolinhas", "Rede para Gatos de Janela"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Carregador Magsafe", "Mini Projetor Portátil", "Smartwatch Ultra Series", "Teclado Mecânico RGB", "Suporte Articulado para Monitor", "Power Bank Indução"],
    "🚗 Acessórios Automotivos": ["Suporte Celular Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon App", "Polidor de Farol", "Câmera de Ré Visão Noturna", "Organizador de Banco Couro"],
    "🗄️ Organização & Limpeza": ["Etiquetadora Bluetooth", "Caixas Organizadoras Empilháveis", "Sacos de Vácuo para Roupas", "Mini Aspirador de Mesa", "Suporte de Vassouras Adesivo", "Dispenser de Sabão Automático"],
    "🌿 Ferramentas & Jardinagem": ["Kit de Poda Profissional", "Regador Automático Solar", "Vaso de Auto-irrigação", "Parafusadeira Viral sem Fio", "Lanterna Tática Militar", "Kit de Ferramentas Rosa"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento Refletiva", "Kit Meias Performance", "Carteira Slim Antifurto", "Pulseira de Couro Masculina"],
    "👟 Calçados Masculinos": ["Tênis Nuvem Confort", "Sapato Social Flex", "Sandália de Couro Ortopédica", "Bota Adventure Impermeável", "Tênis de Academia Knit"],
    "💪 Produtos de Academia": ["Garrafa de Água Motivacional", "Kit de Faixas Elásticas", "Massageador Muscular Turbo", "Corda de Pular Digital", "Tapete de Yoga Antiderrapante", "Rolo de Liberação Miofascial"],
    "🌎 Internacional (High Ticket)": ["ProDentim Original", "Suplemento BioFit", "Renovador Facial 24k", "Redutor de Medidas Viral", "Sérum Anti-Idade Suíço"]
}

# --- MOTOR DE INTELIGÊNCIA ARTIFICIAL ---
def motor_ia_avancado(tipo, produto=None, preco=None, marketplace=None):
    if tipo == "Venda":
        ganchos = [
            f"🚨 ALERTA DE TENDÊNCIA: O {produto} CHEGOU PARA MUDAR TUDO! 🚨",
            f"🔥 O SEGREDO FOI REVELADO! Você não pode ficar sem esse {produto}! 🔥",
            f"😱 PARE TUDO! Se você estava esperando um sinal para ter seu {produto}, é esse!",
            f"💎 EXCLUSIVIDADE: O {produto} que viralizou na gringa finalmente disponível!",
            f"👑 STATUS E LUXO: O {produto} que as blogueiras não te mostram por onde compram!",
            f"⚠️ ÚLTIMO AVISO: O estoque do {produto} está zerando agora em todo o Brasil!",
            f"🌟 TRANSFORMAÇÃO: Como o {produto} vai facilitar sua rotina hoje mesmo!",
            f"🤫 O QUE NINGUÉM TE CONTA: Por que o {produto} é o melhor investimento do ano?"
        ]
        corpos = [
            "A qualidade é simplesmente surreal e foi testada pessoalmente por mim. Esqueça as réplicas que só trazem decepção. Aqui o acabamento é premium e a durabilidade é garantida.",
            "Sabe aquele item que resolve sua vida de forma inteligente e ainda te deixa com cara de rica? É exatamente esse! Elegância e praticidade em um só lugar.",
            "O design exclusivo e a performance desse produto fazem dele o desejo número 1 de todas as redes sociais. Você merece o melhor e nós trouxemos a elite para você.",
            "Tecnologia de ponta aliada a um custo-benefício que parece erro de sistema. Eu usei, aprovei e garanto: o resultado é imediato e vai transformar sua rotina.",
            "Não é apenas mais um produto no seu carrinho, é um investimento na sua autoestima e no seu bem-estar. Sinta a diferença de ter algo realmente original."
        ]
        chamadas = [
            "Estoque físico nas últimas unidades! Garanta o seu agora ou aceite pagar o dobro depois.",
            "⚠️ AVISO IMPORTANTE: Sem previsão de reposição com esse valor promocional!",
            "🚀 CORRE PRO LINK! A demanda está surreal e o botão vai sair do ar a qualquer segundo!",
            "Clique no link seguro abaixo e faça parte do grupo seleto que já garantiu essa maravilha!"
        ]

        if marketplace == "Shopee 🛍️":
            link = "https://collshp.com/luhveestores?view=storefront"
            loja = "LuhVee Stores na Shopee 🛍️"
        else:
            link = "https://www.mercadolivre.com.br/social/axwelloliveira"
            loja = "LuhVee Stores no Mercado Livre 📦"
        
        return f"{random.choice(ganchos)}\n\n{random.choice(corpos)}\n\n💎 DIFERENCIAIS:\n✅ Qualidade Premium Testada\n✅ Envio Imediato e Seguro\n✅ Garantia Total LuhVee\n\n😱 POR APENAS: R$ {preco}\n\n{random.choice(chamadas)}\n\n🛒 LINK SEGURO NO {marketplace.upper()}:\n👉 {link}\n\n{loja}"

    elif tipo == "Vibes":
        vibes_corpo = [
            "A jornada da vida não é uma corrida contra o tempo, mas um ciclo constante de renovação. Valorize cada pequeno passo, pois são eles que constroem seu destino extraordinário.",
            "Status do dia: Em busca da minha versão milionária, porque a versão linda já cansou de carregar boletos no lombo! 😂 A gente nasceu para o luxo, o resto é detalhe.",
            "Respire fundo. Cada cicatriz que você carrega é uma vitória silenciosa que te trouxe até aqui. Você é rara, preciosa e o milagre que tanto procurava.",
            "Minha terapia favorita é ver a notificação do rastreio dizendo que o produto 'saiu para entrega'. Renova a alma e melhora o humor na hora! ☕🛍️",
            "Não deixe ninguém apagar o seu brilho hoje. O sol nasce com força total para quem cultiva a luz interior e não desiste dos seus sonhos.",
            "Dizem que dinheiro não traz felicidade, mas eu preferia muito mais estar chorando em um resort em Paris do que na fila do mercado às 6 da manhã, né gata?",
            "Foca no café forte, no brilho nos olhos e nos seus objetivos. Os seus sonhos são grandes demais para você parar agora. O topo é o seu lugar!",
            "Sorria sempre, afinal, o botox está caro e rir de tudo ainda é o melhor tratamento de beleza gratuito e eficaz que existe no mundo! 💅"
        ]
        fechamento_vibe = [
            "Confira meu Hub Central de Ofertas:",
            "Dê um up na sua rotina com o que tem de melhor no meu Hub:",
            "O link da sua transformação está no meu Hub Central:",
            "Acesse todas as minhas vitrines e novidades aqui no Hub:"
        ]
        hub_principal = "https://links-luhveestore.streamlit.app/"
        return f"{random.choice(vibes_corpo)}\n\n✨ {random.choice(fechamento_vibe)}\n👉 {hub_principal}\n\nCom carinho, LuhVee Stores ❤️"

# --- MENU LATERAL ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Selecione a Missão:", ["🛍️ Postar Produtos", "🔎 Minerador de Ouro", "✨ Vibes do Dia (IA)"])

# --- ABA 1: POSTAR PRODUTOS ---
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada de Conversão Milionária")
    mkt_sel = st.selectbox("Qual o Marketplace de hoje?", ["Shopee 🛍️", "Mercado Livre 📦"])
    col1, col2 = st.columns(2)
    with col1: prod_nome = st.text_input("📦 Nome do Produto:", placeholder="Ex: Escova 5 em 1 Titanium")
    with col2: prod_preco = st.text_input("💰 Preço de Venda:", placeholder="Ex: 89,90")
    
    if st.button("🚀 GERAR COPY INFINITA"):
        if prod_nome:
            random.seed(time.time())
            texto_gerado = motor_ia_avancado("Venda", produto=prod_nome, preco=prod_preco, marketplace=mkt_sel)
            st.code(texto_gerado, language="text")
            st.markdown("### 🗺️ Roteiro de Postagem:")
            st.info("📸 Insta: Stories + Reels | 📱 TikTok: Gancho 3s | 💬 Whats: Grupos")
        else: st.warning("Luh, digite o nome do produto!")

# --- ABA 2: MINERADOR DE OURO ---
elif aba == "🔎 Minerador de Ouro":
    st.title("🔎 Caçador de Tendências Pro")
    nicho_sel = st.selectbox("Escolha o Nicho:", list(nichos_completos.keys()))
    if st.button("📡 INICIAR VARREDURA"):
        produto_escolhido = random.choice(nichos_completos[nicho_sel])
        st.markdown(f"<div style='background-color: #111; padding: 20px; border-radius: 10px; border: 1px solid #ff69b4;'><h2 style='color: #ff69b4;'>💎 Produto Encontrado:</h2><p style='color: white; font-size: 24px;'>{produto_escolhido}</p></div>", unsafe_allow_html=True)

# --- ABA 3: FRASES MOTIVACIONAIS ---
else:
    st.title("✨ Vibes LuhVee Stores (Corpo da Mensagem)")
    st.write("Gere o corpo da mensagem abaixo e adicione sua saudação (Bom dia, etc) manualmente ao postar!")
    
    if st.button("🪄 GERAR CORPO DA MENSAGEM (IA)"):
        random.seed(time.time())
        mensagem_ia = motor_ia_avancado("Vibes")
        st.code(mensagem_ia, language="text")
        st.balloons()
