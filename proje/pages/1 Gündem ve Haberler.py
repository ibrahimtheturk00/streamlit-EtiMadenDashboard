import random
import time
import streamlit as st
from streamlit_timeline import timeline
import json
import feedparser
st.sidebar.image("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\indir.jpeg", width=200)
st.sidebar.title("Bilgi & Linkler")
# CSS ile sekmeleri ortala
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)
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
tabs = st.tabs(["Güncel Haberler", "Son 24 Saat Verileri"])
with tabs[0]:
    st.markdown("""
    <style>
        .news-card {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 15px #333;
        }
        .news-title {
            font-size: 20px;
            font-weight: bold;
            color: #00c3ff;
            text-decoration: none;
        }
        .news-date {
            font-size: 13px;
            color: #aaa;
            margin-top: 5px;
        }
        .news-summary {
            font-size: 15px;
            color: #ddd;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

    st.markdown("""
    <style>
        .news-card {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 15px #333;
        }
        .news-title {
            font-size: 20px;
            font-weight: bold;
            color: #00c3ff;
            text-decoration: none;
        }
        .news-date {
            font-size: 13px;
            color: #aaa;
            margin-top: 5px;
        }
        .news-summary {
            font-size: 15px;
            color: #ddd;
            margin-top: 10px;
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
        <h200>Güncel Haberler</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
# Google News RSS feed
    url = "https://news.google.com/rss/search?q=bor+madeni+OR+bor+karbür+OR+eti+maden&hl=tr&gl=TR&ceid=TR:tr"
    feed = feedparser.parse(url)

# Filtreleme ve sıralama
    anahtar_kelimeler = ["bor madeni", "bor karbür", "eti maden", "bor üretimi", "bor tesisi"]
    haberler = []

    for entry in feed.entries:
        metin = (entry.title + " " + entry.summary).lower()
        if any(k in metin for k in anahtar_kelimeler):
            haberler.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "published_parsed": entry.published_parsed,
            "summary": ""
        })

# Tarihe göre sıralama (en yeni en üstte)
    haberler_sorted = sorted(haberler, key=lambda x: time.mktime(x["published_parsed"]), reverse=True)

# Gösterim
    for haber in haberler_sorted:
        st.markdown(f"""
    <div class="news-card">
        <a class="news-title" href="{haber['link']}" target="_blank">{haber['title']}</a>
        <div class="news-date">{haber['published']}</div>
        <div class="news-summary">{haber['summary']}</div>
    </div>
    """, unsafe_allow_html=True)

with tabs[1]:
    st.markdown("<br><br>", unsafe_allow_html=True)
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
        <h200>Son 24 Saat Verileri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
# Başlangıç değerleri
    sevkiyat = 2500
    ihracat = 12800.0
    uretim = 5400000

# Kart oluşturma fonksiyonu
    def kart(title, icon, value, unit, color):
        st.markdown(f"""
        <div style='
            background-color: #1e1e1e;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 0 20px {color};
            margin-bottom: 30px;
        '>
            <div style='font-size: 30px; font-weight: bold; color: {color};'>
                {icon} {title}
            </div>
            <div style='font-size: 50px; color: white; font-weight: bold; margin-top: 10px;'>
                {value}
            </div>
            <div style='font-size: 20px; color: white;'>
                {unit}
            </div>
        </div>
    """, unsafe_allow_html=True)

# 3 kart için placeholder tanımla
    sevkiyat_placeholder = st.empty()
    ihracat_placeholder = st.empty()
    uretim_placeholder = st.empty()

# Sonsuz animasyonlu sayaç döngüsü
    while True:
    # Sayısal artışları simüle et
        sevkiyat += random.randint(1, 10)
        sevkiyat -= random.randint(1, 10)
        ihracat += random.uniform(0.5, 2.5)
        uretim += random.randint(10, 50)

    # Kartları güncelle
        with sevkiyat_placeholder:
            kart("Canlı Bor Sevkiyatı", "", f"{sevkiyat:,}", "adet", "#00c3ff")
        with ihracat_placeholder:
            kart("Anlık İhracat Hacmi", "", f"{ihracat:,.2f}", "M$", "#00ff88")
        with uretim_placeholder:
            kart("Toplam Üretim", "", f"{uretim:,}", "ton", "#ff6b00")
        time.sleep(1)