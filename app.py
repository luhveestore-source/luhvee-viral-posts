import streamlit as st
import random
import requests
from bs4 import BeautifulSoup
import time

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee AI Vendas PRO", layout="wide")

# CSS para deixar o App com cara de software caro
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .stButton>button { background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%); color: white; border: none; font-weight: bold; height: 50px; font-size: 18px; }
    .copy-box { background-color: #1a1a1a; padding: 20px; border-left: 5px solid #ff4b2b; border-radius: 10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- ENGINE DE COPYWRITING (O CORAÇÃO DO NEGÓCIO) ---
# Aqui colocamos gatilhos mentais reais
ESTRUTURA = {
    "aberturas": [
        "🔥 PARE TUDO! Acabei de encontrar uma brecha no preço do {produto}!",
        "🚨 ALERTA DE OPORTUNIDADE: O {produto} baixou para o menor valor do ano!",
        "😱 Você não vai acreditar no que eu achei... O {produto} está quase de graça!",
        "💎 ACHADINHO VIP: Se você estava esperando o {produto}, a hora é AGORA!",
        "✨ O queridinho do momento {produto} entrou em queima de estoque!"
    ],
    "desenvolvimento": [
        "Sério, a qualidade disso aqui é outro nível e o preço está bizarro de baixo.",
        "Quem me segue sabe que eu só posto o que vale a pena, e esse {produto} superou tudo.",
        "É aquele item que todo mundo quer, mas poucos pegam com esse desconto exclusivo.",
        "Não é sorte, é oportunidade! O {produto} com desconto real direto da loja."
    ],
    "urgencia": [
        "⚠️ O estoque está voando, restam pouquíssimas unidades com esse valor!",
        "⏳ A última vez que postei, esgotou em 10 minutos. Corre!",
        "🛑 De R${p_orig} por APENAS R${p_promo}. Não tem como ignorar!",
        "💸 Economia real de verdade. O valor original era R${p_orig}!"
    ],
    "fechamento": [
        "🛍️ Garanta o seu antes que o link expire: {link}",
        "👉 Clique aqui e seja rápido(a): {link}",
        "🔗 O link seguro para compra é esse: {link}",
        "🚀 Voe para o site e aproveite: {link}"
    ]
}

# --- SCRAPER AVANÇADO (TENTA BURLAR O BLOQUEIO) ---
def buscar_dados_v3(url):
    # Simulando um navegador real muito específico
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.google.com/"
    }
    try:
        res = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Busca agressiva de título
        titulo = "Produto Selecionado"
        t_tags = [soup.find("h1"), soup.find("meta", property="og:title"), soup.find("title")]
        for tag in t_tags:
            if tag:
                content = tag.get("content") if tag.name == "meta" else tag.get_text()
                if content and len(content) > 5:
                    titulo = content.strip().split('|')[0].split('-')[0]
                    break
        
        # Busca agressiva de preço
        preco = 0.0
        p_tag = soup.find("meta", property="product:price:amount")
        if p_tag:
            preco = float(p_tag["content"])
        else:
            # Tenta encontrar números com R$ no texto
            precos_no_texto = re.findall(r"R\$\s?(\d+[\d.,]*)", res.text)
            if precos_no_texto:
                preco = float(precos_no_texto[0].replace('.', '').replace(',', '.'))

        return titulo[:50], preco # Corta o título para não ficar gigante
    except:
        return None, None

import re # Necessário para a busca de preços no texto

# --- INTERFACE ---
st.title("👑 LuhVee AI: Sales Master Pro 3.0")
st.markdown("#### Gere vendas automáticas com links da Shopee e Mercado Livre")

col_link, col_btn = st.columns([3, 1])
with col_link:
    url_input = st.text_input("Cole o Link do Produto aqui:", placeholder="https://mercadolivre.com.br/...")
with col_btn:
    st.write("") # Alinhamento
    btn_puxar = st.button("🔍 PUXAR DADOS")

# Inicializa estados
if 'p_nome' not in st.session_state: st.session_state.p_nome = ""
if 'p_valor' not in st.session_state: st.session_state.p_valor = 0.0

if btn_puxar:
    with st.spinner("IA hackeando as informações do produto..."):
        nome, valor = buscar_dados_v3(url_input)
        if nome:
            st.session_state.p_nome = nome
            st.session_state.p_valor = valor
            st.success("Dados Capturados com Sucesso!")
        else:
            st.error("O site bloqueou a leitura automática. Mas não pare! Digite o nome abaixo:")

# --- AJUSTE MANUAL ---
st.divider()
c1, c2, c3 = st.columns(3)
nome_prod = c1.text_input("Confirme o Nome:", value=st.session_state.p_nome)
v_orig = c2.number_input("Preço Original (R$):", value=float(st.session_state.p_valor))
v_promo = c3.number_input("Preço com Desconto (R$):", value=v_orig * 0.8)

# --- GERAÇÃO DE MENSAGENS ---
if st.button("🚀 GERAR VARIAÇÕES DE ALTA CONVERSÃO"):
    if nome_prod and url_input:
        st.subheader("📌 Suas Copies Prontas para Lucrar:")
        
        for i in range(3):
            # Lógica de montagem aleatória
            txt = f"{random.choice(ESTRUTURA['aberturas']).format(produto=nome_prod.upper())}\n\n" \
                  f"{random.choice(ESTRUTURA['desenvolvimento']).format(produto=nome_prod)}\n\n" \
                  f"{random.choice(ESTRUTURA['urgencia']).format(p_orig=f'{v_orig:.2f}', p_promo=f'{v_promo:.2f}')}\n\n" \
                  f"{random.choice(ESTRUTURA['fechamento']).format(link=url_input)}"
            
            st.markdown(f"<div class='copy-box'>{txt.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
            st.code(txt, language="text") # Facilita copiar no celular
    else:
        st.warning("Preencha o link e o nome do produto!")

st.info("💡 Dica de Expert: Para vender esse app, diga que ele usa 'Matriz de Copywriting Dinâmica' que evita o bloqueio de links no WhatsApp.")
