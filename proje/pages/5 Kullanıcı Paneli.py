import streamlit as st
import sqlite3
import bcrypt
import datetime
import plotly.graph_objects as go


st.set_page_config(page_title="Kullanıcı Paneli")
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

# --- Üst Başlık ---
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

# ==================== CSS ====================
st.markdown("""
<style>
.info-card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
    text-align: center;
    color: white;
    font-size: 18px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.info-card:hover {
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 0 20px rgba(184,184,191,0.6), 0 0 30px rgba(184,184,191,0.4);
}
.card-title {
    font-weight: bold;
    font-size: 30px;
    margin-bottom: 5px;
    color: #b8b8bf;
}
</style>
""", unsafe_allow_html=True)

# ==================== DB BAĞLANTISI ====================
conn = sqlite3.connect("kullanicilar.db", check_same_thread=False)
c = conn.cursor()

# Tablolar
c.execute("""
CREATE TABLE IF NOT EXISTS kullanicilar (
    tcno TEXT PRIMARY KEY,
    sifre TEXT,
    ad TEXT,
    soyad TEXT,
    departman TEXT,
    pozisyon TEXT,
    tesis TEXT,
    izin_toplam INTEGER,
    izin_kullanilan INTEGER,
    mesai_saat INTEGER
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS duyurular (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    baslik TEXT,
    icerik TEXT,
    departman TEXT,
    tesis TEXT,
    tarih TEXT
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS hedefler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    departman TEXT,
    ay TEXT,
    hedef INTEGER,
    gerceklesen INTEGER
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS raporlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tcno TEXT,
    rapor_adi TEXT,
    pdf_yolu TEXT
)
""")
conn.commit()

# ==================== ÖRNEK VERİLER ====================
ornek_kullanicilar = [
    ("1", "1", "Ahmet", "Yılmaz", "Üretim", "Vardiya Amiri", "Bandırma", 20, 5, 12),
    ("2", "2", "Mehmet", "Kaya", "Lojistik", "Depo Sorumlusu", "Kırka", 18, 10, 5),
]
for tc, sifre_plain, ad, soyad, departman, pozisyon, tesis, izin_toplam, izin_kullanilan, mesai_saat in ornek_kullanicilar:
    mevcut = c.execute("SELECT 1 FROM kullanicilar WHERE tcno = ?", (tc,)).fetchone()
    if mevcut is None:
        hashed_pw = bcrypt.hashpw(sifre_plain.encode(), bcrypt.gensalt()).decode()
        c.execute("""
        INSERT INTO kullanicilar VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (tc, hashed_pw, ad, soyad, departman, pozisyon, tesis, izin_toplam, izin_kullanilan, mesai_saat))
conn.commit()


# ==================== ÖRNEK VERİLER ====================
ornek_kullanicilar = [
    ("1", "1", "Ahmet", "Yılmaz", "Üretim", "Vardiya Amiri", "Bandırma", 20, 5, 12),
    ("23456789012", "654321", "Mehmet", "Kaya", "Lojistik", "Depo Sorumlusu", "Kırka", 18, 10, 5),
]
for tc, sifre_plain, ad, soyad, departman, pozisyon, tesis, izin_toplam, izin_kullanilan, mesai_saat in ornek_kullanicilar:
    mevcut = c.execute("SELECT 1 FROM kullanicilar WHERE tcno = ?", (tc,)).fetchone()
    if mevcut is None:
        hashed_pw = bcrypt.hashpw(sifre_plain.encode(), bcrypt.gensalt()).decode()
        c.execute("""
        INSERT INTO kullanicilar VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (tc, hashed_pw, ad, soyad, departman, pozisyon, tesis, izin_toplam, izin_kullanilan, mesai_saat))
conn.commit()

