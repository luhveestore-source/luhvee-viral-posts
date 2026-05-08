import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar Viral Pro 2026", page_icon="🔥", layout="wide")

# Estilo personalizado para ficar mais profissional no telemóvel
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# 2. INTELIGÊNCIA DE NICHO MELHORADA
def analisar_mercado_profundo(produto):
    p = produto.lower()
    # Base de dados de inteligência local
    if any(k in p for k in ['rosto', 'pele', 'maquiagem', 'creme', 'serum', 'cabelo']):
        return "Beleza & Skincare", "Mulheres 20-45", "Autoestima/Beleza", "TikTok/Reels"
    elif any(k in p for k in ['fone', 'celular', 'tech', 'gamer', 'teclado', 'mouse', 'smartwatch']):
        return "Tecnologia & Gadgets", "Homens/Jovens 16-35", "Inovação/Status", "YouTube/Twitter"
    elif any(k in p for k in ['casa', 'cozinha', 'decoração', 'limpeza', 'organizador', 'roupa']):
        return "Moda & Lar", "Público Adulto 25-50", "Praticidade/Conforto", "Instagram/Pinterest"
    else:
        return "Nicho Geral", "Público Amplo", "Curiosidade", "Instagram/Facebook"

# 3. MINERAÇÃO COM FILTROS DE VENDA
def minerar_tendencias_reais(termo):
    # Adicionamos termos que indicam que algo está a ser vendido ou é tendência
    query = f"{termo} (tendência OR viral OR shopee OR lançamento) brasil 2026"
    url = f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'xml')
        itens = soup.find_all('item', limit=8)
        
        resultados = []
        for item in itens:
            # Limpar o título para ficar mais curto
            titulo = item.title.text.split(" - ")[0]
            resultados.append({
                "🔥 Oportunidade/Notícia": titulo,
                "Fonte": item.source.text,
                "Link": item.link.text
            })
        return pd.DataFrame(resultados)
    except:
        return pd.DataFrame()

# --- INTERFACE ---
st.title("🔥 Radar Viral: Inteligência de Vendas")

# Entrada do Produto
produto_input = st.text_input("O que pretendes vender hoje?", placeholder="Ex: Vestido de Verão, Smartwatch, etc.")

if produto_input:
    nicho, persona, gatilho, canal = analisar_mercado_profundo(produto_input)
    
    # Métricas Principais
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Nicho", nicho)
    with col_b:
        st.metric("Público", persona)
    with col_c:
        st.metric("Canal Forte", canal)

    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🌐 Tendências Encontradas")
        with st.spinner('A analisar o mercado...'):
            df_vendas = minerar_tendencias_reais(produto_input)
            if not df_vendas.empty:
                # Mostrar como uma lista de links mais amigável
                for i, row in df_vendas.iterrows():
                    st.markdown(f"📍 **{row['🔥 Oportunidade/Notícia']}**")
                    st.caption(f"Fonte: {row['Fonte']} | [Abrir Notícia]({row['Link']})")
            else:
                st.warning("Não foram encontradas notícias específicas. Tenta um termo mais focado (ex: em vez de 'Roupas', usa 'Moda Feminina').")

    with col2:
        st.subheader("🎯 Estratégia de Venda")
        st.info(f"**Gatilho:** {gatilho}")
        
        st.write("**Sugestão de Criativo:**")
        if "TikTok" in canal:
            st.write("🎥 Vídeo rápido (15s) mostrando o 'Antes e Depois' ou o unboxing.")
        else:
            st.write("📸 Foto Lifestyle (uso no dia a dia) com cores vibrantes.")

    st.divider()
    
    # Gerador de Legenda Pro
    st.subheader("💡 Sugestão de Copy (Legenda)")
    copy = f"""🔥 ESTÁ TODO MUNDO FALANDO DISSO! 

Se você busca {gatilho.lower()}, o novo {produto_input} é exatamente o que você precisa. 🚀

✅ Tendência confirmada para 2026
✅ Qualidade premium
✅ Estoque limitado!

Não fique de fora da tendência que está dominando o {canal.split('/')[0]}. 

👉 Clique no link da bio e garanta o seu agora! #vendas #tendencia #{nicho.replace(' ', '')}"""
    
    st.code(copy, language="text")

else:
    st.info("Insere um produto acima para começar a mineração de dados.")
