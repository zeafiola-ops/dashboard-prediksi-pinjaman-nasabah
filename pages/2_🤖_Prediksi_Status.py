# ==========================================================
# DASHBOARD PREDIKSI STATUS PINJAMAN NASABAH
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

from pathlib import Path
from datetime import datetime

import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Prediksi Status Pinjaman",
    page_icon="🧠",
    layout="wide"
)

# ==========================================================
# PATH PROJECT
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "random_forest_model (1).pkl"

FEATURE_PATH = BASE_DIR / "data" / "feature_names.pkl"

LOGO_PATH = BASE_DIR / "assets" / "logo.png"

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    model = joblib.load(MODEL_PATH)

    feature_names = joblib.load(FEATURE_PATH)

    return model, feature_names


model, feature_names = load_model()

# ==========================================================
# CSS
# ==========================================================

st.markdown("""

<style>

/* Background */

.stApp{

background:linear-gradient(180deg,#EEF6FF 0%,#DCEBFF 100%);

}

/* Container */

.main .block-container{

padding-top:2rem;

padding-left:2.8rem;

padding-right:2.8rem;

padding-bottom:2rem;

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:linear-gradient(180deg,#1545B3,#4E96FF);

}

section[data-testid="stSidebar"] *{

color:white;

}

/* Card */

.card{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0 5px 20px rgba(0,0,0,.08);

margin-bottom:25px;

}

/* Title */

.title{

font-size:46px;

font-weight:700;

text-align:center;

color:#1848A5;

}

/* Subtitle */

.subtitle{

text-align:center;

font-size:18px;

color:#666666;

margin-bottom:15px;

}

/* Section */

.section-title{

font-size:28px;

font-weight:bold;

color:#1848A5;

margin-bottom:10px;

}

/* Tombol */

.stButton>button{

width:100%;

background:linear-gradient(90deg,#5FA9FF,#245CFF);

color:white;

font-size:18px;

font-weight:bold;

border-radius:15px;

padding:12px;

border:none;

}

.stButton>button:hover{

background:linear-gradient(90deg,#245CFF,#1746B1);

}

/* Metric */

[data-testid="metric-container"]{

background:white;

border-radius:18px;

padding:15px;

box-shadow:0px 5px 18px rgba(0,0,0,.08);

border-left:6px solid #2E7DFF;

}

</style>

""", unsafe_allow_html=True)
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(str(LOGO_PATH), use_container_width=True)

    st.markdown("""
    <div style="text-align:center;">

    <h2 style="margin-bottom:0;">
    Dashboard Prediksi
    </h2>

    <p style="font-size:16px;">
    Status Pinjaman Nasabah
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
### 📌 Informasi Model

- **Metode :** Random Forest
- **Target :** Status Pinjaman
- **Kelas :** 2
- **1 = Lancar**
- **0 = Tidak Lancar**

""")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="title">

🧠 Prediksi Status Pinjaman Nasabah

</div>

<div class="subtitle">

Masukkan data calon nasabah untuk memperoleh hasil prediksi
status pinjaman menggunakan model <b>Random Forest</b>.

</div>

""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# CARD INFORMASI
# ==========================================================

st.markdown("""

<div class="card">

<h2 style="color:#1848A5;">

📋 Informasi Prediksi

</h2>
<p style="font-size:17px; line-height:1.8;">
Halaman ini digunakan untuk memprediksi status pinjaman nasabah
berdasarkan karakteristik calon peminjam menggunakan model
<b>Random Forest</b>.

Silakan isi seluruh data calon nasabah pada formulir yang tersedia,
kemudian klik tombol <b>Prediksi Status Pinjaman</b> untuk melihat
hasil prediksi beserta tingkat probabilitasnya.

</p>

</div>

""", unsafe_allow_html=True)
