import streamlit as st
import pandas as pd
import plotly.express as px

# Veri yükle
@st.cache_data
def load_data():
    df = pd.read_csv("bor_verileri_2000_2020_ek_turev.csv")
    return df

df = load_data()

# Sayfa başlığı
st.title("Bor Verileri Dashboard (2000-2020)")

# Yıl aralığı seçimi
min_year = int(df["Yil"].min())
max_year = int(df["Yil"].max())

yil_aralik = st.slider("Yıl Aralığı Seçin:", min_year, max_year, (min_year, max_year), step=1)

# Seçilen aralıktaki veriyi filtrele
filtered_df = df[(df["Yil"] >= yil_aralik[0]) & (df["Yil"] <= yil_aralik[1])]

# Sektörel katkı (pie chart)
st.subheader("Sektörel Kullanım Dağılımı")
sector_pie = filtered_df.groupby("Sektor")["Kullanim_Orani_Yuzde"].sum().reset_index()
fig_pie = px.pie(sector_pie, names="Sektor", values="Kullanim_Orani_Yuzde", hole=0.4)
st.plotly_chart(fig_pie)

# Yıllara göre üretim
st.subheader("Yıllara Göre Bor Üretimi")
uretim_df = filtered_df.groupby("Yil")["Uretim_Milyon_Ton"].sum().reset_index()
fig_uretim = px.line(uretim_df, x="Yil", y="Uretim_Milyon_Ton", markers=True)
st.plotly_chart(fig_uretim)

# Yıllara göre ihracat ve gelir
st.subheader("Yıllara Göre İhracat ve İhracat Geliri")
ihracat_df = filtered_df.groupby("Yil")[["Ihracat_Miktari_Milyon_Ton", "Ihracat_Geliri_Milyon_Dolar"]].sum().reset_index()
fig_ihracat = px.bar(ihracat_df, x="Yil", y=["Ihracat_Miktari_Milyon_Ton", "Ihracat_Geliri_Milyon_Dolar"], barmode="group")
st.plotly_chart(fig_ihracat)

# Ek: Bor türü bazlı üretim
st.subheader("Bor Türü Bazlı Üretim Dağılımı")
bor_tur_df = filtered_df.groupby("Bor_Turleri")["Uretim_Milyon_Ton"].sum().reset_index()
fig_bor = px.bar(bor_tur_df, x="Bor_Turleri", y="Uretim_Milyon_Ton", color="Bor_Turleri")
st.plotly_chart(fig_bor)
