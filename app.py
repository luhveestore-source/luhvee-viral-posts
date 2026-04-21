import streamlit as st
import random
import time
import io
# Importação crucial para as imagens:
try:
    from PIL import Image, ImageDraw, ImageFont
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

# --- MOTOR DE GERAÇÃO DE IMAGEM COM MARCA D'ÁGUA ---
def criar_post_premium(nome_prod, preco, foto_file, logo_file):
    base = Image.new('RGB', (1080, 1350), color=(0, 0, 0))
    
    if logo_file:
        logo = Image.open(logo_file).convert("RGBA")
        bg_logo_width = int(1080 * 0.7)
        w_percent = (bg_logo_width / float(logo.size[0]))
        h_size = int((float(logo.size[1]) * float(w_percent)))
        logo_bg = logo.resize((bg_logo_width, h_size), Image.Resampling.LANCZOS)
        
        wm_layer = Image.new('RGBA', (1080, 1350), (0,0,0,0))
        bg_wm_pos = ((1080 - logo_bg.size[0]) // 2, (1350 - logo_bg.size[1]) // 2)
        wm_layer.paste(logo_bg, bg_wm_pos, logo_bg)
        
        # Opacidade da marca d'água no fundo
        alpha = wm_layer.split()[3]
        alpha = alpha.point(lambda p: p * 0.15) # 15% de visibilidade
        wm_layer.putalpha(alpha)
        
        base = Image.alpha_composite(base.convert("RGBA"), wm_layer).convert("RGB")

    draw = ImageDraw.Draw(base)

    if foto_file:
        pimg = Image.open(foto_file).convert("RGBA")
        pimg.thumbnail((850, 850), Image.Resampling.LANCZOS)
        p_pos = ((1080 - pimg.size[0]) // 2, (1350 - pimg.size[1]) // 2 - 50)
        base.paste(pimg, p_pos, pimg)

    try: font_nome = ImageFont.truetype("arial.ttf", 65)
    except: font_nome = ImageFont.load_default()
    
    draw.text((540, 120), nome_prod.upper(), fill="white", font=font_nome, anchor="mm")
    
    # Retângulo do Preço Estilo Premium
    draw.rounded_rectangle([200, 1120, 880, 1260], radius=60, fill=(255, 105, 180)) # Rosa LuhVee
    
    try: font_preco = ImageFont.truetype("arial.ttf", 90)
    except: font_preco = ImageFont.load_default()
    
    draw.text((540, 1190), f"R$ {preco}", fill="white", font=font_preco, anchor="mm")

    return base

# --- MOTOR MÁQUINA DE VENDAS (FORMATO INSANO) ---
def motor_maquina_vendas(produto, preco, parcelas, marketplace, rede):
    link_venda = LINK_SHOPEE if marketplace == "Shopee 🛍️" else LINK_ML
    preco_formatado = f"R$ {preco}"
    parc = f"\n💳 {parcelas}" if parcelas else ""

    hooks = [f"🚨 {produto.upper()} TÁ VIRALIZANDO!", f"🔥 TODO MUNDO QUER ISSO!", f"⚠️ ÚLTIMA CHANCE!"]
    desejos = ["facilita sua vida!", "praticidade que você merece!", "resultado garantido!"]
    
    copies = []
    for _ in range(5):
        copy = f"""{random.choice(hooks)}

{produto.upper()} 🔥

💡 {random.choice(desejos)}

💰 {preco_formatado}{parc}

👉 GARANTA NO LINK:
{link_venda}

Bjs da LuhVee Stores 🛍️"""
        copies.append(copy)

    return copies

# --- INTERFACE ---
st.sidebar.title("👑 Comando LuhVee ELITE")
aba = st.sidebar.radio("Navegação:", ["🛍️ Postar Produtos", "🔎 Minerador", "💖 Mensagens"])

if aba == "🛍️ Postar Produtos":
    st.title("🔥 Máquina de Vendas Premium")

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
        prod = st.text_input("Nome do Produto")
        prc = st.text_input("Preço")
        parc = st.text_input("Parcelas")

    if st.button("🚀 GERAR POST COMPLETO"):
        if prod and prc and foto_up:
            random.seed(time.time())
            # Imagem
            img_final = criar_post_premium(prod, prc, foto_up, logo_up)
            st.image(img_final, use_container_width=True)
            
            buf = io.BytesIO()
            img_final.save(buf, format="PNG")
            st.download_button("📥 BAIXAR BANNER", buf.getvalue(), "post.png", "image/png")

            # Copys
            cps = motor_maquina_vendas(prod, prc, parc, mkt, rede)
            for i, c in enumerate(cps):
                st.text_area(f"Legenda {i+1}", c, height=200)
        else:
            st.warning("Carregue a FOTO, o NOME e o PREÇO!")

elif aba == "🔎 Minerador":
    st.title("🔎 Minerador")
    if st.button("📡 MINERAR"):
        st.success(f"Sugestão: {random.choice(['Sérum Glow', 'Mop Inox', 'Escova 3 em 1'])}")

else:
    st.title("💖 Mensagens")
    if st.button("✨ GERAR"):
        st.text_area("Vibe", f"Bom dia! 💖\n\n👉 {LINK_HUB}", height=150)