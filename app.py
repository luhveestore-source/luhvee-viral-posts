import streamlit as st
import random
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Gerador profissional de conteúdo para afiliados")

# ===== LINKS AFILIADOS =====
LINK_AFILIADO_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_AFILIADO_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# ===== BANCO DE FRASES =====
HOOKS = [
    "😳 mano, olha isso aqui",
    "🚨 ninguém tá falando disso",
    "🔥 isso aqui tá viralizando",
    "😱 eu não esperava isso",
    "💥 isso explodiu do nada",
]

CURIOSIDADE = [
    "eu achei que era besteira…",
    "não botei fé até testar…",
    "parecia inútil… mas olha isso",
    "vi muita gente falando e fui ver…",
]

BENEFICIOS = [
    "facilita MUITO o dia a dia",
    "economiza tempo de verdade",
    "resolve algo chato em segundos",
    "é muito mais útil do que parece",
]

URGENCIA = [
    "⚠️ isso aqui pode esgotar rápido",
    "🔥 tá vendendo muito hoje",
    "🚨 tendência forte agora",
]

CTA = [
    "👉 link na bio",
    "👉 pega antes que acabe",
    "👉 se eu fosse você, garantia agora",
]

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

# ===== GERAR COPIES =====
def gerar_copies(produto, preco, link):

    preco_formatado = formatar_preco(preco)
    copies = []

    for _ in range(5):
        hook = random.choice(HOOKS)
        curiosidade = random.choice(CURIOSIDADE)
        beneficio = random.choice(BENEFICIOS)
        urgencia = random.choice(URGENCIA)
        cta = random.choice(CTA)

        copy = f"""{hook}

{curiosidade}

🔥 {produto}

💡 {beneficio}

💰 só {preco_formatado}

👉 {link}

{urgencia}
{cta}
"""
        copies.append(copy)

    return copies

# ===== BOTÃO COPIAR =====
def copiar_box(texto, key):
    st.text_area("Copiar", texto, key=key)

# ===== INPUT =====
link = st.text_input("🔗 Cole o link do produto")

produto = ""
preco = ""

if st.button("🤖 PUXAR DADOS"):
    if link:
        produto, preco = extrair_dados(link)
        st.session_state.produto = produto
        st.session_state.preco = preco
        st.success("Dados carregados!")

produto = st.text_input("📦 Produto", value=st.session_state.get("produto", ""))
preco = st.text_input("💰 Preço", value=st.session_state.get("preco", ""))

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

        for nome, link_final in links:
            st.markdown(f"## 🔗 {nome}")

            copies = gerar_copies(produto, preco, link_final)

            for i, c in enumerate(copies):
                copiar_box(c, f"{nome}_{i}")