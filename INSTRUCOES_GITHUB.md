# 📦 Como Publicar no GitHub

## Opção 1: Criar Manualmente (Mais Simples)

### Passo 1: Criar o Repositório no GitHub

1. Acesse: https://github.com/new
2. **Nome do repositório**: `calculadora-python`
3. **Descrição**: `Calculadora simples em Python com todas as operações matemáticas básicas`
4. **Visibilidade**: Selecione **Público** ✅
5. **IMPORTANTE**: NÃO marque nenhuma opção (não adicione README, .gitignore ou licença - já temos!)
6. Clique em **"Create repository"**

### Passo 2: Conectar e Fazer Push

Depois de criar o repositório, execute os seguintes comandos no terminal:

```bash
# Navegue até a pasta do projeto
cd "C:\Users\yehud\OneDrive - Adventistas\Documentos\Asimov\CursorIA"

# Adicione o remote (substitua SEU-USUARIO pelo seu nome de usuário do GitHub)
git remote add origin https://github.com/SEU-USUARIO/calculadora-python.git

# Renomeie a branch para main (se necessário)
git branch -M main

# Faça o push do código
git push -u origin main
```

### Passo 3: Verificar

Acesse: `https://github.com/SEU-USUARIO/calculadora-python`

---

## Opção 2: Usando GitHub CLI (Mais Rápido)

### Passo 1: Instalar GitHub CLI

1. Baixe em: https://cli.github.com/
2. Instale o aplicativo
3. Execute no terminal: `gh auth login`

### Passo 2: Criar e Publicar

```bash
cd "C:\Users\yehud\OneDrive - Adventistas\Documentos\Asimov\CursorIA"
gh repo create calculadora-python --public --source=. --remote=origin --push
```

Isso criará o repositório e fará o push automaticamente!

---

## Opção 3: Usando Script Python com API

Se você tiver um **Personal Access Token** do GitHub:

1. Crie um token em: https://github.com/settings/tokens
2. Dê permissão `repo` ao token
3. Execute o script `criar_repositorio.py` e siga as instruções

---

## ✅ Verificação Final

Após fazer o push, você deve ver:
- ✅ Arquivo `calculadora.py`
- ✅ Arquivo `README.md`
- ✅ Arquivo `.gitignore`

No repositório: `https://github.com/SEU-USUARIO/calculadora-python`
