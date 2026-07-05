import streamlit as st
from pathlib import Path

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================

st.set_page_config(
    page_title="Informasi Penelitian",
    page_icon="📚",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"

# ======================================================
# CSS
# ======================================================

st.markdown("""
<style>

/* =========================
   Background
========================= */

.stApp{
    background: linear-gradient(180deg,#EEF5FF 0%,#DDEBFF 100%);
}

/* =========================
   Main Container
========================= */

.main .block-container{
    padding-top:2rem;
    padding-left:2.5rem;
    padding-right:2.5rem;
    padding-bottom:2rem;
}

/* =========================
   Sidebar
========================= */

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#1746B5,#4B8DFF);
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* =========================
   Card
========================= */

.card{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 5px 18px rgba(0,0,0,.08);
    margin-bottom:25px;
}

/* =========================
   Title
========================= */

.title{

font-size:48px;

font-weight:700;

color:#1848B8;

text-align:center;

margin-bottom:10px;

}

/* =========================
   Subtitle
========================= */

.subtitle{

font-size:22px;

text-align:center;

color:#4B5563;

line-height:1.8;

}
/* =========================
   Footer
========================= */

.footer{
    margin-top:40px;
    padding:20px;
    background:white;
    border-radius:15px;
    text-align:center;
    color:#666;
    box-shadow:0px 4px 15px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)
# ======================================================
# HEADER INFORMASI PENELITIAN
# ======================================================

LOGO_DARMAJAYA = BASE_DIR / "assets" / "logo_darmajaya.png"

col1, col2, col3 = st.columns([1.2, 2.5, 1.2])

with col1:
    st.image(str(LOGO_PATH), width=180)

with col2:

    st.markdown("""
    <div class="title">
        📚 Informasi Penelitian
    </div>

    <div class="subtitle">
        <b>Prediksi Status Pinjaman Nasabah</b><br>
        Menggunakan Metode Random Forest
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.image(str(LOGO_DARMAJAYA), width=170)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()
