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
# ==========================================================
# BAGIAN 3
# FORM INPUT DATA NASABAH
# ==========================================================

st.markdown("""
<div class="card">

<h2 style="color:#1848A5;">
📝 Form Input Data Nasabah
</h2>

<p style="font-size:16px;">
Silakan lengkapi seluruh informasi calon nasabah pada formulir berikut.
Data yang dimasukkan akan digunakan oleh model Random Forest untuk
memprediksi status pinjaman.
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

# ==========================================================
# KOLOM KIRI
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
        value=5.0,
        step=1.0
    )

    pendapatan = st.number_input(
        "💰 Pendapatan Tahunan (Rp)",
        min_value=0,
        value=50000000,
        step=1000000
    )

    skor_kredit = st.number_input(
        "⭐ Skor Kredit",
        min_value=300,
        max_value=900,
        value=650
    )

    lama_riwayat = st.number_input(
        "📅 Lama Riwayat Kredit (Tahun)",
        min_value=0.0,
        value=5.0,
        step=1.0
    )

    aset_tabungan = st.number_input(
        "🏦 Aset Tabungan (Rp)",
        min_value=0,
        value=10000000,
        step=500000
    )

    hutang = st.number_input(
        "💳 Total Hutang (Rp)",
        min_value=0,
        value=5000000,
        step=500000
    )

# ==========================================================
# KOLOM KANAN
# ==========================================================

with right:

    gagal_bayar = st.selectbox(
        "⚠️ Pernah Gagal Bayar",
        ["Tidak", "Ya"]
    )

    tunggakan = st.number_input(
        "📌 Jumlah Tunggakan",
        min_value=0,
        value=0
    )

    catatan_negatif = st.number_input(
        "📄 Catatan Negatif",
        min_value=0,
        value=0
    )

    jumlah_pinjaman = st.number_input(
        "💵 Jumlah Pinjaman (Rp)",
        min_value=0,
        value=10000000,
        step=1000000
    )

    suku_bunga = st.number_input(
        "📈 Suku Bunga (%)",
        min_value=0.0,
        value=10.0,
        step=0.1
    )

    status_pekerjaan = st.selectbox(
        "👔 Status Pekerjaan",
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

# ==========================================================
# CARD PROSES PREDIKSI
# ==========================================================

st.markdown("""
<div class="card">

<h2 style="color:#1848A5;">
🤖 Proses Prediksi
</h2>

<p>
Klik tombol di bawah untuk melakukan prediksi status pinjaman berdasarkan
data yang telah dimasukkan.
</p>

</div>
""", unsafe_allow_html=True)

prediksi = st.button(
    "🔍 Prediksi Status Pinjaman",
    use_container_width=True
)
# ==========================================================
# BAGIAN 4
# PROSES PREDIKSI
# ==========================================================

if prediksi:

    # ==========================================
    # Membuat dictionary seluruh feature = 0
    # ==========================================

    input_data = {feature: 0 for feature in feature_names}

    # ==========================================
    # FEATURE NUMERIK
    # ==========================================

    numeric_features = {
        "usia": usia,
        "lama_bekerja_tahun": lama_bekerja,
        "pendapatan_tahunan": pendapatan,
        "skor_kredit": skor_kredit,
        "lama_riwayat_kredit_tahun": lama_riwayat,
        "aset_tabungan": aset_tabungan,
        "hutang_saat_ini": hutang,
        "tunggakan_2thn_terakhir": tunggakan,
        "catatan_negatif": catatan_negatif,
        "jumlah_pinjaman": jumlah_pinjaman,
        "suku_bunga": suku_bunga
    }

    for kolom, nilai in numeric_features.items():

        if kolom in input_data:

            input_data[kolom] = nilai

    # ==========================================
    # GAGAL BAYAR
    # ==========================================

    if "gagal_bayar_tercatat" in input_data:

        input_data["gagal_bayar_tercatat"] = (
            1 if gagal_bayar == "Ya" else 0
        )

    # ==========================================
    # FITUR RASIO
    # ==========================================

    if pendapatan > 0:

        if "rasio_hutang_terhadap_pendapatan" in input_data:

            input_data["rasio_hutang_terhadap_pendapatan"] = (
                hutang / pendapatan
            )

        if "rasio_pinjaman_terhadap_pendapatan" in input_data:

            input_data["rasio_pinjaman_terhadap_pendapatan"] = (
                jumlah_pinjaman / pendapatan
            )

        if "rasio_pembayaran_terhadap_pendapatan" in input_data:

            input_data["rasio_pembayaran_terhadap_pendapatan"] = (
                (jumlah_pinjaman * (suku_bunga / 100))
                / pendapatan
            )

    # ==========================================
    # ONE HOT ENCODING
    # ==========================================

    nama = f"status_pekerjaan_{status_pekerjaan}"

    if nama in input_data:
        input_data[nama] = 1

    nama = f"tipe_produk_{tipe_produk}"

    if nama in input_data:
        input_data[nama] = 1

    nama = f"tujuan_pinjaman_{tujuan}"

    if nama in input_data:
        input_data[nama] = 1

    # ==========================================
    # DATAFRAME
    # ==========================================

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(
        columns=feature_names,
        fill_value=0
    )

    # ==========================================
    # PREDIKSI
    # ==========================================

    try:

        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0]

        st.session_state["prediction"] = prediction
        st.session_state["prob_lancar"] = probability[1]
        st.session_state["prob_tidak_lancar"] = probability[0]
        st.session_state["input_df"] = input_df

        st.success("✅ Prediksi berhasil dilakukan.")

    except Exception as e:

        st.error(f"Terjadi kesalahan saat prediksi: {e}")
