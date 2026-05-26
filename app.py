import streamlit as st
import google.generativeai as genai

# --- 1. IDENTIDADE VISUAL (Estilo Luhvee Stores) ---
st.set_page_config(page_title="Central Luhvees Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")
    st.stop()

# --- 3. BANCO DE LINKS OFICIAIS LUHVEES ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Hub": "https://links-luhveestore.streamlit.app/",
    "Shopintegra": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "@luhveestore"
}

# --- 4. NAVEGAÇÃO LATERAL ---
aba = st.sidebar.radio("Selecione o que postar:", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "💬 Mensagens de Grupo"])

# --- PILAR 1: CALÇADOS ---
if aba == "👠 Calçados (Shoes)":
    st.subheader("👟 Gerador Luhvee Shoes - Neurocopy Ativada")
    nome_calca = st.text_input("Nome do Produto / REF.")
    valor_calca = st.text_input("Preço (R$)")
    desc_calca = st.text_area("Descrição Técnica")

    if st.button("🚀 GERAR POST DE CALÇADOS"):
        if nome_calca and valor_calca:
            copy_shoes = f"""😤 CANSADO DE PROCURAR?\n\n{nome_calca.upper()} ORIGINAL está AQUI! 👈\n\nSem fake, sem enganação! ✅\n\n{desc_calca}\n\n💰 R$ {valor_calca}\n\nFim da busca! 🎉\n\n🛒 COMPRE AGORA:\n🏪 Catálogo: {LINKS['Shopintegra']}\n\n💬 WhatsApp: {LINKS['WhatsApp']}\n\n💳 Formas de Pagamento:\n✅ Cartão de Crédito\n✅ Link de Pagamento\n✅ PIX\n\n📲 Instagram: {LINKS['Instagram']}\n🔗 Mais Links: {LINKS['Hub']}"""
            st.text_area("Pronto para copiar:", copy_shoes, height=450)
        else:
            st.warning("Preencha o Nome e o Valor.")

# --- PILAR 2: ACHADINHOS (Mensagem Única, Curta e Direta) ---
elif aba == "🎁 Achadinhos":
    st.subheader("🎁 Gerador de Achadinhos - Rápido e Direto")
    prod_achado = st.text_input("Nome do Produto", placeholder="Ex: Caixa de Areia Furba")
    preco_achado = st.text_input("Preço (R$)", placeholder="39,90")
    loja_principal = st.selectbox("Escolha a Loja Principal do Link:", ["Shopee", "Shein"])

    if st.button("🚀 GERAR MENSAGENS"):
        if prod_achado and preco_achado:
            with st.spinner("IA criando uma copy rápida e matadora..."):
                
                # Forcei o prompt a exigir textos extremamente resumidos e sem enrolação
                prompt = f"""
                Atue como copywriter especialista em e-commerce de resposta rápida.
                Crie um texto de venda ULTRA CURTO e DIRETO ao ponto para o produto '{prod_achado}' por R$ {preco_achado}.
                
                Regras Obrigatórias (Seja o mais resumido possível):
                1. Cabeçalho: Comece com '🚨 OFERTA IMPERDÍVEL! 🚨' ou similar em caixa alta.
                2. Introdução: Apenas uma frase curta e impactante atiçando o desejo ou resolvendo um problema.
                3. Lista: Crie APENAS 3 tópicos super curtos (máximo de 5 palavras por linha) destacando os maiores benefícios. Alterne os marcadores entre ✨ e ✔.
                4. Preço: O último tópico deve ser rigorosamente: '✔ APENAS R$ {preco_achado}! Poucas unidades!'
                5. Fechamento: Finalize com 'Não perca essa! Seu pet e sua casa agradecem. 🐾🏠' (ajuste os emojis se não for produto pet).
                
                Não coloque explicações, dê apenas o texto pronto.
                """
                response = model.generate_content(prompt)
                
                # Rodapé do seu jeitinho com os links automáticos e sua assinatura
                texto_final = (
                    f"{response.text.strip()}\n\n"
                    f"👉 **Compre JÁ:** {LINKS[loja_principal]}\n\n"
                    f"*Ainda não encontrou o que precisa, me chama que coloco na vitrine*\n\n"
                    f"🛒 **LINK PARA COMPRAR ({loja_principal.upper()}):**\n"
                    f"🔗 {LINKS[loja_principal]}\n\n"
                    f"🛍️ **COMPRAR NO MERCADO LIVRE:**\n"
                    f"🔗 {LINKS['Mercado Livre']}\n\n"
                    f"🌐 **VEJA TODOS OS ACHADINHOS:**\n"
                    f"👉 {LINKS['Hub']}\n\n"
                    f"Boas compras 🛍️ bjs da Luh ❤️"
                )
                
                st.text_area("Cópia Única para Todas as Redes:", texto_final, height=500)
        else:
            st.warning("Preencha o Nome do Produto e o Preço.")

# --- PILAR 3: MENSAGENS DE GRUPO ---
elif aba == "💬 Mensagens de Grupo":
    st.subheader("💬 Máquina de Engajamento - Mensagens Premium")
    contexto_extra = st.text_input("Tema de Motivação do Dia:", placeholder="Ex: Sabadou, Foco nos objetivos...")

    if st.button("🚀 GERAR TODAS AS MENSAGENS"):
        with st.spinner("IA criando as mensagens..."):
            tema = contexto_extra if contexto_extra else "um dia maravilhoso de conquistas"
            
            prompt_grupo = f"Atue como copywriter para WhatsApp. Crie 3 mensagens separadas: uma de BOM DIA (MANHÃ), uma de BOA TARDE (TARDE) e uma de BOA NOITE (NOITE). O tema motivacional é '{tema}'. Regras obrigatórias: Use títulos em CAIXA ALTA com emojis fortes, quebre o texto em tópicos curtos usando '✨' ou '✔️', e coloque o '@todos' destacado no fim de cada mensagem."
            response = model.generate_content(prompt_grupo)
            
            st.text_area("Mensagens Prontas para o Grupo:", response.text, height=600)