ornek_duyurular = [
    ("Bakım Planı", "Bandırma tesisinde 12 Ağustos bakım yapılacaktır.", "Üretim", "Bandırma", "2025-08-05"),
    ("Vardiya Değişikliği", "Gece vardiyası 1 saat erken başlayacaktır.", "Üretim", "Bandırma", "2025-08-04"),
]
for b, i, d, t, tarih in ornek_duyurular:
    mevcut = c.execute("SELECT 1 FROM duyurular WHERE baslik = ? AND tarih = ?", (b, tarih)).fetchone()
    if mevcut is None:
        c.execute("INSERT INTO duyurular (baslik, icerik, departman, tesis, tarih) VALUES (?, ?, ?, ?, ?)", (b, i, d, t, tarih))
conn.commit()

ornek_hedefler = [
    ("Üretim", "Ağustos 2025", 50000, 32000),
    ("Lojistik", "Ağustos 2025", 2000, 1400),
]
for d, ay, h, g in ornek_hedefler:
    mevcut = c.execute("SELECT 1 FROM hedefler WHERE departman = ? AND ay = ?", (d, ay)).fetchone()
    if mevcut is None:
        c.execute("INSERT INTO hedefler (departman, ay, hedef, gerceklesen) VALUES (?, ?, ?, ?)", (d, ay, h, g))
conn.commit()

ornek_raporlar = [
    ("1", "Eğitim Sertifikası", "raporlar/egitim.pdf"),
    ("23456789012", "Performans Raporu", "raporlar/performans.pdf"),
]
for tc, ad, yol in ornek_raporlar:
    mevcut = c.execute("SELECT 1 FROM raporlar WHERE tcno = ? AND rapor_adi = ?", (tc, ad)).fetchone()
    if mevcut is None:
        c.execute("INSERT INTO raporlar (tcno, rapor_adi, pdf_yolu) VALUES (?, ?, ?)", (tc, ad, yol))
conn.commit()

# ==================== FONKSİYONLAR ====================
def giris_yap(tcno, sifre):
    c.execute("SELECT sifre FROM kullanicilar WHERE tcno = ?", (tcno,))
    sonuc = c.fetchone()
    if sonuc and bcrypt.checkpw(sifre.encode(), sonuc[0].encode()):
        st.session_state["giris"] = True
        st.session_state["tcno"] = tcno
        return True
    return False

# ==================== LOGIN KONTROL ====================
if "giris" not in st.session_state:
    st.session_state["giris"] = False
if "tcno" not in st.session_state:
    st.session_state["tcno"] = None

if not st.session_state["giris"]:
    # Giriş ekranı
    st.markdown(f"""
    <style>
    .section-header {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }}
    .section-header h98 {{
        font-size: 50px;
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
        <h98>Kullanıcı Girişi</h98>
    </div>
    """, unsafe_allow_html=True)

    tcno = st.text_input("TC Kimlik No")
    sifre = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if giris_yap(tcno, sifre):
            st.success("✅ Giriş başarılı")
            st.rerun()
        else:
            st.error("❌ TC No veya şifre yanlış")

