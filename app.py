import streamlit as st
import random
from itertools import cycle

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="👑 LuhVee Vendas Turbo", layout="wide")

# 🔗 SEUS LINKS
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

st.title("👑 LuhVee Vendas Turbo - Multicanal Pro")
st.markdown("Gere copies estratégicas otimizadas para WhatsApp, Instagram e Facebook! 🚀")

# ===== BANCO DE DADOS DE PRODUTOS =====

# Descrições por categoria (para enriquecer as mensagens)
descricoes_categoria = {
    "Casa": {
        "adjetivos": ["prático", "funcional", "moderno", "elegante", "resistente"],
        "beneficios": ["economiza espaço", "facilita o dia a dia", "dura anos", "vale muito a pena", "muda sua rotina"]
    },
    "Beleza": {
        "adjetivos": ["poderoso", "eficaz", "natural", "profissional", "transformador"],
        "beneficios": ["deixa você mais linda", "resultado garantido", "pele impecável", "cabelo dos sonhos", "valor de salão"]
    },
    "Tech": {
        "adjetivos": ["inovador", "inteligente", "poderoso", "fácil de usar", "essencial"],
        "beneficios": ["facilita a vida", "aumenta produtividade", "super prático", "tecnologia pura", "vida mais fácil"]
    },
    "Pet": {
        "adjetivos": ["confortável", "seguro", "carinhoso", "prático", "especial"],
        "beneficios": ["pet ama", "conforto máximo", "saúde do seu pet", "qualidade premium", "amor e cuidado"]
    },
    "Moda": {
        "adjetivos": ["estiloso", "trendy", "elegante", "confortável", "versátil"],
        "beneficios": ["transforma o look", "combina com tudo", "estilo garantido", "trend do momento", "clássico sempre"]
    },
    "Alimentos": {
        "adjetivos": ["delicioso", "saudável", "fresco", "premium", "natural"],
        "beneficios": ["vicia", "pra toda família", "sabor perfeito", "qualidade máxima", "vale cada centavo"]
    }
}

# ===== ESTRATÉGIAS DE VENDAS =====

# ESTRATÉGIA 1: URGÊNCIA
urgencia_whatsapp = [
    "🚨 PROMOÇÃO RELÂMPAGO! {produto} com DESCONTO ABSURDO!\n\nDe R${preco_original} por APENAS R${preco_promocional}\n\n⏰ *TÁ ACABANDO!*\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "⚡ ATENÇÃO! {produto} saiu na nossa loja!\n\nR${preco_promocional} (Era R${preco_original})\n\n⏳ Estoque LIMITADO! Não vai durar!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "🔥 CORRE! {produto} está VOANDO!\n\nPreço de R${preco_promocional} (Tá barato demais!)\n\n⚠️ Próxima rodada pode sair mais caro!\n\n{link}\n\nBjs da Luh da LuhVee ❤️"
]

urgencia_instagram = [
    "🚨 ALERTA DE OFERTA URGENTE! 🚨\n\n{produto} QUEBRANDO PREÇO!\n\nDe R${preco_original} por APENAS R${preco_promocional}! 😱\n\n⏰ Tá saindo rápido demais!\n\n🛒 Corra pro link na BIO!\n{link}\n\n#ofertas #promoção #shopeebrasil #mercadolivre #urgente #luhvee",
    "🔥 GRITANDO AQUI! {produto} em PROMOÇÃO DOIDA!\n\n💰 R${preco_promocional} só por hoje!\n\n⚡ Depois dessa preço volta ao normal!\n\n👉 Link na BIO, corre!\n\n#achadinhos #desconto #deals #luhveestores",
    "⏳ ATENÇÃO PESSOAL! {produto} está VIRALIZANDO!\n\n🛍️ Só R${preco_promocional}! Tá barato?\n\n⚠️ Tá sumindo do estoque!\n\n🔗 Bora? {link}\n\n#promoção #shopeebrasil #mercadolivre #ofertasdo #luhvee"
]

urgencia_facebook = [
    "🚨 PROMOÇÃO FLASH ACONTECENDO AGORA! 🚨\n\n{produto} COM DESCONTO BRUTAL!\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n⏰ *ESTOQUE LIMITADO!* Não vai durar muito tempo!\n\n✅ Compra 100% Segura\n✅ Entrega Rápida\n\nCORRA e garanta o seu: {link}\n\n#promoção #oferta #luhveestores",
    "⚡ ALERTA! {produto} DESAPARECENDO!\n\nPreço abaixou para R${preco_promocional}! (Antes era R${preco_original})\n\n⏳ Tá acabando estoque!\n\nNão deixa passar essa! {link}\n\nBjs da Luh da LuhVee ❤️",
]

