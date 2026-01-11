#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Profissional com Interface Streamlit
Interface web moderna e interativa
"""

import streamlit as st
import math
from calculadora import (
    adicao, subtracao, multiplicacao, divisao, potencia,
    raiz_quadrada, raiz_n_esima, resto_divisao, fatorial,
    seno, cosseno, tangente, logaritmo
)

# Configuração da página
st.set_page_config(
    page_title="🧮 Calculadora Profissional",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para melhorar o design
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .operation-section {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        font-size: 1rem;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar histórico na sessão
if 'historico' not in st.session_state:
    st.session_state.historico = []

def adicionar_ao_historico(operacao, resultado, num1=None, num2=None):
    """Adiciona cálculo ao histórico"""
    if num2 is not None:
        texto = f"{operacao}: {num1} e {num2} = **{resultado}**"
    elif num1 is not None:
        texto = f"{operacao}: {num1} = **{resultado}**"
    else:
        texto = f"{operacao} = **{resultado}**"
    
    st.session_state.historico.append(texto)
    # Manter apenas os últimos 50 cálculos
    if len(st.session_state.historico) > 50:
        st.session_state.historico.pop(0)

def main():
    # Título principal
    st.markdown('<h1 class="main-header">🧮 Calculadora Profissional</h1>', unsafe_allow_html=True)
    
    # Sidebar com informações
    with st.sidebar:
        st.header("ℹ️ Informações")
        st.info("""
        **Calculadora completa** com todas as operações matemáticas básicas e avançadas.
        
        Digite os números nos campos abaixo e escolha a operação desejada.
        """)
        
        st.header("📊 Estatísticas")
        st.metric("Cálculos realizados", len(st.session_state.historico))
        
        if st.button("🗑️ Limpar Histórico", use_container_width=True):
            st.session_state.historico = []
            st.rerun()
        
        st.header("💡 Dicas")
        st.caption("""
        • Use ponto (.) para decimais
        • Funções trigonométricas usam radianos
        • Para logaritmo, deixe base vazia para base 10
        • Digite 'e' para logaritmo natural
        """)
    
    # Layout principal em colunas
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Entrada de Dados")
        
        # Campos de entrada
        num1 = st.number_input(
            "Número 1",
            value=0.0,
            step=0.1,
            format="%.10f",
            help="Digite o primeiro número"
        )
        
        num2 = st.number_input(
            "Número 2",
            value=0.0,
            step=0.1,
            format="%.10f",
            help="Digite o segundo número (opcional para algumas operações)"
        )
        
        # Campo especial para base do logaritmo
        base_log = st.text_input(
            "Base do Logaritmo (opcional)",
            value="",
            help="Deixe vazio para base 10, digite 'e' para logaritmo natural, ou um número para base personalizada"
        )
    
    with col2:
        st.header("🎯 Operação")
        
        # Seleção de operação
        operacao = st.selectbox(
            "Escolha a operação:",
            [
                "➕ Adição",
                "➖ Subtração",
                "✖️ Multiplicação",
                "➗ Divisão",
                "🔢 Potência",
                "📊 Resto da Divisão",
                "√ Raiz Quadrada",
                "ⁿ√ Raiz N-ésima",
                "! Fatorial",
                "sin Seno",
                "cos Cosseno",
                "tan Tangente",
                "log Logaritmo"
            ],
            help="Selecione a operação matemática desejada"
        )
        
        # Botão de cálculo
        calcular = st.button("🚀 Calcular", use_container_width=True, type="primary")
    
    # Área de resultado
    st.markdown("---")
    
    if calcular:
        try:
            resultado = None
            operacao_nome = operacao.split(" ", 1)[1] if " " in operacao else operacao
            
            if operacao == "➕ Adição":
                resultado = adicao(num1, num2)
                adicionar_ao_historico("Adição", resultado, num1, num2)
            
            elif operacao == "➖ Subtração":
                resultado = subtracao(num1, num2)
                adicionar_ao_historico("Subtração", resultado, num1, num2)
            
            elif operacao == "✖️ Multiplicação":
                resultado = multiplicacao(num1, num2)
                adicionar_ao_historico("Multiplicação", resultado, num1, num2)
            
            elif operacao == "➗ Divisão":
                resultado = divisao(num1, num2)
                adicionar_ao_historico("Divisão", resultado, num1, num2)
            
            elif operacao == "🔢 Potência":
                resultado = potencia(num1, num2)
                adicionar_ao_historico("Potência", resultado, num1, num2)
            
            elif operacao == "📊 Resto da Divisão":
                resultado = resto_divisao(num1, num2)
                adicionar_ao_historico("Resto da Divisão", resultado, num1, num2)
            
            elif operacao == "√ Raiz Quadrada":
                resultado = raiz_quadrada(num1)
                adicionar_ao_historico("Raiz Quadrada", resultado, num1)
            
            elif operacao == "ⁿ√ Raiz N-ésima":
                resultado = raiz_n_esima(num1, num2)
                adicionar_ao_historico(f"Raiz {num2}-ésima", resultado, num1)
            
            elif operacao == "! Fatorial":
                if num1 != int(num1):
                    st.error("❌ Erro: O fatorial só é definido para números inteiros!")
                else:
                    resultado = fatorial(int(num1))
                    adicionar_ao_historico("Fatorial", resultado, int(num1))
            
            elif operacao == "sin Seno":
                resultado = seno(num1)
                adicionar_ao_historico("Seno", resultado, num1)
            
            elif operacao == "cos Cosseno":
                resultado = cosseno(num1)
                adicionar_ao_historico("Cosseno", resultado, num1)
            
            elif operacao == "tan Tangente":
                resultado = tangente(num1)
                adicionar_ao_historico("Tangente", resultado, num1)
            
            elif operacao == "log Logaritmo":
                if not base_log or base_log.strip() == "":
                    resultado = logaritmo(num1)
                    adicionar_ao_historico("Logaritmo (base 10)", resultado, num1)
                elif base_log.lower() == "e":
                    resultado = logaritmo(num1, math.e)
                    adicionar_ao_historico("Logaritmo Natural (ln)", resultado, num1)
                else:
                    try:
                        base = float(base_log)
                        resultado = logaritmo(num1, base)
                        adicionar_ao_historico(f"Logaritmo (base {base})", resultado, num1)
                    except ValueError:
                        st.error("❌ Erro: Base do logaritmo inválida!")
                        resultado = None
            
            if resultado is not None:
                # Exibir resultado em destaque
                st.markdown(f"""
                <div class="result-box">
                    <h2 style="color: #1f77b4; margin: 0;">Resultado</h2>
                    <p style="font-size: 2rem; font-weight: bold; margin: 1rem 0; color: #2c3e50;">
                        {resultado}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.success(f"✅ Cálculo realizado com sucesso!")
        
        except ValueError as e:
            st.error(f"❌ {str(e)}")
        except Exception as e:
            st.error(f"❌ Erro inesperado: {str(e)}")
    
    # Histórico de cálculos
    st.markdown("---")
    st.header("📜 Histórico de Cálculos")
    
    if st.session_state.historico:
        # Mostrar histórico em ordem reversa (mais recente primeiro)
        historico_reverso = list(reversed(st.session_state.historico))
        for i, calc in enumerate(historico_reverso):
            st.markdown(f"{i+1}. {calc}")
    else:
        st.info("📝 Nenhum cálculo realizado ainda. Faça seu primeiro cálculo acima!")
    
    # Rodapé
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 1rem;">
        <p>🧮 Calculadora Profissional | Desenvolvido com ❤️ usando Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