else:
    # Kullanıcı bilgilerini getir
    tcno = st.session_state["tcno"]
    c.execute("""
        SELECT ad, soyad, departman, pozisyon, tesis, izin_toplam, izin_kullanilan, mesai_saat
        FROM kullanicilar WHERE tcno = ?
    """, (tcno,))
    bilgi = c.fetchone()

    if not bilgi:
        st.error("Kullanıcı bilgileri bulunamadı.")
    else:
        # Hoşgeldiniz başlığı
        st.markdown(f"""
        <div class="section-header">
            <h14>👤 Hoş geldiniz, {bilgi[0]} {bilgi[1]}</h14>
            <div class="line"></div>
        </div>
        """, unsafe_allow_html=True)

        # Bilgi kartları
        col1, col2, col3 = st.columns(3)
        col1.markdown(f"<div class='info-card'><div class='card-title'>Departman</div>{bilgi[2]}</div>", unsafe_allow_html=True)
        col2.markdown(f"<div class='info-card'><div class='card-title'>Pozisyon</div>{bilgi[3]}</div>", unsafe_allow_html=True)
        col3.markdown(f"<div class='info-card'><div class='card-title'>Tesis</div>{bilgi[4]}</div>", unsafe_allow_html=True)

        # Kalan izin
        kalan_izin = bilgi[5] - bilgi[6]
        oran = (kalan_izin / bilgi[5]) * 100

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"""
<style>
.section-header {{
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}}
.section-header h199 {{
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
.section-header:hover h199 {{
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

/* Progress bar stili */
.custom-progress {{
    position: relative;
    height: 28px;
    background-color: #333;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 0 6px rgba(184,184,191,0.3);
}}
.custom-progress .fill {{
    height: 100%;
    background: linear-gradient(90deg, #474747, #89898f, #cdcdd4);
    animation: progressGlow 2s infinite alternate;
    transition: width 0.5s ease;
}}
@keyframes progressGlow {{
    0% {{ box-shadow: 0 0 5px #b8b8bf; }}
    100% {{ box-shadow: 0 0 15px #b8b8bf; }}
}}
.custom-progress .label {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-weight: bold;
    color: black;
}}
</style>

<div class="section-header">
    <h199>İzin Durumu</h199>
    <div class="line"></div>
</div>

<div class="custom-progress">
    <div class="fill" style="width: {oran}%;"></div>
    <div class="label">{kalan_izin} / {bilgi[5]} gün</div>
</div>
""", unsafe_allow_html=True)


        # Fazla mesai
        max_mesai = 40
        oran_mesai = (bilgi[7] / max_mesai) * 100
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="section-header">
            <h200>Fazla Mesai</h200>
            <div class="line"></div>
        </div>
        <div class="custom-progress">
            <div class="fill" style="width: {oran_mesai}%; background: linear-gradient(90deg, #6a6a6f, #b8b8bf, #e0e0e4);"></div>
            <div class="label">{bilgi[7]} / {max_mesai} saat</div>
        </div>
        """, unsafe_allow_html=True)
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
        <h200>Kişisel Performans Grafikleri</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .plotly-chart {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

    aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos"]
    kisisel_mesai = [10, 12, 8, 15, 14, 9, 13, bilgi[7]]
    departman_ortalama = [8, 10, 9, 12, 11, 8, 10, 11]

    fig = go.Figure()

    # Kişisel Mesai
    fig.add_trace(go.Scatter(
        x=aylar, y=kisisel_mesai,
        mode='lines+markers',
        name='Kişisel Mesai',
        line=dict(width=4, color='rgba(184, 184, 191, 1)'),
        marker=dict(size=10, color='rgba(184, 184, 191, 1)', line=dict(width=2, color='white'))
    ))

    # Departman Ortalaması
    fig.add_trace(go.Scatter(
        x=aylar, y=departman_ortalama,
        mode='lines+markers',
        name='Departman Ort.',
        line=dict(width=4, dash='dot', color='rgba(100, 100, 105, 0.8)'),
        marker=dict(size=8, color='rgba(100, 100, 105, 0.8)', line=dict(width=2, color='white'))
    ))

    # Tema ayarları
    fig.update_layout(
    margin=dict(t=5, b=0, l=40, r=40),  # b=0 alt boşluğu kaldırır
    plot_bgcolor='rgba(30,30,30,0.9)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#b8b8bf', size=14),
    legend=dict(
        bgcolor='rgba(0,0,0,0)',
        bordercolor='rgba(0,0,0,0)',
        font=dict(color='#b8b8bf')
    ),
    xaxis=dict(
        showgrid=True, gridcolor='rgba(80,80,80,0.3)',
        zeroline=False
    ),
    yaxis=dict(
        showgrid=True, gridcolor='rgba(80,80,80,0.3)',
        zeroline=False
    )
)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
# Günlük duyurular
    st.markdown("""
