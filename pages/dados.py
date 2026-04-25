import pandas as pd
import streamlit as st
import os

# Caminho dinâmico
base_user = os.path.expanduser("~")
caminho_arquivo = os.path.join(base_user, "Downloads", "GD", "1otif", "1otif.xlsx")

# Leitura
df = pd.read_excel(caminho_arquivo)

st.subheader("OTIF")


df['Data'] = pd.to_datetime(df['Data']).dt.date

# Filtro
df = df[df['Centro Expedidor'] == '99 - Cd São Paulo']

# Agrupamentos
total_entregas = df.groupby('Data')['Qtde Total Entregue'].sum()

entregue_no_prazo = df.groupby('Data')[
    ['Qtde Produtos Entregue Antes Prazo', 'Qtde Produtos Entregue Prazo']
].sum().sum(axis=1)

# Junta
df_agrupado = pd.concat([total_entregas, entregue_no_prazo], axis=1)
df_agrupado.columns = ['Total_Volumes', 'OTIF_SIM']

df_agrupado = df_agrupado.round(0).astype(int)

df_pivot = df_agrupado.T
df_pivot.columns = df_pivot.columns.astype(str)

st.dataframe(df_pivot)







import pandas as pd
import streamlit as st


# Caminho dinâmico
base_user = os.path.expanduser("~")
caminho_arquivo = os.path.join(base_user, "Downloads", "GD", "2ots", "2ots.xlsx")

# Leitura
df = pd.read_excel(caminho_arquivo)


st.subheader("OTS")


df['Data'] = pd.to_datetime(df['Data']).dt.date

# Total de entregas por dia
df_total = df.groupby('Data')['Qtd Entregas'].sum()

# Total de OTS SIM por dia
df_sim = df[df['OTS'] == 'Sim'].groupby('Data')['Qtd Entregas'].sum()

# Junta em um único DataFrame
df_agrupado = pd.concat([df_total, df_sim], axis=1)
df_agrupado.columns = ['Total_Pedidos', 'OTS_SIM']

# Arredonda para inteiro (caso tenha casas decimais)
df_agrupado = df_agrupado.round(0).astype(int)

# Transpõe para pivotar: datas como colunas, métricas como linhas
df_pivot = df_agrupado.T
df_pivot.columns = df_pivot.columns.astype(str)  # garante que colunas sejam string

# Exibe no Streamlit e imprime no console
st.dataframe(df_pivot)
# print(df_pivot)





import pandas as pd
import streamlit as st


# Caminho dinâmico
base_user = os.path.expanduser("~")
caminho_arquivo = os.path.join(base_user, "Downloads", "GD", "3faturamento", "3faturamento.xlsx")

# Leitura
df = pd.read_excel(caminho_arquivo)

st.subheader("PEDIDOS FATURADOS")


# Converte para data (sem hora)
df['Data'] = pd.to_datetime(df['Data']).dt.date

# Filtra apenas os tipos de movimento desejados
df_filtrado = df[df['Tipo Movimento'].isin([
    "Reentrega Faturada (Print)",
    "Venda Faturada"
])]

# Agrupa por Data e conta pedidos únicos
df_agrupado = df_filtrado.groupby('Data')['Pedido'].nunique()

# Transpõe para pivotar: datas como colunas, métricas como linhas
df_pivot = df_agrupado.to_frame(name='Total_Faturado').T
df_pivot.columns = df_pivot.columns.astype(str)  # garante que as colunas sejam string

# Exibe no Streamlit e imprime no console
st.dataframe(df_pivot)
# print(df_pivot)









import pandas as pd
import streamlit as st


# Caminho dinâmico
base_user = os.path.expanduser("~")
caminho_arquivo = os.path.join(base_user, "Downloads", "GD", "4atrasados", "4atrasados.xlsx")

# Leitura
df = pd.read_excel(caminho_arquivo)

st.subheader("PEDIDOS ATRASADOS")


df['Data_Formato'] = pd.to_datetime(df['Data_Formato']).dt.date

# Total de entregas por dia
df_total = df.groupby('Data_Formato')['Pedido'].nunique()

# Total de OTS SIM por dia
df_sim = df[df['Status Pedido'] == 'ATRASADO'].groupby('Data_Formato')['Pedido'].nunique()

# Junta em um único DataFrame
df_agrupado = pd.concat([df_total, df_sim], axis=1)
df_agrupado.columns = ['Total_Pedidos', 'Total_Atrasados']

# Arredonda para inteiro (caso tenha casas decimais)
df_agrupado = df_agrupado.round(0).astype(int)

# Transpõe para pivotar: datas como colunas, métricas como linhas
df_pivot = df_agrupado.T
df_pivot.columns = df_pivot.columns.astype(str)  # garante que colunas sejam string

# Exibe no Streamlit e imprime no console
st.dataframe(df_pivot)
# print(df_pivot)