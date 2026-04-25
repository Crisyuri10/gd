import streamlit as st
import subprocess

st.set_page_config(layout="wide")
st.title("Automação QLIK")
st.divider()

# Usuários autorizados: nome → LDAP
usuarios = {
    "Cristian Yuri": "51068683",
    "Beatriz": "1234567",
    "Mirian": "7654321",
    "Kelvin": "1122334"
}

# Seleção de usuário e senha
usuario_nome = st.selectbox("Selecione o usuário:", list(usuarios.keys()))
senha = st.text_input("Senha LDAP:", type="password")

# Botão de execução
if st.button("Executar Automação"):
    if not senha:
        st.error("Digite sua senha LDAP!")
    else:
        # Pega o LDAP correspondente ao nome
        usuario_ldap = usuarios[usuario_nome]
        st.success(f"Bem-vindo {usuario_nome}! Executando scripts...")

        # Lista de scripts
        scripts = [
            "1_otif.py"
        #     "2_ots.py", 
        #     "3_faturamento.py",
        #     "4_atrasados.py", 
        #     "5_tarefas.py", 
        #     "6_share_aut.py"
        ]

        # Executa scripts passando LDAP e senha
        for s in scripts:
            subprocess.run(["python", s, usuario_ldap, senha], check=True)

        st.success("Automação finalizada!")