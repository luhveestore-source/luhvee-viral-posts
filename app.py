import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL PREMIUM ---
st.set_page_config(page_title="LuhVee GOD MODE v27.0", page_icon="👑", layout="wide")

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

st.title("👑 LuhVee Stores - Ferramenta de Elite")
st.subheader("Gerador de Copywriting Agressivo & Gestão de Estratégia")

# --- BANCO DE NICHOS COMPLETO ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Organizador Luxo", "Mini Selador Viral", "Luminária Pôr do Sol"],
    "👗 Moda & Acessórios": ["Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real"],
    "🤱 Moda Mamãe e Bebê": ["Bolsa Maternidade Térmica", "Almofada de Amamentação", "Kit Saída de Maternidade"],
    "💪 Produtos de Academia": ["Garrafa Motivacional", "Kit Elásticos", "Massageador Muscular Turbo"],
    "👔 Moda Masculina": ["Camisa Linho Premium", "Calça Jogger Tech", "Jaqueta Corta-Vento"],
    "🌎 Internacional (High Ticket)": ["ProDentim", "Suplemento BioFit", "Renovador Facial"]
}

# --- MENU LATERAL ---
aba = st.sidebar.radio("Selecione a Missão:", ["🛍️ Postar Produtos", "🔎 Minerador de Ouro", "✨ Vibes do Dia"])

# --- FUNÇÃO GERADORA DE TEXTO ROBUSTO ---
def gerar_copy_ia_elite(rede, produto, preco, marketplace, link):
    prod = produto.upper() if produto else "ITEM EXCLUSIVO"
    valor = f"R$ {preco}" if preco else "PREÇO DE OPORTUNIDADE"
    lk = link if link else "https://collshp.com/luhveestores"
    
    if rede == "TikTok/Reels":
        return (
            f"😱 PARE DE COMPRAR ERRADO! Você já viu esse {prod} por aí, mas só aqui na LuhVee você garante o original que realmente funciona! 🔥\n\n"
            f"Diferente de tudo que você já testou, esse modelo tem tecnologia premium e acabamento de luxo. Eu usei, testei e não vivo mais sem. "
            f"Sabe aquele item que resolve sua vida e ainda te deixa com cara de rica? É ESSE!\n\n"
            f"💎 DIFERENCIAIS:\n✅ Qualidade Superior (Não é réplica!)\n✅ Design Exclusivo Tendência 2026\n✅ Envio Imediato e Seguro\n\n"
            f"💸 INVESTIMENTO: {valor}\n"
            f"🔗 LINK NA BIO OU COMENTA 'EU QUERO'!\n\n"
            f"#achadinhos #viral #luhveestores #shopeebrasil #mercadolivre #beleza"
        )
    
    elif rede == "WhatsApp Grupos":
        return (
            f"🚨 *SÓ PARA QUEM É VIP!* O estoque do *{prod}* acaba de chegar e eu consegui uma condição de fábrica para vocês! 🚨\n\n"
            f"Meninas, esse é o produto que está bombando nas redes vizinhas. A qualidade é impecável e o resultado é imediato. "
            f"Não adianta procurar em outro lugar, esse preço com essa garantia você só encontra aqui na minha curadoria.\n\n"
            f"🔥 *POR QUE VOCÊ PRECISA DISSO AGORA?*\n"
            f"O fornecedor avisou que o lote é limitado. Quem boletar primeiro garante. Não quero ninguém chorando no meu direct depois porque perdeu!\n\n"
            f"💰 *APENAS:* {valor}\n"
            f"🛒 *LINK SEGURO ({marketplace.upper()}):*\n"
            f"👉 {lk}\n\n"
            f"LuhVee Stores 🛍️ - Só o que é luxo!"
        )

# --- CONTEÚDO DAS ABAS ---
if aba == "🛍️ Postar Produtos":
    st.write("### 🔥 Madeirada de Alta Conversão")
    mkt = st.selectbox("Qual o destino do link?", ["Shopee 🛍️", "Mercado Livre 📦"])
    
    col1, col2 = st.columns(2)
    with col1:
        produto_nome = st.text_input("Nome Profissional do Produto:", placeholder="Ex: Escova Alisadora 5 em 1 Titanium")
    with col2:
        preco_produto = st.text_input("Preço de Venda:", placeholder="Ex: 87,90")
    
    link_final = st.text_input("🔗 Cole o Link de Venda (ML ou Shopee):")

    if st.button("🚀 GERAR CAMPANHA COMPLETA"):
        if not produto_nome:
            st.error("Luh, coloque o nome do produto para a IA trabalhar!")
        else:
            st.balloons()
            st.markdown("<div class='copy-section'>", unsafe_allow_html=True)
            st.write("### 🎬 Para Reels / TikTok / Shorts")
            st.code(gerar_copy_ia_elite("TikTok/Reels", produto_nome, preco_produto, mkt, link_final), language="text")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='copy-section'>", unsafe_allow_html=True)
            st.write("### 💬 Para Grupos de WhatsApp / Telegram")
            st.code(gerar_copy_ia_elite("WhatsApp Grupos", produto_nome, preco_produto, mkt, link_final), language="text")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("### 🗺️ Roteiro de Stories (Conversão Rápida)")
            st.info("📌 **Passo 1:** Foto do produto com o gancho: 'O segredo da minha rotina chegou!'\n"
                    "📌 **Passo 2:** Vídeo curto (7s) mostrando o acabamento premium.\n"
                    "📌 **Passo 3:** Link com sticker chamativo: 'ÚLTIMAS UNIDADES NESSE PREÇO!'")

elif aba == "🔎 Minerador de Ouro":
    st.write("### 🔎 Inteligência de Mercado")
    escolha_nicho = st.selectbox("Selecione o Nicho:", list(nichos_completos.keys()))
    if st.button("📡 VARREDURA DE TENDÊNCIAS"):
        sugestao = random.choice(nichos_completos[escolha_nicho])
        st.success(f"💡 O produto **{sugestao}** está em fase de explosão no TikTok e Pinterest! Excelente para mineração hoje.")

else:
    st.write("### ✨ Vibes LuhVee Stores (300 Letras)")
    estilo = st.radio("Qual a vibe de hoje?", ["Profunda/Inspiradora", "Engraçada/Vibes"])
    if st.button("🪄 GERAR MENSAGEM PARA STATUS"):
        if estilo == "Profunda/Inspiradora":
            msg = ("A vida não é uma corrida contra o tempo, mas uma jornada sagrada de cura e redescoberta. "
                   "Cada cicatriz que você carrega é um mapa de uma batalha vencida em silêncio. Valorize seus passos, "
                   "pois são eles que constroem o seu destino extraordinário. Você é rara, preciosa e o milagre que "
                   "tanto procurava já habita em você. Floresça no seu tempo! ✨❤️")
        else:
            msg = ("Status do dia: Em busca da minha versão milionária, porque a linda já cansou de boletos! 😂 "
                   "Dizem que dinheiro não traz felicidade, mas eu preferia muito mais chorar em Paris do que na "
                   "fila do mercado às seis da manhã. Foca no café, no brilho e nos objetivos, porque a gente nasceu "
                   "para o luxo e os sonhos não se pagam sozinhos! 💅✨")
        st.code(msg, language="text")
