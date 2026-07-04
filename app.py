import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from PIL import Image

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Dashboard Prediksi Status Pinjaman Nasabah",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PATH PROJECT
# ==========================================
BASE_DIR = Path(__file__).parent

DATA_PATH = BASE_DIR / "data" / "hasil_prediksi_deployment_google_sheets.xlsx"
FEATURE_PATH = BASE_DIR / "data" / "feature_names.pkl"
MODEL_PATH = BASE_DIR / "model" / "random_forest_model.pkl"
LOGO_PATH = BASE_DIR / "assets" / "logo.png"

# ==========================================
# LOAD DATASET
# ==========================================
@st.cache_data
def load_data():
    return pd.read_excel(DATA_PATH)

df = load_data()

# ==========================================
# LOAD FEATURE
# ==========================================
@st.cache_resource
def load_feature():
    return joblib.load(FEATURE_PATH)

feature_names = load_feature()

# ==========================================
# LOAD MODEL
# ==========================================
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

# Jika model belum ada, dashboard tetap bisa dibuka
try:
    model = load_model()
except:
    model = None

# ==========================================
# LOAD LOGO
# ==========================================
logo = Image.open(LOGO_PATH)

# ==========================================
# HOME
# ==========================================

col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image(logo, width=170)

st.markdown("""
<div style="text-align:center; margin-top:-10px;">

<h1 style="
color:#1E3A8A;
font-size:58px;
font-weight:900;
margin:0;
padding:0;
line-height:1.1;
">

Selamat Datang

</h1>

<h3 style="
color:#2563EB;
font-size:30px;
font-weight:700;
margin-top:10px;
margin-bottom:8px;
line-height:1.2;
">

Dashboard Prediksi Status Pinjaman Nasabah

</h3>

<p style="
font-size:20px;
color:#64748B;
margin:0;
line-height:1.5;
">

Analisis Prediksi Status Pinjaman Nasabah<br>
Menggunakan Metode <b>Random Forest</b>

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================
# LOAD CSS
# ==========================================
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
# =====================================================
# DESKRIPSI DASHBOARD
# =====================================================

st.markdown("## 📋 Deskripsi Dashboard")

st.markdown(
"""
Dashboard Prediksi Status Pinjaman Nasabah merupakan aplikasi visualisasi berbasis
**Business Intelligence** yang dikembangkan untuk membantu proses analisis data
pinjaman nasabah menggunakan **metode Random Forest**.

Dashboard ini menyajikan informasi secara interaktif mulai dari ringkasan data,
visualisasi karakteristik nasabah, evaluasi performa model, hingga fitur prediksi
status pinjaman berdasarkan data yang dimasukkan oleh pengguna.

Melalui dashboard ini, pengguna dapat memperoleh informasi secara lebih cepat,
mudah dipahami, dan mendukung proses pengambilan keputusan berdasarkan hasil
analisis data.
"""
)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# BAGIAN 3 - KPI DASHBOARD
# ==========================================================
# ==========================================================
# KPI DASHBOARD
# ==========================================================

st.markdown("## 📊 Ringkasan Dashboard")

# ==============================
# Menghitung KPI
# ==============================

total_data = len(df)

total_lancar = len(df[df["status_prediksi"] == 1])

total_tidak_lancar = len(df[df["status_prediksi"] == 0])

nama_model = "Random Forest"

# ==============================
# Membuat 4 Kolom
# ==============================

col1, col2, col3, col4 = st.columns(4)

# ==============================
# KPI 1
# ==============================

with col1:

    st.metric(

        label="👥 Total Data",

        value=f"{total_data:,}"

    )

# ==============================
# KPI 2
# ==============================

with col2:

    st.metric(

        label="✅ Status Lancar",

        value=f"{total_lancar:,}"

    )

# ==============================
# KPI 3
# ==============================

with col3:

    st.metric(

        label="❌ Tidak Lancar",

        value=f"{total_tidak_lancar:,}"

    )

# ==============================
# KPI 4
# ==============================

with col4:

    st.metric(

        label="🌲 Model",

        value=nama_model

    )

st.markdown("<br>", unsafe_allow_html=True)
