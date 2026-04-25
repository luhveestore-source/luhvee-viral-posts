import streamlit as st
import random
import json
import os
from datetime import datetime

st.set_page_config(page_title="👑 LuhVee Vendas PRO TURBINADO", layout="wide")

LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

ARQUIVO_HISTORICO = "luhvee_posts_historico.json"

st.title("👑 LuhVee Vendas PRO TURBINADO")
st.markdown("Copies AGRESSIVAS + CTAs PODEROSOS = MAIS VENDAS! 🔥💰")

# ===== FUNÇÕES =====

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_historico(posts):
    try:
        with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
    except:
        pass

def adicionar_ao_historico(produto, preco_promo, preco_original, estrategia, copies):
    historico = carregar_historico()
    novo_post = {
        "id": len(historico) + 1,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "produto": produto,
        "preco_promocional": preco_promo,
        "preco_original": preco_original,
        "estrategia": estrategia,
        "copies": copies
    }
    historico.append(novo_post)
    salvar_historico(historico)
    return novo_post

# ===== ESTRATÉGIAS TURBINADAS =====

# 1️⃣ URGÊNCIA (5 variações)
urgencia_wa = [
    "🚨🚨🚨 PROMOÇÃO RELÂMPAGO! 🚨🚨🚨\n\n{produto}\n\nDE R${preco_original} POR APENAS R${preco_promocional}!\n\n⏰ ⏰ ⏰ ACABANDO AGORA! ⏰ ⏰ ⏰\n\n❌ NÃO DEIXE PASSAR!\n\n👉 COMPRA AGORA: {link}\n\n🔥 ÚLTIMA CHANCE! 🔥\n\nLuhvee Stores ❤️",
    
    "⚡ ALERTA MEGA DESCONTO! ⚡\n\n{produto}\n\nERA R${preco_original} ➡️ AGORA R${preco_promocional}!\n\n⏳ O ESTOQUE TÁ VOANDO!\n\n🔴 SÉRIO, VAI FALTAR!\n\n👊 CLICA AQUI E COMPRA: {link}\n\n⚠️ ACABOU DEMAIS RÁPIDO SEMANA PASSADA ⚠️\n\nLuhvee Stores ❤️",
    
    "🎯 AVISO URGENTE! 🎯\n\n{produto}\n\n💥 PREÇO DE LOUCURA: R${preco_promocional}\n\nNORMAL: R${preco_original}\n\n✋ SÓ ENQUANTO TEM ESTOQUE!\n\n🏃 CORRE, NÃO VAI TER MAIS!\n\n➡️ VEM AQUI: {link}\n\nLuhvee Stores ❤️",
    
    "💣 BOMBA PROMOCIONAL 💣\n\n{produto} - R${preco_promocional}\n\nDesconto ABSURDO de R${preco_original}!\n\n⚡ LÁ SE VÃO! ⚡\n\nOLHA, ACABOU O SEU TAMANHO!\n\n🎁 VEM PEGAR O SEU: {link}\n\n👈 CLICA AGORA MESMO!\n\nLuhvee Stores ❤️",
    
    "🔥 FOGO 🔥 FOGO 🔥\n\n{produto}\n\nR${preco_promocional} ÓH MEUS DEUS!\n\nNÃO É BRINCADEIRA!\n\nNÃO DEIXA FALTAR PRO SEU!\n\n☎️ VEM JÁ: {link}\n\nACABANDO AGORA!\n\nLuhvee Stores ❤️"
]

urgencia_ig = [
    "🚨 ALERTA 🚨\n\n{produto}\n\nDE R${preco_original} 😱\nPOR R${preco_promocional}! 🤯\n\n⏰ SEMANA QUE VEM NÃO TEM!\n\n🛍️ {link}\n\n#OfertaDoAno #NãoPerde #Urgente #LuhVee",
    
    "⚡ MEGA OFERTA ⚡\n\n{produto}\n\nESTÁ SAINDO POR ESSA MIXARIA!\n\nR${preco_promocional}!!! 💰\n\n👉 NÃO DEIXA PASSAR\n\n🎯 {link}\n\n#PromoAmaldiçoada #VaiAcabar #ShopeeBrasil",
    
    "🔥 IMPERDÍVEL 🔥\n\n{produto}\n\nDESCONTO QUE DURA POUCO!\n\nR${preco_promocional} 🎉\n\n⏳ CLICA AGORA!\n\n👆 {link}\n\n#OfertaMaluca #NãoDeixa #Luhvee"
]

