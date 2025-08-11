import random
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import pycountry
import streamlit as st
import random
import json
from streamlit_timeline import timeline

st.set_page_config()
# Logo ve üst açıklama
# Sidebar başlığı
st.sidebar.image("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\indir.jpeg", width=200)
st.sidebar.title("Bilgi & Linkler")

# --- 1. Dış Linkler ---
st.sidebar.subheader("Dış Linkler")
st.sidebar.markdown("""
- [Eti Maden Resmi Sitesi](https://www.etimaden.gov.tr)
- [Destek Sayfası](mailto:destek@etimaden.gov.tr)
- [İletişim](mailto:iletisim@etimaden.gov.tr)
""")

st.sidebar.markdown("---")

# --- 3. Bilgilendirici Notlar ---
st.sidebar.subheader("Bilgilendirici Notlar")
st.sidebar.markdown("""
- **Uygulama Amacı:**  
Eti Maden İşletmeleri bor üretimi ve ihracatına dair kapsamlı analiz ve görselleştirme.

- **Veri Kaynağı:**  
Bu projede örnek veriler kullanılmıştır, değerler ve bilgiler gerçeği yansıtmamaktadır.

- **Son Güncelleme:**  
05 Ağustos 2025
""")
df_tesis = pd.read_csv(
    "C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_uretim_ihracat_2000_2023.csv",
    encoding="ISO-8859-9"
)
df_tur = pd.read_csv(
    "C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_verileri_2000_2020_ek_turev.csv",
    encoding="ISO-8859-9"
)
st.markdown(f"""
<style>
.section-header {{
    display: flex;
    align-items: center;
    margin-bottom: 30px;
}}

.section-header h14 {{
    font-size: 42px;
    font-weight: 1000;
    background: linear-gradient(90deg, #474747, #89898f, #cdcdd4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    white-space: nowrap;
    letter-spacing: 1px;
    transition: transform 0.3s ease, letter-spacing 0.3s ease, text-shadow 0.3s ease;
    text-shadow: none;
}}

.section-header:hover h14 {{
    transform: scale(1.03);
    letter-spacing: 2px;
    text-shadow: 0 0 8px rgba(184, 184, 191, 0.6), 
                 0 0 16px rgba(184, 184, 191, 0.4);
}}

.section-header .line {{
    flex-grow: 1;
    height: 3px;
    background: linear-gradient(90deg, #9a9aa0, #b8b8bf, #d6d6dc);
    border-radius: 5px;
    margin-left: 20px;
}}
</style>

<div class="section-header">
    <h14>ETİMADEN</h14>
    <div class="line"></div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<p style="margin-top:-15px; font-size: 18px; color: white;">Bu proje, Eti Maden'in bor madenciliği faaliyetlerine ilişkin canlı verileri, interaktif grafikler ve görselleştirmelerle birlikte sunar. Hedefimiz, şeffaflık, anlık izleme ve veriye dayalı karar alma süreçlerini desteklemektir.

### Neden Önemli?

Türkiye, **dünya bor rezervlerinin %73'üne** sahiptir. Bu platform, ülkemizin bu stratejik kaynağını nasıl yönettiğini ve dünyaya nasıl sunduğunu şeffaf şekilde izlemek için tasarlanmıştır.

*Veriler demo amaçlıdır ve canlı sistem entegrasyonu için yapılandırılabilir.*
</p>
""", unsafe_allow_html=True)
# CSS ile sekmeleri ortala
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Sekmeleri oluştur
tabs = st.tabs(["Bor Türleri Sektör Bazlı Sorgulama", "Dünya İhracat Haritası"])
with tabs[0]:
    st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }}
    .section-header h200 {{
        font-size: 32px;
        font-weight: 1000;
        background: linear-gradient(90deg, #474747, #89898f, #cdcdd4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        white-space: nowrap;
        letter-spacing: 1px;
        transition: transform 0.3s ease, letter-spacing 0.3s ease, text-shadow 0.3s ease;
        text-shadow: none;
    }}
    .section-header:hover h200 {{
        transform: scale(1.03);
        letter-spacing: 2px;
        text-shadow: 0 0 8px rgba(184, 184, 191, 0.6),
                     0 0 16px rgba(184, 184, 191, 0.4);
    }}
    .section-header .line {{
        flex-grow: 1;
        height: 3px;
        background: linear-gradient(90deg, #9a9aa0, #b8b8bf, #d6d6dc);
        border-radius: 5px;
        margin-left: 20px;
    }}
    </style>
    <div class="section-header">
        <h200>Bor Türleri  Sektör Bazlı Sorgulama</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 0px;
    }}
    .section-header h98 {{
        font-size: 20px;
        font-weight: 1000;
        background: linear-gradient(90deg, #cdcdd4, #89898f, #474747);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        white-space: nowrap;
        letter-spacing: 0px;
        transition: transform 0.3s ease, letter-spacing 0.3s ease, text-shadow 0.3s ease;
        text-shadow: none;
    }}
    .section-header:hover h98 {{
        transform: scale(1.03);
        letter-spacing: 0px;
        text-shadow: 0 0 8px rgba(184, 184, 191, 0.6), 
                     0 0 16px rgba(184, 184, 191, 0.4);
    }}
    </style>
    <div class="section-header">
        <h98>Veri hakkında sorunuzu yazın (örn: '2015 yılında Borik Asit üretimi')</h98>
    </div>
    """, unsafe_allow_html=True)
    soru = st.text_input("")
    if st.button("Sorgula"):
        if soru:
            bulunan_yil = None
            for y in df_tur["Yil"].unique():
                if str(y) in soru:
                    bulunan_yil = y
                    break
        
            bulunan_tur = None
            for t in df_tur["Bor_Turleri"].dropna().unique():
                if str(t).lower() in soru.lower():
                    bulunan_tur = t
                    break
        
            if bulunan_tur and bulunan_yil:
                sonuc = df_tur[
                    (df_tur["Bor_Turleri"] == bulunan_tur) &
                    (df_tur["Yil"] == bulunan_yil)
            ]
                if not sonuc.empty:
                    st.success(f"{bulunan_yil} yılında {bulunan_tur} verileri:")

                # 📋 Scroll destekli tablo
                    styled_sonuc = sonuc.to_html(index=False, classes="custom-table")
                    st.markdown('<div style="overflow-x: auto;">' + styled_sonuc + '</div>', unsafe_allow_html=True)

                    st.bar_chart(
                        sonuc[["Uretim_Milyon_Ton", "Ihracat_Miktari_Milyon_Ton"]].T
                )
                else:
                    st.warning("Veri bulunamadı.")
            else:
                st.warning("Soru içinde bor türü ve yıl belirtmelisiniz.")

with tabs[1]:
        st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }}
    .section-header h200 {{
        font-size: 32px;
        font-weight: 1000;
        background: linear-gradient(90deg, #474747, #89898f, #cdcdd4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        white-space: nowrap;
        letter-spacing: 1px;
        transition: transform 0.3s ease, letter-spacing 0.3s ease, text-shadow 0.3s ease;
        text-shadow: none;
    }}
    .section-header:hover h200 {{
        transform: scale(1.03);
        letter-spacing: 2px;
        text-shadow: 0 0 8px rgba(184, 184, 191, 0.6),
                     0 0 16px rgba(184, 184, 191, 0.4);
    }}
    .section-header .line {{
        flex-grow: 1;
        height: 3px;
        background: linear-gradient(90deg, #9a9aa0, #b8b8bf, #d6d6dc);
        border-radius: 5px;
        margin-left: 20px;
    }}
    </style>
    <div class="section-header">
        <h200>Dünya İhracat Haritası</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
        countries = [
    'United States', 'Canada', 'Brazil', 'Argentina', 'Mexico',
    'Germany', 'France', 'United Kingdom', 'Italy', 'Spain',
    'Russia', 'Ukraine', 'Poland', 'Sweden', 'Norway',
    'Finland', 'Denmark', 'Netherlands', 'Belgium', 'Switzerland',
    'India', 'China', 'Japan', 'South Korea', 'Indonesia',
    'Saudi Arabia', 'United Arab Emirates', 'South Africa', 'Egypt', 'Nigeria',
    'Australia', 'New Zealand', 'Thailand', 'Vietnam', 'Malaysia',
    'Colombia', 'Chile', 'Peru', 'Venezuela', 'Ecuador',
    'Iran', 'Iraq', 'Pakistan', 'Bangladesh', 'Philippines',
    'Morocco', 'Algeria', 'Greece', 'Portugal', 'Czechia'
]

# Sahte ihracat değerleri üret (örnek amaçlı)
        exports = [random.randint(10, 300) for _ in countries]

# DataFrame oluştur
        df = pd.DataFrame({
    "Ülke": countries,
    "İhracat": exports
})

# ISO A3 kodlarını eklemek için ülke adlarını kodlara çevireceğiz

        def get_iso_a3(country_name):
            try:
                return pycountry.countries.lookup(country_name).alpha_3
            except LookupError:
                return None  # Bulunamayan ülkelere None döner

        df["ISO_A3"] = df["Ülke"].apply(get_iso_a3)

# None olanları filtrele
        df = df.dropna(subset=["ISO_A3"])

# Sahte veri
        values = np.random.randint(10, 100, size=len(countries))

        custom_data = ["Ülke", "İhracat"]

        fig = px.choropleth(
    df,
    locations="ISO_A3",
    color="İhracat",
    hover_name="Ülke",
    projection="orthographic",
    color_continuous_scale="blues",
    custom_data=custom_data
)

        fig.update_geos(
    showcoastlines=True,
    showland=True,
    projection_type="orthographic",
    landcolor="rgb(30,30,30)",
    oceancolor="#02031a",     # OKYANUSUN RENGİ DEĞİŞTİRİLDİ
    showocean=True,
    bgcolor="#0d0f16"         # ARKA PLAN RENGİ
)

        fig.update_layout(
    paper_bgcolor="#0d0f16",
    height=500,  # sayfadaki harita yüksekliği
    plot_bgcolor="#0d0f16",
    font=dict(color='white'),
    geo=dict(
        showframe=False,
        showcoastlines=True,
    ),
    coloraxis_colorbar=dict(
        title=dict(
            text="Değer",
            font=dict(color='white', size=14)
        ),
        tickfont=dict(color='white'),
        bgcolor='#02031a'
    )
)
        fig.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br>İhracat Değeri: %{customdata[1]} M$<extra></extra>"
)
        st.plotly_chart(fig, use_container_width=True)
# Otomatik yenileme (her 1 saniyede bir)
        st.info("""
**Küresel Bor İhracat Dağılımı Haritası**

Bu harita, dünya genelinde bor ihracatının ülkelere göre dağılımını görselleştirmektedir. 
Renk skalası, daha yüksek ihracat değerlerini koyu mavi tonlarında; daha düşük değerleri ise açık mavi olarak yansıtır.

🔹 Özellikle **Orta Doğu**, **Asya** ve **Avrupa** bölgelerinde dikkat çeken bir yoğunluk gözlemlenmektedir.  
🔹 **Türkiye'nin** merkezde yer alması, bor sevkiyatında stratejik bir konumda olduğunu gösterir.  
🔹 **Gelişmiş sanayi ülkeleri** (örneğin Almanya, Çin, Güney Kore) yüksek ithalat potansiyeli ile ön plana çıkmaktadır.  
🔹 Bazı Afrika ve Güney Amerika ülkelerinde ise düşük veya sıfır sevkiyat dikkati çekmektedir.

Bu görselleştirme, bor ihracat stratejilerinin küresel ölçekte değerlendirilmesi için güçlü bir içgörü sağlar.
""")

        st.markdown("---")