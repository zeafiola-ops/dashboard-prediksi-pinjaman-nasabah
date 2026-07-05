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

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================================
# PATH
# ==========================================================

BASE_DIR = Path(__file__).parent.parent

LOGO_PATH = BASE_DIR / "assets" / "logo.png"

MODEL_PATH = BASE_DIR / "model" / "random_forest_model (1).pkl"

FEATURE_PATH = BASE_DIR / "data" / "feature_names.pkl"

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# ==========================================================
# LOAD FEATURE
# ==========================================================

@st.cache_resource
def load_feature():

    return joblib.load(FEATURE_PATH)

feature_names = load_feature()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(str(LOGO_PATH), use_container_width=True)

    st.markdown(
        """
        <div style="text-align:center;">
        <h2>Dashboard Prediksi</h2>
        <p>Status Pinjaman Nasabah</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
        background:linear-gradient(135deg,#1E88E5,#1565C0);
        padding:18px;
        border-radius:15px;
        color:white;
        ">

        <h4>🤖 Tentang Prediksi</h4>

        <p>

        Halaman ini digunakan
        untuk melakukan prediksi
        status pinjaman nasabah
        menggunakan model
        <b>Random Forest</b>.

        </p>

        <hr>

        ✅ Akurat <br>
        ⚡ Cepat <br>
        💻 Mudah Digunakan

        </div>

        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("© 2026 Dashboard Prediksi")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<h1 style='text-align:center;color:#174EA6;'>
🤖 Prediksi Status Pinjaman Nasabah
</h1>
<p style='text-align:center;
font-size:18px;
color:#555;'>
<b>Halaman ini digunakan untuk memprediksi status pinjaman nasabah berdasarkan 
data yang dimasukkan menggunakan model Random Forest.
</b> 
</p>

""", unsafe_allow_html=True)

st.divider()
st.divider()
# ==========================================================
# FORM INPUT DATA NASABAH
# ==========================================================

st.markdown("""
<div class="section-card">

<h3>📝 Form Input Data Nasabah</h3>

<p>
Silakan lengkapi data calon nasabah pada formulir berikut untuk memperoleh hasil prediksi status pinjaman.
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

# ==========================================================
# INPUT KOLOM KIRI
# ==========================================================

with left:

    usia = st.number_input(
        "👤 Usia",
        min_value=18,
        max_value=100,
        value=30
    )

    lama_bekerja = st.number_input(
        "💼 Lama Bekerja (Tahun)",
        min_value=0.0,
        value=5.0
    )

    pendapatan = st.number_input(
        "💰 Pendapatan Tahunan",
        min_value=0,
        value=50000000,
        step=1000000
    )

    skor_kredit = st.number_input(
        "📊 Skor Kredit",
        min_value=300,
        max_value=900,
        value=650
    )

    lama_riwayat = st.number_input(
        "📅 Lama Riwayat Kredit (Tahun)",
        min_value=0.0,
        value=5.0
    )

    aset_tabungan = st.number_input(
        "🏦 Aset Tabungan",
        min_value=0,
        value=10000000,
        step=500000
    )

    hutang = st.number_input(
        "💳 Hutang Saat Ini",
        min_value=0,
        value=5000000,
        step=500000
    )

# ==========================================================
# INPUT KOLOM KANAN
# ==========================================================

with right:

    gagal_bayar = st.selectbox(
        "❌ Pernah Gagal Bayar",
        ["Tidak", "Ya"]
    )

    tunggakan = st.number_input(
        "📌 Tunggakan 2 Tahun Terakhir",
        min_value=0,
        value=0
    )

    catatan_negatif = st.number_input(
        "📄 Jumlah Catatan Negatif",
        min_value=0,
        value=0
    )

    jumlah_pinjaman = st.number_input(
        "💵 Jumlah Pinjaman",
        min_value=0,
        value=10000000,
        step=1000000
    )

    suku_bunga = st.number_input(
        "📈 Suku Bunga (%)",
        min_value=0.0,
        value=10.0
    )

    status_pekerjaan = st.selectbox(
        "💼 Status Pekerjaan",
        [
            "Pegawai",
            "Mahasiswa",
            "Wiraswasta"
        ]
    )

    tipe_produk = st.selectbox(
        "🏦 Tipe Produk",
        [
            "Kredit Baru",
            "Kredit Berjalan",
            "Pinjaman Pribadi"
        ]
    )

    tujuan = st.selectbox(
        "🎯 Tujuan Pinjaman",
        [
            "Kendaraan",
            "Konsolidasi Hutang",
            "Medis",
            "Pendidikan",
            "Pribadi",
            "Renovasi Rumah"
        ]
    )

st.divider()