urgencia_fb = [
    "🚨 AVISO IMPORTANTE! 🚨\n\n{produto}\n\nDE R${preco_original} PARA APENAS R${preco_promocional}!!!\n\n⏰ ÚLTIMA CHANCE! ⏰\n\nNÃO DEIXE FALTAR!\n\n👉 COMPRA AGORA: {link}\n\n🔥 ESTOQUE LIMITADÍSSIMO! 🔥\n\nLuhvee Stores ❤️",
    
    "BOMBA 💣 DE DESCONTO!\n\n{produto}\n\nR${preco_promocional}!!!\n\nNÃO É FAKE!\n\n⚡ CLICA ANTES QUE ACABE ⚡\n\n{link}\n\nLuhvee Stores ❤️"
]

# 2️⃣ FOMO - Fear of Missing Out (5 variações)
fomo_wa = [
    "😱 ENQUANTO VOCÊ LÊ ISSO, ALGUÉM JÁ PEGOU! 😱\n\n{produto}\n\nJÁ SAIU DA MODA!\n\nVAI FICAR COM INVEJA!\n\nR${preco_promocional} 💸\n\n👉 NÃO FICA PRÁ TRÁS: {link}\n\n🔴 TEUS AMIGAS JÁ COMPRARAM!\n\nLuhvee Stores ❤️",
    
    "🚀 OMG!! 🚀\n\n{produto}\n\nTODO MUNDO TALKANDO DISSO!\n\nSÓ VOCÊ SEM?\n\nR${preco_promocional}\n\n👇 VEM SER LEGAL: {link}\n\n⚠️ VAI FICAR PARA TRÁS!\n\nLuhvee Stores ❤️",
    
    "🤔 VOCÊ JÁ VIU?\n\n{produto}\n\nTÁ NA BOCA DE TODOS!\n\nTODAS AS INFLUENCERS TÃO COM!\n\nVOCÊ VAI SER A ÚLTIMA?\n\n😰 R${preco_promocional} AQUI: {link}\n\n🔥 RÁPIDO! 🔥\n\nLuhvee Stores ❤️",
    
    "💥 VIROU FEBRE! 💥\n\n{produto}\n\nNÃO TEM MAIS NINGUÉM SEM!\n\nSÓ VOCÊ FALTANDO!\n\nR${preco_promocional} (EU COMPREI 3!)\n\n👉 {link}\n\n⏰ ANTES QUE ACABE\n\nLuhvee Stores ❤️",
    
    "🌟 TRENDING TOPIC 🌟\n\n{produto}\n\nTÁ EXPLODINDO NA INTERNET!\n\nTODOS COMENTANDO SOBRE!\n\nVOCÊ AINDA NÃO TEM?\n\n😅 R${preco_promocional}: {link}\n\nLuhvee Stores ❤️"
]

fomo_ig = [
    "😱 AVISO! 😱\n\n{produto}\n\nCAI NA TIMELINE E NÃO SAÍ!\n\nTODO MUNDO COM ESSE!\n\nVAI FICAR DESATUALIZADA?\n\n🛍️ R${preco_promocional}\n\n{link}\n\n#TodoMundoTem #VoceNão #VaiAcabar",
    
    "🔴 BREAKING NEWS 🔴\n\n{produto}\n\nVIRALIZOU MESMO!\n\nTODAS COMPRANDO!\n\n💰 R${preco_promocional}\n\n👇 {link}\n\n#Trending #VaiAcabar #Luhvee",
    
    "⚡ HOT ALERT ⚡\n\n{produto}\n\nESTE MOMENTO TEM GENTE COMPRANDO!\n\nVocê quer ficar de fora?\n\n👉 {link}\n\n#NãoFicaParaTrás #Luhvee"
]