# ESTRATÉGIA 2: FOMO (Fear of Missing Out)
fomo_whatsapp = [
    "😱 ENQUANTO VOCÊ LÊ, ALGUÉM JÁ PEGOU!\n\n{produto} está SUMINDO da loja!\n\nR${preco_promocional} (Era R${preco_original})\n\n🔥 Será que você quer ficar de fora?\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "👀 VIU? MAIS UM(A) COMPROU {produto}!\n\nTodos estão descobrindo essa oferta!\n\nR${preco_promocional} só enquanto durar!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "🤦‍♀️ TODO MUNDO JÁ PEGOU!\n\n{produto} é aquele que NÃO PODE FALTAR!\n\nPor R${preco_promocional} está ROUBO!\n\n{link}\n\nBjs da Luh da LuhVee ❤️"
]

fomo_instagram = [
    "👀 VIRA ESSA VOLTA QUE TEM MAIS!\n\n{produto} VIRALIZOU! 😱\n\nTodos estão falando! Será que você quer ficar de fora?\n\n💰 R${preco_promocional}\n\n🔗 Corre pro link na BIO antes que acabe!\n\n#viral #trending #luhveestores #shopeebrasil #oferta",
    "😭 NÃO SEJA A ÚLTIMA A SABER!\n\n{produto} está na boca de todos!\n\nSeu amigo já pegou! Você quer?\n\n🛍️ R${preco_promocional}\n\n👉 Link na BIO! {link}\n\n#luhvee #estilo #imperdível #ofertasdodia",
    "🔥 AVISO: {produto} ESTÁ VIRANDO SAUDADE!\n\nTodo mundo quer! Você vai ficar vendo os outros usando?\n\n💳 R${preco_promocional}\n\n⚡ Clica no link: {link}\n\n#achadinhos #promoção #luhveestores"
]

fomo_facebook = [
    "😱 GENTE, OLHA SÓ! {produto} ESTÁ NA BOCA DE TODOS!\n\nTodos estão comprando! Você quer ficar de fora?\n\nR${preco_promocional} (De R${preco_original})\n\n🤦‍♀️ Não seja a última a descobrir!\n\nGaranta aqui: {link}\n\nBjs da Luh da LuhVee ❤️",
    "👀 VIRA ESSA VOLTA! {produto} está SUMINDO!\n\nTodo mundo quer pegar! Corre que a gente avisa quando voltar!\n\n💰 R${preco_promocional}\n\n{link}\n\n#ofertas #shopeebrasil #mercadolivre",
]

# ESTRATÉGIA 3: DESCONTO/ECONOMIA
desconto_whatsapp = [
    "💰 ACHADO DEMAIS! {produto} em PROMOÇÃO!\n\nSAI DE R${preco_original} por APENAS R${preco_promocional}! 🎉\n\nEconomiza MUITO assim! 💸\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "🤑 GRANA GUARDADA! {produto} está barato!\n\nDe R${preco_original} por R${preco_promocional}!\n\nQualidade + Preço = Sucesso! ✅\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "💵 SEU BOLSO VIA FELIZ! {produto} com desconto!\n\nR${preco_promocional} (Custa R${preco_original} em outro lugar!)\n\nQualidade garantida! 👍\n\n{link}\n\nBjs da Luh da LuhVee ❤️"
]

desconto_instagram = [
    "💰 QUER ECONOMIZAR? {produto} TÁ NA PROMOÇÃO!\n\nDe R${preco_original} por R${preco_promocional}! 🎉\n\n💳 Qualidade sem esvaziar o bolso!\n\n🛒 Corra pra BIO! {link}\n\n#desconto #economia #oferta #luhveestores #shopeebrasil #mercadolivre",
    "🤑 ECONOMIZA PRA CARAMBA! {produto}\n\nR${preco_promocional} (ANTES ERA R${preco_original}!) 😱\n\n✨ Qualidade + Preço = Melhor combinação!\n\n👉 {link}\n\n#achadinhos #desconto #promoção #luhvee",
    "💵 BOLSA AGRADECE! {produto} em DESCONTO!\n\nR${preco_promocional} é ROUBO de preço!\n\n💎 Qualidade garantida, preço amigo!\n\n🔗 Link na BIO! {link}\n\n#economia #desconto #oferta #compras"
]

