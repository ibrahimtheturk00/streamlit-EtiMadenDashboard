import streamlit as st

st.set_page_config(page_title="Ürünler ve Sektörler")
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
st.markdown(f"""
<style>
.section-header {{
    display: flex;
    align-items: center;
    margin-bottom: 30px;
}}

.section-header h15 {{
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

.section-header:hover h15 {{
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
    <h15>ETİMADEN</h15>
    <div class="line"></div>
</div>
""", unsafe_allow_html=True)
# ===== CSS =====
st.markdown("""
<style>
.stTabs [role="tablist"] {
    justify-content: center;
}
.blog-card {
    background-color: #1e1e1e;
    background: linear-gradient(90deg, #262626, #323333, #4a4a4a);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 35px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
}
.blog-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.5);
}
.blog-card h3 {
    font-size: 22px;
    font-weight: bold;
    background: linear-gradient(90deg, #c7c7c7, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}
.blog-card p {
    color: #d1d1d1;
    font-size: 16px;
    text-align: justify;
}
img {
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# ===== ETİMADEN Başlığı =====

# ===== Sekmeler =====
tab1, tab2 = st.tabs(["Ürünler", "Sektörler"])

# --- ÜRÜNLER ---
with tab1:
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
        <h200>Bor Ürünleri ve Kullanım Alanları</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    urunler = [
    {
        "ad": "Boraks",
        "aciklama": "Boraks, doğada kristal formda bulunan beyaz renkli bir mineraldir ve en önemli bor bileşiklerinden biridir. Cam ve seramik sektöründe ısıl dayanımı artırmak, deterjanlarda temizlik gücünü yükseltmek ve metalurji endüstrisinde ergitme sıcaklığını düşürmek için yaygın olarak kullanılır. Ayrıca ahşap koruyucu, su yumuşatıcı ve çeşitli kimyasal reaksiyonlarda katalizör olarak da görev yapar.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\boraks.png"
    },
    {
        "ad": "Borik Asit",
        "aciklama": "Borik asit, hafif asidik özellikte beyaz toz halinde bir bor bileşiğidir. Cam üretiminde şeffaflığı ve mukavemeti artırmak, elektronik sektöründe ısı direncini geliştirmek, tıp alanında antiseptik ve mantar önleyici olarak kullanılır. Ayrıca ahşap koruma, böcek ilacı yapımı ve alev geciktirici uygulamalarda da önemli bir rol oynar.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\borikasit.png"
    },
    {
        "ad": "Etidot-67",
        "aciklama": "Etidot-67, özellikle tarım sektöründe bor eksikliğini gidermek amacıyla kullanılan suda çözünebilen bir bor bileşiğidir. Bitkilerin büyüme ve gelişiminde önemli bir rol oynar, çiçeklenme ve meyve tutumunu artırır. Ayrıca toprak düzenleyici olarak kullanılarak tarımsal verimliliği artırmaya yardımcı olur.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\etidot67.png"
    },
    {
        "ad": "Susuz Boraks",
        "aciklama": "Susuz boraks, yüksek saflıkta üretilen ve nem içermeyen bir bor bileşiğidir. Cam elyafı, seramik fritler, emaye kaplamalar ve metalurji endüstrisinde ergitme maddesi olarak kullanılır. Yüksek sıcaklıklara dayanıklılığı ve düşük erime sıcaklığı sayesinde çeşitli endüstriyel üretim süreçlerinde tercih edilir.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\susuzboraks.png"
    }
]

    for u in urunler:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(u["gorsel"], width=220)
        with col2:
            st.markdown(f"<div class='blog-card'><h3>{u['ad']}</h3><p>{u['aciklama']}</p></div>", unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
# --- SEKTÖRLER ---
with tab2:
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
        <h200>Bor Kullanılan Sektörler</h200>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)
    sektorler = [
    {
        "ad": "Cam",
        "aciklama": "Bor, cam üretiminde ısıl genleşmeyi azaltarak camın dayanıklılığını artırır. Özellikle borosilikat cam üretiminde tercih edilir çünkü yüksek sıcaklık değişimlerine karşı dayanıklıdır. Laboratuvar ekipmanları, fırın camları ve optik cihazlarda sıkça kullanılır.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\cam.png"
    },
    {
        "ad": "Deterjan",
        "aciklama": "Bor bileşikleri, deterjanlarda suyun sertliğini azaltarak temizleme gücünü artırır. Ayrıca lekelerin çözülmesine yardımcı olur ve kumaşlarda renklerin korunmasına katkı sağlar. Çamaşır deterjanlarından endüstriyel temizlik malzemelerine kadar geniş bir kullanım alanına sahiptir.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\deterjan.png"
    },
    {
        "ad": "Metalurji",
        "aciklama": "Metalurji sektöründe bor, alaşımların sertliğini ve dayanıklılığını artırmak için kullanılır. Kaynak akılarında ergime sıcaklığını düşürerek enerji tasarrufu sağlar. Ayrıca çelik üretiminde mukavemeti artırıcı katkı maddesi olarak görev yapar.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\metal.png"
    },
    {
        "ad": "Seramik",
        "aciklama": "Seramik sektöründe bor, sırların pürüzsüz ve parlak olmasını sağlar. Ayrıca ürünlerin darbelere ve çizilmelere karşı dayanıklılığını artırır. Fayans, porselen ve dekoratif objelerde yaygın olarak kullanılır.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\seramik.png"
    },
    {
        "ad": "Yakıt Hücreleri",
        "aciklama": "Bor bileşikleri, hidrojen depolama sistemlerinde enerji yoğunluğunu artırmak için kullanılır. Yakıt hücrelerinde enerji dönüşüm verimliliğini yükseltir ve uzun süreli enerji depolama sağlar.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\yakithucresi.png"
    },
    {
        "ad": "Zirai İlaç",
        "aciklama": "Bor, bitki gelişiminde gerekli bir mikro elementtir ve zirai ilaçlarda verimliliği artırmak amacıyla kullanılır. Bitkilerin çiçeklenme, polen oluşumu ve meyve gelişimini destekler.",
        "gorsel": r"C:\\Users\\turki\\OneDrive\\Desktop\\proje\\pages\\zirailac.png"
    }
]

    for s in sektorler:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(s["gorsel"], width=220)
        with col2:
            st.markdown(f"<div class='blog-card'><h3>{s['ad']}</h3><p>{s['aciklama']}</p></div>", unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)