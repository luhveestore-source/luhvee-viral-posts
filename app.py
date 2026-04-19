import streamlit as st
import random
import datetime
import requests
from bs4 import BeautifulSoup
from moviepy.editor import ImageClip
from PIL import Image, ImageDraw
import tempfile

st.set_page_config(page_title="LuhVee GOD MODE", layout="centered")

st.title("🚀 LuhVee GOD MODE")
st.caption("Máquina automática de conteúdo + vídeo")

# ===== LINKS AFILIADOS =====
LINK_AFILIADO_SHOPEE = "https://collshp.com/luhveestores?view=storefront"
LINK_AFILIADO_ML = "https://www.mercadolivre.com.br/social/axwelloliveira"

# ===== ESTADO =====
if "historico" not in st.session_state:
    st.session_state.historico = []

# ===== LINK AFILIADO =====
def gerar_link_afiliado(link):
    link_lower = link.lower()
    if "shopee" in link_lower:
        return LINK_AFILIADO_SHOPEE
    elif "mercadolivre" in link_lower:
        return LINK_AFILIADO_ML
    return link

# ===== SCRAPING =====
def extrair_dados(link):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(link, headers