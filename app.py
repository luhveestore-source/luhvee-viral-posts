import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Gerador profissional por plataforma")

# ===== LINKS AFILIADOS =====
LINK_AFILIADO_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_AFILIADO_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# ===== FORMATAR PREÇO =====
def formatar_preco(preco):
    preco = preco.replace("R$", "").strip()
    return f"R$ {preco}"

# ===== SCRAPING =====
def extrair_dados(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        titulo = soup.title.string if soup.title else "Produto"

        preco = "??"
        for span in soup.find_all("span"):
            if "R$" in span.text:
                preco = span.text.strip()
                break

        return titulo[:80], preco

    except:
        return "Produto", "??"

# ===== GERAR LINKS =====
def gerar_links(plataformas):
    lista = []
    if "Shopee" in plataformas:
        lista.append(("Shopee", LINK_AFILIADO_SHOPEE))
    if "Mercado Livre" in plataformas:
        lista.append(("Mercado Livre", LINK_AFILIADO_ML))
    return lista

# ===== COPY POR PLATAFORMA =====
def gerar_copies_por_plataforma(produto, preco, link):

    preco_formatado = formatar_preco(preco)

    tiktok = f"""😳 mano olha isso

{produto}

💰 {preco_formatado}

👉 {link}

⚠️ isso aqui tá viralizando
"""

    instagram = f"""🔥 {produto}

💰 {preco_formatado}

👉 {link}

⚠️ pode acabar rápido

#achadinhos #promoção #oferta #viral #compras #desconto
"""

    whatsapp = f"""🚨 OLHA ISSO

{produto}

💰 {preco_formatado}

Achei muito barato hoje 😳

👉 {link}

Corre antes que acabe!
"""

    return {
        "TikTok": tiktok,
        "Instagram": instagram,
        "WhatsApp": whatsapp
    }

# ===== BOTÃO COPIAR =====
def copiar_box(texto, key):
    st.text_area("Copiar conteúdo", texto, key=key)

# ===== INPUT =====
link = st.text_input("🔗 Cole o link do produto")

if "produto" not in st.session_state:
    st.session_state.produto = ""

if "preco" not in st.session_state:
    st.session_state.preco = ""

if st.button("🤖 PUXAR DADOS"):
    if link:
        produto, preco = extrair_dados(link)
        st.session_state.produto = produto
        st.session_state.preco = preco
        st.success("Dados carregados!")

produto = st.text_input("📦 Produto", value=st.session_state.produto)
preco = st.text_input("💰 Preço", value=st.session_state.preco)

plataformas = st.multiselect(
    "🌍 Onde quer gerar link?",
    ["Shopee", "Mercado Livre"],
    default=["Mercado Livre"]
)

# ===== GERAR =====
if st.button("⚡ GERAR CONTEÚDO"):

    if not produto or not preco or not plataformas:
        st.warning("Preencha tudo!")
    else:
        links = gerar_links(plataformas)

        for nome_loja, link_final in links:

            st.markdown(f"## 🛒 {nome_loja}")

            copies = gerar_copies_por_plataforma(produto, preco, link_final)

            for plataforma_nome, texto in copies.items():
                st.markdown(f"### 📱 {plataforma_nome}")
                copiar_box(texto, f"{nome_loja}_{plataforma_nome}")