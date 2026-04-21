import streamlit as st
import random
import time
from PIL import Image, ImageDraw, ImageFont
import io

# --- CONFIGURAÇÃO VISUAL ---
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
    .stTextArea>div>div>textarea { background-color: #1a1a1a !important; color: #ff69b4 !important; border: 1px solid #ff69b4 !important; }
    </style>
""", unsafe_allow_html=True)

# --- LINKS ---
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- NICHOS ---
nichos_completos = {
    "✨ Beleza & Autoestima": ["Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro"],
    "🏠 Casa & Decoração": ["MOP Giratório Inox", "Luminária Pôr do Sol", "Projetor Astronauta"],
    "📱 Tecnologia & Gadgets": ["Fone Noise Cancelling", "Mini Projetor Portátil", "Smartwatch Ultra"]
}

# --- MOTOR DE GERAÇÃO DE IMAGEM PREMIUM COM MARCA D'ÁGUA ---
def criar_post_premium(nome_prod, preco, foto_file, logo_file):
    # Criar fundo (preto para contraste premium ou gradiente LuhVee)
    base = Image.new('RGB', (1080, 1350), color=(0, 0, 0))
    
    # Inserir Marca d'água (Logo transparente) de fundo
    if logo_file:
        # Abre o logo, converte para RGBA para garantir transparência
        logo = Image.open(logo_file).convert("RGBA")
        
        # Redimensiona o logo para ficar grande no fundo (ex: 80% da largura)
        bg_logo_width = int(1080 * 0.8)
        w_percent = (bg_logo_width / float(logo.size[0]))
        h_size = int((float(logo.size[1]) * float(w_percent)))
        logo_bg = logo.resize((bg_logo_width, h_size), Image.Resampling.LANCZOS)
        
        # Cria uma camada de transparência para a marca d'água (ex: 15% de opacidade)
        wm_layer = Image.new('RGBA', logo_bg.size, (0,0,0,0))
        wm_draw = ImageDraw.Draw(wm_layer)
        # Cola o logo na camada transparente
        wm_layer.paste(logo_bg, (0,0), logo_bg)
        
        # Define a opacidade (0-255). 40 é cerca de 15%
        wm_layer.putalpha(40)
        
        # Centraliza a marca d'água no fundo
        bg_wm_pos = ((1080 - logo_bg.size[0]) // 2, (1350 - logo_bg.size[1]) // 2)
        
        # Combina a marca d'água com o fundo preto
        base = base.convert("RGBA")
        base.paste(wm_layer, bg_wm_pos, wm_layer)
        base = base.convert("RGB") # Converte de volta para salvar

    draw = ImageDraw.Draw(base)

    # Inserir Foto do Produto (Centralizada)
    if foto_file:
        pimg = Image.open(foto_file).convert("RGBA")
        # Redimensionar mantendo proporção (ex: max 800px)
        pimg.thumbnail((800, 800), Image.Resampling.LANCZOS)
        # Centralizar
        p_pos = ((1080 - pimg.size[0]) // 2, (1350 - pimg.size[1]) // 2 - 100)
        base.paste(pimg, p_pos, pimg)

    # Inserir Texto: Nome do Produto (Superior, Branco)
    try: font_nome = ImageFont.truetype("arial.ttf", 60)
    except: font_nome = ImageFont.load_default()
    
    draw.text((540, 100), nome_prod.upper(), fill="white", font=font_nome, anchor="mm")

    # Inserir Retângulo de Preço (Inferior, Amarelo/LuhVee)
    draw.rounded_rectangle([240, 1100, 840, 1250], radius=50, fill=(255, 215, 0)) # Amarelo Ouro
    
    # Texto do Preço (Preto no retângulo amarelo)
    try: font_preco = ImageFont.truetype("arial.ttf", 100)
    except: font_preco = ImageFont.load_default()
    
    draw.text((540, 1175), f"R$ {preco}", fill="black", font=font_preco, anchor="mm")

    return base

# --- MOTOR MÁQUINA DE VENDAS (FORMATO INSANO INTEGRADO) ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace, rede):
    link_venda = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML
    preco_formatado = f"R$ {preco.replace('R$', '').strip()}"
    parcela_txt = f"\n💳 {parcelas}" if parcelas else ""

    hooks = [
        f"🚨 {produto.upper()} TÁ VIRALIZANDO AGORA",
        f"😳 COMO ISSO FICOU TÃO BARATO?",
        f"🔥 TODO MUNDO TÁ COMPRANDO ISSO",
        f"💥 ISSO AQUI EXPLODIU DO NADA",
        f"⚠️ VOCÊ PRECISA VER ISSO"
    ]
    dores = [
        "se você ainda não tem isso, tá perdendo tempo todo dia",
        "isso resolve algo que muita gente sofre sem perceber",
        "a maioria das pessoas ainda não descobriu isso"
    ]
    desejos = [
        "facilita sua rotina absurdamente",
        "deixa tudo mais prático e rápido",
        "você vai usar isso todo dia"
    ]
    provas = [
        "tá entre os mais vendidos",
        "todo mundo que compra recomenda",
        "explodiu nos vídeos essa semana"
    ]
    urgencias = [
        "⚠️ pode acabar a qualquer momento",
        "🔥 estoque limitado",
        "🚨 preço pode subir"
    ]
    ctas = [
        "👉 garante o seu agora",
        "👉 clica e aproveita",
        "👉 corre enquanto dá tempo"
    ]

    intensidades = ["leve", "medio", "agressivo"]
    copies = []

    for _ in range(5):
        nivel = random.choice(intensidades)
        if nivel == "leve":
            copy = f"""✨ NOVIDADE: {random.choice(hooks)}

🔥 {produto.upper()}
💡 {random.choice(desejos)}

💰 {preco_formatado}{parcela_txt}

👉 COMPRE AQUI:
{link_venda}
"""
        elif nivel == "medio":
            copy = f"""{random.choice(hooks)}

{random.choice(dores)}

🔥 {produto}
💡 {random.choice(desejos)}
😳 {random.choice(provas)}

💰 {preco_formatado}{parcela_txt}

👉 LINK SEGURO:
{link_venda}

{random.choice(urgencias)}
"""
        else:
            copy = f"""{random.choice(hooks)}

{random.choice(dores).upper()}

🔥 {produto.upper()}
💥 {random.choice(desejos).upper()}
😱 {random.choice(provas).upper()}

💰 {preco_formatado}{parcela_txt}

👉 GARANTA O SEU AGORA:
{link_venda}

{random.choice(urgencias)}
{random.choice(ctas)}
"""
        copies.append(copy)

    estrategias = {
        "Instagram 📸": "💡 STORY + CTA forte nos Stickers",
        "TikTok 📱": "💡 Use áudio trend + Legenda curta",
        "WhatsApp 💬": "💡 Envie no Status agora"
    }
    return copies, estrategias[rede]

# --- MENSAGENS ---
def gerar_mensagem_unica(periodo):
    return f"{periodo} 💖 Nunca desista!\n\n👉 {LINK_HUB}"

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Navegação:", ["🛍️ Postar Produtos", "🔎 Minerador", "💖 Mensagens"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Máquina de Vendas Premium")

    # Campos de Upload (Novos)
    st.subheader("1. Carregue as Imagens do Post")
    col_logo, col_foto = st.columns(2)
    with col_logo:
        logo_file = st.file_uploader("Sua Logo (PNG Transparente)", type=['png'])
    with col_foto:
        foto_file = st.file_uploader("Foto do Produto", type=['png', 'jpg', 'jpeg'])

    st.subheader("2. Detalhes da Venda")
    col1, col2 = st.columns(2)
    with col1:
        mkt = st.selectbox("Marketplace:", ["Shopee 🛍️", "Mercado Livre 📦"])
        rede_sel = st.selectbox("Rede:", ["Instagram 📸", "TikTok 📱", "WhatsApp 💬"])
    with col2:
        prod = st.text_input("Nome do Produto", placeholder="Ex: ESCOVA 3 EM 1")
        prc = st.text_input("Preço", placeholder="39.90")
        parc = st.text_input("Parcelamento", placeholder="Ex: 6x sem juros")

    if st.button("🚀 GERAR POST COMPLETO (IMAGEM + 5 COPYS)"):
        if prod and prc:
            random.seed(time.time())

            # 1. Gerar Imagem
            if foto_file:
                with st.spinner("Criando imagem premium com marca d'água..."):
                    pil_image = criar_post_premium(prod, prc, foto_file, logo_file)
                    st.image(pil_image, caption="Post Gerado para Redes Sociais", use_container_width=True)
                    
                    # Botão de Download da Imagem
                    buf = io.BytesIO()
                    pil_image.save(buf, format="PNG")
                    st.download_button("📥 BAIXAR FOTO DO POST", buf.getvalue(), file_name="post_luhvee.png", mime="image/png")
            else:
                st.warning("⚠️ Carregue a foto do produto para gerar a imagem.")

            # 2. Gerar Copys
            copies, dica = motor_maquina_vendas(prod, prc, parc, mkt, rede_sel)
            st.subheader("📋 Legendas Geradas (Copiou, Colou, Vendeu)")
            for i, c in enumerate(copies):
                st.text_area(f"Copy {i+1}", c, height=250)
            st.success(dica)

        else:
            st.warning("Preencha o Nome e o Preço para gerar.")

elif aba == "🔎 Minerador":
    st.title("🔎 Minerador de Produtos")
    nicho = st.selectbox("Nicho", list(nichos_completos.keys()))
    if st.button("📡 MINERAR"):
        st.success(random.choice(nichos_completos[nicho]))

else:
    st.title("💖 Mensagens")
    periodo = st.selectbox("Período", ["Bom dia", "Boa tarde", "Boa noite"])
    if st.button("✨ GERAR"):
        st.text_area("Mensagem", gerar_mensagem_unica(periodo), height=200)