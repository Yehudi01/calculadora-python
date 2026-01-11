#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Simples em Python
Suporta todas as operações matemáticas básicas
"""

import math

def adicao(a, b):
    """Realiza a adição de dois números"""
    return a + b

def subtracao(a, b):
    """Realiza a subtração de dois números"""
    return a - b

def multiplicacao(a, b):
    """Realiza a multiplicação de dois números"""
    return a * b

def divisao(a, b):
    """Realiza a divisão de dois números"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a / b

def potencia(a, b):
    """Eleva a ao expoente b"""
    return a ** b

def raiz_quadrada(a):
    """Calcula a raiz quadrada de um número"""
    if a < 0:
        raise ValueError("Erro: Não é possível calcular raiz quadrada de número negativo!")
    return math.sqrt(a)

def raiz_n_esima(a, n):
    """Calcula a raiz n-ésima de um número"""
    if a < 0 and n % 2 == 0:
        raise ValueError("Erro: Não é possível calcular raiz par de número negativo!")
    if n == 0:
        raise ValueError("Erro: O índice da raiz não pode ser zero!")
    return a ** (1 / n)

def resto_divisao(a, b):
    """Calcula o resto da divisão (módulo)"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a % b

def fatorial(n):
    """Calcula o fatorial de um número"""
    if n < 0:
        raise ValueError("Erro: Fatorial não é definido para números negativos!")
    if n != int(n):
        raise ValueError("Erro: Fatorial só é definido para números inteiros!")
    return math.factorial(int(n))

def seno(angulo):
    """Calcula o seno de um ângulo em radianos"""
    return math.sin(angulo)

def cosseno(angulo):
    """Calcula o cosseno de um ângulo em radianos"""
    return math.cos(angulo)

def tangente(angulo):
    """Calcula a tangente de um ângulo em radianos"""
    return math.tan(angulo)

def logaritmo(a, base=10):
    """Calcula o logaritmo de a na base especificada"""
    if a <= 0:
        raise ValueError("Erro: Logaritmo só é definido para números positivos!")
    if base <= 0 or base == 1:
        raise ValueError("Erro: A base do logaritmo deve ser positiva e diferente de 1!")
    if base == 10:
        return math.log10(a)
    elif base == math.e:
        return math.log(a)
    else:
        return math.log(a, base)

def exibir_menu():
    """Exibe o menu de operações disponíveis"""
    print("\n" + "="*50)
    print("          CALCULADORA SIMPLES")
    print("="*50)
    print("1.  Adição (+)")
    print("2.  Subtração (-)")
    print("3.  Multiplicação (*)")
    print("4.  Divisão (/)")
    print("5.  Potenciação (^)")
    print("6.  Raiz Quadrada (√)")
    print("7.  Raiz N-ésima")
    print("8.  Resto da Divisão (módulo %)")
    print("9.  Fatorial (!)")
    print("10. Seno (sin)")
    print("11. Cosseno (cos)")
    print("12. Tangente (tan)")
    print("13. Logaritmo (log)")
    print("0.  Sair")
    print("="*50)

def obter_numero(mensagem="Digite um número: "):
    """Obtém um número válido do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número válido!")

def obter_numero_inteiro(mensagem="Digite um número inteiro: "):
    """Obtém um número inteiro válido do usuário"""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido!")

def main():
    """Função principal da calculadora"""
    print("Bem-vindo à Calculadora Simples!")
    
    while True:
        exibir_menu()
        escolha = input("\nEscolha uma operação (0-13): ").strip()
        
        if escolha == "0":
            print("\nObrigado por usar a calculadora! Até logo!")
            break
        
        try:
            if escolha == "1":  # Adição
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = adicao(a, b)
                print(f"\nResultado: {a} + {b} = {resultado}")
            
            elif escolha == "2":  # Subtração
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = subtracao(a, b)
                print(f"\nResultado: {a} - {b} = {resultado}")
            
            elif escolha == "3":  # Multiplicação
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = multiplicacao(a, b)
                print(f"\nResultado: {a} × {b} = {resultado}")
            
            elif escolha == "4":  # Divisão
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = divisao(a, b)
                print(f"\nResultado: {a} ÷ {b} = {resultado}")
            
            elif escolha == "5":  # Potenciação
                a = obter_numero("Digite a base: ")
                b = obter_numero("Digite o expoente: ")
                resultado = potencia(a, b)
                print(f"\nResultado: {a} ^ {b} = {resultado}")
            
            elif escolha == "6":  # Raiz Quadrada
                a = obter_numero("Digite o número: ")
                resultado = raiz_quadrada(a)
                print(f"\nResultado: √{a} = {resultado}")
            
            elif escolha == "7":  # Raiz N-ésima
                a = obter_numero("Digite o número: ")
                n = obter_numero("Digite o índice da raiz: ")
                resultado = raiz_n_esima(a, n)
                print(f"\nResultado: {n}√{a} = {resultado}")
            
            elif escolha == "8":  # Resto da Divisão
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = resto_divisao(a, b)
                print(f"\nResultado: {a} % {b} = {resultado}")
            
            elif escolha == "9":  # Fatorial
                n = obter_numero_inteiro("Digite um número inteiro: ")
                resultado = fatorial(n)
                print(f"\nResultado: {n}! = {resultado}")
            
            elif escolha == "10":  # Seno
                angulo = obter_numero("Digite o ângulo em radianos: ")
                resultado = seno(angulo)
                print(f"\nResultado: sin({angulo}) = {resultado}")
            
            elif escolha == "11":  # Cosseno
                angulo = obter_numero("Digite o ângulo em radianos: ")
                resultado = cosseno(angulo)
                print(f"\nResultado: cos({angulo}) = {resultado}")
            
            elif escolha == "12":  # Tangente
                angulo = obter_numero("Digite o ângulo em radianos: ")
                resultado = tangente(angulo)
                print(f"\nResultado: tan({angulo}) = {resultado}")
            
            elif escolha == "13":  # Logaritmo
                a = obter_numero("Digite o número: ")
                base = input("Digite a base (Enter para base 10, 'e' para base e): ").strip()
                if base == "":
                    resultado = logaritmo(a)
                    print(f"\nResultado: log₁₀({a}) = {resultado}")
                elif base.lower() == "e":
                    resultado = logaritmo(a, math.e)
                    print(f"\nResultado: ln({a}) = {resultado}")
                else:
                    try:
                        base_num = float(base)
                        resultado = logaritmo(a, base_num)
                        print(f"\nResultado: log_{base_num}({a}) = {resultado}")
                    except ValueError:
                        print("Erro: Base inválida!")
                        continue
            
            else:
                print("\nErro: Opção inválida! Por favor, escolha uma opção de 0 a 13.")
                continue
            
            input("\nPressione Enter para continuar...")
        
        except ValueError as e:
            print(f"\n{e}")
            input("\nPressione Enter para continuar...")
        
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