fomo_fb = [
    "😱 CUIDADO!! 😱\n\n{produto}\n\nSUA MÃESINHA JÁ PEDIU!\n\nSUA MELHOR AMIGA JÁ COMPROU!\n\nVOCÊ VAI SER A ÚLTIMA?\n\nR${preco_promocional} AQUI: {link}\n\n⚠️ ACORDAAAA! ⚠️\n\nLuhvee Stores ❤️",
    
    "👀 OLHA ISSO 👀\n\n{produto}\n\nJÁ SAIU DO ESTOQUE 3 VEZES!\n\nTANTA PROCURA!\n\nNÃO FICA DE FORA!\n\n👉 {link}\n\nR${preco_promocional}\n\nLuhvee Stores ❤️"
]

# 3️⃣ DESCONTO - Foco em Economia (5 variações)
desconto_wa = [
    "💰 MATEMÁTICA SIMPLES 💰\n\n{produto}\n\nERA: R${preco_original}\nAGORA: R${preco_promocional}\n\n✂️ ECONOMIZA MUITO!\n\n🎉 CLICA E COMPRA: {link}\n\n👊 NÃO VAI ACHAR MAIS BARATO!\n\nLuhvee Stores ❤️",
    
    "🤑 DINHEIRO NOS BOLSOS! 🤑\n\n{produto}\n\nDESCONTO QUE FAZ DIFERENÇA!\n\nR${preco_promocional} É ROUBO!\n\n💸 ANTES DE TERMINAR: {link}\n\n⚡ ESSE PREÇO NÃO VOLTA!\n\nLuhvee Stores ❤️",
    
    "💎 ACHADO DO DIA! 💎\n\n{produto}\n\nTÃO BOM QUE PARECE FAKE!\n\nMAS NÃO É!\n\nR${preco_promocional} 🎊\n\n👉 APROVEITA: {link}\n\nLuhvee Stores ❤️",
    
    "🏆 MELHOR PREÇO GARANTIDO 🏆\n\n{produto}\n\nR${preco_promocional}\n\nPROCUREI EM TODO LUGAR!\n\nNÃO TEM MAIS BARATO!\n\n{link}\n\n💯 CONFIÁVELLL\n\nLuhvee Stores ❤️",
    
    "💵 ECONOMIA QUE SOBRA! 💵\n\n{produto}\n\nDEIXA DINHEIRO NO BOLSO!\n\nPRÉMIO IMPERDÍVEL!\n\nR${preco_promocional}\n\n🛒 COMPRA JÁ: {link}\n\nLuhvee Stores ❤️"
]

desconto_ig = [
    "💸 BARATEZA 💸\n\n{produto}\n\nERA R${preco_original}\nAGORA R${preco_promocional}!\n\n💰 ECONOMIA QUE CABE NA CONTA\n\n👇 {link}\n\n#SuperOferta #EconomiaDinheiro",
    
    "🤑 PREÇO INSANO 🤑\n\n{produto}\n\nNÃO ACREDITA NOS OLHOS!\n\nR${preco_promocional}!!\n\n👉 {link}\n\n#MelhorPreço #ShopeeBrasil",
    
    "💎 ACHADO DOOOOO DIA 💎\n\n{produto}\n\nR${preco_promocional}\n\nNÃO É BRINCADEIRA!\n\n🎉 {link}\n\n#Descontaço #Luhvee"
]

desconto_fb = [
    "💰 SOBRA GRANA! 💰\n\n{produto}\n\nDE R${preco_original} POR R${preco_promocional}!\n\nQUASE BRINDE!\n\n👉 APROVEITA: {link}\n\n🎁 PRESENTE PARA SI MESMA!\n\nLuhvee Stores ❤️",
    
    "💸 ACHADO RARO! 💸\n\n{produto}\n\nESSE PREÇO TÁ INSANO!\n\nR${preco_promocional} É ROUBO!\n\n{link}\n\nLuhvee Stores ❤️"
]

