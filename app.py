import streamlit as st
import random
import time
import io
import textwrap

# Importação crucial para as imagens:
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    st.error("Erro: A biblioteca Pillow não foi encontrada. Rode 'pip install Pillow' no seu terminal.")

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
    .stTextArea>div>div>textarea { background-color: #1a1a1a !important; color: #ff69b4 !important; border: 1px solid #ff69b4 !important; }
    </style>
""", unsafe_allow_html=True)

# --- LINKS ---
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- MOTOR DE GERAÇÃO DE IMAGEM COM VISIBILIDADE MAXIMIZADA ---
def criar_post_elite(nome_prod, preco, foto_file, logo_file):
    # Base Premium (Fundo Preto com Marca D'água Sutil)
    base = Image.new('RGB', (1080, 1920), color=(0, 0, 0))
    
    # Inserir Marca d'água no fundo
    if logo_file:
        try:
            logo = Image.open(logo_file).convert("RGBA")
            bg_logo_width = int(1080 * 0.9)
            w_percent = (bg_logo_width / float(logo.size[0]))
            h_size = int((float(logo.size[1]) * float(w_percent)))
            logo_bg = logo.resize((bg_logo_width, h_size), Image.Resampling.LANCZOS)
            
            # Criar camada para marca d'água com baixa opacidade
            wm_layer = Image.new('RGBA', (1080, 1920), (0,0,0,0))
            wm_position = ((1080 - logo_bg.size[0]) // 2, (1920 - logo_bg.size[1]) // 2)
            wm_layer.paste(logo_bg, wm_position, logo_bg)
            
            # Opacidade sutil (10%)
            alpha = wm_layer.split()[3]
            alpha = alpha.point(lambda p: p * 0.1) 
            wm_layer.putalpha(alpha)
            
            base = Image.alpha_composite(base.convert("RGBA"), wm_layer).convert("RGB")
        except: pass

    draw = ImageDraw.Draw(base)

    # Inserir Foto do Produto (ZONA CENTRAL, MAXIMIZADA)
    if foto_file:
        try:
            pimg = Image.open(foto_file).convert("RGBA")
            pimg.thumbnail((1000, 1200), Image.Resampling.LANCZOS)
            p_pos = ((1080 - pimg.size[0]) // 2, (1920 - pimg.size[1]) // 2 - 100)
            base.paste(pimg, p_pos, pimg)
        except: pass

    # --- TEXTOS GIGANTES (VISIBILIDADE TOTAL) ---
    # Usar uma fonte padrão boa, mas tentar Arial Bold se tiver
    try: font_gigante_bold = ImageFont.truetype("arialbd.ttf", 150)
    except: font_gigante_bold = ImageFont.load_default()
    
    try: font_gigante = ImageFont.truetype("arial.ttf", 120)
    except: font_gigante = ImageFont.load_default()

    # Preço Rosa Neon (Super Destaque na base)
    preco_txt = f"R$ {preco}"
    # Sombra para efeito neon
    draw.text((545, 1725), preco_txt, fill=(255, 20, 147), font=font_gigante_bold, anchor="mm") # Rosa Escuro
    draw.text((540, 1720), preco_txt, fill=(255, 105, 180), font=font_gigante_bold, anchor="mm") # Rosa LuhVee

    # Nome do Produto (GIGANTE, no topo)
    nome_prod_up = nome_prod.upper()
    wrapped_nome = textwrap.fill(nome_prod_up, width=15) # Wrap automático se for longo
    y_nome = 200
    for line in wrapped_nome.split('\n'):
        draw.text((540, y_nome), line, fill="white", font=font_gigante_bold, anchor="mm")
        y_nome += 160

    # --- STICKER "LINK NA BIO" GIGANTE (Topo Direito, Rosa Neon) ---
    stk_width, stk_height = 500, 180
    stk_pos = (550, 50) # Canto superior direito
    
    # Retângulo Neon com Sombra
    draw.rounded_rectangle([stk_pos[0]+5, stk_pos[1]+5, stk_pos[0]+stk_width+5, stk_pos[1]+stk_height+5], radius=40, fill=(139, 0, 139)) # Sombra Roxo
    draw.rounded_rectangle([stk_pos[0], stk_pos[1], stk_pos[0]+stk_width, stk_pos[1]+stk_height], radius=40, fill=(255, 20, 147)) # Rosa Neon

    # Texto LINK NA BIO Gigante
    try: font_sticker = ImageFont.truetype("arialbd.ttf", 80)
    except: font_sticker = ImageFont.load_default()
    
    # Texto Branco com Sombra Rosa
    draw.text((stk_pos[0] + stk_width//2 + 3, stk_pos[1] + stk_height//2 + 3), "LINK NA BIO 🔗", fill=(255, 215, 0), font=font_sticker, anchor="mm")
    draw.text((stk_pos[0] + stk_width//2, stk_pos[1] + stk_height//2), "LINK NA BIO 🔗", fill="white", font=font_sticker, anchor="mm")

    return base

# --- MOTOR MÁQUINA DE VENDAS ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace, rede):
    link_venda = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML
    preco_formatado = f"R$ {preco}"
    parc = f"\n💳 {parcelas}" if parcelas else ""

    hooks = [f"🚨 {produto.upper()} TÁ VIRALIZANDO!", f"🔥 O QUERIDINHO CHEGOU!", f"⚠️ CORRE ANTES QUE ACABE!"]
    desejos = ["qualidade surreal!", "design premium!", "praticidade total!"]
    
    copies = []
    for _ in range(3): # Menos copies, mas mais agressivas
        copy = f"""{random.choice(hooks)}

{produto.upper()} 🔥
💡 {random.choice(desejos)}

😱 APENAS: {preco_formatado}{parc}

🏃‍♀️ GARANTA NO LINK NA BIO OU NOS STORIES!
LuhVee Stores ❤️🛍️

👇 LINK DIRETO:
{link_venda}
"""
        copies.append(copy)

    return copies

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Navegação:", ["🛍️ Postar Produtos", "🔎 Minerador", "💖 Mensagens"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Madeirada Curta & Lucrativa")

    st.subheader("1. Imagens (Marca d'água + Produto)")
    c_logo, c_foto = st.columns(2)
    with c_logo: logo_up = st.file_uploader("Sua Logo (PNG)", type=['png'])
    with c_foto: foto_up = st.file_uploader("Foto do Produto", type=['png', 'jpg', 'jpeg'])

    st.subheader("2. Detalhes")
    col1, col2 = st.columns(2)
    with col1:
        mkt = st.selectbox("Marketplace:", ["Shopee 🛍️", "Mercado Livre 📦"])
        rede = st.selectbox("Rede:", ["Instagram 📸", "TikTok 📱", "WhatsApp 💬"])
    with col2:
        prod = st.text_input("Nome do Produto", placeholder="Ex: Bota Adventure")
        prc = st.text_input("Preço", placeholder="Ex: 213,66")
        parc = st.text_input("Parcelas", placeholder="Ex: Ou 12x s/ juros")

    if st.button("🚀 GERAR POST AGRESSIVA"):
        if prod and prc and foto_up:
            random.seed(time.time())
            
            # Imagem
            with st.spinner("Criando banner de visibilidade total..."):
                img_final = criar_post_elite(prod, prc, foto_up, logo_up)
                st.image(img_final, caption="Banner Premium LuhVee Stores", use_container_width=True)
                
                buf = io.BytesIO()
                img_final.save(buf, format="PNG")
                st.download_button("📥 BAIXAR BANNER AGORA", buf.getvalue(), "post_luhvee.png", "image/png")

            # Copys
            cps = motor_maquina_vendas(prod, prc, parc, mkt, rede)
            st.subheader("📋 Legendas Agressivas (LINK NA BIO)")
            for i, c in enumerate(cps):
                st.text_area(f"Legenda {i+1}", c, height=220)
        else:
            st.warning("Luh! FOTO, NOME e PREÇO são obrigatórios!")

elif aba == "🔎 Minerador":
    st.title("🔎 Minerador Profissional")
    if st.button("📡 MINERAR"):
        st.success(f"Sugestão Viral: {random.choice(['Sérum Glow', 'Mop Spray Inox', 'Relógio Luxury Rose'])}")

else:
    st.title("💖 Mensagens LuhVee")
    if st.button("✨ GERAR VIBE"):
        st.text_area("Vibe", f"Ei! 💖 Nunca desista dos seus sonhos.\n\n👉 {LINK_HUB}", height=150)