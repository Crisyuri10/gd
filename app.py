import streamlit as st
import subprocess

st.set_page_config(layout="wide")
st.title("Automação QLIK")
st.divider()

usuarios = {
    "Cristian Yuri": "51068683",
    "Beatriz": "1234567",
    "Mirian": "7654321",
    "Kelvin": "1122334"
}

usuario_nome = st.selectbox("Selecione o usuário:", list(usuarios.keys()))
senha = st.text_input("Senha LDAP:", type="password")

if st.button("Executar Automação"):
    if not senha:
        st.error("Digite sua senha LDAP!")
    else:
        usuario_ldap = usuarios[usuario_nome]
        st.success(f"Bem-vindo {usuario_nome}! Executando scripts...")

        scripts = ["1_otif.py",
                   "2_ots.py", 
                   "3_faturamento.py",
                   "4_atrasados.py"
        ]

        for s in scripts:
            try:
                subprocess.run(["python", s, usuario_ldap, senha], check=True)
            except subprocess.CalledProcessError:
                st.error(f"Erro ao executar {s}")
                st.stop()

        st.success("Automação finalizada!")