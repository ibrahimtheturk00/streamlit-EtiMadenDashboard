import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from streamlit_lottie import st_lottie
import json
plt.style.use("dark_background")  # Matplotlib dark teması
sns.set_theme(style="darkgrid")   # Seaborn koyu gridli tema
df_tesis = pd.read_csv(
    "C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_uretim_ihracat_2000_2023.csv",
    encoding="ISO-8859-9"
)
df_tur = pd.read_csv(
    "C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_verileri_2000_2020_ek_turev.csv",
    encoding="ISO-8859-9"
)
st.set_page_config(page_title="Bor Dashboard")
# Örnek df yükleme (senin dosya yolunla değiştir)
df = pd.read_csv("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_verileri_2000_2020_ek_turev.csv", encoding="ISO-8859-9")
df.columns = df.columns.str.strip()

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

# --- 2. İstatistik / Özet ---
st.sidebar.subheader("📊 İstatistik & Özet")

toplam_uretim = df["Uretim_Milyon_Ton"].sum()
toplam_ihracat = df["Ihracat_Miktari_Milyon_Ton"].sum()

st.sidebar.markdown(f"- **Toplam Üretim:** {toplam_uretim:,.2f} Milyon Ton")
st.sidebar.markdown(f"- **Toplam İhracat:** {toplam_ihracat:,.2f} Milyon Ton")

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

tabs = st.tabs([
    "Üretim & İhracat",
    "Bor Türleri",
    "Sektörel Kullanım",
    "İhracat Geliri & Kur",
    "Tahminler",
    "Tesis Karşılaştırma"
])
# CSS ile sekmeleri ortala
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)
# Sayfa ayarları
st.set_page_config()


# CSV Yükle
df = pd.read_csv("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\bor_verileri_2000_2020_ek_turev.csv", encoding="ISO-8859-9")
df.columns = df.columns.str.strip()



# Tema
sns.set_style("dark")

# ------------------ 1. ÜRETİM & İHRACAT ANALİZİ ------------------
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
        <h200>Yıllık Bor Üretim ve İhracat Grafiği</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
