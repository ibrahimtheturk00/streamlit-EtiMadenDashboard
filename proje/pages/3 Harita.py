import streamlit as st
import pandas as pd
import pydeck as pdk
from prophet import Prophet
from streamlit_lottie import st_lottie
import json
# Sayfa ayarı
st.set_page_config(page_title="Bor Üretim Haritası")
# Sidebar başlığı
st.sidebar.image("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\indir.jpeg", width=200)
st.sidebar.title("Bilgi & Linkler")

# --- 1. Dış Linkler ---
st.sidebar.subheader("🔗 Dış Linkler")
st.sidebar.markdown("""
- [Eti Maden Resmi Sitesi](https://www.etimaden.gov.tr)
- [Destek Sayfası](mailto:destek@etimaden.gov.tr)
- [İletişim](mailto:iletisim@etimaden.gov.tr)
""")

st.sidebar.markdown("---")

# --- 3. Bilgilendirici Notlar ---
st.sidebar.subheader("ℹ️ Bilgilendirici Notlar")
st.sidebar.markdown("""
- **Uygulama Amacı:**  
Eti Maden İşletmeleri bor üretimi ve ihracatına dair kapsamlı analiz ve görselleştirme.

- **Veri Kaynağı:**  
Bu projede örnek veriler kullanılmıştır, değerler ve bilgiler gerçeği yansıtmamaktadır.

- **Son Güncelleme:**  
01 Ağustos 2025
""")
# Logo ve üst açıklama
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

# CSS ile sekmeleri ortala
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

tabs = st.tabs(["Bor Üretim ve İhracat Haritası", "Tesislere Göre Üretim ve İhracat Trendleri"])
with tabs[0]:
# Koyu arka plan
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
        <h200>Bor Üretim ve İhracat Haritası</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
        body {
            background-color: #0d0f16;
            color: white;
        }
        .stApp {
            background-color: #0d0f16;
            color: white;
        }
        .stSlider > div {
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Veri yükleme
    df = pd.read_csv("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_uretim_ihracat_2000_2023.csv", encoding="ISO-8859-9")
    df["yer"] = df["yer"].replace("600 Evler", "Balıkesir")

# Prophet tahmini için yıllar
    future_years = list(range(2024, 2031))
    forecast_rows = []

    for yer_adi in df["yer"].unique():
        sub = df[df["yer"] == yer_adi][["yil", "uretim", "ihracat", "lat", "lon"]].copy()
        sub["ds"] = pd.to_datetime(sub["yil"], format="%Y")

    # Prophet: Üretim
        model_uretim = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
        model_uretim.fit(sub[["ds", "uretim"]].rename(columns={"uretim": "y"}))
        future_uretim = model_uretim.make_future_dataframe(periods=7, freq="Y")
        forecast_uretim = model_uretim.predict(future_uretim)[["ds", "yhat"]]

    # Prophet: İhracat
        model_ihracat = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
        model_ihracat.fit(sub[["ds", "ihracat"]].rename(columns={"ihracat": "y"}))
        future_ihracat = model_ihracat.make_future_dataframe(periods=7, freq="Y")
        forecast_ihracat = model_ihracat.predict(future_ihracat)[["ds", "yhat"]]

    # Sonuçları birleştir
        for i in range(len(future_uretim)):
            yil = future_uretim["ds"].dt.year.iloc[i]
            if yil in future_years:
                forecast_rows.append({
                "yer": yer_adi,
                "yil": yil,
                "uretim": max(0, forecast_uretim["yhat"].iloc[i]),
                "ihracat": max(0, forecast_ihracat["yhat"].iloc[i]),
                "lat": sub["lat"].iloc[0],
                "lon": sub["lon"].iloc[0]
            })

    forecast_df = pd.DataFrame(forecast_rows)
    df_all = pd.concat([df, forecast_df], ignore_index=True)

# Yıl seçici
    year = st.slider("Yıl Seçin", min_value=2000, max_value=2030, value=2023)
    filtered = df_all[df_all["yil"] == year].copy()
    filtered["tooltip_text"] = (
    "Yer: " + filtered["yer"] + "\n" +
    "Yıl: " + filtered["yil"].astype(str) + "\n" +
    "Üretim: " + filtered["uretim"].round(0).astype(int).astype(str) + "\n" +
    "İhracat: " + filtered["ihracat"].round(0).astype(int).astype(str)
)

    filtered["radius_scaled"] = filtered["uretim"] * 0.5  # (önceden değiştirmiştik)

# Bu satırı buraya ekle:
    filtered["radius_scaled"] = filtered["uretim"] * 0.25

# Harita
    st.pydeck_chart(pdk.Deck(
    map_style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
    initial_view_state=pdk.ViewState(
        latitude=40.0,
        longitude=29.5,
        zoom=7,
        pitch=0
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered,
            get_position='[lon, lat]',
            get_radius="radius_scaled",
            get_fill_color='[255, 50, 120, 160]',
            get_line_color='[255, 255, 255]',
            line_width_min_pixels=1,
            pickable=True,
            auto_highlight=True
        ),
        pdk.Layer(
            "TextLayer",
            data=filtered,
            get_position='[lon, lat + 0.2]',
            get_text="yer",
            get_size=16,
            get_color=[255, 255, 255],
            get_angle=0,
            get_alignment_baseline="'bottom'"
        ),
        pdk.Layer(
            "HeatmapLayer",
            data=filtered,
            get_position='[lon, lat]',
            get_weight='uretim',
            radiusPixels=60
        )
    ],
    tooltip={"text": "{tooltip_text}"}
))