<style>
.section-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.section-header h200 {
    font-size: 32px;
    font-weight: 1000;
    background: linear-gradient(90deg, #474747, #89898f, #cdcdd4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    white-space: nowrap;
    letter-spacing: 1px;
    transition: transform 0.3s ease, letter-spacing 0.3s ease, text-shadow 0.3s ease;
}
.section-header:hover h200 {
    transform: scale(1.03);
    letter-spacing: 2px;
    text-shadow: 0 0 8px rgba(184, 184, 191, 0.6),
                 0 0 16px rgba(184, 184, 191, 0.4);
}
.section-header .line {
    flex-grow: 1;
    height: 3px;
    background: linear-gradient(90deg, #9a9aa0, #b8b8bf, #d6d6dc);
    border-radius: 5px;
    margin-left: 20px;
}

/* Duyuru kartı */
.announcement-card {
    background: rgba(30, 30, 30, 0.95);
    padding: 15px 20px;
    margin-bottom: 15px;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,0,0,0.3);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    border: 1px solid rgba(184,184,191,0.3);
}
.announcement-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 18px rgba(184,184,191,0.4);
}
.announcement-card strong {
    font-size: 20px;
    color: #b8b8bf;
}
.announcement-date {
    float: right;
    font-size: 14px;
    color: #888;
}
.announcement-card p {
    color: #ddd;
    margin-top: 8px;
}
</style>
<div class="section-header">
    <h200>📢 Günlük Duyurular</h200>
    <div class="line"></div>
</div>
""", unsafe_allow_html=True)

# --- Duyuru verilerini çek ---
    c.execute(
    "SELECT baslik, icerik, tarih FROM duyurular WHERE departman = ? OR tesis = ?",
    (bilgi[2], bilgi[4])
)

# --- Duyuruları göster ---
    for baslik, icerik, tarih in c.fetchall():
        st.markdown(
        f"""
        <div class="announcement-card">
            <strong>{baslik}</strong>
            <span class="announcement-date">{tarih}</span>
            <p>{icerik}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br><br>", unsafe_allow_html=True)
# Başlık - Temaya Uygun
    st.markdown("""
<style>
.section-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.section-header h200 {
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
}
.section-header:hover h200 {
    transform: scale(1.03);
    letter-spacing: 2px;
    text-shadow: 0 0 8px rgba(184, 184, 191, 0.6), 
                 0 0 16px rgba(184, 184, 191, 0.4);
}
.section-header .line {
    flex-grow: 1;
    height: 3px;
    background: linear-gradient(90deg, #9a9aa0, #b8b8bf, #d6d6dc);
    border-radius: 5px;
    margin-left: 20px;
}

/* Özel progress bar */
.custom-progress {
    position: relative;
    height: 26px;
    background-color: #333;
    border-radius: 13px;
    overflow: hidden;
    box-shadow: 0 0 6px rgba(184,184,191,0.3);
    margin-bottom: 15px;
}
.custom-progress .fill {
    height: 100%;
    background: linear-gradient(90deg, #6a6a6f, #b8b8bf, #e0e0e4);
    animation: progressGlow 2s infinite alternate;
    transition: width 0.5s ease;
}
@keyframes progressGlow {
    0% { box-shadow: 0 0 5px #b8b8bf; }
    100% { box-shadow: 0 0 15px #b8b8bf; }
}
.custom-progress .label {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-weight: bold;
    color: black;
}
</style>

<div class="section-header">
    <h200>🎯 Departman Hedefleri</h200>
    <div class="line"></div>
</div>
""", unsafe_allow_html=True)

