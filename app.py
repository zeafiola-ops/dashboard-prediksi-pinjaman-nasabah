import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
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
# HOME
# ==========================================

col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image(logo, width=180)

# Jarak logo ke judul
st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">

<h1 style="
font-size:60px;
font-weight:900;
color:#1E3A8A;
line-height:1.0;
margin:0;
">
Selamat Datang

</h1>

<h3 style="
font-size:30px;
font-weight:700;
color:#2563EB;
line-height:1.0;
margin:8px 0px 5px 0px;
">
Dashboard Prediksi Status Pinjaman Nasabah

</h3>

<p style="
font-size:19px;
color:#64748B;
line-height:1.4;
margin:0;
">
Analisis Prediksi Status Pinjaman Nasabah<br>
Menggunakan Metode <b>Random Forest</b>

</p>

</div>
""", unsafe_allow_html=True)
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

# ==========================================================
# BAGIAN 3
# VISUALISASI DATA
# ==========================================================

st.divider()

st.markdown("""
<h2 style="
color:#2F3A4A;
font-size:34px;
font-weight:800;
margin-bottom:5px;
">
📊 Visualisasi Data
</h2>
""", unsafe_allow_html=True)
st.markdown("""
<p style="
color:#64748B;
font-size:17px;
margin-top:0px;
margin-bottom:20px;
">Visualisasi karakteristik data dan hasil prediksi status pinjaman nasabah menggunakan algoritma <b>Random Forest</b>.
</p>
""", unsafe_allow_html=True)
# ==========================================================
# FILTER DASHBOARD
# ==========================================================

st.markdown("### 🔎 Filter Dashboard")

status_filter = st.selectbox(
    "Pilih Status Prediksi",
    ["Semua", "Lancar", "Tidak Lancar"]
)

if status_filter == "Lancar":
    df_filter = df[df["status_prediksi"] == 1]

elif status_filter == "Tidak Lancar":
    df_filter = df[df["status_prediksi"] == 0]

else:
    df_filter = df.copy()

# ==========================================================
# PERHITUNGAN KPI
# ==========================================================

total_data = len(df_filter)

total_lancar = (df_filter["status_prediksi"] == 1).sum()

total_tidak_lancar = (df_filter["status_prediksi"] == 0).sum()

rata_pinjaman = df_filter["jumlah_pinjaman"].mean()

rata_skor = df_filter["skor_kredit"].mean()

rata_usia = df_filter["usia"].mean()

rata_lama_bekerja = df_filter["lama_bekerja_tahun"].mean()

rata_riwayat = df_filter["lama_riwayat_kredit_tahun"].mean()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">👥</div>
        <div class="kpi-title">Total Data</div>
        <div class="kpi-value">{total_data:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">✅</div>
        <div class="kpi-title">Status Lancar</div>
        <div class="kpi-value">{total_lancar:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">❌</div>
        <div class="kpi-title">Status Tidak Lancar</div>
        <div class="kpi-value">{total_tidak_lancar:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">💰</div>
        <div class="kpi-title">Rata-rata Pinjaman</div>
        <div class="kpi-value">Rp {rata_pinjaman:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col5, col6, col7, col8 = st.columns(4)
with col5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">⭐</div>
        <div class="kpi-title">Rata-rata Skor Kredit</div>
        <div class="kpi-value">{rata_skor:.1f}</div>
    </div>
    """, unsafe_allow_html=True)
with col6:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">👤</div>
        <div class="kpi-title">Rata-rata Usia</div>
        <div class="kpi-value">{rata_usia:.1f} Tahun</div>
    </div>
    """, unsafe_allow_html=True)
with col7:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">💼</div>
        <div class="kpi-title">Lama Bekerja</div>
        <div class="kpi-value">{rata_lama_bekerja:.1f} Tahun</div>
    </div>
    """, unsafe_allow_html=True)