# Tablo
# Tablo
    st.markdown("<br>", unsafe_allow_html=True)
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
        <h200>{year} Yılı Üretim ve İhracat Verileri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    display_df = filtered[["yer", "yil", "uretim", "ihracat"]].copy()
    display_df["Yıl"] = filtered["yil"].astype(str)  # yıl string olarak
    display_df = display_df[["yer", "Yıl", "uretim", "ihracat"]]  # sırayı düzenle

    st.table(display_df.sort_values("uretim", ascending=False))

with tabs[1]:
# Grafikler
    st.markdown("<br>", unsafe_allow_html=True)
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
        <h200>Tesislere Göre Üretim ve İhracat Trendleri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    for yer_adi in df_all["yer"].unique():
        sub = df_all[df_all["yer"] == yer_adi].sort_values("yil")
        st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }}
    .section-header h98 {{
        font-size: 32px;
        font-weight: 1000;
        background: linear-gradient(90deg, #102973, #5293cc, #4791d1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        white-space: nowrap;
        letter-spacing: 1px;
        transition: transform 0.3s ease, letter-spacing 0.3s ease, text-shadow 0.3s ease;
        text-shadow: none;
    }}
    .section-header:hover h98 {{
        transform: scale(1.03);
        letter-spacing: 2px;
        text-shadow: 0 0 8px rgba(184, 184, 191, 0.6), 
                     0 0 16px rgba(184, 184, 191, 0.4);
    }}
    </style>
    <div class="section-header">
        <h98>{yer_adi}</h98>
    </div>
    """, unsafe_allow_html=True)
        st.line_chart(sub.set_index("yil")[["uretim", "ihracat"]])
        st.markdown("---")
# Emet Analizi
    st.info("""
**Emet (2000–2023)**  
İhracat ve üretim grafikleri birbirine yakın seyretmiştir. Özellikle 2005, 2017 ve 2020 yıllarında ihracatta yükselişler gözlenirken; üretim bu dönemlerde daha istikrarlı seyretmiştir.  
**Emet (2024–2030 Tahmini)**  
Eğilim doğrultusunda ihracatın 1.800-2.000 bandında sabit kalması, üretimin ise 1.400-1.600 arasında dalgalanması beklenmektedir. Büyük sıçramalar öngörülmemektedir.
""")

# Bandırma Analizi
    st.info("""
**Bandırma (2000–2023)**  
İhracat genelde üretimin üzerinde seyrederken; 2023’te üretim ciddi şekilde ihracatın altına düşmüştür. 2024 öncesinde 2026’ya kadar kademeli artış, sonrasında keskin düşüş gözlemlenmiştir.  
**Bandırma (2024–2030 Tahmini)**  
İhracatın 9.000’e yaklaşan seviyelerde istikrar kazanacağı, üretimde ise 5.500-6.500 arasında salınım olacağı öngörülmektedir. Aradaki fark artarak sürebilir.
""")

# Bursa Analizi
    st.info("""
**Bursa (2000–2023)**  
İhracat ve üretim birbirine çok yakın seviyelerde seyretti. 2020 ve 2027'de ihracatın üretime fark attığı gözlendi. 2022'de ise hem ihracat hem üretimde düşüş oldu.  
**Bursa (2024–2030 Tahmini)**  
Her iki göstergenin de 4.000 seviyelerinde istikrar kazanacağı, dönem dönem birbirine yaklaşacağı öngörülüyor. Büyük dalgalanma beklenmiyor.
""")

# Balıkesir Analizi
    st.info("""
**Balıkesir (2000–2023)**  
2001 ve 2008 yıllarında ihracat belirgin şekilde zirve yapmıştır. Üretimle ihracat arasında yıllara göre fark artmış ve azalmıştır. 2015 ve 2021’de üretim düşerken ihracat sabit kalmıştır.  
**Balıkesir (2024–2030 Tahmini)**  
İhracatın 9.000-10.000 bandında kalacağı, üretimin ise 8.000 civarında seyredeceği tahmin ediliyor. İki değer arasındaki fark azalabilir.
""")

# Eskişehir Analizi
    st.info("""
**Eskişehir (2000–2023)**  
İhracat genelde üretimin üzerinde seyretmiş ve 2027'de zirve yapmıştır. 2022’de her iki kalemde de düşüş olmuş ancak sonrası toparlama göstermiştir.  
**Eskişehir (2024–2030 Tahmini)**  
İhracatın 9.000-10.000 arasında, üretimin ise 7.000-8.000 seviyelerinde artan bir trendle devam edeceği öngörülüyor. İhracatın üretim üzerindeki üstünlüğü sürecektir.
""")

# Genel Başarı Durumu
    st.success("""
**Genel Başarı Değerlendirmesi**  
- Eskişehir ve Balıkesir tesisleri yüksek ihracat kapasitesine sahip.  
- Emet tesisi istikrarlı ve risksiz bir yapı sergiliyor.  
- Bursa’da üretim ve ihracat dengeli ilerliyor, yönetilebilir bir yapı mevcut.  
- Bandırma, yüksek ihracat potansiyeline rağmen üretim kapasitesini iyileştirme ihtiyacı duyuyor.
""")

# Uyarı ve Gelişim Alanları
    st.warning("""
**Geliştirme Gereken Alanlar**  
- Bandırma’da üretim artışı sağlanamazsa, ihracatın sürdürülebilirliği riske girebilir.  
- Balıkesir'de üretim dalgalanmaları kontrol altına alınmalı.  
- Eskişehir’de üretimin ihracata yetişmesi için kapasite artışı düşünülebilir.  
- Bursa’da ihracat potansiyeli daha yukarı çekilebilir.
""")

    with open("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\etimadende.json", "r", encoding="utf-8") as f:
        lottie_json = json.load(f)
        st_lottie(lottie_json, speed=1, reverse=False, loop=True, quality="high", height=500)