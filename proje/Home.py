import random
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
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