<div style="text-align: center;">
Bu grafik, 2000-2020 yılları arasında Türkiye'nin bor madeni üretim ve ihracat miktarlarının yıllık olarak değişimini göstermektedir.  
Üretim ve ihracat verileri, Türkiye’nin bor sektöründeki performansını ve dış pazarlardaki etkinliğini değerlendirmeye yardımcı olur.
</div>
""", unsafe_allow_html=True)
    st.markdown("\n\n")

    # Üretim ve İhracat Miktarı
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.lineplot( color="#cf2950", data=df, x="Yil", y="Uretim_Milyon_Ton", label="Üretim (Milyon Ton)", marker="o", ax=ax1)
    sns.lineplot(data=df, x="Yil", y="Ihracat_Miktari_Milyon_Ton", label="İhracat (Milyon Ton)", marker="o", ax=ax1)
    ax1.set_xlabel("Yıl")
    ax1.set_ylabel("Miktar (Milyon Ton)")
    ax1.legend()
    st.pyplot(fig1)
    # İhracat Geliri (Bar Grafiği, üstünde rakamlar)
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
        <h200>Yıllık İhracat Geliri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="text-align: center;">
Bu bölümde, Türkiye'nin bor ihracatından elde ettiği yıllık gelirler (milyon dolar cinsinden) grafik üzerinde gösterilmektedir.  
İhracat gelirleri, ülke ekonomisine katkısını ve sektördeki büyüme trendlerini analiz etmek için önemli bir göstergedir.
</div>
""", unsafe_allow_html=True)
    st.markdown("\n\n")

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    barplot = sns.barplot(
    data=df,
    x="Yil",
    y="Ihracat_Geliri_Milyon_Dolar",
    color="#c75467",
    ax=ax2,
    edgecolor="skyblue",
    linewidth=0,
    ci=None  # Hata çubuklarını kapatır
    )
    ax2.set_title("Yıllık İhracat Geliri (Milyon Dolar)", fontsize=14)
    ax2.set_xlabel("Yıl")
    ax2.set_ylabel("İhracat Geliri (Milyon $)")
    ax2.tick_params(axis='x', rotation=45)

    # Barların üzerine değer yazdırma
    for container in barplot.containers:
        barplot.bar_label(container, labels=[f"{int(v.get_height()):,}" for v in container], label_type='edge', padding=3, fontsize=9)

    st.pyplot(fig2)
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
        <h200>Üretim ve İhracat Trend Analizi</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("\n")
    st.info("""
Bu grafikte 2000–2023 yılları arasında Türkiye'nin bor madeni **üretim** ve **ihracat** miktarları karşılaştırmalı olarak verilmiştir:

- **Genel Eğilim**: Üretim ve ihracat yıllar boyunca dalgalı bir seyir izlese de genel olarak **artan bir trend** göstermektedir.  
- **Üretim**: 2010 sonrası özellikle 2015’ten itibaren üretimde belirgin bir artış gözlemlenmiştir. 2020 yılında kısa süreli bir düşüş olsa da sonraki yıllarda üretim tekrar istikrarlı şekilde artmıştır.  
- **İhracat**: Üretime kıyasla daha istikrarlı bir çizgide seyretmiş, ancak zaman zaman üretimle arasındaki fark genişlemiştir.  
- **2020 ve Sonrası**: Pandemi dönemiyle birlikte hem üretimde hem ihracatta kısa süreli düşüş gözlemlenmiş, ancak 2021 itibarıyla toparlanma sağlanmıştır.  
- **İhracat / Üretim Oranı**: Yıllar içinde üretimin ihracata oranla daha hızlı arttığı bazı dönemler dikkat çekmektedir. Bu, Türkiye'nin iç piyasada bor kullanımını artırdığını veya stok oluşturduğunu düşündürmektedir.
""")

    with open("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\Business.json", "r", encoding="utf-8") as f:
        lottie_json = json.load(f)

    st_lottie(lottie_json, speed=1, reverse=False, loop=True, quality="high", height=300)
    st.markdown("<p style='text-align:center; font-size: 13px; color: gray;'>İbrahim Türk - 2025</p>", unsafe_allow_html=True)
# ------------------ 2. BOR TÜRLERİ KARŞILAŞTIRMASI ------------------
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
        <h200>Yıllara Göre Bor Türleri Dağılımı</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    # Kullanıcının yıl seçmesi
    selected_year = st.selectbox("Bir yıl seçiniz:", sorted(df["Yil"].unique()))
    filtered_df = df[df["Yil"] == selected_year]

    bor_grouped = filtered_df.groupby("Bor_Turleri")["Uretim_Milyon_Ton"].sum().reset_index()

# Tema renkleri
    tema_renkler = ["#b8b8bf", "#89898f", "#6a6a6f", "#474747", "#d6d6dc"]

# Pie chart çizimi (temaya uygun)
    fig3, ax3 = plt.subplots(figsize=(3.5, 3.5), facecolor='#1e1e1e')
    ax3.set_facecolor('#1e1e1e')  # Arka plan

    wedges, texts, autotexts = ax3.pie(
    bor_grouped["Uretim_Milyon_Ton"],
    labels=bor_grouped["Bor_Turleri"],
    autopct='%1.1f%%',
    startangle=100,
    colors=tema_renkler,
    wedgeprops={'linewidth': 1, 'edgecolor': '#1e1e1e'},
    radius=1.0,
    labeldistance=1.1,
    pctdistance=0.7
)

# Yazı renkleri ve stilleri
    for text in texts:
        text.set_color("#e0e0e4")
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_color("black")
        autotext.set_fontweight("bold")

# Başlık
    ax3.set_title(
    f"{selected_year} Yılında Bor Türlerine Göre Üretim Dağılımı",
    pad=20,
    fontsize=12,
    fontweight="bold",
    color="#b8b8bf"
)

    plt.subplots_adjust(top=0.85)
    st.pyplot(fig3)
    st.markdown("---\n")
    

    
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
        <h200>Yıllara Göre Bor Türevlerinin Üretim Miktarları</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    # Bor türlerini al (tüm veri üzerinden)
    bor_turleri = df['Bor_Turleri'].unique()