# 4️⃣ SOCIAL PROOF - Aprovação Social (5 variações)
social_wa = [
    "👥 CENTENAS AMANDO! 👥\n\n{produto}\n\n⭐⭐⭐⭐⭐ APROVADÍSSIMO!\n\nTODO MUNDO RECOMENDA!\n\nR${preco_promocional}\n\n👉 VOCÊ JÁ PEGOU? {link}\n\n✨ REFERÊNCIA DE QUALIDADE ✨\n\nLuhvee Stores ❤️",
    
    "💯 MELHOR DO MERCADO 💯\n\n{produto}\n\nMIL PESSOAS FALARAM BEM!\n\nNÃO TEM CRÍTICA!\n\nR${preco_promocional}\n\n🎯 COMPRA SEGURO: {link}\n\n👍 TESTADO E APROVADO!\n\nLuhvee Stores ❤️",
    
    "🌟 QUERIDINHA DO POVO 🌟\n\n{produto}\n\nSEUS AMIGOS JÁ TÊMLOVE!\n\nTODOS VOLTAVAM A COMPRAR!\n\nR${preco_promocional}\n\n👊 NÃO TEM ARREPENDIDA: {link}\n\nLuhvee Stores ❤️",
    
    "✅ 5 ESTRELAS ✅\n\n{produto}\n\nMIL CLIENTES SATISFEITOS!\n\n\"CHEGOU RÁPIDO!\"\n\"PRODUTO MUITO BOM!\"\n\"VALEU A PENA!\"\n\nR${preco_promocional}\n\n👉 VIRA VOCÊ TAMBÉM! {link}\n\nLuhvee Stores ❤️",
    
    "🎖️ CAMPEÃO DE VENDAS 🎖️\n\n{produto}\n\nMAIS PEDIDO DO MÊS!\n\nEVIDÊNCIA DE QUALIDADE!\n\nR${preco_promocional}\n\n💪 BORA? {link}\n\nLuhvee Stores ❤️"
]

social_ig = [
    "👑 QUERIDINHA DEMAIS 👑\n\n{produto}\n\nTODO MUNDO TEM E AMA!\n\n⭐⭐⭐⭐⭐\n\nR${preco_promocional}\n\n👇 {link}\n\n#Recomendado #MilAprovações",
    
    "💯 PROVA VIVA 💯\n\n{produto}\n\nMIL PESSOAS FELIZES!\n\nZERO ARREPENDIDA!\n\n👉 {link}\n\n#Qualidade #Recomendo",
    
    "🏆 #1 MAIS PEDIDO 🏆\n\n{produto}\n\nTODO MUNDO QUERENDO!\n\n⭐⭐⭐⭐⭐\n\n{link}\n\n#Luhvee #TopVendas"
]

social_fb = [
    "👨‍👩‍👧‍👦 FAMÍLIA TODO PEDINDO! 👨‍👩‍👧‍👦\n\n{produto}\n\nATÉ A MÃE QUER!\n\nTODO MUNDO INDICA!\n\n⭐⭐⭐⭐⭐ NOTA 10!\n\nR${preco_promocional}\n\n👉 CONFIA: {link}\n\nLuhvee Stores ❤️",
    
    "✨ QUERIDINHO DEMAIS ✨\n\n{produto}\n\nTODOS AMAM MESMO!\n\nMIL APROVAÇÕES!\n\nR${preco_promocional}\n\n{link}\n\nLuhvee Stores ❤️"
]

# 5️⃣ EXCLUSIVIDADE - Ser Especial (5 variações)
exclusivo_wa = [
    "👑 PARA GENTE VIP! 👑\n\n{produto}\n\nNÃO É PARA TODO MUNDO!\n\nSÓ PESSOAS COM BOM GOSTO!\n\nR${preco_promocional}\n\n💎 VOCÊ MERECE: {link}\n\n✨ SER ESPECIAL CUSTA CARO ✨\n\nLuhvee Stores ❤️",
    
    "🎩 EXCLUSIVIDADE! 🎩\n\n{produto}\n\nPOUCA GENTE TEM!\n\nVOCÊ PODE SER UMA DELAS!\n\nR${preco_promocional}\n\n👜 PEGUE O SEU: {link}\n\nLuhvee Stores ❤️",
    
    "💫 SELECIONADO A DEDO! 💫\n\n{produto}\n\nNÃO QUALQUER UM TEM!\n\nSÓ AS MELHORES CLIENTES!\n\nR${preco_promocional}\n\n🌟 VOCÊ TÁ INCLUÍDA? {link}\n\nLuhvee Stores ❤️",
    
    "🌹 BELEZA QUE FAZ DIFERENÇA 🌹\n\n{produto}\n\nPESSOAS CHIQUES AMAM!\n\nSE QUISER SER NOTADA!\n\nR${preco_promocional}\n\n👑 COMPRA AGORA: {link}\n\nLuhvee Stores ❤️",
    
    "💼 CLASSE GARANTIDA 💼\n\n{produto}\n\nSÓ AS MELHORES!\n\nVOCÊ MERECE!\n\nR${preco_promocional}\n\n✨ {link}\n\nLuhvee Stores ❤️"
]