desconto_facebook = [
    "💰 ECONOMIZA DEMAIS! {produto} em PROMOÇÃO ESPECIAL!\n\nDe R${preco_original} por APENAS R${preco_promocional}!\n\n✅ Qualidade Garantida\n✅ Preço Imbatível\n\nSua carteira agradece! 💳\n\nCompre aqui: {link}\n\nBjs da Luh da LuhVee ❤️",
    "🤑 DESCONTO QUE DUELE! {produto}\n\nR${preco_promocional} é BARATO!\n\nQualidade + Economia = Esse achado!\n\n{link}\n\n#promoção #desconto #oferta",
]

# ESTRATÉGIA 4: SOCIAL PROOF
social_whatsapp = [
    "⭐ TODO MUNDO AMANDO! {produto} é QUERIDINHO!\n\nJá tem CENTENAS de pessoas usando e AMANDO!\n\nR${preco_promocional} (Era R${preco_original})\n\n🌟 Você quer entrar nessa onda?\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "👥 RECOMENDAÇÃO QUE VEM CRESCENDO!\n\n{produto} está na lista dos MAIS VENDIDOS!\n\nAs pessoas JURAM por isso! 💯\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "✅ APROVADO POR MILHARES! {produto}\n\nQuem compra, VOLTA pra comprar de novo!\n\nReputação que vale OURO! 👍\n\nR${preco_promocional}\n\n{link}\n\nBjs da Luh da LuhVee ❤️"
]

social_instagram = [
    "⭐ APROVADO POR TODOS! {produto} é QUERIDO!\n\n💯 Centenas de clientes satisfeitos!\n\n🌟 As reviews não mentem! Veja só:\n\n💬 'Adorei!' 'Recomendo!' 'Vale muito!'\n\n💰 R${preco_promocional}\n\n🛒 Peça no DM ou link na BIO! {link}\n\n#recomendação #aprovado #luhveestores",
    "👑 BESTSELLER AQUI! {produto}\n\n✨ Quem compra volta pra comprar mais!\n\n💬 Reviews incríveis de quem usa!\n\n💳 R${preco_promocional}\n\n🔗 {link}\n\n#bestseller #aprovado #luhvee #satisfação",
]

social_facebook = [
    "⭐ APROVADO E RECOMENDADO! {produto}\n\n✅ Centenas de clientes SATISFEITOS!\n✅ Reviews INCRÍVEIS!\n✅ Quem compra, volta pra comprar de novo!\n\nR${preco_promocional} (De R${preco_original})\n\n👍 Você também vai amar! Garanta o seu:\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
]

# ESTRATÉGIA 5: EXCLUSIVIDADE
exclusivo_whatsapp = [
    "👑 ACESSO EXCLUSIVO! {produto} é RARIDADE!\n\nSelecionado a dedo pra quem tem BOM GOSTO! 💎\n\nR${preco_promocional} (Lugar limitado!)\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "🔐 NEM TODO MUNDO CONSEGUE! {produto}\n\nAcesso restrito aos que entendem de QUALIDADE! 👑\n\nR${preco_promocional} só pra você!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "✨ VIP ALERT! {produto} para VOCÊ!\n\nEscolhido porque você TEM BUEN GOSTO!\n\nR${preco_promocional} (Lugar limitado!)\n\n{link}\n\nBjs da Luh da LuhVee ❤️"
]

exclusivo_instagram = [
    "👑 EXCLUSIVO! {produto} é SÓ PRA VOCÊ!\n\n✨ Selecionado com carinho pra quem tem bom gosto!\n\n💎 Qualidade que fala por si!\n\n💰 R${preco_promocional}\n\n🔗 Seu lugar é aqui! {link}\n\n#exclusivo #premium #luhveestores #qualidade #estilo",
    "🔐 NEM TODO MUNDO SABE! {produto}\n\n👑 Só pra quem conhece QUALIDADE!\n\n✨ Seu nível de exigência vai amar!\n\n💳 R${preco_promocional}\n\n{link}\n\n#premium #luhvee #qualidade #exclusivo",
]

