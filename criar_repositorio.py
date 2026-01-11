#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para criar repositório no GitHub e fazer push do código
"""

import subprocess
import sys
import os

def criar_repositorio_github():
    """Cria o repositório no GitHub usando a API"""
    print("Para criar o repositório no GitHub, você tem duas opções:\n")
    print("OPÇÃO 1 - Usando GitHub CLI (recomendado):")
    print("1. Instale o GitHub CLI: https://cli.github.com/")
    print("2. Execute: gh auth login")
    print("3. Execute: gh repo create calculadora-python --public --source=. --remote=origin --push\n")
    
    print("OPÇÃO 2 - Criar manualmente no GitHub:")
    print("1. Acesse: https://github.com/new")
    print("2. Nome do repositório: calculadora-python")
    print("3. Selecione: Público")
    print("4. NÃO marque 'Add a README file' (já temos um)")
    print("5. Clique em 'Create repository'")
    print("6. Depois execute os comandos abaixo:\n")
    print("   git remote add origin https://github.com/SEU-USUARIO/calculadora-python.git")
    print("   git branch -M main")
    print("   git push -u origin main\n")
    
    resposta = input("Deseja tentar criar automaticamente usando a API do GitHub? (s/n): ").strip().lower()
    
    if resposta == 's':
        token = input("Digite seu GitHub Personal Access Token (ou pressione Enter para pular): ").strip()
        if not token:
            print("\nVocê precisará criar o repositório manualmente ou usar o GitHub CLI.")
            return False
        
        username = input("Digite seu nome de usuário do GitHub: ").strip()
        if not username:
            print("\nNome de usuário é obrigatório!")
            return False
        
        repo_name = "calculadora-python"
        
        try:
            import requests
            import json
            
            url = f"https://api.github.com/user/repos"
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
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 201:
                print(f"\n✅ Repositório '{repo_name}' criado com sucesso!")
                repo_url = f"https://github.com/{username}/{repo_name}.git"
                
                # Adicionar remote e fazer push
                subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
                subprocess.run(["git", "branch", "-M", "main"], check=True)
                subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
                
                print(f"\n✅ Código enviado para: https://github.com/{username}/{repo_name}")
                return True
            else:
                print(f"\n❌ Erro ao criar repositório: {response.status_code}")
                print(f"Resposta: {response.text}")
                return False
                
        except ImportError:
            print("\n❌ Biblioteca 'requests' não encontrada.")
            print("Instale com: pip install requests")
            return False
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Erro ao executar comando git: {e}")
            return False
        except Exception as e:
            print(f"\n❌ Erro: {e}")
            return False
    
    return False

if __name__ == "__main__":
    criar_repositorio_github()
