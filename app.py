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
# HOME SEMENTARA
# ==========================================
st.image(logo, width=120)

st.title("Selamat Datang")

st.write("Dashboard Prediksi Status Pinjaman Nasabah")
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
