
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("database_titanic.csv")

st.write("""
# Base de datos del Titanic
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



st.set_page_config(
    page_title="Ejercicio simple Titanic",
    layout="wide"
)

st.title("Ejercicio de layouts en Streamlit")


@st.cache_data
def cargar_datos():
    return pd.read_csv("database_titanic.csv")


df = cargar_datos()

st.write("Usamos el archivo **database_titanic.csv**")

# ======================
# SIDEBAR  → filtros
# ====================== sidebar conteiner, columna expander 
with st.sidebar:
    st.header("Filtros")

    # Filtro de edad
    edad_min = int(df["Age"].min(skipna=True)) if df["Age"].notna().any() else 0
    edad_max = int(df["Age"].max(skipna=True)) if df["Age"].notna().any() else 80

    rango_edad = st.slider(
        "Rango de Edad",
        min_value=edad_min,
        max_value=edad_max,
        value=(max(edad_min, 10), min(edad_max, 50))
    )




