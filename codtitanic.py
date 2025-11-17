
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("database_titanic.csv")

st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")

#SlideBar

with st.sidebar:
  st.write("# Opciones")

  div = st.slider("Número de bins:", 1, 10, 2)

  st.write("Bins", div)

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)

df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color = "pink")

st.pyplot(fig)

st.write("""
## Muestra de datos cargados
""")

st.table(df.head())


#Agrupación de Survive por sexo

st.write("## Sobrevivientes por sexo")

survivors_by_sex = df.groupby("Sex")["Survived"].sum()

#Gráfico

fig2, ax2 = plt.subplots(figsize=(8,3))
ax2.bar(["Masculino", "Femenino"], survivors_by_sex, color=["blue", "pink"])
ax2.set_title("Sobrevivientes por sexo") # eje x
ax2.set_ylabel("Cantidad") # eje y
st.pyplot(fig2)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