# Departman hedeflerini özel progress bar ile göster
    c.execute("SELECT ay, hedef, gerceklesen FROM hedefler WHERE departman = ?", (bilgi[2],))
    for ay, hedef, gerceklesen in c.fetchall():
        oran = gerceklesen / hedef * 100
        st.markdown(f"""
    <div><strong>{ay}</strong></div>
    <div class="custom-progress">
        <div class="fill" style="width: {min(oran,100)}%;"></div>
        <div class="label">{gerceklesen} / {hedef} ton ({oran:.1f}%)</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

 # ==================== KİŞİSEL RAPORLAR ====================
    st.markdown("""
<style>
.report-card {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(184,184,191,0.3);
    color: #b8b8bf;
    font-size: 18px;
    margin-bottom: 8px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.report-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(184,184,191,0.5);
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
        <h200>📂 Kişisel Raporlar</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

# Burada veritabanından rapor adlarını alıyoruz
    c.execute("SELECT rapor_adi FROM raporlar WHERE tcno = ?", (tcno,))
    raporlar_db = c.fetchall()

# Eğer DB'den rapor gelmezse örnek listeyi göster
    if raporlar_db:
        raporlar = [r[0] for r in raporlar_db]
    else:
        raporlar = [
        "Eğitim Sertifikası",
        "Performans Raporu",
        "Yıllık İzin Durum Raporu",
        "Fazla Mesai Analiz Raporu",
        "Sağlık Kontrol Formu"
    ]

    for rapor in raporlar:
        st.markdown(f"<div class='report-card'>📄 {rapor}</div>", unsafe_allow_html=True)


        st.markdown("<br><br>", unsafe_allow_html=True)
    # Vardiya Tablosu Başlık
        st.markdown("""
<style>
.section-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.section-header h200 {
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
}
.section-header:hover h200 {
    transform: scale(1.03);
    letter-spacing: 2px;
    text-shadow: 0 0 8px rgba(184, 184, 191, 0.6), 
                 0 0 16px rgba(184, 184, 191, 0.4);
}
.section-header .line {
    flex-grow: 1;
    height: 3px;
    background: linear-gradient(90deg, #9a9aa0, #b8b8bf, #d6d6dc);
    border-radius: 5px;
    margin-left: 20px;
}
</style>

<div class="section-header">
    <h200>Vardiya Tablosu</h200>
    <div class="line"></div>
</div>
""", unsafe_allow_html=True)
# Vardiya verileri
    bugun = datetime.date.today().strftime("%Y-%m-%d")
    vardiya_veri = [
    ["2025-08-04", "Gece", "00:00 - 08:00"],
    ["2025-08-05", "Gündüz", "08:00 - 16:00"],
    ["2025-08-06", "Akşam", "16:00 - 00:00"],
]

# Gün satırı arka plan renkleri
    row_colors = [
    "rgba(184,184,191,0.2)" if tarih == bugun else "rgba(30,30,30,0.95)"
    for tarih, _, _ in vardiya_veri
]

# Tablo oluşturma
    fig = go.Figure(data=[go.Table(
    columnwidth=[80, 100, 120],
    header=dict(
        values=["<b>Tarih</b>", "<b>Vardiya</b>", "<b>Saat</b>"],
        fill_color="rgba(71,71,71,1)",
        line_color="rgba(120,120,120,0.3)",
        font=dict(color="white", size=20, family="Arial Black"),
        align="center",
        height=45
    ),
    cells=dict(
        values=list(zip(*vardiya_veri)),
        fill_color=[row_colors],
        line_color="rgba(120,120,120,0.3)",
        font=dict(color="#b8b8bf", size=18),
        align="center",
        height=40
    )
)])
    fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),  # b=0 ile alt boşluğu tamamen kaldır
    paper_bgcolor="rgba(0,0,0,0)",
)

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown("""
<style>
/* Plotly chart ile sonraki eleman arasındaki boşluğu kaldır */
.block-container > div {
    margin-bottom: 0rem !important;
    padding-bottom: 0rem !important;
}
</style>
""", unsafe_allow_html=True)

# ==================== OTURUMU KAPAT BUTONU ====================
    # ==================== OTURUMU KAPAT BUTONU ====================
    st.markdown("""
<style>
div[data-testid="stButton"] button {
    background: linear-gradient(90deg, #474747, #89898f, #cdcdd4);
    color: black !important;
    border: none;
    padding: 8px 20px;
    font-size: 16px;
    font-weight: 800px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 0 8px rgba(184,184,191,0.4);
    text-align: center;
}
div[data-testid="stButton"] button:hover {
    background: linear-gradient(90deg, #5a5a5a, #a0a0a7, #e0e0e4);
    box-shadow: 0 0 15px rgba(184,184,191,0.7);
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Oturumu Kapat"):
            st.session_state["giris"] = False
            st.session_state["tcno"] = None
            st.rerun()

