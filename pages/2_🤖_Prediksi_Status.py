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

Masukkan informasi calon nasabah
untuk memperoleh hasil prediksi
status pinjaman menggunakan
<b>Random Forest</b>.

</p>

""", unsafe_allow_html=True)

st.divider()
