import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar Viral Pro 2026", page_icon="🚀", layout="wide")

# 2. LÓGICA DE CATEGORIZAÇÃO (O "Cérebro" do App)
def identificar_nicho(produto):
    produto = produto.lower()
    if any(k in produto for k in ['rosto', 'pele', 'maquiagem', 'creme', 'serum', 'cabelo']):
        return "Beleza & Skincare"
    elif any(k in produto for k in ['fone', 'celular', 'tech', 'gamer', 'teclado', 'mouse', 'smartwatch']):
        return "Tecnologia & Gadgets"
    elif any(k in produto for k in ['casa', 'cozinha', 'decoração', 'limpeza', 'organizador']):
        return "Casa & Organização"
    elif any(k in produto for k in ['roupa', 'tênis', 'moda', 'acessório', 'bolsa']):
        return "Moda & Estilo"
    else:
        return "Geral / Tendências"

# 3. MINERAÇÃO DE DADOS REAL
def minerar_vendas(termo):
    # Busca notícias recentes sobre o produto + termos de venda
    query = f"{termo} tendência lançamento brasil 2026"
    url = f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'xml')
        itens = soup.find_all('item', limit=5)
        
        resultados = []
        for item in itens:
            resultados.append({
                "Notícia/Tendência": item.title.text,
                "Data": item.pubDate.text[:16],
                "Link": item.link.text
            })
        return pd.DataFrame(resultados)
    except:
        return pd.DataFrame({"Aviso": ["Sem dados recentes para este termo."]})

# 4. GERADOR DE ESTRATÉGIA ASSERTIVA
def gerar_estrategia(nicho, hora):
    if nicho == "Beleza & Skincare":
        publico, rede, gatilho = "Mulheres 18-45", "TikTok/Instagram", "Autoestima e Prova Social"
    elif nicho == "Tecnologia & Gadgets":
        publico, rede, gatilho = "Homens/Jovens 18-35", "YouTube/Twitter", "Performance e Exclusividade"
    elif nicho == "Casa & Organização":
        publico, rede, gatilho = "Público 25-55", "Pinterest/Facebook", "Praticidade e Conforto"
    else:
        publico, rede, gatilho = "Público Amplo", "Instagram/Google", "Curiosidade"

    return publico, rede, gatilho

# --- INTERFACE ---
st.title("🔥 Radar Viral Pro: Inteligência de Vendas")
st.markdown(f"**Análise Ativa:** {datetime.now().strftime('%d/%m/%Y %H:%M')} | Foco: Conversão Assertiva")

# Sidebar
st.sidebar.header("⏰ Painel de Horário")
hora_atual = datetime.now().hour
if 6 <= hora_atual < 12:
    st.sidebar.info("🌅 **Manhã:** Foco em Conteúdo Educativo.")
elif 12 <= hora_atual < 18:
    st.sidebar.warning("☀️ **Tarde:** Foco em Ofertas e Escassez.")
else:
    st.sidebar.success("🌙 **Noite:** Foco em Entretenimento e Desejo.")

# Entrada do Utilizador
produto_input = st.text_input("Qual produto você quer analisar hoje?", placeholder="Ex: Smartwatch, Base Facial, Organizador de Geladeira...")

if produto_input:
    nicho_detectado = identificar_nicho(produto_input)
    publico, rede, gatilho = gerar_estrategia(nicho_detectado, hora_atual)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"🌐 Tendências para: {produto_input}")
        with st.spinner('Minerando notícias e mercado...'):
            df_vendas = minerar_vendas(produto_input)
            if not df_vendas.empty:
                st.dataframe(df_vendas, use_container_width=True)
            else:
                st.write("Nenhuma notícia de tendência encontrada para este termo específico.")

    with col2:
        st.subheader("🎯 Perfil Certeiro")
        st.metric("Nicho Identificado", nicho_detectado)
        st.write(f"**Público-Alvo:** {publico}")
        st.write(f"**Melhor Canal:** {rede}")
        st.write(f"**Gatilho Mental:** {gatilho}")

    st.divider()
    
    # Gerador de Postagem
    st.subheader("💡 Sugestão de Copy (Legenda)")
    if 12 <= hora_atual < 18:
        legenda = f"🔥 ALERTA DE TENDÊNCIA: O {produto_input} está dominando o mercado! Se você busca {gatilho.lower()}, precisa conhecer isso antes que o estoque acabe. Link na Bio! 🏃‍♂️"
    else:
        legenda = f"Você já viu isso? ✨ O {produto_input} é o segredo para quem quer {gatilho.lower()}. Perfeito para sua rotina! Dê um upgrade no seu dia a dia. Comenta 'EU QUERO' 👇"
    
    st.code(legenda, language="text")
    st.caption("Copy gerada automaticamente com base no nicho e horário de pico.")