exclusivo_facebook = [
    "👑 SELEÇÃO ESPECIAL! {produto}\n\n✨ Escolhido a dedo pra você que tem BOM GOSTO!\n\n💎 Qualidade que MERECIA cuidado!\n\nR${preco_promocional}\n\n👉 Acesso exclusivo aqui: {link}\n\nBjs da Luh da LuhVee ❤️",
]

# ESTRATÉGIA 6: CURIOSIDADE
curiosidade_whatsapp = [
    "🤔 ADIVINHA O QUÊ? {produto} CHEGOU!\n\nAquele que MUITO buscava está aqui! 🎉\n\nR${preco_promocional} (Só tem poucos!)\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "❓ SABE AQUELE {produto} QUE VOCÊ QUERIA?\n\n✨ Pois é... está AQUI AGORA!\n\nR${preco_promocional} pra você não perder!\n\n{link}\n\nBjs da Luh da LuhVee ❤️",
    "🔍 ENCONTREI! {produto} ESPECIAL!\n\nAquele tipo que faz TODA DIFERENÇA! 💫\n\nR${preco_promocional} (Enquanto durar!)\n\n{link}\n\nBjs da Luh da LuhVee ❤️"
]

curiosidade_instagram = [
    "🤔 ACHEI ALGO QUE VOCÊ VAI AMAR! {produto}\n\n✨ É daquele tipo que VICIA!\n\n💫 Qualidade + Estilo = Combinação perfeita!\n\n💰 R${preco_promocional}\n\n👉 Vem descobrir! {link}\n\n#achado #descoberta #luhveestores #estilo",
    "❓ JÁ PENSOU EM TER {produto}?\n\nPois é! Achei perfeito pra você! 😍\n\n✨ Vem conhecer!\n\n🛍️ R${preco_promocional}\n\n{link}\n\n#novidade #descoberta #luhvee #imperdível",
]

curiosidade_facebook = [
    "🤔 OLHA O QUE EU ENCONTREI! {produto}\n\n✨ É daquele tipo que VOCÊ VIM PROCURANDO!\n\nAquele que faz diferença na vida de quem compra!\n\nR${preco_promocional}\n\n👉 Descobre mais aqui: {link}\n\nBjs da Luh da LuhVee ❤️",
]

# Dicionário com todas as estratégias
ESTRATEGIAS = {
    "🚨 Urgência": {
        "whatsapp": urgencia_whatsapp,
        "instagram": urgencia_instagram,
        "facebook": urgencia_facebook
    },
    "😱 FOMO": {
        "whatsapp": fomo_whatsapp,
        "instagram": fomo_instagram,
        "facebook": fomo_facebook
    },
    "💰 Desconto": {
        "whatsapp": desconto_whatsapp,
        "instagram": desconto_instagram,
        "facebook": desconto_facebook
    },
    "⭐ Social Proof": {
        "whatsapp": social_whatsapp,
        "instagram": social_instagram,
        "facebook": social_facebook
    },
    "👑 Exclusividade": {
        "whatsapp": exclusivo_whatsapp,
        "instagram": exclusivo_instagram,
        "facebook": exclusivo_facebook
    },
    "🤔 Curiosidade": {
        "whatsapp": curiosidade_whatsapp,
        "instagram": curiosidade_instagram,
        "facebook": curiosidade_facebook
    }
}

# ===== FUNÇÕES =====

def gerar_copies(produto, preco_promo, preco_original, estrategia, plataforma, link):
    """Gera copies usando a estratégia escolhida"""
    templates = ESTRATEGIAS[estrategia][plataforma]
    
    # Embaralha para variedade
    random.shuffle(templates)
    
    copies_geradas = []
    for template in templates:
        copy = template.format(
            produto=produto,
            preco_original=preco_original,
            preco_promocional=preco_promo,
            link=link
        )
        copies_geradas.append(copy)
    
    return copies_geradas

def gerar_multiplos(produto, preco_promo, preco_original, estrategia, link, quantidade=3):
    """Gera múltiplas variações para A/B testing"""
    resultados = {}
    
    for canal in ["whatsapp", "instagram", "facebook"]:
        copies = gerar_copies(produto, preco_promo, preco_original, estrategia, canal, link)
        # Pega só a quantidade solicitada
        resultados[canal] = copies[:quantidade]
    
    return resultados

# ===== INTERFACE =====

st.markdown("---")

