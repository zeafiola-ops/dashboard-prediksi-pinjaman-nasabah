# ==========================================================
# DASHBOARD PREDIKSI STATUS PINJAMAN NASABAH
# Halaman Prediksi
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
# PATH
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
# CSS DASHBOARD
# ==========================================================

st.markdown("""
<style>

/* =========================================================
BACKGROUND
========================================================= */

.stApp{

background:linear-gradient(180deg,#EEF5FF 0%,#DDEBFF 100%);

}

/* =========================================================
CONTAINER
========================================================= */

.main .block-container{

padding-top:2rem;

padding-left:3rem;

padding-right:3rem;

padding-bottom:2rem;

}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"]{

background:linear-gradient(180deg,#0F3FA9,#4D93FF);

}

section[data-testid="stSidebar"] *{

color:white;

}

/* =========================================================
CARD
========================================================= */

.section-card{

background:white;

padding:28px;

border-radius:22px;

box-shadow:0px 8px 25px rgba(0,0,0,.08);

margin-bottom:25px;

}

/* =========================================================
METRIC CARD
========================================================= */

.metric-card{

background:white;

padding:25px;

border-radius:20px;

text-align:center;

box-shadow:0px 6px 18px rgba(0,0,0,.08);

border-left:7px solid #2E7DFF;

}

/* =========================================================
FORM
========================================================= */

.stNumberInput{

background:white;

border-radius:12px;

padding:8px;

}

.stSelectbox{

background:white;

border-radius:12px;

padding:8px;

}

/* =========================================================
BUTTON
========================================================= */

.stButton>button{

width:100%;

background:linear-gradient(90deg,#5FA8FF,#1F5EFF);

color:white;

font-size:18px;

font-weight:bold;

border:none;

padding:14px;

border-radius:15px;

transition:.3s;

}

.stButton>button:hover{

background:linear-gradient(90deg,#1F5EFF,#174EA6);

transform:scale(1.01);

}

/* =========================================================
TITLE
========================================================= */

.big-title{

font-size:48px;

font-weight:700;

text-align:center;

color:#174EA6;

}

/* =========================================================
SUB TITLE
========================================================= */

.sub-title{

font-size:19px;

text-align:center;

color:#666;

margin-bottom:15px;

}

/* =========================================================
SECTION TITLE
========================================================= */

.section-title{

font-size:32px;

font-weight:bold;

color:#174EA6;

margin-bottom:10px;

}

/* =========================================================
FOOTER
========================================================= */

.footer{

text-align:center;

padding:20px;

color:gray;

font-size:15px;

}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# BAGIAN 2
# SIDEBAR & HEADER
# ==========================================================

# ----------------------------
# SIDEBAR
# ----------------------------

with st.sidebar:

   st.image(str(LOGO_PATH), use_container_width=True)

    st.markdown("""
    <div style='text-align:center;'>

    <h2 style='color:#174EA6;margin-bottom:0;'>
    Dashboard Prediksi
    </h2>

    <p style='color:gray;font-size:15px;'>
    Status Pinjaman Nasabah
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.info("""
📌 **Metode**

Random Forest

📂 **Jumlah Fitur**

24

🎯 **Target**

Status Pinjaman

🧠 **Kelas**

2 (Lancar & Tidak Lancar)
""")

st.markdown("""

<div class="section-card">

<h2 style="color:#174EA6;">

📋 Informasi Prediksi

</h2>

<p style="font-size:17px;">

Masukkan seluruh informasi calon nasabah pada formulir di bawah ini.
Model Random Forest akan menganalisis data yang dimasukkan untuk memprediksi status pinjaman menjadi <b>Lancar</b> atau <b>Tidak Lancar</b>.

</p>

</div>

""",unsafe_allow_html=True)
