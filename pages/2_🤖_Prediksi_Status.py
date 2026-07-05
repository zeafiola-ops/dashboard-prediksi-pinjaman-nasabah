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
# CSS
# ==========================================================

st.markdown("""

<style>

.block-container{

padding-top:2rem;

padding-bottom:2rem;

}

.metric-card{

background:white;

padding:20px;

border-radius:20px;

box-shadow:0px 5px 20px rgba(0,0,0,0.08);

text-align:center;

}

.section-card{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0px 5px 18px rgba(0,0,0,0.08);

margin-bottom:25px;

}

.big-title{

font-size:45px;

font-weight:bold;

color:#174EA6;

text-align:center;

}

.sub-title{

font-size:18px;

text-align:center;

color:gray;

}

</style>

""", unsafe_allow_html=True)
