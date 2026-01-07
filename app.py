import streamlit as st

st.title("Verificação de Nota do Aluno")

num1 = st.number_input(
    "Qual a nota do aluno?",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

if st.button("Verificar"):
    if num1 >= 7:
        st.success(f"Parabéns! Sua nota foi {num1}. Você está aprovado 🎉")
    else:
        st.error(f"Sua nota foi {num1}. Você reprovou 😢")
