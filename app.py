import streamlit as st

# --- 1. CONFIGURAÇÃO VISUAL (Estilo Luhvee Stores) ---
st.set_page_config(page_title="Luhvee Shoes - Gerador de Post", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LINKS E INFORMAÇÕES FIXAS ---
CATALOGO_SHOES = "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes"
WHATSAPP = "https://wa.me/5511948021428"
INSTAGRAM = "@luhveestore"

# --- 3. INTERFACE DE ENTRADA ---
st.title("👟 Gerador de Copy: Luhvee Shoes")
st.write("Preencha os detalhes técnicos do calçado abaixo:")

col1, col2 = st.columns(2)
with col1:
    nome_ref = st.text_input("Nome do Calçado | REF.", placeholder="Ex: BOTA COTURNO SOLA TRATORADA COURO | REF.: 36A")
    preco = st.text_input("Valor (R$)", placeholder="Ex: 189.90")
    material = st.text_input("Material", placeholder="Ex: Couro Preto")

with col2:
    enfeites = st.text_input("Enfeites", placeholder="Ex: Elástico na Cor Preto")
    palmilha = st.text_input("Palmilha", placeholder="Ex: 8 mm de Espessura, EVA")
    forro = st.text_input("Forro", placeholder="Ex: Cacharrel espumado")
    solado = st.text_input("Solado", placeholder="Ex: Tratorado Preto")

# --- 4. LÓGICA DE MONTAGEM DA MENSAGEM ---
if st.button("🚀 GERAR MENSAGEM PARA CALÇADOS"):
    if nome_ref and preco:
        # Template exato conforme solicitado pelo usuário
        copy_final = f"""😤 CANSADO DE PROCURAR?

{nome_ref.upper()} ORIGINAL está AQUI! 👈

Sem fake, sem enganação! ✅

🔥 Material: {material};

Enfeites: {enfeites};

Palmilha: {palmilha};

Forro: {forro};

Solado {solado}.

💰 R$ {preco}

Fim da busca! 🎉

🛒 COMPRE AGORA:
🏪 Catálogo: {CATALOGO_SHOES}

💬 WhatsApp: {WHATSAPP}

💳 Formas de Pagamento:
✅ Cartão de Crédito
✅ Link de Pagamento
✅ PIX

📲 Instagram: {INSTAGRAM}

📲 {INSTAGRAM}"""

        st.divider()
        st.subheader("📋 Mensagem Pronta (Clique para copiar)")
        st.text_area("Copie e cole no WhatsApp/Instagram:", copy_final, height=500)
    else:
        st.warning("Por favor, preencha pelo menos o Nome/REF e o Preço.")
