import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
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
    st.image(logo, width=180)

# Jarak logo ke judul
st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">

<h1 style="
font-size:60px;
font-weight:900;
color:#1E3A8A;
line-height:1.0;
margin:0;
">
Selamat Datang

</h1>

<h3 style="
font-size:30px;
font-weight:700;
color:#2563EB;
line-height:1.0;
margin:8px 0px 5px 0px;
">
Dashboard Prediksi Status Pinjaman Nasabah

</h3>

<p style="
font-size:19px;
color:#64748B;
line-height:1.4;
margin:0;
">
Analisis Prediksi Status Pinjaman Nasabah<br>
Menggunakan Metode <b>Random Forest</b>

</p>

</div>
""", unsafe_allow_html=True)
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
# ==========================================================
# BAGIAN 4
# VISUALISASI DATA
# ==========================================================

st.markdown("---")

st.markdown("""
<h2 style="
color:#1E3A8A;
font-weight:700;
margin-bottom:5px;
">

("## 📊Visualisasi Data")
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
color:#64748B;
font-size:18px;
margin-top:0px;
margin-bottom:20px;
">
Visualisasi karakteristik data dan hasil prediksi status pinjaman nasabah menggunakan metode Random Forest.

</p>
""", unsafe_allow_html=True)
