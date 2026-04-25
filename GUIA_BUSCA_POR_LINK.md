# 🔍 GUIA: BUSCA DE PRODUTOS POR LINK

## ✨ NOVA FUNCIONALIDADE!

Agora você pode **colar o link do produto** e o sistema automaticamente extrai:
- ✅ Nome do produto
- ✅ Preço original
- ✅ Preço com desconto

---

## 📁 ARQUIVO NOVO

**Nome:** `luhvee_vendas_pro_trending_com_busca.py`

Coloque este arquivo no seu GitHub!

---

## 🎯 COMO USAR

### PASSO 1: Instalar Dependências

```bash
pip install streamlit pytrends requests beautifulsoup4
```

### PASSO 2: Executar

```bash
streamlit run luhvee_vendas_pro_trending_com_busca.py
```

### PASSO 3: Usar a Busca

#### Opção 1️⃣: Buscar por LINK

1. Abra a **Aba "Gerar Copies"**
2. Na seção **"OPÇÃO 1: Buscar por LINK"**
3. Cole o link do produto:
   ```
   https://mercadolivre.com.br/seu-produto
   ou
   https://shopee.com.br/seu-produto
   ```
4. Clique em **"🔍 Buscar Produto"**
5. **Automático!** Preenche:
   - Nome do produto
   - Preço original
   - Preço promocional

#### Opção 2️⃣: Preencher Manualmente

Se a busca não funcionar, preencha manualmente como antes!

---

## 📊 EXEMPLO PRÁTICO

### Mercado Livre

```
Link: https://www.mercadolivre.com.br/bolsa-ombro-premium/p/MLA12345678

Resultado automático:
├─ Nome: Bolsa De Ombro Premium
├─ Preço Original: R$ 150.00
└─ Preço Promocional: R$ 89.90
```

### Shopee

```
Link: https://shopee.com.br/BOLSA-OMBRO-p-123456789

Resultado automático:
├─ Nome: BOLSA OMBRO
├─ Preço Original: R$ 140.00
└─ Preço Promocional: R$ 79.90
```

---

## ⚙️ CONFIGURAÇÃO

### Atualizar `requirements.txt`

```
streamlit>=1.28.0
pytrends>=4.9.0
requests>=2.31.0
beautifulsoup4>=4.12.0
```

---

## 🔧 COMO FUNCIONA

### 1. Você cola o link
```
https://mercadolivre.com.br/seu-produto
```

### 2. O código:
```python
def buscar_produto_por_link(link):
    if "mercadolivre" in link:
        return extrair_mercado_livre(link)
    elif "shopee" in link:
        return extrair_shopee(link)
```

### 3. Extrai os dados do HTML
```python
# Nome do produto
# Preço original
# Preço com desconto
```

### 4. Preenche automaticamente
```python
st.session_state.nome_produto = resultado["nome"]
st.session_state.preco_original = resultado["preco_original"]
st.session_state.preco_promocional = resultado["preco_promocional"]
```

### 5. Você gera as copies!
```
✅ Nome já está preenchido
✅ Preço original já está preenchido
✅ Preço promocional já está preenchido
✅ Só clicar "GERAR COPIES"!
```

---

## 🎯 TIPOS DE LINKS SUPORTADOS

### ✅ MERCADO LIVRE

```
https://www.mercadolivre.com.br/seu-produto/p/MLU123456789
https://mercadolivre.com.br/seu-produto
https://m.mercadolivre.com.br/seu-produto
```

### ✅ SHOPEE

```
https://www.shopee.com.br/seu-produto-i.123456789.123456789
https://shopee.com.br/seu-produto
https://m.shopee.com.br/seu-produto
```

---

## ❌ SE A BUSCA NÃO FUNCIONAR

### Motivos comuns:

1. **Link incorreto**
   - Verifique se é Mercado Livre ou Shopee
   - Copie o link correto do navegador

2. **Produto não existe**
   - Produto foi deletado
   - Link quebrado
   - Produto não está mais disponível

3. **Rede lenta**
   - Aguarde mais tempo
   - Tente novamente

### Solução:

**Use a Opção 2 (Preencher Manualmente)!**

Você pode sempre preencher os dados na mão se a busca falhar!

---

## 📝 EXEMPLO COMPLETO

### Cenário:

```
1. Você encontra um produto bom no Mercado Livre
2. Copia o link
3. Cola na app
4. Clica "Buscar"
5. App extrai dados automaticamente
6. Você escolhe estratégia
7. Gera as 3 copies (WhatsApp, Instagram, Facebook)
8. Cola nos seus canais
9. VENDA! 💰
```

---

## 🚀 BENEFÍCIOS

✅ **Rápido** - Não precisa digitar nome e preço
✅ **Preciso** - Extrai dados direto da fonte
✅ **Fácil** - Basta colar e pronto
✅ **Seguro** - Dados verificados
✅ **Flexível** - Se falhar, preenche manualmente

---

## 🔄 FLUXO VISUAL

```
┌─────────────────────────────────────┐
│  Você cola o LINK do produto        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  App identifica plataforma           │
│  (Mercado Livre ou Shopee)          │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Acessa o link                      │
│  Extrai HTML                        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Encontra:                          │
│  - Nome do produto                  │
│  - Preço original                   │
│  - Preço com desconto               │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Preenche automaticamente!          │
│  Pronto para gerar copies! ✅       │
└─────────────────────────────────────┘
```

---

## 📦 ARQUIVO PARA GITHUB

**Nome:** `luhvee_vendas_pro_trending_com_busca.py`

Coloque junto com:
- `requirements.txt` (atualizado com requests e beautifulsoup4)
- Outros arquivos `.py`

---

## 💡 DICAS

1. **Use links completos** - Copia toda a URL
2. **Tira os parâmetros extras** - Links muito longos podem não funcionar
3. **Aguarde a busca** - Leva alguns segundos
4. **Tente novamente** - Se falhar na primeira

---

## ✅ CHECKLIST

- [ ] Arquivo: `luhvee_vendas_pro_trending_com_busca.py` ✅
- [ ] Dependências: `requests`, `beautifulsoup4` ✅
- [ ] `requirements.txt` atualizado ✅
- [ ] Testei a busca no Mercado Livre ✅
- [ ] Testei a busca no Shopee ✅
- [ ] Funcionou tudo! 🎉

---

**Agora ficou MUITO mais fácil!** 🚀

Basta colar o link e deixar o sistema fazer o trabalho! 💻

**Luhvee Stores ❤️**
