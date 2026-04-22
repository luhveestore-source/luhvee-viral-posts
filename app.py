import streamlit as st
import random
import io
from PIL import Image, ImageDraw, ImageFont

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="👑 LuhVee TURBO - Vendas Agressivas", layout="wide")

# Links Fixos
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# --- FUNÇÕES DE APOIO ---

def formatar_preco(valor):
    # Garante que o preço tenha o formato R$ XX,XX
    valor = valor.replace('R$', '').strip().replace(',', '.')
    try:
        f_valor = float(valor)
        return f"R$ {f_valor:,.2f}".replace('.', 'v').replace(',', '.').replace('v', ',')
    except:
        return f"R$ {valor}"

def criar_post_visual(produto, preco, foto_upload):
    # Criar uma imagem vertical (Story/Reels) 1080x1920
    # Usamos um degradê ou cor sólida moderna
    largura, altura = 1080, 1920
    canvas = Image.new("RGB", (largura, altura), (15, 15, 15)) # Fundo Dark elegante
    draw = ImageDraw.Draw(canvas)

    # Carregar imagem do produto
    img_produto = Image.open(foto_upload).convert("RGBA")
    
    # Redimensionamento Proporcional (Sem distorção)
    max_size = 900
    ratio = min(max_size / img_produto.width, max_size / img_produto.height)
    novo_tamanho = (int(img_produto.width * ratio), int(img_produto.height * ratio))
    img_produto = img_produto.resize(novo_tamanho, Image.LANCZOS)

    # Centralizar imagem
    pos_x = (largura - img_produto.width) // 2
    pos_y = (altura - img_produto.height) // 2
    canvas.paste(img_produto, (pos_x, pos_y), img_produto)

    # Adicionar Textos (Usando fontes padrão se não houver .ttf)
    try:
        font_titulo = ImageFont.truetype("arial.ttf", 80)
        font_preco = ImageFont.truetype("arial.ttf", 150)
    except:
        font_titulo = ImageFont.load_default()
        font_preco = ImageFont.load_default()

    # Desenhar faixas de destaque
    draw.rectangle([0, 150, largura, 350], fill=(255, 20, 147)) # Rosa Choque
    draw.text((largura//2, 250), produto.upper(), fill="white", anchor="mm", font=font_titulo)
    
    draw.text((largura//2, 1700), formatar_preco(preco), fill=(255, 215, 0), anchor="mm", font=font_preco) # Dourado

    return canvas

def gerar_copy_agressiva(produto, preco, plataforma):
    link = LINK_SHOPEE if plataforma == "Shopee" else LINK_ML
    
    hooks = [
        f"🚨 ALERTA DE OPORTUNIDADE: {produto}!",
        f"🔥 O {produto} que todo mundo está procurando chegou!",
        f"⚠️ PARE TUDO! Olha esse preço no {produto}!",
        f"😱 Ninguém acredita no preço desse {produto}..."
    ]
    
    gatilhos = [
        "Estoque renovado, mas voando! 💸",
        "Últimas unidades com esse valor promocional. ⏳",
        "Qualidade premium que você já conhece. ⭐",
        "Frete rápido e compra garantida! 🚚"
    ]
    
    chamada = [
        "Clica no link e garante o seu antes que mude o preço!",
        "Não adianta chorar depois que esgotar! 🏃‍♂️💨",
        "Aproveite a promoção exclusiva de hoje!"
    ]

    copy = f"""{random.choice(hooks)}

{random.choice(gatilhos)}

🛍️ {produto}
💰 Por apenas: {formatar_preco(preco)}

🔥 COMPRE AGORA:
{link}

🔗 Veja mais no nosso catálogo:
{LINK_HUB}

#promoção #ofertadiaria #shopee #mercadolivre #luhvee
"""
    return copy

# --- INTERFACE STREAMLIT ---

st.sidebar.header("👑 PAINEL DE CONTROLE")
menu = st.sidebar.selectbox("O que vamos fazer?", ["Gerador de Post", "Histórico"])

if menu == "Gerador de Post":
    st.title("🚀 Gerador de Vendas Agressivas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome_prod = st.text_input("Nome do Produto", placeholder="Ex: Smartwatch Ultra")
        valor_prod = st.text_input("Preço", placeholder="Ex: 149,90")
        mkt_target = st.radio("Destino", ["Shopee", "Mercado Livre"])
        imagem_arq = st.file_uploader("Foto do Produto", type=["png", "jpg", "jpeg"])

    if st.button("🔥 GERAR POST AGORA"):
        if nome_prod and valor_prod and imagem_arq:
            # Gerar Conteúdo
            img_final = criar_post_visual(nome_prod, valor_prod, imagem_arq)
            texto_copy = gerar_copy_agressiva(nome_prod, valor_prod, mkt_target)
            
            # Mostrar Resultado
            st.image(img_final, caption="Preview do Post (Formato Story)", width=400)
            st.text_area("Copy para Copiar:", texto_copy, height=250)
            
            # Botão de Download
            buf = io.BytesIO()
            img_final.save(buf, format="PNG")
            st.download_button("📥 Baixar Imagem", buf.getvalue(), file_name="post_luhvee.png")
            
            # Salvar no Histórico
            if "historico_v2" not in st.session_state:
                st.session_state.historico_v2 = []
            st.session_state.historico_v2.append(texto_copy)
        else:
            st.error("Preencha todos os campos e suba uma foto!")

elif menu == "Histórico":
    st.title("📜 Últimas Copys Geradas")
    if "historico_v2" in st.session_state:
        for c in reversed(st.session_state.historico_v2):
            st.code(c)
            st.write("---")
    else:
        st.info("Nenhuma postagem gerada ainda.")