exclusivo_ig = [
    "👑 COISA DE GENTE CHIQUE 👑\n\n{produto}\n\nNEM TODO MUNDO TEM!\n\nR${preco_promocional}\n\n💎 {link}\n\n#Exclusivo #Classe #VIP",
    
    "✨ BELEZA PURA ✨\n\n{produto}\n\nSÓ AS MELHORES USAM!\n\n👑 R${preco_promocional}\n\n{link}\n\n#Exclusividade #Luhvee",
    
    "🌟 DESTAQUE GARANTIDO 🌟\n\n{produto}\n\nSER NOTADA COM ESSE!\n\nR${preco_promocional}\n\n👇 {link}\n\n#Classe #Sofisticação"
]

exclusivo_fb = [
    "💎 COISA DE RICO! 💎\n\n{produto}\n\nPESSOAS COM BOM GOSTO AMAM!\n\nTIRAZU DIFERENTE!\n\nR${preco_promocional}\n\n👑 SER VIP: {link}\n\nLuhvee Stores ❤️",
    
    "🌟 VOCÊ MERECE! 🌟\n\n{produto}\n\nSÓ O MELHOR PRO MELHOR!\n\nR${preco_promocional}\n\n✨ {link}\n\nLuhvee Stores ❤️"
]

# 6️⃣ CURIOSIDADE - Gera Interesse (5 variações)
curiosidade_wa = [
    "🤔 QUER SABER O SEGREDO? 🤔\n\n{produto}\n\nTODO MUNDO TÁ FALANDO DISSO!\n\nEU JÁ DESCOBRI!\n\nR${preco_promocional}\n\n👉 VOCÊ TAMBÉM QUER? {link}\n\n🔥 É NOVO! É BOMMMM!\n\nLuhvee Stores ❤️",
    
    "❓ DESCOBRI UMA COISA... ❓\n\n{produto}\n\nQUE TÁ MUDANDO A VIDA!\n\nQUER VER?\n\nR${preco_promocional}\n\n👇 CLICA AQUI: {link}\n\n💥 VAI TE SURPREENDER!\n\nLuhvee Stores ❤️",
    
    "🎁 ACHAS QUE JÁ CONHECES? 🎁\n\n{produto}\n\nPENSA DE NOVO!\n\nTEM COISA QUE NÃO SABES!\n\nR${preco_promocional}\n\n🔍 DESCOBRE COMIGO: {link}\n\nLuhvee Stores ❤️",
    
    "✨ ACHEI ISSO! ✨\n\n{produto}\n\nE NÃO CONSIGO PARAR DE USAR!\n\nVIROU ESSENCIAL!\n\nR${preco_promocional}\n\n👉 {link}\n\n🤯 MUDA TUA VIDA!\n\nLuhvee Stores ❤️",
    
    "🚀 NOVO NÍVEL! 🚀\n\n{produto}\n\nCOMEÇOU A FAZER TREND!\n\nE TÁ ARREBENTANDO!\n\nR${preco_promocional}\n\n💪 VEM TAMBÉM: {link}\n\nLuhvee Stores ❤️"
]

curiosidade_ig = [
    "🔮 O QUE VOCÊ VAI DESCOBRIR 🔮\n\n{produto}\n\nQUE MUDA TUDO!\n\nR${preco_promocional}\n\n👉 {link}\n\n#Descoberta #NovaNível",
    
    "✨ ACHADO ESPECIAL ✨\n\n{produto}\n\nQUE NÃO SABES QUE PRECISAVAS!\n\nR${preco_promocional}\n\n🎁 {link}\n\n#Achado #Luhvee",
    
    "🤔 SÉRIO? 🤔\n\n{produto}\n\nISTO É NOVO NÍVEL!\n\nR${preco_promocional}\n\n👇 {link}\n\n#Trending #Descoberta"
]

