
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("database_titanic.csv")

st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")

with st.sidebar:
  st.write("# Opciones")

  div = st.slider("Número de bins:", 0, 10, 2)

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
