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
# IDENTITAS PENELITIAN
# ==========================================================

st.markdown("""
<div class="card">

<h2 style="
color:#1848A5;
text-align:center;
font-size:32px;
margin-bottom:15px;
">
👤 Identitas Penelitian
</h2>

<p style="
text-align:center;
font-size:18px;
color:#666;
margin-bottom:15px;
">
Informasi umum mengenai penelitian yang dilakukan.
</p>

</div>
""", unsafe_allow_html=True)
