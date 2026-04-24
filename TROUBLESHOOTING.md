# 🔧 Troubleshooting - Se Ainda Tiver Problema

Solução pra TODOS os problemas! 🎯

---

## ❌ PROBLEMA 1: "Comando pip não funciona"

### Solução A
```bash
pip3 install --upgrade pytrends
```

### Solução B
```bash
python -m pip install --upgrade pytrends
```

### Solução C
```bash
py -m pip install --upgrade pytrends
```

**Tenta uma de cada!** Alguma vai funcionar.

---

## ❌ PROBLEMA 2: "Ainda dá erro 400"

### Passo 1: Verifica se é o arquivo correto
```
Arquivo: luhvee_vendas_pro_trending.py
Versão: Tem que ser a CORRIGIDA (com delays)
```

### Passo 2: Delete cache antigo
```bash
rm trending_cache.json
# Ou delete manualmente se não funcionar
```

### Passo 3: Aguarde MAIS tempo
```
Primeira vez: ~60 segundos é normal
Siga a barra de progresso
Não feche antes de terminar!
```

### Passo 4: Tente em horário diferente
```
Google às vezes throttles mais certos horários
Tenta em outro horário
```

---

## ❌ PROBLEMA 3: "Demora muito (congelado?)"

### Não é bug! É esperado!

```
Google Trends é lento
60 segundos é NORMAL primeira vez
Próximas vezes: 1 segundo (cache)
```

### Aguarde completo
```
Deixa rodando
Vê a barra de progresso
Não clique em nada
Pronto em ~60 segundos
```

---

## ❌ PROBLEMA 4: "Mostra dados vazios"

### Significa: Google bloqueou temporariamente

### Solução A: Aguarde 30 minutos
```
Deixa app fechado
Vai tomar um café
Volta e tenta de novo
```

### Solução B: Use cache antigo
```bash
# Se tiver trending_cache.json:
# Dados velhos é melhor que nada!
# App vai usar cache automaticamente
```

### Solução C: Tente com palavras diferentes
```python
# Edite luhvee_vendas_pro_trending.py
# Procure: palavras_chave = {
# Mude: "bolsa" → "saco"
# Tente novamente
```

---

## ❌ PROBLEMA 5: "Erro: ModuleNotFoundError: No module named 'pytrends'"

### Significa: pytrends não instalado

### Solução:
```bash
pip install pytrends
# Aguarde instalar
streamlit run luhvee_vendas_pro_trending.py
```

---

## ❌ PROBLEMA 6: "Erro: ModuleNotFoundError: No module named 'streamlit'"

### Significa: streamlit não instalado

### Solução:
```bash
pip install streamlit
# Aguarde instalar
streamlit run luhvee_vendas_pro_trending.py
```

---

## ❌ PROBLEMA 7: "Streamlit não abre no navegador"

### Solução A: Copie a URL
```
Vê no terminal:
"Local URL: http://localhost:8501"

Copia e cola no navegador
```

### Solução B: Porta ocupada?
```bash
streamlit run luhvee_vendas_pro_trending.py --server.port 8502
# Muda porta se 8501 estiver ocupada
```

### Solução C: Firewall?
```
Verifica firewall do Windows/Mac
Pode tá bloqueando localhost
```

---

## ❌ PROBLEMA 8: "Google Trends funciona mas quer dados REAIS sempre"

### Significa: Cache está ajudando demais

### Se quiser forçar busca nova sempre:
```python
# Edite luhvee_vendas_pro_trending.py
# Procure: @st.cache_data(ttl=3600)
# Mude para: @st.cache_data(ttl=60)
# Agora atualiza a cada 1 minuto
```

---

## ❌ PROBLEMA 9: "Importação falha no Streamlit Cloud"

### Solução: Atualizar requirements.txt

```
Abra: requirements.txt
Adicione: pytrends>=4.9.0

Salve
Faça push no GitHub
Streamlit instala automaticamente!
```

---

## ❌ PROBLEMA 10: "Quer voltar pra versão sem Google Trends"

### Use versão simulada:
```bash
streamlit run luhvee_vendas_pro.py
```

Funciona 100% com dados estáticos!

---

## 🆘 NUCLEAR OPTION (Se nada funcionar)

### Reset Completo

```bash
# 1. Delete tudo relacionado
rm trending_cache.json
rm luhvee_posts_historico.json

# 2. Desinstale e reinstale
pip uninstall pytrends -y
pip uninstall streamlit -y
pip install streamlit
pip install pytrends

# 3. Copie arquivo novo
# Pegue luhvee_vendas_pro_trending.py novamente

# 4. Execute
streamlit run luhvee_vendas_pro_trending.py
```

Se isso não funcionar, probablement é problema do seu ambiente.

---

## 🎯 Diagnóstico Rápido

Responda essas perguntas:

```
1. Conseguiu instalar pytrends? SIM [ ] NÃO [ ]
2. Streamlit abre o app? SIM [ ] NÃO [ ]
3. Clica no botão Buscar? SIM [ ] NÃO [ ]
4. Aparece mensagem de progresso? SIM [ ] NÃO [ ]
5. Demora e depois mostra dados? SIM [ ] NÃO [ ]

Respostas:
SSSSS = Funciona! ✅
SSSNS = Problema de internet
SNSSS = Problema de instalação
NXXXX = Streamlit não funciona
```

---

## 📞 Se NADA Funcionar

### Opção 1: Use versão simulada
```bash
streamlit run luhvee_vendas_pro.py
# Funciona 100%, sem Google Trends
```

### Opção 2: Reinicie tudo
```bash
# Feche tudo
# Reinicie PC
# Tente de novo
```

### Opção 3: Peça ajuda
```
Compartilhe:
- Seu erro (exato)
- Seu comando (que rodou)
- Seu SO (Windows/Mac/Linux)
```

---

## 💡 Dicas Finais

```
✅ Sempre use arquivo CORRIGIDO
✅ Aguarde completo primeira vez
✅ Próximas vezes são instantâneas
✅ Cache é seu amigo
✅ Delays são propositais (evitam erro)
```

---

## 📚 Se Quiser Entender Melhor

Leia: **SOLUCAO_ERRO_400.md** (explicação técnica)

---

**Algum desses problemas? Já deve estar resolvido!** ✅

**Bjs da Luh da LuhVee ❤️**