# Abas principais
tab1, tab2 = st.tabs(["📝 Gerar Copies", "📊 A/B Testing"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚙️ Dados do Produto")
        nome_produto = st.text_input("Nome do Produto", placeholder="Ex: Bolsa De Ombro")
        categoria = st.selectbox("Categoria", list(descricoes_categoria.keys()))
        
    with col2:
        st.subheader("💰 Preços")
        preco_promo = st.text_input("Preço Promocional", placeholder="R$ XX,XX")
        preco_original = st.text_input("Preço Original", placeholder="R$ XX,XX")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("🎯 Estratégia")
        estrategia = st.selectbox("Escolha a estratégia de venda:", list(ESTRATEGIAS.keys()))
    
    with col4:
        st.subheader("🛒 Plataforma")
        plataforma = st.radio("Onde vai vender?", 
                             ["Shopee", "Mercado Livre", "Hub"],
                             horizontal=True)
    
    link_selecionado = {
        "Shopee": LINK_SHOPEE,
        "Mercado Livre": LINK_ML,
        "Hub": LINK_HUB
    }[plataforma]
    
    if st.button("✨ GERAR COPIES", use_container_width=True, type="primary"):
        if nome_produto and preco_promo:
            copies = gerar_copies(
                nome_produto, 
                preco_promo, 
                preco_original, 
                estrategia, 
                "whatsapp",
                link_selecionado
            )
            
            # Abas por canal
            tab_w, tab_i, tab_f = st.tabs(["📱 WhatsApp", "📸 Instagram", "👥 Facebook"])
            
            with tab_w:
                st.subheader("Estilo para Grupos/Canais")
                copy_w = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "whatsapp", link_selecionado)
                for i, copy in enumerate(copy_w, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            
            with tab_i:
                st.subheader("Estilo para Feed/Stories")
                copy_i = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "instagram", link_selecionado)
                for i, copy in enumerate(copy_i, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            
            with tab_f:
                st.subheader("Estilo para Grupos/Timeline")
                copy_f = gerar_copies(nome_produto, preco_promo, preco_original, estrategia, "facebook", link_selecionado)
                for i, copy in enumerate(copy_f, 1):
                    st.code(copy, language="text")
                    st.caption(f"Variação {i}")
                    st.divider()
            
            # Stats
            st.divider()
            col_s1, col_s2, col_s3, col_s4 = st.columns(4)
            with col_s1:
                st.metric("Produto", nome_produto)
            with col_s2:
                st.metric("Estratégia", estrategia.split()[1])
            with col_s3:
                st.metric("Plataforma", plataforma)
            with col_s4:
                st.metric("Copies Geradas", "3 cada canal")
        
        else:
            st.error("Preencha o produto e preço promocional!")

with tab2:
    st.subheader("🧪 A/B Testing - Teste Múltiplas Estratégias")
    st.info("Gere várias estratégias ao mesmo tempo e teste qual converte mais!")
    
    col_test1, col_test2 = st.columns(2)
    
    with col_test1:
        st.text("Dados do Produto")
        nome_test = st.text_input("Nome do Produto", key="test_nome")
        preco_test = st.text_input("Preço Promo", key="test_preco")
    
    with col_test2:
        st.text("Estratégias a Testar")
        estrategias_selecionadas = st.multiselect(
            "Selecione 2-3 estratégias para comparar:",
            list(ESTRATEGIAS.keys()),
            max_selections=3
        )
    
    plat_test = st.radio("Plataforma", ["Shopee", "Mercado Livre", "Hub"], horizontal=True, key="test_plat")
    link_test = link_selecionado = {
        "Shopee": LINK_SHOPEE,
        "Mercado Livre": LINK_ML,
        "Hub": LINK_HUB
    }[plat_test]
    
    if st.button("🔄 COMPARAR ESTRATÉGIAS", use_container_width=True, type="primary"):
        if nome_test and preco_test and estrategias_selecionadas:
            for estrategia_selecionada in estrategias_selecionadas:
                st.subheader(f"{estrategia_selecionada} - WhatsApp")
                copy_test = gerar_copies(
                    nome_test,
                    preco_test,
                    "R$ XX,XX",
                    estrategia_selecionada,
                    "whatsapp",
                    link_test
                )[0]
                st.code(copy_test, language="text")
                st.caption("💡 Dica: Use a que mais combina com seu público!")
                st.divider()
        else:
            st.error("Preencha todos os campos e selecione estratégias!")

# Footer
st.divider()
st.caption("👑 LuhVee Vendas Turbo | Feito com 💖 para suas vendas bomberem | Bjs da Luh da LuhVee ❤️")
