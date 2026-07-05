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
# PATH PROJECT
# ==========================================================

BASE_DIR = Path(__file__).parent.parent

MODEL_PATH = BASE_DIR / "model" / "random_forest_model.pkl"

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
# HEADER
# ==========================================================

st.markdown("""

<h1 style="

text-align:center;

color:#174EA6;

font-weight:700;

">

🤖 Prediksi Status Pinjaman Nasabah

</h1>

<p style="

text-align:center;

font-size:17px;

color:gray;

">

Masukkan data calon nasabah untuk memperoleh
hasil prediksi status pinjaman menggunakan
metode <b>Random Forest</b>.

</p>

""", unsafe_allow_html=True)

st.divider()
