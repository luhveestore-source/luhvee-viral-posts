import streamlit as st
import random
from PIL import Image

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="LuhVee Viral Machine", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'sans serif'; }
    .stButton>button {
        background-color: #ff69b4 !important; color: white !important; 
        border: 2px solid #ffd700 !important; border-radius: 10px; width: 100%;
        font-weight: bold; font-size: 18px;
    }
    .stCode { 
        background-color: #1e1e1e !important; 
        border: 1px solid #ff69b4 !important; 
        color: #ffffff !important; 
        white-space: pre-wrap !important; 
        font-size: 14px !important;
    }
    div[data-baseweb="select"] { background-color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS EXPANDIDO (INTELIGÊNCIA DE MERCADO) ---
tendencias_reais = {
    "✨ Beleza & Autoestima": [
        "Perfume Caviar Night", "Sérum Coreano Glow", "Escova 3 em 1 Pro", "Gloss Volumizador", 
        "Kit de Pincéis de Cristal", "Máscara LED Facial", "Massageador de Quartzo Rosa", "Removedor de Cravo a Vácuo"
    ],
    "🏠 Casa & Decoração": [
        "MOP Giratório Inox", "Organizador de Acrílico Luxo", "Mini Selador Viral", "Luminária Pôr do Sol",
        "Projetor de Galáxia", "Fita LED RGB Bluetooth", "Umidificador de Ar Chama de Fogo", "Aspirador de Pó Portátil"
    ],
    "👗 Moda & Acessórios": [
        "Conjunto Alfaiataria", "Sandália Strass", "Body Modelador Real", "Bolsa Corrente Ouro",
        "Óculos Retrô Vintage", "Relógio Inteligente Rose Gold", "Corrente de Prata 925", "Tiara de Pérolas Luxo"
    ],
    "🧸 Infantil & Brinquedos": [
        "Cacto Dançante", "Mini Câmera Digital Infantil", "Tablet de Desenho LCD", "Blocos de Montar Magnéticos",
        "Luminária de Ursinho", "Almofada de Elefante Gigante", "Kit de Miçangas DIY", "Boneca Reborn Realista"
    ],
    "🐶 Mundo Pet": [
        "Cama Nuvem Relaxante", "Bebedouro Fonte de Água", "Escova Tira Pelos Mágica", "Coleira com LED",
        "Tapete Gelado para Cães", "Brinquedo Interativo de Petisco", "Cadeirinha de Carro para Pet", "Cortador de Unha com Luz"
    ],
    "📱 Tecnologia & Gadgets": [
        "Fone de Ouvido Noise Cancelling", "Carregador Magnético Magsafe", "Suporte de Celular Articulado", "Mini Projetor Portátil",
        "Teclado Mecânico RGB", "Mouse Vertical Ergonômico", "Caixa de Som à Prova d'água", "Anel Inteligente"
    ],
    "🚗 Acessórios Automotivos": [
        "Suporte de Celular por Gravidade", "Aspirador de Carro Sem Fio", "Luz Interna Neon", "Organizador de Banco",
        "Kit de Reparo de Parabrisa", "Compressor de Ar Portátil", "Película de Retrovisor Anti-Chuva", "Sensor de Estacionamento"
    ],
    "🗄️ Organização & Limpeza": [
        "Etiquetadora Bluetooth Portátil", "Caixas Organizadoras Empilháveis", "Cabides Aveludados", "Dispenser de Sabão Automático",
        "Sacos de Vácuo para Roupas", "Gancho Multiuso Sem Furo", "Mop Limpa Vidros Extensível", "Organizador de Fios e Cabos"
    ],
    "🌎 Internacional (High Ticket)": [
        "ProDentim (Saúde Bucal)", "Suplemento BioFit", "Renovador Facial Digistore", "Alinhador Dental Invisível",
        "Smartwatch Ultra Serie 9", "Massageador Cervical Profissional", "Drenagem Linfática Portátil"
    ]
}

# --- FUNÇÃO GERADORA DE TEXTOS PROFUNDOS ---
def gerar_texto_profundo(periodo):
    ganchos = [
        "Às vezes, a pressa do dia a dia nos faz esquecer de quem realmente somos e do que viemos fazer aqui.",
        "Pare um segundo. Respire fundo. Olhe ao seu redor e perceba o quanto você já caminhou até este momento.",
        "O sucesso não é apenas sobre os números na conta, mas sobre a paz que você sente ao deitar a cabeça no travesseiro.",
        "Sabe aquele sonho que você guardou no fundo da alma? Ele ainda pulsa aí dentro, esperando por um movimento seu."
    ]
    reflexoes = [
        "A vida não é uma corrida desenfreada contra o tempo ou contra os outros, mas uma jornada sagrada de cura e redescoberta. Cada cicatriz que você carrega é, na verdade, um mapa detalhado de uma batalha que você venceu em silêncio. Não se compare com o palco de ninguém enquanto você ainda está nos seus bastidores. O seu brilho é único, singular, e a sua essência é exatamente o que faz o mundo ser um lugar mais bonito de se viver. Valorize os pequenos passos, cada respiração, pois são eles que constroem os grandes destinos e as histórias que valem a pena ser contadas.",
        "Muitas vezes depositamos a nossa felicidade no 'quando eu tiver' ou 'quando eu chegar lá'. Mas a verdade nua e crua é que a vida acontece agora, neste exato fôlego, nesta exata batida de coração. Ser uma mulher forte não significa não cansar ou nunca chorar, mas sim ter a sabedoria divina de descansar sem jamais desistir do que te faz vibrar. Você é o projeto mais importante e urgente da sua vida. Cuide-se com o mesmo amor e dedicação que você dedica aos outros, pois o seu coração é o seu templo mais sagrado e ele precisa de luz.",
        "Não permita que o ruído das opiniões alheias abafe a voz suave que vem do fundo do seu coração. Você foi desenhada para coisas grandes, mas a verdadeira grandeza começa na gratidão profunda pelo pouco que se tem hoje. O tempo é o nosso bem mais precioso e escasso; não o gaste tentando provar nada para ninguém, gaste-o construindo a paz que você merece sentir. A sua história é escrita por você, e cada novo amanhecer é uma página em branco pronta para ser preenchida com coragem, fé e um amor-próprio inabalável."
    ]
    conclusoes = [
        "Que este momento seja o início de uma nova perspectiva na sua vida. Você é rara, preciosa e digna de tudo o que é bom.",
        "Lembre-se sempre: você é o milagre que tanto procurava no mundo. Siga com fé, cabeça erguida e muita coragem.",
        "Seja a luz que você deseja ver no mundo. O seu momento de florescer não é amanhã, é hoje. O mundo espera por você."
    ]
    texto = f"{periodo}\n\n{random.choice(ganchos)}\n\n{random.choice(reflexoes)}\n\n{random.choice(conclusoes)}\n\nCom todo carinho do mundo,\nLuhVee Stores 🛍️❤️"
    return texto

# --- LINKS ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "ProDentim": "https://luhvee-store.systeme.io/prodentim-special",
    "Whats": "https://wa.me/5511948021428",
    "Telegram": "https://t.me/luhveestores",
    "Grupo Whats": "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
}

