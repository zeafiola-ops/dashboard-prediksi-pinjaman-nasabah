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
# ======================================================
# VISUALISASI EVALUASI MODEL
# ======================================================

st.markdown("## 📊 Visualisasi Evaluasi Model")

st.markdown("""
<div class="section-card">

<h3>🔷 Confusion Matrix</h3>

<p>
Visualisasi hasil prediksi model terhadap data aktual.
</p>

</div>
""", unsafe_allow_html=True)

fig_cm = px.imshow(
    cm,
    text_auto=True,
    color_continuous_scale="Blues",
    aspect="auto",
    labels={
        "x": "Prediksi",
        "y": "Aktual",
        "color": "Jumlah"
    }
)

fig_cm.update_layout(

    height=520,

    template="plotly_white",

    title_x=0.5,

    font=dict(size=14)

)

st.plotly_chart(
    fig_cm,
    use_container_width=True
)

st.info("""
**Interpretasi**

Nilai pada diagonal menunjukkan jumlah prediksi yang benar.

Nilai di luar diagonal menunjukkan kesalahan prediksi model.
""")
st.divider()
st.markdown("""
<div class="section-card">

<h3>🔷 Confusion Matrix</h3>

<p>
Visualisasi hasil prediksi model terhadap data aktual.
</p>

</div>
""", unsafe_allow_html=True)

importance = importance.sort_values(
    by="Importance",
    ascending=True
)

fig_imp = px.bar(
    importance,
    x="Importance",
    y="Fitur",
    orientation="h",
    color="Importance",
    color_continuous_scale="Blues"
)

fig_imp.update_layout(

    height=650,

    template="plotly_white",

    title_x=0.5,

    font=dict(size=14),

    coloraxis_showscale=False

)

st.plotly_chart(
    fig_imp,
    use_container_width=True
)

st.info("""
**Interpretasi**

Semakin tinggi nilai importance,
semakin besar pengaruh fitur terhadap
prediksi status pinjaman menggunakan Random Forest.
""")
st.divider()
# ======================================================
# CLASSIFICATION REPORT
# ======================================================

st.markdown("""
<div class="section-card">

<h3>📋 Classification Report</h3>

<p>
Ringkasan hasil evaluasi model berdasarkan
Precision, Recall, F1-Score dan Support.
</p>

</div>
""", unsafe_allow_html=True)

st.write(
    """
    Tabel berikut menunjukkan hasil evaluasi model
    berdasarkan nilai Precision, Recall, F1-Score,
    dan Support.
    """
)

st.dataframe(
    report,
    use_container_width=True,
    hide_index=False
)

st.info("""
**Interpretasi**

• Precision menunjukkan ketepatan model dalam memprediksi kelas.

• Recall menunjukkan kemampuan model menemukan seluruh data pada kelas tertentu.

• F1-Score merupakan rata-rata harmonis antara Precision dan Recall.

• Support menunjukkan jumlah data pada masing-masing kelas.
""")
st.divider()
# ======================================================
# KESIMPULAN
# ======================================================

st.markdown("""
<div class="section-card">

<h3>📝 Kesimpulan Evaluasi</h3>

<p>
Interpretasi hasil evaluasi model Random Forest.
</p>

</div>
""", unsafe_allow_html=True)

st.success(f"""

Model **Random Forest** berhasil memperoleh performa yang baik
dengan nilai:

- Accuracy : **{accuracy:.2%}**
- Precision : **{precision:.2%}**
- Recall : **{recall:.2%}**
- F1 Score : **{f1:.2%}**

Hasil ini menunjukkan bahwa model mampu
mengklasifikasikan status pinjaman nasabah
dengan tingkat akurasi yang tinggi sehingga
layak digunakan sebagai model prediksi.
""")
st.divider()
# ======================================================
# FOOTER
# ======================================================

st.markdown("""
<hr>

<div style='text-align:center;color:gray;'>

Dashboard Prediksi Status Pinjaman Nasabah

© 2026 | Sistem Informasi - Business Intelligence

Dikembangkan menggunakan Streamlit & Random Forest

</div>
""", unsafe_allow_html=True)
