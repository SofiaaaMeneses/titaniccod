
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

    # Filtro de tarifa
    fare_min = float(df["Fare"].min())
    fare_max = float(df["Fare"].max())

    max_fare = st.slider(
        "Fare máximo",
        min_value=fare_min,
        max_value=fare_max,
        value=float(np.percentile(df["Fare"], 75))
    )

# Aplicamos filtros del sidebar a una copia
df_filtrado = df.copy()
df_filtrado = df_filtrado[
    df_filtrado["Age"].between(rango_edad[0], rango_edad[1]) &
    (df_filtrado["Fare"] <= max_fare)


with st.container():
    st.subheader("Resumen de datos filtrados")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.metric("Pasajeros filtrados", len(df_filtrado))

    with col_b:
        if "Survived" in df_filtrado.columns and len(df_filtrado) > 0:
            tasa = df_filtrado["Survived"].mean() * 100
            st.metric("Supervivencia", f"{tasa:.1f} %")
        else:
            st.metric("Supervivencia", "N A")

    with col_c:
        if len(df_filtrado) > 0:
            st.metric("Fare promedio", f"{df_filtrado['Fare'].mean():.2f}")
        else:
            st.metric("Fare promedio", "N A")