curiosidade_fb = [
    "🔍 DESCOBRI ISTO! 🔍\n\n{produto}\n\nE NÃO CONSIGO PARAR DE FALAR!\n\nTODOS TÃO QUERENDO!\n\nR${preco_promocional}\n\n👉 VIRA TU TAMBÉM: {link}\n\nLuhvee Stores ❤️",
    
    "💡 NOVA DESCOBERTA! 💡\n\n{produto}\n\nQUE TÁ FAZENDO SUCESSO!\n\nR${preco_promocional}\n\n👇 {link}\n\nLuhvee Stores ❤️"
]

ESTRATEGIAS = {
    "🚨 Urgência": {
        "whatsapp": urgencia_wa,
        "instagram": urgencia_ig,
        "facebook": urgencia_fb
    },
    "😱 FOMO": {
        "whatsapp": fomo_wa,
        "instagram": fomo_ig,
        "facebook": fomo_fb
    },
    "💰 Desconto": {
        "whatsapp": desconto_wa,
        "instagram": desconto_ig,
        "facebook": desconto_fb
    },
    "⭐ Social Proof": {
        "whatsapp": social_wa,
        "instagram": social_ig,
        "facebook": social_fb
    },
    "👑 Exclusividade": {
        "whatsapp": exclusivo_wa,
        "instagram": exclusivo_ig,
        "facebook": exclusivo_fb
    },
    "🤔 Curiosidade": {
        "whatsapp": curiosidade_wa,
        "instagram": curiosidade_ig,
        "facebook": curiosidade_fb
    },
}

def gerar_copies(produto, preco_promo, preco_original, estrategia, plataforma, link):
    templates = ESTRATEGIAS[estrategia][plataforma]
    random.shuffle(templates)
    copies = []
    for template in templates:
        copy = template.format(
            produto=produto,
            preco_original=preco_original,
            preco_promocional=preco_promo,
            link=link
        )
        copies.append(copy)
    return copies

# ===== INTERFACE =====

tab1, tab2, tab3 = st.tabs(["📝 Gerar Copies", "📊 Histórico", "ℹ️ Info"])

