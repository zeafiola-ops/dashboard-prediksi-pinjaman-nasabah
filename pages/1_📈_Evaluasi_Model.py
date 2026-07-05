# ======================================================
# IMPORT LIBRARY
# ======================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================

st.set_page_config(
    page_title="Evaluasi Model",
    page_icon="📈",
    layout="wide"
)

# ======================================================
# LOAD CSS
# ======================================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ======================================================
# LOAD LOGO
# ======================================================

logo = Image.open("assets/logo.png")

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.image(logo, width=180)

    st.markdown("## Dashboard Prediksi")

    st.caption("Status Pinjaman Nasabah")

    st.divider()

    st.success("📈 Evaluasi Model")

# ======================================================
# LOAD DATA
# ======================================================

metrics = pd.read_csv("data/metrics.csv")

cm = pd.read_csv(
    "data/confusion_matrix.csv",
    index_col=0
)

report = pd.read_csv(
    "data/classification_report.csv",
    index_col=0
)

importance = pd.read_csv(
    "data/feature_importance.csv"
)

# ======================================================
# HEADER
# ======================================================

st.markdown("""

<div class="home-header">

<h1 style="text-align:center;">
📈 Evaluasi Model Random Forest
</h1>
<p style="text-align:center;">
Halaman ini menampilkan hasil evaluasi model Random Forest
yang digunakan untuk memprediksi status pinjaman nasabah.
</p>

</div>

""", unsafe_allow_html=True)

st.divider()

# ======================================================
# AMBIL NILAI KPI
# ======================================================

accuracy = metrics.loc[
    metrics["Metric"]=="Accuracy",
    "Value"
].values[0]

precision = metrics.loc[
    metrics["Metric"]=="Precision",
    "Value"
].values[0]

recall = metrics.loc[
    metrics["Metric"]=="Recall",
    "Value"
].values[0]

f1 = metrics.loc[
    metrics["Metric"]=="F1 Score",
    "Value"
].values[0]

# ======================================================
# KPI
# ======================================================

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.markdown(f"""

<div class="kpi-card">

<div class="kpi-icon">
🎯
</div>

<div class="kpi-title">

Accuracy

</div>

<div class="kpi-value">

{accuracy:.2%}

</div>

</div>

""", unsafe_allow_html=True)

with col2:

    st.markdown(f"""

<div class="kpi-card">

<div class="kpi-icon">
📌
</div>

<div class="kpi-title">

Precision

</div>

<div class="kpi-value">

{precision:.2%}

</div>

</div>

""", unsafe_allow_html=True)

with col3:

    st.markdown(f"""

<div class="kpi-card">

<div class="kpi-icon">
📊
</div>

<div class="kpi-title">

Recall

</div>

<div class="kpi-value">

{recall:.2%}

</div>

</div>

""", unsafe_allow_html=True)

with col4:

    st.markdown(f"""

<div class="kpi-card">

<div class="kpi-icon">
🏆
</div>

<div class="kpi-title">

F1 Score

</div>

<div class="kpi-value">

{f1:.2%}

</div>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