# --- MENU LATERAL ---
st.sidebar.title("Comando LuhVee")
aba = st.sidebar.radio("Escolha a ferramenta:", ["🛍️ Postar Produtos", "🔎 Pesquisa Viral IA", "✨ Frases Motivacionais", "🔗 Vitrines & Hub"])

# ==========================================
# ABA 1: GERADOR DE MADEIRADA
# ==========================================
if aba == "🛍️ Postar Produtos":
    st.title("🔥 Gerador de Madeirada Profissional")
    produto = st.text_input("Nome do Produto:", placeholder="Ex: Escova 3 em 1")
    foto = st.file_uploader("📸 Escolha a foto", type=["png", "jpg", "jpeg"])
    if foto: st.image(Image.open(foto), use_column_width=True)
    loja = st.radio("Link de qual loja?", ["Shopee", "Mercado Livre", "ProDentim"])
    link_f = LINKS[loja]

    if st.button("🚀 GERAR COPY DE ALTA CONVERSÃO"):
        if produto:
            st.success("✅ ESTRATÉGIA DE VENDA GERADA!")
            copy_story = (
                f"🚨 Meninas, para TUDO o que vocês estão fazendo! 🚨\n\n"
                f"Sabe aquele problema de perder tempo tentando ficar pronta, ou aquele detalhe que falta para dar um UP no visual? "
                f"Eu encontrei o {produto} que é o segredo das blogueiras e finalmente entendi o porquê de todo esse barulho! ✨\n\n"
                f"A qualidade é surreal! É aquele tipo de achadinho que a gente não guarda, a gente espalha! "
                f"Mas corre, porque toda vez que posto, o estoque da loja zera em minutos. 💨\n\n"
                f"👇 Toque no link abaixo para garantir o seu antes que acabe:\n🔗 {link_f}\n\n"
                f"LuhVee Stores 🛍️ – Onde a tendência chega primeiro!"
            )
            copy_viral = (
                f"POV: Você finalmente parou de gastar dinheiro com coisas que não funcionam e comprou o {produto} dos sonhos! 😍✨\n\n"
                f"Não é apenas um produto, é O INVESTIMENTO que vai facilitar a sua rotina e te deixar ainda mais maravilhosa. "
                f"Se você estava esperando um sinal para se dar esse mimo, O SINAL É ESSE! 🎀\n\n"
                f"🔗 LINK NA MINHA BIO! Digita 'EU QUERO' que eu te mando no direct! 🔥\n\n"
                f"#luhveestores #achadinhosshopee #viral #shopeebrasil"
            )
            st.markdown("### 📱 Copy para Status/Stories")
            st.code(copy_story, language="text")
            st.markdown("### 🎬 Copy para TikTok/Reels")
            st.code(copy_viral, language="text")
        else: st.warning("Luh, digite o nome do produto! 😘")