with tab1:
    st.subheader("⚙️ Dados do Produto")
    
    col1, col2 = st.columns(2)
    with col1:
        nome_produto = st.text_input(
            "Nome do Produto",
            placeholder="Ex: Bolsa De Ombro Premium"
        )
        categoria = st.selectbox("Categoria", ["Casa", "Beleza", "Tech", "Pet", "Moda"])
    
    with col2:
        preco_original = st.text_input(
            "Preço Original",
            placeholder="150.00"
        )
        preco_promocional = st.text_input(
            "Preço Promocional",
            placeholder="89.90"
        )
    
    st.divider()
    st.subheader("🎯 Configuração")
    
    col3, col4 = st.columns(2)
    with col3:
        estrategia = st.selectbox(
            "Escolha a Estratégia",
            list(ESTRATEGIAS.keys())
        )
    
    with col4:
        plataforma_venda = st.radio(
            "Onde vai vender?",
            ["Shopee", "Mercado Livre", "Hub"],
            horizontal=True
        )
    
    link_escolhido = {
        "Shopee": LINK_SHOPEE,
        "Mercado Livre": LINK_ML,
        "Hub": LINK_HUB
    }[plataforma_venda]
    
    if st.button("✨ GERAR COPIES TURBINADAS", use_container_width=True, type="primary"):
        if nome_produto and preco_promocional:
            
            copies_wa = gerar_copies(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                "whatsapp",
                link_escolhido
            )
            
            copies_ig = gerar_copies(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                "instagram",
                link_escolhido
            )
            
            copies_fb = gerar_copies(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                "facebook",
                link_escolhido
            )
            
            novo_post = adicionar_ao_historico(
                nome_produto,
                preco_promocional,
                preco_original,
                estrategia,
                {
                    "whatsapp": copies_wa,
                    "instagram": copies_ig,
                    "facebook": copies_fb
                }
            )
            
            st.success(f"✅ Post #{novo_post['id']} TURBINADO criado! 🔥")
            st.divider()
            
            tab_wa, tab_ig, tab_fb = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
            
            with tab_wa:
                st.subheader("🔥 Cópias AGRESSIVAS para WhatsApp")
                for i, copy in enumerate(copies_wa, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i} - Customize se quiser!")
                    if i < len(copies_wa):
                        st.divider()
            
            with tab_ig:
                st.subheader("💥 Cópias para Instagram Stories/Feed")
                for i, copy in enumerate(copies_ig, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    if i < len(copies_ig):
                        st.divider()
            
            with tab_fb:
                st.subheader("⚡ Cópias para Facebook Groups")
                for i, copy in enumerate(copies_fb, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    if i < len(copies_fb):
                        st.divider()
        
        else:
            st.error("❌ Preencha o Nome do Produto e Preço Promocional!")

with tab2:
    st.subheader("📊 Histórico de Posts")
    
    historico = carregar_historico()
    
    if historico:
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        
        with col_stat1:
            st.metric("Total de Posts", len(historico))
        
        with col_stat2:
            st.metric("Último Post", historico[-1]["data"])
        
        with col_stat3:
            st.metric("Estratégia Mais Usada", historico[-1]["estrategia"])
        
        st.divider()
        
        for post in reversed(historico):
            with st.expander(f"#{post['id']} - {post['produto']} ({post['data']})"):
                
                col_info1, col_info2, col_info3 = st.columns(3)
                
                with col_info1:
                    st.metric("Estratégia", post['estrategia'])
                
                with col_info2:
                    st.metric("Preço Promo", f"R$ {post['preco_promocional']}")
                
                with col_info3:
                    st.metric("Preço Original", f"R$ {post['preco_original']}")
                
                st.divider()
                
                st.subheader("Copies Salvas:")
                
                if "copies" in post and isinstance(post["copies"], dict):
                    if "whatsapp" in post["copies"]:
                        st.subheader("📱 WhatsApp")
                        for copy in post["copies"]["whatsapp"]:
                            st.code(copy, language="text")
                    
                    if "instagram" in post["copies"]:
                        st.subheader("📸 Instagram")
                        for copy in post["copies"]["instagram"]:
                            st.code(copy, language="text")
                    
                    if "facebook" in post["copies"]:
                        st.subheader("👥 Facebook")
                        for copy in post["copies"]["facebook"]:
                            st.code(copy, language="text")
                
                st.divider()
                
                if st.button(f"🗑️ Deletar Post #{post['id']}", key=f"delete_{post['id']}"):
                    historico.remove(post)
                    salvar_historico(historico)
                    st.success("Post deletado!")
                    st.rerun()
    
    else:
        st.info("📭 Nenhum post no histórico ainda!")

with tab3:
    st.markdown("""
    ### 👑 LuhVee Vendas PRO TURBINADO
    
    **O QUE MUDOU:**
    - 🔥 Copies 10x MAIS AGRESSIVAS
    - 💪 CTAs PODEROSOS em cada copy
    - 📊 5 variações por estratégia (NÃO IGUAIS)
    - 💰 Foco em CONVERSÃO e VENDAS
    - ⚡ Linguagem que VENDE
    
    **6 ESTRATÉGIAS TURBINADAS:**
    
    1. 🚨 **Urgência** - COMPRA AGORA! ÚLTIMO ESTOQUE!
    2. 😱 **FOMO** - TODO MUNDO TEM! VOCÊ VAI FICAR PARA TRÁS?
    3. 💰 **Desconto** - ECONOMIZA MUITO! ESSE PREÇO NÃO VOLTA!
    4. ⭐ **Social Proof** - MIL PESSOAS APROVARAM! CENTENAS AMANDO!
    5. 👑 **Exclusividade** - PARA GENTE VIP! SÓ AS MELHORES!
    6. 🤔 **Curiosidade** - DESCOBRI ISTO! NÃO CONSIGO PARAR!
    
    **DICAS PRA TURBINAR AINDA MAIS:**
    
    - Use emojis estratégicos (aumenta CTR)
    - Repita o CTA (CLICA AGORA, COMPRA JÁ)
    - Use CAPS para urgência
    - Coloca números (R$, %)
    - Cria escassez (ÚLTIMO, ESTOQUE LIMITADO)
    - Aproveita social proof (MIL PESSOAS)
    
    **MELHOR ESTRATÉGIA POR CANAL:**
    - WhatsApp → Urgência (CTAs diretos)
    - Instagram → FOMO (Vira viral)
    - Facebook → Social Proof (Grupos comentam)
    
    ---
    
    **Luhvee Stores ❤️**
    """)

st.divider()
st.caption("👑 LuhVee Vendas PRO TURBINADO - Com Agressividade e CTAs Poderosos | Luhvee Stores ❤️")
