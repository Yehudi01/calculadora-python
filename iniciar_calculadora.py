#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de inicialização da Calculadora
Permite escolher entre diferentes interfaces
"""

import sys
import subprocess

def mostrar_menu():
    """Exibe o menu de opções"""
    print("\n" + "="*60)
    print("          🧮 CALCULADORA PROFISSIONAL")
    print("="*60)
    print("\nEscolha a interface desejada:\n")
    print("1. 🌐 Interface Web Streamlit (Recomendado) ⭐")
    print("2. 🖥️  Interface Gráfica Moderna (CustomTkinter)")
    print("3. 🎨 Interface Gráfica Profissional (Tkinter)")
    print("4. 💻 Versão Terminal (Linha de Comando)")
    print("0. ❌ Sair")
    print("\n" + "="*60)

def main():
    while True:
        mostrar_menu()
        escolha = input("\nDigite sua escolha (0-4): ").strip()
        
        if escolha == "0":
            print("\n👋 Até logo!")
            sys.exit(0)
        
        elif escolha == "1":
            print("\n🚀 Iniciando interface web Streamlit...")
            print("📝 A aplicação abrirá automaticamente no seu navegador!")
            try:
                # Verificar se streamlit está instalado
                import streamlit
                subprocess.run([sys.executable, "-m", "streamlit", "run", "calculadora_streamlit.py"])
            except ImportError:
                print("❌ Erro: Streamlit não está instalado!")
                print("💡 Instale com: pip install streamlit")
            except FileNotFoundError:
                print("❌ Erro: Arquivo calculadora_streamlit.py não encontrado!")
            except Exception as e:
                print(f"❌ Erro ao iniciar: {e}")
        
        elif escolha == "2":
            print("\n🚀 Iniciando interface moderna...")
            try:
                subprocess.run([sys.executable, "calculadora_moderna.py"])
            except FileNotFoundError:
                print("❌ Erro: Arquivo calculadora_moderna.py não encontrado!")
            except Exception as e:
                print(f"❌ Erro ao iniciar: {e}")
        
        elif escolha == "3":
            print("\n🚀 Iniciando interface profissional...")
            try:
                subprocess.run([sys.executable, "calculadora_gui.py"])
            except FileNotFoundError:
                print("❌ Erro: Arquivo calculadora_gui.py não encontrado!")
            except Exception as e:
                print(f"❌ Erro ao iniciar: {e}")
        
        elif escolha == "4":
            print("\n🚀 Iniciando versão terminal...")
            try:
                subprocess.run([sys.executable, "calculadora.py"])
            except FileNotFoundError:
                print("❌ Erro: Arquivo calculadora.py não encontrado!")
            except Exception as e:
                print(f"❌ Erro ao iniciar: {e}")
        
        else:
            print("\n❌ Opção inválida! Por favor, escolha uma opção de 0 a 4.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
