# ==========================================================
# IMPORT LIBRARY
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

from pathlib import Path

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Prediksi Status Pinjaman",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "assets/logo_dashboard.png",
        use_container_width=True
    )

    st.markdown("""
    <div style="text-align:center;">

    <h2 style="color:white;margin-bottom:0px;">
    Dashboard Prediksi
    </h2>

    <p style="color:#D6E4FF;font-size:15px;">
    Status Pinjaman Nasabah
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#1E88E5,#1565C0);
        padding:18px;
        border-radius:15px;
        color:white;
    ">

    <h4>🤖 Tentang Prediksi</h4>

    <p style="font-size:14px;">

    Halaman ini digunakan
    untuk melakukan prediksi
    status pinjaman nasabah
    menggunakan model
    <b>Random Forest</b>.

    </p>

    <hr>

    ✅ Akurat<br>
    ⚡ Cepat<br>
    💻 Mudah Digunakan

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("© 2026 Dashboard Prediksi")

# ==========================================================
# PATH PROJECT
# ==========================================================

BASE_DIR = Path(__file__).parent.parent

MODEL_PATH = BASE_DIR / "model" / "random_forest_model (1).pkl"

FEATURE_PATH = BASE_DIR / "data" / "feature_names.pkl"

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    return model

model = load_model()

# ==========================================================
# LOAD FEATURE NAMES
# ==========================================================

@st.cache_resource
def load_feature_names():
    feature_names = joblib.load(FEATURE_PATH)
    return feature_names

feature_names = load_feature_names()

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<h1 style="text-align:center;color:#174EA6;font-weight:bold;">
🤖 Prediksi Status Pinjaman Nasabah
</h1>

<p style="text-align:center;color:gray;font-size:17px;">
Masukkan informasi calon nasabah untuk memperoleh
hasil prediksi status pinjaman menggunakan
<b>Random Forest</b>.
</p>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# FORM INPUT DATA NASABAH
# ==========================================================

st.markdown("""
<div class="section-card">

<h3>📝 Form Input Data Nasabah</h3>

<p>
Silakan isi data calon nasabah untuk melakukan prediksi status pinjaman.
</p>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ==========================
# KOLOM KIRI
# ==========================

with col1:

    usia = st.number_input(
        "Usia",
        min_value=18,
        max_value=100,
        value=30
    )

    lama_bekerja = st.number_input(
        "Lama Bekerja (Tahun)",
        min_value=0.0,
        value=5.0
    )

    pendapatan = st.number_input(
        "Pendapatan Tahunan",
        min_value=0,
        value=50000000
    )

    skor_kredit = st.number_input(
        "Skor Kredit",
        min_value=300,
        max_value=900,
        value=650
    )

    lama_riwayat = st.number_input(
        "Lama Riwayat Kredit (Tahun)",
        min_value=0.0,
        value=5.0
    )

    aset_tabungan = st.number_input(
        "Aset Tabungan",
        min_value=0,
        value=10000000
    )

    hutang = st.number_input(
        "Hutang Saat Ini",
        min_value=0,
        value=5000000
    )

# ==========================
# KOLOM KANAN
# ==========================

with col2:

    gagal_bayar = st.selectbox(
        "Pernah Gagal Bayar",
        ["Tidak", "Ya"]
    )

    tunggakan = st.number_input(
        "Tunggakan 2 Tahun Terakhir",
        min_value=0,
        value=0
    )

    catatan_negatif = st.number_input(
        "Jumlah Catatan Negatif",
        min_value=0,
        value=0
    )

    jumlah_pinjaman = st.number_input(
        "Jumlah Pinjaman",
        min_value=0,
        value=10000000
    )

    suku_bunga = st.number_input(
        "Suku Bunga (%)",
        min_value=0.0,
        value=10.0
    )

    status_pekerjaan = st.selectbox(
        "Status Pekerjaan",
        [
            "Pegawai",
            "Mahasiswa",
            "Wiraswasta"
        ]
    )

    tipe_produk = st.selectbox(
        "Tipe Produk",
        [
            "Kredit Baru",
            "Kredit Berjalan",
            "Pinjaman Pribadi"
        ]
    )

    tujuan = st.selectbox(
        "Tujuan Pinjaman",
        [
            "Kendaraan",
            "Konsolidasi Hutang",
            "Medis",
            "Pendidikan",
            "Pribadi",
            "Renovasi Rumah"
        ]
    )
