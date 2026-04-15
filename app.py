
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
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 LuhVee Viral Machine")
st.subheader("Sua IA de Postagens de Alta Conversão")

# --- BANCO DE DADOS AMPLIADO (TUDO QUE VOCÊ PEDIU) ---
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

# --- LÓGICA DO BOTÃO MÁGICO ---
if st.button("🔎 IA: PESQUISAR PRODUTOS VIRAIS DO DIA"):
    cat_sorteada = random.choice(list(tendencias.keys()))
    prod_sorteado = random.choice(tendencias[cat_sorteada])
    st.session_state['produto_sugerido'] = prod_sorteado
    st.session_state['categoria_sugerida'] = cat_sorteada
    st.success(f"✅ IA Sugere: {prod_sorteado} (Em {cat_sorteada})")

# --- CAMPOS ---
categoria = st.selectbox("Escolha a Categoria:", list(tendencias.keys()), 
                         index=list(tendencias.keys()).index(st.session_state.get('categoria_sugerida', "Perfumaria e Beleza")))

produto = st.text_input("Nome do Produto:", value=st.session_state.get('produto_sugerido', ""))
link_vitrine = st.text_input("Link da Vitrine (Copia da Shopee/ML):")

# --- GERADOR ---
if st.button("🚀 GERAR POSTS DE ALTA CONVERSÃO"):
    if produto and link_vitrine:
        st.write("---")
        
        st.markdown("#### 📲 WHATSAPP / TELEGRAM")
        copy_whats = f"""🔥 *ALERTA DE PROMOÇÃO!* 🔥

Meninas, olhem que tudo! O *{produto}* está com um preço imperdível hoje! 😱✨

Perfeito para quem ama itens de {categoria}. Esse é o queridinho do momento! 🏆

👇 *Clique no link para garantir o seu:*
{link_vitrine}

Entrega rápida e garantida! 🏃‍♀️💨"""
        st.code(copy_whats, language="text")

        st.markdown("#### 📸 INSTAGRAM / TIKTOK")
        copy_insta = f"""Você não sabia que precisava disso até ver esse vídeo! ✨💖

Apresentamos o {produto}. Qualidade, estilo e utilidade em um só lugar. 🚀

Seja para {categoria} ou para presentear quem você ama, a LuhVee Stores tem o melhor achadinho para você!

🛍️ Gostou? Link direto na Bio e nos Stories! 
{link_vitrine}

#luhveestores #achadinhos #viral #compras #lojaonline #brasil #ofertas"""
        st.code(copy_insta, language="text")
        
    else:
        st.error("Luh, não esquece de colocar o link para o pessoal comprar! 😉")

st.markdown("---")
st.caption("LuhVee Stores - O seu shopping completo na palma da mão.")
