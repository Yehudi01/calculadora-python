#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para publicar o projeto no GitHub
Execute: python publicar_github.py SEU_TOKEN SEU_USUARIO
"""

import sys
import subprocess
import json

try:
    import requests
except ImportError:
    print("❌ Biblioteca 'requests' não encontrada.")
    print("Instale com: pip install requests")
    sys.exit(1)

def criar_repositorio(token, username, repo_name="calculadora-python"):
    """Cria o repositório no GitHub usando a API"""
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": "Calculadora simples em Python com todas as operações matemáticas básicas",
        "public": True,
        "auto_init": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            repo_data = response.json()
            repo_url = repo_data["clone_url"]
            print(f"✅ Repositório '{repo_name}' criado com sucesso!")
            print(f"📦 URL: {repo_data['html_url']}")
            return repo_url
        elif response.status_code == 422:
            print(f"⚠️  Repositório '{repo_name}' já existe ou nome inválido")
            return f"https://github.com/{username}/{repo_name}.git"
        else:
            print(f"❌ Erro ao criar repositório: {response.status_code}")
            print(f"Resposta: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def fazer_push(repo_url):
    """Adiciona remote e faz push do código"""
    try:
        # Remove remote se já existir
        subprocess.run(["git", "remote", "remove", "origin"], 
                     stderr=subprocess.DEVNULL, check=False)
        
        # Adiciona novo remote
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        print("✅ Remote 'origin' adicionado")
        
        # Renomeia branch para main
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        print("✅ Branch renomeada para 'main'")
        
        # Faz push
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Código enviado para o GitHub!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar comando git: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Uso: python publicar_github.py SEU_TOKEN SEU_USUARIO")
        print("\nPara criar um token:")
        print("1. Acesse: https://github.com/settings/tokens")
        print("2. Clique em 'Generate new token (classic)'")
        print("3. Dê um nome e selecione a permissão 'repo'")
        print("4. Copie o token gerado")
        sys.exit(1)
    
    token = sys.argv[1]
    username = sys.argv[2]
    
    print("🚀 Criando repositório no GitHub...")
    repo_url = criar_repositorio(token, username)
    
    if repo_url:
        print("\n📤 Fazendo push do código...")
        if fazer_push(repo_url):
            print(f"\n✅ Sucesso! Acesse: https://github.com/{username}/calculadora-python")
        else:
            print("\n⚠️  Repositório criado, mas houve erro no push.")
            print(f"Execute manualmente:")
            print(f"  git remote add origin {repo_url}")
            print(f"  git branch -M main")
            print(f"  git push -u origin main")
    else:
        print("\n❌ Não foi possível criar o repositório.")

if __name__ == "__main__":
    main()
