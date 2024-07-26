import streamlit as st
import matplotlib.pyplot as plt

# Carregar o logo
logo = "/Users/Enzo/Desktop/TBCredores/logo.png"  # Substitua pelo caminho do seu logo

# Configurar o layout
st.set_page_config(page_title="Processo", page_icon=logo, layout="centered")

# Adicionar o logo no canto superior esquerdo
st.image(logo, width=50)



###############################################################################
########## Antes de tudo fazer um looping para mostrar todas empresas #########
###############################################################################

# Adicionar campos de entrada com chaves únicas
st.write("Número do processo:")

st.write("CNPJ:")

st.write("Nome da empresa:")

st.write("Status:")


###############################################################################
########################### FIM DO LOOPING#####################################
###############################################################################



# Adicionar uma linha de separação
st.markdown("<hr>", unsafe_allow_html=True)


# Graficos

# Adicionar dois blocos centralizados com número e título
col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])

with col2:
    st.write("### 123")
    st.write("HC de Credores do Processo")

with col4:
    st.write("### 456")
    st.write("Valor Total Divida (R$)")


# Adicionar uma linha de separação
st.markdown("<hr>", unsafe_allow_html=True)

# Dados do gráfico de barras
classes = ['Classe I', 'Classe II', 'Classe III', 'Classe IV', 'Classe V', 'Classe VI', 'Classe VII']
valores = [30000, 17000, 12000, 10000, 6500, 6000, 5000]

# Criar o gráfico de barras
fig, ax = plt.subplots()
ax.bar(classes, valores)

# Configurar o gráfico
ax.set_xlabel('Classes')
ax.set_ylabel('Valores')
ax.set_title('Valores por Classe')

# Mostrar o gráfico no Streamlit
st.pyplot(fig)






