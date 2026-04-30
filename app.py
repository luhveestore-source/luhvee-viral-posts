import streamlit as st
import random
import requests
from bs4 import BeautifulSoup
import json
import os
import re
from datetime import datetime

# --- CONFIGURAÇÃO DE ALTA PERFORMANCE ---
st.set_page_config(page_title="LuhVee AI ULTRA PRO", layout="wide", page_icon="👑")

ARQUIVO_HISTORICO = "historico_vendas_luhvee.json"

# Seus Links Oficiais
LINKS_VITRINE = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Hub de Links": "https://links-luhveestore.streamlit.app/"
}

# --- BANCO DE COPYWRITING AGRESSIVO (CONVERSÃO PESADA) ---
MATRIZ_COPY = {
    "whatsapp": [
        "🚨 *ALERTA DE OPORTUNIDADE ÚNICA!* 🚨\n\nEu não acreditei quando vi o preço do *{produto}* hoje! 🔥\n\n📉 De: ~~R$ {p_orig}~~ \n💰 *Por apenas: R$ {p_promo}*\n\n⚠️ O estoque está voando e esse valor não dura até amanhã. É a sua chance de garantir o melhor com um desconto bizarro!\n\n🛍️ *PEGUE O SEU ANTES QUE ACABE:* \n👉 {link}\n\n👑 LuhVee Store - Qualidade que você confia!",
        "😱 *PARE TUDO O QUE ESTÁ FAZENDO!*\n\nO queridinho voltou! O *{produto}* está com uma queima de estoque exclusiva. \n\n💸 Valor de hoje: *R$ {p_promo}* (Economia real!)\n\n🏃‍♂️ Quem avisar primeiro no grupo ganha? Não! Quem clicar primeiro no link leva!\n\n🔗 *LINK SEGURO:* {link}\n\nLuhVee ✨"
    ],
    "instagram": [
        "🔥 ACHADINHO VIP! 🔥\n\nVocês sempre pedem e eu encontrei o melhor preço do Brasil para o {produto}! 😱\n\n✨ De R$ {p_orig} por APENAS R$ {p_promo}!\n\n❌ Sem pegadinhas, é desconto real de queima de estoque. \n\n⚠️ RESTAM POUCAS UNIDADES! \n\n🛒 Link nos Stories ou na Bio:\n👉 {link}\n\n#achadinhos #oferta #shopee #mercadolivre #luhvee #promocao",
        "💎 O QUE É ISSO?! 💎\n\nO {produto} que viralizou no TikTok acabou de entrar em promoção relâmpago! ⚡️\n\n💰 Só hoje: R$ {p_promo}\n⏳ O link vai expirar assim que o lote acabar.\n\n👇 GARANTA O SEU AGORA:\n🔗 {link}\n\n#luhveestore #oportunidade #desconto #compras"
    ]
}

# --- FUNÇÕES DE SISTEMA ---
def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return []
    return []

def salvar_no_historico(produto, preco_promo, plataforma, link_final):
    hist = carregar_historico()
    novo_item = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "produto": produto,
        "preco": f"R$ {preco_promo}",
        "plataforma": plataforma,
        "link": link_final
    }
    hist.append(novo_item)
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(hist, f, ensure_ascii=False, indent=4)

def extrair_dados_v4(url):
    # Cabeçalho ultra-robusto para evitar bloqueios
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9"
    }
    try:
        res = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Tenta pegar o título no ML e Shopee
        titulo = "Produto Selecionado"
        t_tags = [soup.find("h1"), soup.find("title"), soup.find("meta", property="og:title")]
        for t in t_tags:
            if t:
                content = t.get("content") if t.name == "meta" else t.get_text()
                if content:
                    titulo = content.strip().split('|')[0].split('-')[0]
                    break
                    
        # Tenta pegar preço via Regex (mais agressivo)
        precos = re.findall(r"R\$\s?(\d+[\d.,]*)", res.text)
        preco_val = float(precos[0].replace('.', '').replace(',', '.')) if precos else 0.0
        
        return titulo[:60], preco_val
    except:
        return None, None

# --- INTERFACE ---
st.title("👑 LuhVee AI: Sales Master Pro 4.0")

aba_gerador, aba_historico = st.tabs(["🚀 Gerador de Vendas", "📊 Histórico"])

with aba_gerador:
    col1, col2 = st.columns([3, 1])
    with col1:
        url_input = st.text_input("🔗 Cole o Link do Produto (ML ou Shopee):")
    with col2:
        st.write("")
        btn_puxar = st.button("✨ EXTRAIR DADOS")

    if btn_puxar and url_input:
        with st.spinner("IA hackeando os preços..."):
            nome, valor = extrair_dados_v4(url_input)
            if nome:
                st.session_state.p_nome = nome
                st.session_state.p_valor = valor
                st.success("Dados capturados com sucesso!")
            else:
                st.error("Site bloqueou a leitura automática. Digite o nome abaixo!")

    st.divider()
    
    c_plat, c_nome = st.columns([1, 2])
    with c_plat:
        plat_sel = st.selectbox("Plataforma de Venda:", list(LINKS_VITRINE.keys()))
    with c_nome:
        nome_final = st.text_input("Nome do Produto:", value=st.session_state.get('p_nome', ""))

    p1, p2 = st.columns(2)
    v_orig = p1.number_input("Preço Original (R$):", value=float(st.session_state.get('p_valor', 0.0)))
    v_promo = p2.number_input("Preço de Venda (R$):", value=v_orig * 0.85 if v_orig > 0 else 0.0)

    if st.button("🚀 GERAR VARIAÇÕES AGRESSIVAS"):
        if nome_final and url_input:
            link_final = LINKS_VITRINE[plat_sel]
            salvar_no_historico(nome_final, v_promo, plat_sel, link_final)
            
            st.subheader("📱 PARA WHATSAPP (Foco em Grupos)")
            for copy in MATRIZ_COPY["whatsapp"]:
                txt = copy.format(produto=nome_final, p_orig=v_orig, p_promo=v_promo, link=link_final)
                st.code(txt, language="text")
                
            st.subheader("📸 PARA INSTAGRAM (Foco em Stories/Bio)")
            for copy in MATRIZ_COPY["instagram"]:
                txt = copy.format(produto=nome_final, p_orig=v_orig, p_promo=v_promo, link=link_final)
                st.code(txt, language="text")
        else:
            st.error("Preencha todos os campos!")

with aba_historico:
    st.header("📊 Seus Posts Recentes")
    hist = carregar_historico()
    if hist:
        st.table(hist[::-1])
    else:
        st.info("Nenhum post gerado ainda.")
