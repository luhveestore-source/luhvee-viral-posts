import streamlit as st
import random

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-baseweb="select"], input { background-color: #ffffff !important; color: #000000 !important; }
    .stButton>button {
        background-color: #ff69b4 !important; color: white !important; 
        border: 2px solid #ffd700 !important; border-radius: 10px;
        width: 100%; font-weight: bold; height: 50px; margin-top: 10px;
    }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'sans serif'; }
    .stCode { background-color: #1e1e1e !important; border: 1px solid #ff69b4 !important; }
    .stRadio > label { color: #ff69b4 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SEUS LINKS OFICIAIS ---
LINK_SHOPEE = "https://collshp.com/luhveestores"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

st.title("🔥 LuhVee Viral Machine")
st.subheader("Sua IA de Postagens de Alta Conversão")

# --- BANCO DE DADOS DE PRODUTOS ---
tendencias = {
    "Perfumaria e Beleza": ["Perfume Caviar Night", "Body Splash Melancia", "Kit Rapunzel Lola", "Skincare Coreano"],
    "Achadinhos de Casa/Cozinha": ["Mini Processador Sem Fio", "Organizador de Geladeira", "MOP Limpeza", "Air Fryer Retrô"],
    "Pets": ["Fonte de Água para Gatos", "Cama Nuvem Relaxante", "Brinquedo Interativo a Laser", "Kit Banho a Seco"],
    "Ferramentas": ["Parafusadeira Sem Fio", "Jogo de Chaves Completo", "Nível Laser Profissional", "Maleta de Ferramentas Pink"],
    "Jardinagem": ["Kit Horta Vertical", "Regador Automático", "Mini Estufa de Suculentas", "Tesoura de Poda Ergonômica"],
    "Eletrônicos": ["Projetor Full HD", "Caixa de Som à Prova D'água", "Power Bank de Carga Rápida", "Fone com Cancelamento de Ruído"],
    "Móveis": ["Puff Baú Decorativo", "Escrivaninha Compacta", "Mesa de Cabeceira Retrô", "Estante de Livros Minimalista"],
    "Sapatos e Tênis": ["Tênis Chunky Confort", "Tênis Esportivo Versátil", "Sapatilha Confort Flex", "Bota Cano Curto"],
    "Saltos e Scarpins": ["Scarpin Clássico Verniz", "Sandália Salto Bloco", "Tamanco Transparente", "Salto Agulha Elegance"],
    "Acessórios de Celular": ["Capa Anti-Impacto Luxo", "Lente para Foto Pro", "Suporte Veicular Magnético", "Cabo Reforçado 3 metros"],
    "Informática": ["Teclado Mecânico RGB", "Mouse Gamer Sem Fio", "Hub USB Tipo C", "Suporte Articulado de Monitor"],
    "Lingerie": ["Conjunto Renda Sem Bojo", "Body Modelador Invisível", "Robê de Seda", "Baby Doll Conforto"],
    "Sexshop": ["Vibrador de Sucção Viral", "Óleo de Massagem Hot", "Gel Excitante", "Acessórios Sensuais"],
    "Moda Feminina/Acessórios": ["Vestido Midi Canelado", "Conjunto Linho Verão", "Maxi Colar Dourado", "Cinto Fivela Dupla"]
}

# --- BOTÃO PESQUISAR ---
if st.button("🔎 IA: PESQUISAR PRODUTOS VIRAIS DO DIA"):
    cat_sorteada = random.choice(list(tendencias.keys()))
    prod_sorteado = random.choice(tendencias[cat_sorteada])
    st.session_state['produto_sugerido'] = prod_sorteado
    st.session_state['categoria_sugerida'] = cat_sorteada
    st.success(f"✅ IA Sugere: {prod_sorteado} (Em {cat_sorteada})")

# --- ESCOLHA DA LOJA ---
st.write("---")
loja_escolhida = st.radio("Onde você quer vender esse produto?", ["Shopee", "Mercado Livre", "Outro (Digitar Link)"])

if loja_escolhida == "Shopee":
    link_usar = LINK_SHOPEE
elif loja_escolhida == "Mercado Livre":
    link_usar = LINK_ML
else:
    link_usar = st.text_input("Cole o link específico aqui:", "")

# --- CAMPOS ---
categoria = st.selectbox("Categoria:", list(tendencias.keys()), 
                         index=list(tendencias.keys()).index(st.session_state.get('categoria_sugerida', "Perfumaria e Beleza")))

produto = st.text_input("Nome do Produto:", value=st.session_state.get('produto_sugerido', ""))

# --- GERADOR ---
if st.button("🚀 GERAR POSTS DE ALTA CONVERSÃO"):
    if produto and link_usar:
        st.write("---")
        
        st.markdown("#### 📲 WHATSAPP / TELEGRAM")
        copy_whats = f"""🔥 *ALERTA DE TENDÊNCIA!* 🔥\n\nMeninas, olhem o que eu achei para vocês! O *{produto}* que está todo mundo postando! 😱✨\n\n👇 *Garanta o seu aqui na minha vitrine do {loja_escolhida}:*\n{link_usar}\n\nCorre antes que esgote! 🏃‍♀️💨"""
        st.code(copy_whats, language="text")

        st.markdown("#### 📸 INSTAGRAM / TIKTOK")
        copy_insta = f"""POV: Você encontrou o {produto} que precisava! ✨💖\n\nDireto da LuhVee Stores para a sua casa. O item mais desejado de {categoria} agora a um clique de distância. 🚀\n\n🛍️ Link direto na Bio e nos Stories! \n{link_usar}\n\n#luhveestores #achadinhos #viral #shopee #mercadolivre"""
        st.code(copy_insta, language="text")
    else:
        st.error("Luh, escolha a loja ou cole o link para gerar o post! 😉")
