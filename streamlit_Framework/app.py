import pandas as pd
import streamlit as st
import plotly.express as px

st.write("Hello Word")

df = pd.read_excel("PandasTestes.xlsx")
#df

chart_data = pd.DataFrame (
    {
         "Nome": df["Nome"],
         "Quantidade": df["Quantidade"]
    }

)

df["Month"] = df["Data de chegada"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())
st.dataframe(df.style.format({"Lote": "{:.0f}"}))
df_filtered = df[df["Month"] == month]
df_filtered

fig_date = px.bar(df, x="Nome", y="Quantidade", color= "Sif", 
                  labels={'Sif': 'Sif'}, height=600,
                  title="Quantidade de produtos recebidos")
st.plotly_chart(fig_date)

fig_date_sif = px.bar(df, x="Nome", y="Marca", color = 'Marca',
                      title="Quantidade de produtos por marca",
                      labels={'Marca':'Marca'}, height=400)
st.plotly_chart(fig_date_sif)