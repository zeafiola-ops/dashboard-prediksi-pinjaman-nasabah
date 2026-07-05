# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

import streamlit as st
from pathlib import Path

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Informasi Penelitian",
    page_icon="📚",
    layout="wide"
)

# ==========================================================
# PATH
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

LOGO_DASHBOARD = BASE_DIR / "assets" / "logo.png"
LOGO_DARMAJAYA = BASE_DIR / "assets" / "logo_darmajaya.png"

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

/* =======================================================
BACKGROUND
======================================================= */

.stApp{
    background:linear-gradient(180deg,#EEF6FF 0%,#DCEBFF 100%);
}

/* =======================================================
MAIN CONTAINER
======================================================= */

.main .block-container{
    padding-top:2rem;
    padding-left:2.8rem;
    padding-right:2.8rem;
    padding-bottom:2rem;
}

/* =======================================================
SIDEBAR
======================================================= */

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#1545B3,#4E96FF);
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* =======================================================
HEADER CARD
======================================================= */

.header-card{

    background:white;

    padding:35px;

    border-radius:22px;

    box-shadow:0px 8px 25px rgba(0,0,0,.08);

    margin-bottom:30px;

}

/* =======================================================
TITLE
======================================================= */

.header-title{

    text-align:center;

    font-size:48px;

    font-weight:800;

    color:#1848A5;

    margin-bottom:10px;

}

/* =======================================================
SUBTITLE
======================================================= */

.header-subtitle{

    text-align:center;

    font-size:30px;

    font-weight:600;

    color:#2F2F2F;

    margin-bottom:8px;

}

/* =======================================================
DESCRIPTION
======================================================= */

.header-desc{

    text-align:center;

    font-size:20px;

    color:#666666;

}
/* ==========================================
IDENTITAS CARD
========================================== */

.info-card{

background:white;

padding:25px;

border-radius:18px;

text-align:center;

box-shadow:0px 6px 18px rgba(0,0,0,.08);

transition:0.3s;

border-top:6px solid #1E4DB7;

height:180px;

}

.info-card:hover{

transform:translateY(-5px);

}

.info-icon{

font-size:38px;

margin-bottom:10px;

}

.info-title{

font-size:17px;

font-weight:600;

color:#666;

}

.info-value{

font-size:22px;

font-weight:bold;

color:#1848A5;

margin-top:10px;

}
/* ==========================================
TUJUAN & MANFAAT
========================================== */

.content-card{

background:white;

padding:28px;

border-radius:20px;

box-shadow:0px 6px 18px rgba(0,0,0,.08);

height:100%;

transition:.3s;

}

.content-card:hover{

transform:translateY(-5px);

}

.content-title{

font-size:24px;

font-weight:bold;

color:#1848A5;

margin-bottom:15px;

text-align:center;

}

.content-text{

font-size:17px;

line-height:1.9;

text-align:justify;

color:#444;

}
/* ==========================================
DATASET PENELITIAN
========================================== */

.dataset-card{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0px 6px 18px rgba(0,0,0,.08);

margin-bottom:25px;

}

.dataset-title{

font-size:32px;

font-weight:bold;

color:#1848A5;

text-align:center;

margin-bottom:15px;

}

.dataset-text{

font-size:17px;

line-height:1.9;

text-align:justify;

color:#444;

}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(str(LOGO_DASHBOARD), use_container_width=True)

    st.markdown("""
    <div style="text-align:center;">

    <h2 style="margin-bottom:0;">
    Informasi Penelitian
    </h2>

    <p style="font-size:16px;">
    Prediksi Status Pinjaman Nasabah
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""

### 📚 Tentang Halaman

Halaman ini berisi informasi lengkap mengenai penelitian, mulai dari identitas peneliti, tujuan penelitian, dataset, metode Random Forest, hingga tools yang digunakan dalam pembangunan dashboard.

""")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("<div class='header-card'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.3,4,1.3])

with col1:

    st.image(
        str(LOGO_DASHBOARD),
        width=90
    )

with col2:

    st.markdown("""

<div class="header-title">

📚 Informasi Penelitian

</div>

<div class="header-subtitle">

Prediksi Status Pinjaman Nasabah

</div>

<div class="header-desc">

Menggunakan Metode Random Forest

</div>

""", unsafe_allow_html=True)

with col3:

    st.image(
        str(LOGO_DARMAJAYA),
        width=230
    )

st.markdown("</div>", unsafe_allow_html=True)

st.divider()
# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

st.markdown("""
<div class="card">

<h2 style="
text-align:center;
color:#1848A5;
font-size:32px;
">
👤 Profil Penelitian
</h2>
<hr>

<table style="width:100%;font-size:18px;line-height:2.2;">

<tr>
<td width="240"><b>Nama Peneliti</b></td>
<td>: Muhammad Rizki Maulidin</td>
</tr>

<tr>
<td><b>NPM</b></td>
<td>: 2211050009</td>
</tr>

<tr>
<td><b>Program Studi</b></td>
<td>: Sistem Informasi</td>
</tr>

<tr>
<td><b>Judul Skripsi</b></td>
<td>: Prediksi Status Pinjaman Nasabah Menggunakan Metode Random Forest</td>
</tr>

<tr>
<td><b>Metode</b></td>
<td>: Random Forest</td>
</tr>

<tr>
<td><b>Tahun Penelitian</b></td>
<td>: 2026</td>
</tr>

</table>

</div>

""", unsafe_allow_html=True)

st.divider()
st.subheader("🌐 Informasi Pendukung")

k1,k2,k3 = st.columns(3)

with k1:

    st.link_button(

        "📂 Dataset Kaggle",

        "https://www.kaggle.com/datasets/ardava/dataset-klasifikasi-status-pinjaman",

        use_container_width=True

    )

with k2:

    st.link_button(

        "🏫 Website Darmajaya",

        "https://www.darmajaya.ac.id",

        use_container_width=True

    )

with k3:

    st.link_button(

        "🌲 Random Forest",

        "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html",

        use_container_width=True

    )

st.divider()
# ==========================================================
# TUJUAN DAN MANFAAT PENELITIAN
# ==========================================================

st.markdown("""
<div class="card">

<h2 style="
text-align:center;
color:#1848A5;
font-size:32px;
">

🎯 Tujuan dan Manfaat Penelitian

</h2>

<p style="
text-align:center;
color:#666;
font-size:17px;
">

Penelitian ini bertujuan untuk membangun model prediksi status
pinjaman nasabah menggunakan metode Random Forest serta
menyajikan hasil analisis dalam bentuk dashboard interaktif.

</p>

</div>
""", unsafe_allow_html=True)
kiri, kanan = st.columns(2)

with kiri:

    st.markdown("""
<div class="content-card">

<div class="content-title">

🎯 Tujuan Penelitian

</div>

<div class="content-text">

<ul>

<li>Membangun model prediksi status pinjaman nasabah menggunakan metode <b>Random Forest</b>.</li>

<li>Menghasilkan prediksi yang dapat membantu proses pengambilan keputusan.</li>

<li>Menyediakan dashboard interaktif sebagai media visualisasi hasil prediksi.</li>

<li>Memberikan informasi prediksi secara cepat, mudah dipahami, dan informatif.</li>

</ul>

</div>

</div>
""", unsafe_allow_html=True)

with kanan:

    st.markdown("""
<div class="content-card">

<div class="content-title">

💡 Manfaat Penelitian

</div>

<div class="content-text">

<ul>

<li>Membantu lembaga keuangan dalam mengidentifikasi potensi kelayakan pinjaman.</li>

<li>Meningkatkan efisiensi proses analisis data pinjaman.</li>

<li>Menyediakan media visualisasi berbasis dashboard untuk mendukung pengambilan keputusan.</li>

<li>Menjadi referensi penelitian selanjutnya pada bidang Business Intelligence dan Machine Learning.</li>

</ul>

</div>

</div>
""", unsafe_allow_html=True)

st.divider()
# ==========================================================
# DATASET PENELITIAN
# ==========================================================

st.markdown("""
<div class="dataset-card">

<div class="dataset-title">

📂 Dataset Penelitian

</div>

<div class="dataset-text">

Dataset yang digunakan dalam penelitian ini merupakan
<b>Dataset Klasifikasi Status Pinjaman</b> yang diperoleh dari
platform <b>Kaggle</b>. Dataset ini digunakan sebagai sumber
data utama untuk membangun model prediksi status pinjaman
nasabah menggunakan metode <b>Random Forest</b>.

</div>

</div>

""", unsafe_allow_html=True)
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "📊 Jumlah Data",
        "50.000"
    )

with col2:
    st.metric(
        "📑 Jumlah Fitur",
        "20"
    )

with col3:
    st.metric(
        "🎯 Target",
        "Status Pinjaman"
    )

with col4:
    st.metric(
        "📈 Kelas",
        "2"
    )
    st.info("""

🟢 **Kelas Target**

**1 = Lancar**

**0 = Tidak Lancar**

""")
    st.link_button(

    "🌐 Buka Dataset Kaggle",

    "https://www.kaggle.com/datasets/ardava/dataset-klasifikasi-status-pinjaman",

    use_container_width=True

)

st.divider()
