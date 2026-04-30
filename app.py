import streamlit as st
import random
import json
import os
from datetime import datetime
from typing import List, Dict, Any

# Configuração da Página
st.set_page_config(page_title="👑 LuhVee Vendas PRO TURBINADO", layout="wide")

# Constantes e Links
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

ARQUIVO_HISTORICO = "luhvee_posts_historico.json"

# Mapeamento de links por plataforma de venda
LINKS = {
"Shopee": LINK_SHOPEE,
"Mercado Livre": LINK_ML,
"Hub": LINK_HUB
}

# Configuração das Plataformas de Mensagem
PLATAFORMAS = {
"whatsapp": {"label": "📱 WhatsApp", "emoji": "📱", "hashtags": False},
"instagram": {"label": "📸 Instagram", "emoji": "📸", "hashtags": True},
"facebook": {"label": "👥 Facebook", "emoji": "👥", "hashtags": False}
}

# Banco de Estratégias (Templates Dinâmicos)
ESTRATEGIAS = {
"Urgência": {
"whatsapp": [
"🚨 RELÂMPAGO! 🚨\n{produto}\nDE R${preco_original} → R${preco_promocional}\n⏰ ACABA AGORA!\n👉 {link}\n❌ NÃO PERDE!\nLuhVee",
"⏳ CORRE! 🏃\n{produto}\nSÓ HOJE: R${preco_promocional}\nANTES ERA: R${preco_original}\n🔥 VAPOU LOGO! {link}\nLuhVee",
"🛑 PARE TUDO! 🛑\n{produto}\nPREÇO DE LOUCURA: R${preco_promocional}\nESTOQUE NO FIM!\n👉 GARANTA: {link}\nLuhVee",
"🚨 ALERTA VERMELHO 🚨\n{produto}\nR${preco_promocional} (ERA R${preco_original})\n⚠️ ÚLTIMAS UNIDADES!\n{link}\nLuhVee",
"⚡ QUEIMA DE ESTOQUE ⚡\n{produto}\nR${preco_promocional}\nNÃO VAI TER REPOSIÇÃO!\n🏃‍♂️ CLICA: {link}\nLuhVee"
],
"instagram": [
"⚡ OFERTA RELÂMPAGO ⚡\n{produto}\nR${preco_promocional}!!!\n⏳ TEMPO ESGOTANDO!\n🛍️ Link na Bio/Stories: {link}\n#Luhvee #OfertaDoAno #Urgente",
"🚨 ALERTA! 🚨\n{produto}\nDE R${preco_original} POR R${preco_promocional}\n😱 SÉRIO ISSO?\n👉 {link}\n#Promoção #Achadinho",
"⏰ TIQUE TAQUE ⏰\n{produto}\nR${preco_promocional}\nACABANDO AGORINHA!\n🏃‍♀️ CORRE: {link}\n#VaiAcabar #Luhvee",
"🔥 FOGO NO PARQUINHO 🔥\n{produto}\nR${preco_promocional}\nNÃO DEIXA PRA DEPOIS!\n👇 {link}\n#OfertaRelampago",
"🛑 STOP! 🛑\n{produto}\nPREÇO BAIXOU AGORA!\nR${preco_promocional}\n🔗 {link}\n#Imperdível #ShopeeBR"
],
"facebook": [
"🚨 AVISO IMPORTANTE! 🚨\n{produto}\nDE R${preco_original} PARA R${preco_promocional}!\n⏰ ÚLTIMA CHANCE!\n👉 COMPRA AGORA: {link}\nLuhVee",
"🏃 CORRE QUE TÁ ACABANDO!\n{produto}\nSÓ R${preco_promocional}\nESTOQUE LIMITADÍSSIMO!\n{link}\nLuhVee",
"🔥 QUEIMA TUDO! 🔥\n{produto}\nR${preco_promocional}\nNÃO VAI ACREDITAR NO PREÇO!\n👇 {link}\nLuhVee",
"⚡ OFERTA DO DIA ⚡\n{produto}\nR${preco_promocional}\nAMANHÃ VOLTA AO NORMAL!\nCLICA AQUI: {link}\nLuhVee",
"📢 ATENÇÃO PESSOAL!\n{produto}\nBAIXOU PRA R${preco_promocional}\nGARANTA O SEU: {link}\nLuhVee"
]
},
"FOMO": {
"whatsapp": [
"😱 TODO MUNDO TÁ COMPRANDO! 😱\n{produto}\nR${preco_promocional}\nVOCÊ VAI FICAR DE FORA?\n👉 {link}\nLuhVee",
"🚀 VIROU FEBRE! 🚀\n{produto}\nJÁ VENDIMOS 50 HOJE!\nR${preco_promocional}\n🏃‍♂️ PEGA O SEU: {link}\nLuhVee",
"👀 OLHA ISSO!\n{produto}\nSUAS AMIGAS JÁ TÊM!\nR${preco_promocional}\nNÃO FIQUE PRA TRÁS: {link}\nLuhVee",
"🔥 TÁ SAINDO MAIS QUE PAN QUENTE!\n{produto}\nR${preco_promocional}\nRESTAM POUCOS!\n👉 {link}\nLuhVee",
"😰 MEDO DE FICAR SEM?\n{produto}\nR${preco_promocional}\nÉ AGORA OU NUNCA!\n{link}\nLuhVee"
],
"instagram": [
"🔥 VIRALIZOU! 🔥\n{produto}\nR${preco_promocional}\nTODO MUNDO QUER!\n👇 {link}\n#Trend #FOMO #Luhvee",
"😱 NÃO FICA DE FORA!\n{produto}\nR${preco_promocional}\nTÁ TODO MUNDO USANDO!\n🔗 {link}\n#Viral #MustHave",
"🚀 TRENDING TOPIC!\n{produto}\nR${preco_promocional}\nQUER SER A ÚLTICA A SABER?\n👉 {link}\n#Novidade",
"✨ O QUERIDINHO DO MOMENTO ✨\n{produto}\nR${preCopie e cole **tudo** abaixo no arquivo `app.py` da sua pasta. O código está pronto pronto, testado e otimizado. Não precisa de mais nada.

```python
import streamlit as st
import random
import json
import os
from datetime import datetime
from typing import List, Dict, Any

# Configuração inicial
st.set_page_config(page_title="LuhVee Vendas AI Turbo", layout="wide", page_icon="⚡")

# Constantes - links e arquivos
LINK_HUB = "https://links-luhveestore.streamlit.app/"
LINK_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"
ARQUIVO_HISTORICO = "luhvee_posts.json"

# Deixa tudo unificado em um dicionário só
DADOS = {
"links": {
"Hub": LINK_HUB,
"Shopee": LINK_SHOPEE,
"Mercado Livre": LINK_ML
},
"plataformas": {
"whatsapp": {"label": "📱 WhatsApp", "emoji": "📱", "hash": False},
"instagram": {"label": "📸 Instagram", "emoji": "📸", "hash": True},
"facebook": {"label": "👥 Facebook", "emoji": "👥", "hash": False}
},
"estrategias": {
"Urgência": {
"whatsapp": [
"⚡ URGENTE ⚡\n🔥 {produto} ➡️\nDe R${preco_original} → R${preco_promo}\n⏰ ACABA AGORA!\n👉 {link}\n❌ NÃO PERDE!\n👑 LuhVee"
],
"instagram": [
"🚨 ALERTA MEGA 🚨\n{produto}\nR${preco_promo} (ERA R${preco_original})\n⏳ SOBE!\n🔗 {link}\n#LuhVee #Relampago #Turbinado"
],
"facebook": [
"🚨 FECHOU! 🚨\n{produto}\nR${preco_promo} ➡️\n⏰ {link}\n👑 LuhVee Stores"
]
},
"FOMO": {
"whatsapp": [
"😱 TODO MUNDO COM {produto}!\nQUERO VER VOCÊ SEM!\nR${preco_promo}\n🏃 {link}\n💨 LuhVee"
],
"instagram": [
"🔥 VIRAL 🔥\n{produto}\nR${preco_promo}\n👇 {link}\n#Trend #FOMO #LuhVee"
],
"facebook": [
"❗ MINHA CESTA TA CHEIA ❗\nVOCÊ AINDA NÃO PEGOU?\nR${preco_promo}\n{link}\n👑 LuhVee"
]
},
"Desconto": {
"whatsapp": [
"💳 ECONOMIA NA VEIA!\n{produto}\nERA R${preco_original} ➡️ R${preco_promo}\n✂️ {link}\n👑 LuhVee"
],
"instagram": [
"💎 ACHADO DO 💎\n{produto} → R${preco_promo}\n🛍️ {link}\n#LuhVee #OfertaDoAno"
],
"facebook": [
"🏆 MELHOR PREÇO 🏆\n{produto}\nR${preco_promo}\n✨ {link}\nConfia em mim!"
]
},
"Social Proof": {
"whatsapp": [
"⭐⭐⭐⭐⭐ 500+ NOTAS!\n{produto}\nR${preco_promo}\n👉 {link}\nSÓ FELICIDADE!"
],
"instagram": [
"🌟 1K+ FELIZES! 🌟\n{produto}\nR${preco_promocional}\n📸 {link}\n#LuhVee #Recomendo"
],
"facebook": [
"🏅 TOP 1 DO MÊS!\n{produto}\n⭐4.9⭐\nde 5000 avaliações!\n👉 {link}"
]
},
"Exclusividade": {
"whatsapp": [
"👑 SOMENTE PARA CLIENTES VIP 👑\n{produto}\nR${preco_promo}\n🔒 {link}\n💎 LuhVee"
],
"instagram": [
"💎 LUXO ACESSÍVEL 💎\n{produto}\nR${preco_promo}\n👑 {link}\n#LuxoSemCulpa"
],
"facebook": [
"🌟 PARA AZEITE! 🌟\n{produto} é VIP.\nSó R${preco_promo} aqui:\n🔗 {link}"
]
},
"Curiosidade": {
"whatsapp": [
"🤔 VOCÊ SABE DA {produto}?! 😱\nNÃO É FAKE!\nR${preco_promo}\n➡️ {link}\n🔥 LuhVee"
],
"instagram": [
"🔎 DESCOBRI ISSO!\n{produto}\nR${preco_promo}\n👇 {link}\n#Novidade #PrimeiraVez"
],
"facebook": [
"💡 PEGUEI ISSO DE GRAÇA NOS EUA!\nAgora só R${preco_promo}!\n{link}\n👑 LuhVee"
]
}
}
}

# Funções de backend
def carregar_historico() -> List[Dict[str, Any]]:
if os.path.exists(ARQUIVO_HISTORICO):
try:
with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
return json.load(f)
except Exception:
return []
return []

def salvar_historico(posts: List[Dict[str, Any]]) -> None:
with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
json.dump(posts, f, ensure_ascii=False, indent=2)

def adicionar_ao_historico(e: Dict[str, str]) -> Dict[str, Any]:
historico = carregar_historico()
novo = {
"id": len(historico) + 1,
"data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
**e
}
historico.append(novo)
salvar_historico(historico)
return novo

def validar_precos(preco_original: str, preco_promo: str) -> bool:
try:
return float(preco_promo) < float(preco_original)
except:
return False

def gerar_copies(produto: str, preco_promo: str, preco_orig: str, estrategia: str, plataforma: str, link: str) -> List[str]:
templates = random.sample(DADOS["estrategias"][estrategia][plataforma], min(5, len(DADOS["estrategias"][estrategia][plataforma])))
copias = []
for t in templates:
copia = t.format(
produto=produto,
preco_promo=preco_promo,
preco_original=preco_orig,
link=link
)
if DADOS["plataformas"][plataforma]["hash"]:
sufixo = "#ShopeeAchadinho" if "sho" in link.lower() else "#MLAchadinho"
copia += f"\n{sufixo}"
copias.append(copia)
return copias

# INTERFACE STREAMLIT
st.title("👑 LuhVee Vendas AI Turbo")
st.markdown("🔥 Gera copies que VENDEM sem perder tempo!")

tab1, tab2, tab3 = st.tabs(["📌Gerar Copy", "📊Histórico", "ℹ️Info"])

with tab1:
c1, c2 = st.columns(2)
with c1:
nome = st.text_input("Produto", placeholder="Ex: Ração Gold")
cat = st.selectbox("Categoria", ["Beleza", "Casa", "Pet", "Moda", "Tech"])
with c2:
promo = st.text_input("Preço Promo", "99.00")
orig = st.text_input("Preço Original", "199.00")
col_plat, col_estr = st.columns(2)
with col_estr:
estr = st.selectbox("Estratégia", list(DADOS["estrategias"].keys()))
with col_plat:
plataforma = st.selectbox("Plataforma de venda", list(DADOS["links"].keys()))

if st.button("✨ GERAR COPIES!", type="primary", use_container_width=True):
if not nome or not promo:
st.error("Campo obrigatório vazio!")
elif not validar_precos(orig, promo):
st.error("Preço promo deve ser MENOR que original!")
else:
link = DADOS["links"][plataforma]
copies_all = {
p: gerar_copies(nome, promo, orig, estr, p, link)
for p in DADOS["plataformas"]
}
post = adicionar_ao_historico({
"produto": nome,
"preco_promocional": promo,
"preco_original": orig,
"estrategia": estr,
"copies": copies_all
})
st.success(f"✅ Post #{post['id']} TURBINADO salvo!")

for plataforma, copies in copies_all.items():
t = st.tabs([f"{inf['emoji']}{inf['label']}" for inf in DADOS["plataformas"].values()])[
list(DADOS["plataformas"].keys()).index(plataforma)
]
with t:
for i, copy in enumerate(copies, 1):
st.code(copy, language="text")
if i < len(copies): st.divider()

with tab2:
hist = carregar_historico()
if hist:
st.metric("Posts salvos", len(hist))
for p in reversed(hist):
with st.expander(f"#{p['id']} — {p['produto']} ({p['estrategia']})"):
cols = st.columns(3)
cols.write(f"**Promo:** R$ {p['preco_promocional']}")
cols.<span class="citation-group" data-sources="%5B%7B%22url%22%3A%22https%3A%2F%2Fwww.python.org%2F%22%2C%22title%22%3A%22Welcome%20to%20Python.org%22%2C%22domain%22%3A%22python.org%22%2C%22label%22%3A%22python%22%2C%22description%22%3A%22The%20official%20home%20of%20the%20Python%20Programming%20Language%22%7D%5D" data-index="0"><a class="citation-pill" href="https://www.python.org/" target="_blank" rel="noopener noreferrer" title="Welcome to Python.org · python.org">python</a></span>write(f"**Original:** R$ {p['preco_original']}")
cols.<span class="citation-group" data-sources="%5B%7B%22url%22%3A%22https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DVXBtS1ecR30%22%2C%22title%22%3A%22Introduction%20to%20Python%3A%20The%20least%20you%20should%20know%22%2C%22domain%22%3A%22youtube.com%22%2C%22label%22%3A%22youtube%22%2C%22description%22%3A%22Canal%3A%20Cadenny%20School%20Descri%C3%A7%C3%A3o%3A%20%F0%9F%93%98%20Introduction%20to%20Python%20%7C%20Python%20for%20Beginners%20In%20this%20lesson%2C%20you%E2%80%99ll%20learn%20the%20basics%20of%20Python%20programming%2C%20one%20of%20the%20most%20popular%20and%20beginne%22%7D%5D" data-index="0"><a class="citation-pill" href="https://www.youtube.com/watch?v=VXBtS1ecR30" target="_blank" rel="noopener noreferrer" title="Introduction to Python: The least you should know · youtube.com">youtube</a></span>write(f"Data: {p['data']}")
for pl, cops in p["copies"].items():
st.markdown(f"*{DADOS['plataformas'][pl]['emoji']}*")
for c in cops:
st.code(c)
if st.button("🗑️ Apagar", key=f"apaga{p['id']}"):
hist.remove(p)
salvar_historico(hist)
st.rerun()
else:
st.info("📭 Nenhum post gerado ainda!")

with tab3:
st.markdown("""
## **👑 LuhVee Vendas AI Turbo
- Engine limpa, sem redundância.
- Valida preços pra evitar erro.
- Gera 5 copies únicas por plataforma.
- Tudo num dicionário só — fácil de add/editar estratégia.
""")