# ==========================================
# ABA 2: PESQUISA VIRAL IA (BANCO DE DADOS RESTAURADO)
# ==========================================
elif aba == "🔎 Pesquisa Viral IA":
    st.title("🔎 Inteligência de Mercado")
    st.subheader("O que está bombando nas redes?")
    
    categoria = st.selectbox("Escolha um nicho para minerar:", list(tendencias_reais.keys()))
    
    if st.button("🔥 BUSCAR PRODUTO VIRAL"):
        sugestao = random.choice(tendencias_reais[categoria])
        st.write("---")
        st.header(f"💡 Sugestão: {sugestao}")
        st.info(f"Dica LuhVee: Este item de {categoria} está com alto engajamento no TikTok hoje. Perfeito para postar agora!")

# ==========================================
# ABA 3: MOTIVACIONAIS
# ==========================================
elif aba == "✨ Frases Motivacionais":
    st.title("✨ Vibes LuhVee Stores")
    periodo = st.selectbox("Escolha o momento:", ["Bom Dia ☀️", "Boa Tarde 🌤️", "Boa Noite 🌙"])
    if st.button("✨ GERAR MENSAGEM PROFUNDA"):
        mensagem_viva = gerar_texto_profundo(periodo)
        st.code(mensagem_viva, language="text")

# ==========================================
# ABA 4: VITRINES & HUB
# ==========================================
else:
    st.title("🔗 Minhas Vitrines Oficiais")
    for nome, url in LINKS.items():
        st.markdown(f"**{nome}**")
        st.code(url, language="text")