with col8:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">📅</div>
        <div class="kpi-title">Riwayat Kredit</div>
        <div class="kpi-value">{rata_riwayat:.1f} Tahun</div>
    </div>
    """, unsafe_allow_html=True)
status = df_filter["status_prediksi"].replace({
    1: "Lancar",
    0: "Tidak Lancar"
})

col1, col2 = st.columns(2)

# PIE CHART
fig_pie = px.pie(
    names=status,
    hole=0.45,
    title="Persentase Status Prediksi",
    color=status,
    color_discrete_map={
        "Lancar": "#2563EB",
        "Tidak Lancar": "#EF4444"
    }
)

fig_pie.update_layout(
    title_x=0.5,
    height=430,
    transition_duration=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    legend_title="Status Prediksi"
)

fig_pie.update_traces(
    textinfo="percent+label",
    textfont_size=15,
    pull=[0.03,0],
    hovertemplate=
    "<b>%{label}</b><br>" +
    "Jumlah : %{value}<br>" +
    "Persentase : %{percent}<extra></extra>"
)

with col1:
    st.plotly_chart(
        fig_pie,
        use_container_width=True,
        config={
            "displaylogo":False
        }
    )

    st.caption(
        "Grafik menunjukkan proporsi status pinjaman nasabah berdasarkan hasil prediksi Random Forest."
    )

# BAR CHART
status_count = status.value_counts().reset_index()
status_count.columns = ["Status", "Jumlah"]

fig_bar = px.bar(
    status_count,
    x="Status",
    y="Jumlah",
    text="Jumlah",
    color="Status",
    color_discrete_map={
        "Lancar": "#2563EB",
        "Tidak Lancar": "#EF4444"
    },
    title="Jumlah Status Prediksi"
)
fig_bar.update_layout(
    title_x=0.5,
    height=430,
    transition_duration=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Status Prediksi",
    yaxis_title="Jumlah Nasabah"
)

fig_bar.update_traces(
    textposition="outside",
    marker_line_color="white",
    marker_line_width=2,
    hovertemplate=
    "<b>%{x}</b><br>" +
    "Jumlah Nasabah : %{y}<extra></extra>"
)

with col2:
    st.plotly_chart(
        fig_bar,
        use_container_width=True,
        config={
            "displaylogo":False
        }
    )

    st.caption(
        "Grafik batang membandingkan jumlah nasabah berdasarkan status pinjaman."
    )
# ==========================================================
# HISTOGRAM & SCATTER
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

# Histogram Jumlah Pinjaman
fig_hist = px.histogram(
    df_filter,
    x="jumlah_pinjaman",
    nbins=20,
    title="Distribusi Jumlah Pinjaman",
    color_discrete_sequence=["#2563EB"]
)

fig_hist.update_layout(
    title_x=0.5,
    height=430,
    transition_duration=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Jumlah Pinjaman",
    yaxis_title="Frekuensi"
)

fig_hist.update_traces(
    opacity=0.9,
    hovertemplate=
    "Jumlah Pinjaman : %{x}<br>" +
    "Frekuensi : %{y}<extra></extra>"
)
with col3:
    st.plotly_chart(
        fig_hist,
        use_container_width=True,
        config={
            "displaylogo":False
        }
    )

    st.caption(
        "Histogram menunjukkan distribusi jumlah pinjaman yang diajukan oleh nasabah."
    )
    # Scatter Plot
fig_scatter = px.scatter(
    df_filter,
    x="skor_kredit",
    y="jumlah_pinjaman",
    color=status,
    title="Hubungan Skor Kredit dan Jumlah Pinjaman",
    color_discrete_map={
        "Lancar":"#2563EB",
        "Tidak Lancar":"#EF4444"
    }
)

fig_scatter.update_layout(
    title_x=0.5,
    height=430,
    transition_duration=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Skor Kredit",
    yaxis_title="Jumlah Pinjaman"
)

fig_scatter.update_traces(
    marker=dict(
        size=10,
        line=dict(
            width=1,
            color="white"
        )
    ),
    hovertemplate=
    "Skor Kredit : %{x}<br>" +
    "Jumlah Pinjaman : %{y}<extra></extra>"
)
with col4:
    st.plotly_chart(
        fig_scatter,
        use_container_width=True,
        config={
            "displaylogo":False
        }
    )

    st.caption(
        "Scatter plot menunjukkan hubungan antara skor kredit dan jumlah pinjaman nasabah."
    )
# ==========================================================
# PREVIEW DATASET
# ==========================================================

st.divider()

st.markdown("""
<h2 style="
color:#2F3A4A;
font-size:32px;
font-weight:700;
margin-bottom:0px;
">
📋 Preview Dataset
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
font-size:17px;
color:#5F6B7A;
margin-top:-10px;
">
Menampilkan seluruh fitur dataset yang digunakan pada proses analisis
dan prediksi status pinjaman nasabah.
</p>
""", unsafe_allow_html=True)

# Informasi dataset
col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"📄 Jumlah Data : **{len(df_filter):,}**")

with col2:
    st.info(f"📊 Jumlah Fitur : **{df_filter.shape[1]}**")

with col3:
    st.info(f"📌 Kolom Target : **status_prediksi**")

st.markdown("<br>", unsafe_allow_html=True)

# Preview Dataset
st.dataframe(
    df_filter,
    use_container_width=True,
    hide_index=True,
    height=500
)
st.markdown("""
<div class="footer">

<h3>Dashboard Prediksi Status Pinjaman Nasabah</h3>

<p>Menggunakan Metode Random Forest</p>

<p>© 2026 | Sistem Informasi | Business Intelligence</p>

</div>
""", unsafe_allow_html=True)