# Her bor türü için grafik çiz
    for bor_turu in bor_turleri:
    # Bu bor türüne ait yıllık veriyi al
        bor_df = df[df['Bor_Turleri'] == bor_turu].sort_values(by='Yil')
    
    # Grafik oluştur
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(data=bor_df, x='Yil', y='Uretim_Milyon_Ton',ci=None, marker='o', ax=ax, color='#d95573')

        st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }}
    .section-header h98 {{
        font-size: 25px;
        font-weight: 1000;
        background: linear-gradient(90deg, #cdcdd4, #89898f, #474747);
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
        <h98>{bor_turu} Üretimi (Milyon Ton)</h98>
    </div>
    """, unsafe_allow_html=True)



        ax.set_xlabel("Yıl")
        ax.set_ylabel("Üretim (Milyon Ton)")
        ax.grid(True, linestyle="--", alpha=0.5)
        sns.despine()
        fig.tight_layout(pad=1.5)
    
        st.pyplot(fig) 
        st.markdown("---")
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
        <h200>Genel Değerlendirme: Bor Türevlerinin Geleceği</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.info("""
**2020 sonrası tahminlerde bazı bor türevlerinde artış, bazılarında ise azalma gözlemlenmiştir. Bu eğilim şu şekilde açıklanabilir:**

🔹 **Borik Asit** ve **Etidot-67**, cam, seramik, tarım, ilaç ve enerji gibi modern sektörlerde daha yaygın kullanılmakta, bu da talebi artırmaktadır.  
🔹 Bu ürünler çevre dostu ve insan sağlığı açısından daha güvenli kabul edilir; bu da sürdürülebilirlik politikalarıyla örtüşmektedir.  
🔹 Türkiye'nin üretim ve ihracat stratejileri artık ham madde yerine katma değeri yüksek ürünlere odaklanmaktadır.  
🔹 **Boraks** ve **Susuz Boraks**, geleneksel ve daha sınırlı sektörlerde kullanıldığından, yerini daha ileri formlara bırakmaktadır.

Bu nedenle 2020 sonrası **Borik Asit** ve **Etidot-67** üretiminde artış, **Boraks** ve **Susuz Boraks**'ta ise azalma eğilimi öngörülmektedir.
""")
    with open("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\factory.json", "r", encoding="utf-8") as f:
        lottie_json = json.load(f)
        st_lottie(lottie_json, speed=1, reverse=False, loop=True, quality="high", height=450)
        st.markdown("<p style='text-align:center; font-size: 13px; color: gray;'>İbrahim Türk - 2025</p>", unsafe_allow_html=True)
# ------------------ 3. SEKTÖREL KULLANIM ------------------
with tabs[2]:
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
        <h200>Yıl Bazında Sektörel Kullanım Oranları</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

# Veriyi hazırlama
    sector_df = df.groupby(["Yil", "Sektor"])["Kullanim_Orani_Yuzde"].mean().reset_index()
    sectors = sector_df["Sektor"].unique()

# Her sektör için ayrı grafik çizimi
    for sector in sectors:
        
        st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }}
    .section-header h98 {{
        font-size: 25px;
        font-weight: 1000;
        background: linear-gradient(90deg, #cdcdd4, #89898f, #474747);
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
        <h98>{sector} Sektörü</h98>
    </div>
    """, unsafe_allow_html=True)
    
        sector_data = sector_df[sector_df["Sektor"] == sector]

        fig, ax = plt.subplots(figsize=(12, 4))
        sns.lineplot(data=sector_data, x="Yil", y="Kullanim_Orani_Yuzde", marker="o", ax=ax, color="teal")
        ax.set_ylabel("Kullanım Oranı (%)")
        ax.set_xlabel("Yıl")
        ax.grid(True)
    
        st.pyplot(fig)
        st.markdown("---")
        
        import streamlit as st

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
        <h200>Sektörel Kullanım Oranı Analizi</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
# 1. Yakıt Hücreleri - info
    st.info(""" ### Yakıt Hücreleri
    Yakıt hücreleri sektörü zaman zaman atılım gösterse de genellikle dalgalı bir seyir izlemektedir.
    2012 ve 2014 yıllarında zirveye ulaşsa da bu artışlar sürdürülememiştir.
    2023 yılına gelindiğinde kullanım oranı tekrar düşüşe geçmiştir.
    """)

# 2. Zirai İlaç - success
    st.info(""" ### Zirai İlaç
    Zirai ilaç sektörü genellikle %15-25 bandında istikrar sağlamıştır.
    2011’de yaşanan ani düşüş dışında, genel olarak dengeli bir görünüm sergilemiştir.
    Bu durum sektörün güçlü bir yapıya sahip olduğunu göstermektedir.
    """)

# 3. Metalurji - warning
    st.info(""" ### Metalurji
    Metalurji sektörü uzun yıllar güçlü bir kullanım oranına sahipken,
    2016 sonrası hızlı bir düşüşe geçmiştir. 2023’e doğru oranlar %5 seviyesine kadar gerilemiştir.
    Bu, sektördeki yapısal sorunlara veya dışsal baskılara işaret ediyor olabilir.
    """)

# 4. Seramik - info
    st.info(""" ### Seramik
    Seramik sektörü genel olarak dengeli bir grafik çizmiş ve özellikle 2015 sonrası istikrarlı bir büyüme göstermiştir.
    2023 yılında en yüksek kullanım oranına ulaşması dikkat çekicidir.
    """)

# 5. Cam - success
    st.info(""" ### Cam
    2000–2010 arasında güçlü bir artış gösteren cam sektörü, 2010 sonrası düşüş trendine girmiştir.
    Ancak hâlâ orta seviyelerde kullanım oranını korumaktadır. Geçmiş başarılar,
    yeniden canlanma potansiyeli olduğunu düşündürmektedir.
    """)

# 6. Deterjan - warning
    st.info(""" ### Deterjan
    Deterjan sektörü çok sık dalgalanma yaşamış, %5 ile %30 arasında gidip gelen bir kullanım oranına sahiptir.
    Sektörün ekonomik ve sosyal gelişmelere aşırı duyarlı olduğu gözlemlenmektedir.
    Bu nedenle risk analizi yapılmadan yatırım yapılması sakıncalı olabilir.
    """)

    with open("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\analytic.json", "r", encoding="utf-8") as f:
        lottie_json = json.load(f)
        st_lottie(lottie_json, speed=1, reverse=False, loop=True, quality="high", height=500)
        st.markdown("<p style='text-align:center; font-size: 13px; color: gray;'>İbrahim Türk - 2025</p>", unsafe_allow_html=True)
with tabs[3]:
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
        <h200>Yıl Bazında İhracat ve Kur Oranı</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    fig, ax1 = plt.subplots(figsize=(12,6))

    df_yearly = df.groupby('Yil').agg({
    'Ihracat_Geliri_Milyon_Dolar': 'sum',
    'USD_TRY': 'mean'
    }).reset_index()

    color = 'tab:blue'
    ax1.set_xlabel('Yıl')
    ax1.set_ylabel('İhracat Geliri (Milyon $)', color=color)
    ax1.plot(df_yearly['Yil'], df_yearly['Ihracat_Geliri_Milyon_Dolar'], color=color, marker='o')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('USD/TRY Kuru', color=color)
    ax2.plot(df_yearly['Yil'], df_yearly['USD_TRY'], color=color, marker='x')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.grid(True)
    plt.tight_layout()
    st.pyplot(fig)
    st.markdown("---")
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
        <h200>İhracat ve Kur Analizi</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    st.success("""
📈 **Olumlu Gözlemler:**

- **2001, 2008 ve 2011 yıllarında** ihracat gelirlerinde ciddi artışlar yaşanmıştır (yaklaşık 8.000 milyon $ ve üzeri).
- **2009 sonrası toparlanma**, küresel finans krizine rağmen ihracatın dirençli olduğunu göstermektedir.
- **2017 yılında**, hem ihracat gelirinde artış hem de kurda göreceli istikrar gözlemlenmiştir.
- **2021 sonrası**, kurun artmasına rağmen ihracat gelirinde tekrar yükseliş eğilimi görülmüştür.
""")

    st.warning("""
⚠️ **Dikkat Edilmesi Gereken Noktalar:**

- **2013–2019 döneminde**, USD/TRY kuru sürekli artarken ihracat gelirleri genellikle azalmış veya sabit kalmıştır.
- **Kur artışı**, beklenenin aksine **ihracat gelirini doğrudan artırmamıştır** – bu, kurun tek başına etkili olmadığını gösterir.
- **2020 yılında** ihracat gelirinde sert düşüş yaşanmıştır. Bu, muhtemelen pandemi kaynaklı tedarik zinciri ve üretim sorunlarından kaynaklanmıştır.
- **2012, 2014 ve 2018 yıllarında** dövizdeki artışa rağmen ihracat düşmüş ya da sınırlı kalmıştır – bu da yapısal sorunların varlığına işaret edebilir.
""")


    with st.expander("📈 Olumlu Gözlemler"):
        st.success("• 2001, 2008 ve 2011 yıllarında ihracat gelirlerinde yüksek artışlar görülmüştür. 2017 yılında kur istikrarı ve ihracat artışı birlikte gözlemlenmiştir...")

    with st.expander("⚠️ Dikkat Edilmesi Gerekenler"):
        st.warning("• 2013-2019 arasında kur artışı olmasına rağmen ihracat gelirleri sabit kalmıştır. 2020 yılında pandemi etkisiyle ihracat keskin düşüş yaşamıştır...")
    with open("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\Finance.json", "r", encoding="utf-8") as f:
        lottie_json = json.load(f)
        st_lottie(lottie_json, speed=1, reverse=False, loop=True, quality="high", height=500)
        st.markdown("<p style='text-align:center; font-size: 13px; color: gray;'>İbrahim Türk - 2025</p>", unsafe_allow_html=True)
with tabs[4]:
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
        <h200>2024-2030 Bor Üretim Tahminleri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    for bor_turu in df['Bor_Turleri'].unique():
        temp = df.groupby(['Yil','Bor_Turleri'])['Uretim_Milyon_Ton'].sum().reset_index()
        temp = temp[temp['Bor_Turleri']==bor_turu]
        temp = temp.rename(columns={'Yil':'ds','Uretim_Milyon_Ton':'y'})
        temp['ds'] = pd.to_datetime(temp['ds'], format='%Y')
        
        m = Prophet(yearly_seasonality=True)
        m.fit(temp)

        # 10 yıllık tahmin
        future = m.make_future_dataframe(periods=10, freq='Y')
        forecast = m.predict(future)

        # 2024–2030 arası
        forecast_filtered = forecast[
            (forecast['ds'].dt.year >= 2024) & (forecast['ds'].dt.year <= 2030)
        ]

        ax.plot(
            forecast_filtered['ds'].dt.year,
            forecast_filtered['yhat'],
            marker='o',
            label=bor_turu
        )

    ax.set_title("2024-2030 Bor Türlerine Göre Üretim Tahminleri")
    ax.set_xlabel("Yıl")
    ax.set_ylabel("Üretim (Milyon Ton)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    # Grafik kodunun hemen altına ekleyebilirsin
    st.info("""
2024–2030 dönemi için yapılan Prophet model tahminleri, Türkiye’nin bor türevleri üretiminde **dengeli fakat çeşitlenen bir büyüme eğilimi** gösteriyor. Geçmiş veriler (2000–2020) ışığında oluşturulan model, bor üretiminin farklı türevlerde farklı hızlarda seyredeceğini öngörüyor.
""")

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
        <h200>Bor Türevi Bazında Eğilimler</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

# Susuz Boraks
    with st.expander("**Susuz Boraks**"):
     st.write("""
Gelecek dönemde üretim miktarı en yüksek kalmaya devam edecek.
2024–2030 arasında 6–7 milyon ton bandında istikrarlı bir üretim öngörülüyor.
Bu ürünün sanayi ve kimya sektöründe temel hammadde olarak ağırlığını koruduğu görülüyor.
""")

# Boraks
    with st.expander("**Boraks**"):
        st.write("""
2025 sonrası belirgin bir artış eğilimi söz konusu.
2027’de zirve noktasına ulaşarak 5 milyon tonun üzerine çıkması, sonrasında 2028’de bir miktar düşüp tekrar yükselişe geçmesi bekleniyor.
""")

# Etidot-67
    with st.expander("**Etidot-67**"):
        st.write("""
Cam, tarım ve enerji sektörlerindeki kullanımların etkisiyle orta vadede sürekli artış göstermesi öngörülüyor.
2027’ye kadar yükseliş eğilimi devam ederken 2028’de kısa süreli düşüş, ardından tekrar artış öngörülüyor.
""")

# Borik Asit
    with st.expander("**Borik Asit**"):
        st.write("""
Diğer türevlere kıyasla daha düşük üretim miktarına sahip, ancak trend istikrarlı ve hafif dalgalı bir seyir gösteriyor.
2024’ten sonra yıllık 1,3–2 milyon ton civarında üretim bekleniyor.
""")

    st.success("""
### 2. **Genel Trendler**

- **Çeşitlilik Artışı:**  
  2000–2020 döneminde belirgin olan ham bor üretimindeki ağırlığın 2020 sonrasında azaldığı, daha katma değerli türevlerin üretim payının arttığı gözleniyor.

- **İstikrar ve Yükseliş:**  
  2024’ten itibaren büyük bir düşüş beklenmiyor. Özellikle **2025–2027 arası dönemde üretimde genel bir yükseliş eğilimi** öne çıkıyor.

- **2028 Yılında Geçici Yavaşlama:**  
  Tüm ürünlerde 2028 yılında dikkat çeken bir yavaşlama tahmini mevcut. Bu, ekonomik koşullar, küresel piyasa dalgalanmaları veya modelin geçmişteki benzer dönemleri referans almasıyla ilişkili olabilir.
""")

    st.warning("""
### 3. **Stratejik Çıkarımlar**

- **Katma Değerli Ürünler:**  
  Türkiye’nin bor politikası, **ham madde ihracatından rafine ve ileri teknoloji ürünlere geçiş** sürecini destekliyor. Etidot-67 ve borik asit gibi ürünlerin artış trendi bunu gösteriyor.

- **Sanayi ve İhracat:**  
  Artan üretim miktarı, borun cam, tarım, enerji ve yeni nesil batarya sektörlerinde stratejik rolünü daha da güçlendirecek.

- **2024–2030 Dönemi Beklentisi:**  
  Genel olarak **bor üretimi artmaya devam edecek, ürünler arasında dengeli bir dağılım oluşacak** ve Türkiye’nin dünya bor pazarındaki liderliği pekişecektir.
""")
    st.markdown("---")
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
        <h200>2024-2030 Bor Sektörel Kullanım Oranı Tahminleri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    # Orijinal veri hazırlığı
    sector_df = df.groupby(["Yil", "Sektor"])["Kullanim_Orani_Yuzde"].mean().reset_index()

    tahmin_listesi = []

    # Prophet ile her sektör için tahmin
    for sector in sector_df["Sektor"].unique():
        sec_data = sector_df[sector_df["Sektor"] == sector].copy()
        sec_data = sec_data.rename(columns={"Yil": "ds", "Kullanim_Orani_Yuzde": "y"})
        sec_data["ds"] = pd.to_datetime(sec_data["ds"], format="%Y")

        # Prophet modeli
        m = Prophet(yearly_seasonality=True)
        m.fit(sec_data)

        future = m.make_future_dataframe(periods=10, freq="Y")
        forecast = m.predict(future)

        forecast["Sektor"] = sector
        tahmin_listesi.append(forecast)

    # Tüm tahminleri birleştir
    tahmin_sonucu = pd.concat(tahmin_listesi)
    tahmin_sonucu["Yil"] = tahmin_sonucu["ds"].dt.year

    # 2024-2030 dönemi
    tahmin_2024_2030 = tahmin_sonucu[(tahmin_sonucu["Yil"] >= 2024) & (tahmin_sonucu["Yil"] <= 2030)]

    # -------------------------------
    # 1. FACET GRAFİKLER
    # -------------------------------
    sectors = tahmin_2024_2030["Sektor"].unique()
    fig, axes = plt.subplots(len(sectors), 1, figsize=(10, 3 * len(sectors)), sharex=True)

    for i, sector in enumerate(sectors):
        sec_tahmin = tahmin_2024_2030[tahmin_2024_2030["Sektor"] == sector]
        axes[i].plot(sec_tahmin["Yil"], sec_tahmin["yhat"], marker="o", color="teal")
        axes[i].set_title(sector, fontsize=12)
        axes[i].set_ylabel("Kullanım (%)")
        axes[i].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")

    # -------------------------------
    # 2. BARCHART – Toplam (ortalama) kullanım oranı
    # -------------------------------
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
        <h200>2024-2030 Ortalama Sektörel Kullanım Oranı (%)</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    toplam_sektor = (
        tahmin_2024_2030.groupby("Sektor")["yhat"]
        .mean()
        .reset_index()
        .sort_values(by="yhat", ascending=False)
    )

    fig_bar, ax_bar = plt.subplots(figsize=(10, 5))
    sns.barplot(data=toplam_sektor, x="Sektor", y="yhat", ax=ax_bar, palette="pastel")
    ax_bar.set_xlabel("Sektör")
    ax_bar.set_ylabel("Ortalama Kullanım Oranı (%)")
    plt.xticks(rotation=45)
    st.pyplot(fig_bar)

    st.info("""
Yukarıdaki grafiklerde:
- **Üstteki grafiklerde** her sektör için 2024-2030 yılları arasındaki tahmini değişim gösterilir.
- **Alttaki grafikte** ise bu dönemdeki ortalama kullanım oranları karşılaştırmalı olarak gösterilir.
\nBu analiz, 2024–2030 yılları arasında sektörlere göre bor kullanım oranlarını değerlendirmektedir. Grafiklerdeki veriler bu dönemdeki eğilimlere dayalıdır.""")

# Olumlu bulgular (tek success bloğu)
    st.success("""
✅ Zirai İlaç sektörü, 2024–2030 döneminde en yüksek **ortalama kullanım oranına (%17.2)** sahiptir. Bu sektör, tarım gibi kritik alanlarda bor kullanımının önemini vurgular.

✅ Yakıt Hücreleri sektörü, modern enerji sistemleriyle ilişkili olduğu için ikinci en yüksek kullanım oranına sahip. Aynı zamanda bu sektör, 2027’de %17.7 gibi zirve bir değere ulaşmıştır.

✅ Deterjan ve Seramik sektörleri de istikrarlı bir şekilde yüksek kullanım oranlarına sahiptir (ortalama %15.8 civarında). Bu sektörler, borun geleneksel endüstrilerdeki rolünü göstermektedir.
""")

# Sektör bazlı detaylar (expander içinde)
    with st.expander("Zirai İlaç"):
        st.write("- Kullanım oranı yıllar içinde genelde yüksek seyretmiştir.")
        st.write("- 2027’de %16.4 ile en düşük seviyeye inmiş, ardından tekrar yükselmiştir.")
        st.write("- Ortalama kullanım oranı en yüksek olan sektördür.")

    with st.expander("Yakıt Hücreleri"):
        st.write("- Yenilenebilir enerji alanında kullanılması, stratejik önemini artırıyor.")
        st.write("- 2027 yılında zirveye ulaşmış, 2030’a doğru yeniden yükselmiştir.")

    with st.expander("Deterjan"):
        st.write("- Kimya sektörünün temel bileşenidir.")
        st.write("- 2028 yılında önemli bir artış yaşanmıştır (%17.1).")

    with st.expander("Seramik"):
        st.write("- Geleneksel sanayi ürünlerinde bor kullanımı açısından istikrarlı.")
        st.write("- 2027’de minimuma düşmüş (%14.1) fakat hemen ardından toparlamıştır.")

    with st.expander("Metalurji"):
        st.write("- 2027’de ani bir düşüş yaşasa da genel trend yataydır.")
        st.write("- Diğer sektörlere kıyasla daha düşük ortalama kullanım oranına sahiptir.")

    with st.expander("Cam"):
        st.write("- Kullanım oranı giderek düşmüş ve 2030’da neredeyse sıfırlanmıştır.")
        st.write("- En düşük ortalama kullanım oranına sahip sektördür.")

# Olumsuz bulgular (tek warning bloğu)
    st.warning("""
⚠️ Cam sektörü, bor kullanım oranında ciddi bir düşüş yaşamıştır. 2024'te %6 seviyelerinde olan kullanım, 2030’da %0.2’ye kadar düşmüştür.

⚠️ Metalurji sektörü, sanayi için önemli olmasına rağmen diğer sektörlere göre görece düşük bir kullanım oranına sahiptir.

⚠️ 2027 yılı çoğu sektör için düşüş yılıdır. Bu durum, politik, ekonomik veya dış ticaret kaynaklı olabilir.
""")
    with open("C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\ai.json", "r", encoding="utf-8") as f:
        lottie_json = json.load(f)
        st_lottie(lottie_json, speed=1, reverse=False, loop=True, quality="high", height=500)
        st.markdown("<p style='text-align:center; font-size: 13px; color: gray;'>İbrahim Türk - 2025</p>", unsafe_allow_html=True)
with tabs[5]:
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
        <h200>Tesis ve Yıl Bazlı Karşılaştırma</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    default_tesisler = list(df_tesis["yer"].unique())[:2]
    tesisler = st.multiselect(
        "Tesis Seçin",
        options=sorted(df_tesis["yer"].unique()),
        default=default_tesisler
    )
with col2:
    yillar = st.slider(
        "Yıl Aralığı Seçin",
        int(df_tesis["yil"].min()),
        int(df_tesis["yil"].max()),
        (2015, 2020)
    )

if tesisler:
    filtered_df = df_tesis[
        (df_tesis["yer"].isin(tesisler)) &
        (df_tesis["yil"].between(yillar[0], yillar[1]))
    ]

    sns.set_style("darkgrid")
    fig, ax = plt.subplots(figsize=(10, 5))
    for tesis in tesisler:
        sub = filtered_df[filtered_df["yer"] == tesis]
        ax.plot(sub["yil"], sub["uretim"], marker="o", label=f"{tesis} Üretim")
        ax.plot(sub["yil"], sub["ihracat"], marker="s", linestyle="--", label=f"{tesis} İhracat")
    ax.set_xlabel("Yıl")
    ax.set_ylabel("Miktar (Bin Ton)")
    ax.legend()
    st.pyplot(fig)
    # Sütun adlarını değiştir
    filtered_df = filtered_df.rename(columns={
    "yer": "Yer",
    "yil": "Yıl",
    "uretim": "Üretim",
    "ihracat": "İhracat"
})
    # 📋 Şık HTML Tablo
    styled_table = filtered_df.drop(columns=["lat", "lon"]).to_html(
        index=False,
        classes="custom-table"
    )

    st.markdown("""
    <style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 16px;
        background-color: #1e1e1e;
        color: white;
    }
    .custom-table th {
        background: linear-gradient(90deg, #474747, #89898f);
        padding: 10px;
        text-align: center;
        font-weight: bold;
        color: white;
    }
    .custom-table td {
        padding: 8px;
        text-align: center;
        border-bottom: 1px solid #444;
    }
    .custom-table tr:hover {
        background-color: #2a2a2a;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(styled_table, unsafe_allow_html=True)

st.markdown("---")