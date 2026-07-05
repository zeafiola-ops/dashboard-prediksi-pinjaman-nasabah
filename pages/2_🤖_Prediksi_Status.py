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
/* ============================= */
/* KPI CARD */
/* ============================= */

.kpi-card{

background:white;

padding:22px;

border-radius:18px;

text-align:center;

box-shadow:0px 6px 18px rgba(0,0,0,.08);

border-left:6px solid #2E7DFF;

transition:0.3s;

margin-bottom:20px;

}

.kpi-card:hover{

transform:translateY(-4px);

box-shadow:0px 10px 24px rgba(0,0,0,.15);

}

.kpi-icon{

font-size:36px;

margin-bottom:8px;

}

.kpi-title{

font-size:16px;

color:#666;

}

.kpi-value{

font-size:28px;

font-weight:bold;

color:#1848A5;

margin-top:10px;

}

</style>
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
# ==========================================================
# BAGIAN 5
# HASIL PREDIKSI
# ==========================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]
    prob_lancar = st.session_state["prob_lancar"]
    prob_tidak_lancar = st.session_state["prob_tidak_lancar"]
st.divider()

st.markdown("""
<h2 style="color:#1848A5;">
📊 Ringkasan Hasil Prediksi
</h2>
""", unsafe_allow_html=True)

confidence = max(prob_lancar, prob_tidak_lancar) * 100
status = "🟢 Lancar" if prediction == 1 else "🔴 Tidak Lancar"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 📌")
    st.metric(
        label="Status Prediksi",
        value=status
    )

with col2:
    st.markdown("### 📈")
    st.metric(
        label="Probabilitas Lancar",
        value=f"{prob_lancar*100:.2f}%"
    )

with col3:
    st.markdown("### ⚠️")
    st.metric(
        label="Probabilitas Tidak Lancar",
        value=f"{prob_tidak_lancar*100:.2f}%"
    )

with col4:
    st.markdown("### 🧠")
    st.metric(
        label="Tingkat Keyakinan",
        value=f"{confidence:.2f}%"
    )

st.divider()

    st.markdown("""
    <div class="card">

    <h2 style="text-align:center;color:#1848A5;">
    📊 Hasil Prediksi Status Pinjaman
    </h2>

    </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # PROGRESS BAR
    # ======================================================

    st.subheader("📈 Tingkat Keyakinan Model")

    if prediction == 1:

        st.progress(float(prob_lancar))

        st.caption(
            f"Model memiliki keyakinan sebesar {prob_lancar*100:.2f}% bahwa status pinjaman adalah **Lancar**."
        )

    else:

        st.progress(float(prob_tidak_lancar))

        st.caption(
            f"Model memiliki keyakinan sebesar {prob_tidak_lancar*100:.2f}% bahwa status pinjaman adalah **Tidak Lancar**."
        )

    st.divider()

    # ======================================================
    # GAUGE CHART
    # ======================================================

    nilai = prob_lancar if prediction == 1 else prob_tidak_lancar

    fig_gauge = go.Figure(go.Indicator(

        mode="gauge+number",

        value=nilai*100,

        number={'suffix': "%"},

        title={'text': "Tingkat Keyakinan Model"},

        gauge={

            'axis': {'range': [0,100]},

            'bar': {'color': "#1E88E5"},

            'steps': [

                {'range':[0,50],'color':'#FFCDD2'},

                {'range':[50,75],'color':'#FFE082'},

                {'range':[75,100],'color':'#C8E6C9'}

            ]

        }

    ))

    fig_gauge.update_layout(height=350)

    st.plotly_chart(
        fig_gauge,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # BAR CHART
    # ======================================================

    chart_df = pd.DataFrame({

        "Status":[
            "Lancar",
            "Tidak Lancar"
        ],

        "Probabilitas":[
            prob_lancar,
            prob_tidak_lancar
        ]

    })

    fig = px.bar(

        chart_df,

        x="Status",

        y="Probabilitas",

        color="Status",

        text_auto=".2%",

        title="Perbandingan Probabilitas Prediksi"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        title_x=0.5,

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# ==========================================================
# BAGIAN 6
# RINGKASAN DATA
# ==========================================================

if "prediction" in st.session_state:

    st.divider()

    st.markdown("""
    <div class="card">

    <h2 style="color:#1848A5;">
    📋 Ringkasan Data Nasabah
    </h2>

    </div>
    """, unsafe_allow_html=True)

    ringkasan = pd.DataFrame({

        "Variabel":[

            "Usia",

            "Lama Bekerja",

            "Pendapatan Tahunan",

            "Skor Kredit",

            "Lama Riwayat Kredit",

            "Aset Tabungan",

            "Total Hutang",

            "Pernah Gagal Bayar",

            "Jumlah Tunggakan",

            "Catatan Negatif",

            "Jumlah Pinjaman",

            "Suku Bunga",

            "Status Pekerjaan",

            "Tipe Produk",

            "Tujuan Pinjaman"

        ],

        "Nilai":[

            usia,

            lama_bekerja,

            f"Rp {pendapatan:,.0f}",

            skor_kredit,

            lama_riwayat,

            f"Rp {aset_tabungan:,.0f}",

            f"Rp {hutang:,.0f}",

            gagal_bayar,

            tunggakan,

            catatan_negatif,

            f"Rp {jumlah_pinjaman:,.0f}",

            f"{suku_bunga:.2f} %",

            status_pekerjaan,

            tipe_produk,

            tujuan

        ]

    })

    st.dataframe(
        ringkasan,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

# ==========================================================
# INTERPRETASI
# ==========================================================

    st.markdown("""
    <div class="card">

    <h2 style="color:#1848A5;">
    💡 Interpretasi Hasil
    </h2>

    </div>
    """, unsafe_allow_html=True)

    if prediction == 1:

        st.success("""

### ✅ Status Pinjaman Diprediksi **LANCAR**

Model Random Forest memperkirakan bahwa calon nasabah
memiliki kemungkinan besar untuk memenuhi kewajiban pembayaran pinjaman.

Semakin tinggi probabilitas **Lancar**, semakin kecil
tingkat risiko kredit.

""")

    else:

        st.error("""

### ❌ Status Pinjaman Diprediksi **TIDAK LANCAR**

Model Random Forest memperkirakan bahwa calon nasabah
memiliki risiko lebih tinggi mengalami gagal bayar.

Semakin tinggi probabilitas **Tidak Lancar**, semakin tinggi
risiko kredit.

""")

    st.divider()

# ==========================================================
# INFORMASI MODEL
# ==========================================================

    st.markdown("""
    <div class="card">

    <h2 style="color:#1848A5;">
    📌 Informasi Model
    </h2>

    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c1:

        st.metric(
            "Metode",
            "Random Forest"
        )

    with c2:

        st.metric(
            "Jumlah Fitur",
            len(feature_names)
        )

    with c3:

        st.metric(
            "Jumlah Kelas",
            "2"
        )

    st.divider()

# ==========================================================
# DOWNLOAD HASIL
# ==========================================================

    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    hasil = pd.DataFrame({

        "Status Prediksi":[

            "Lancar" if prediction==1 else "Tidak Lancar"

        ],

        "Probabilitas Lancar":[

            round(prob_lancar*100,2)

        ],

        "Probabilitas Tidak Lancar":[

            round(prob_tidak_lancar*100,2)

        ],

        "Waktu Prediksi":[

            waktu

        ]

    })

    csv = hasil.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Hasil Prediksi",

        csv,

        "hasil_prediksi.csv",

        "text/csv",

        use_container_width=True

    )

    st.info(f"🕒 Prediksi dilakukan pada : **{waktu}**")

    st.divider()

# ==========================================================
# FOOTER
# ==========================================================

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<div style="text-align:center;">

<h3 style="color:#1E4DB7;">
📊 Dashboard Prediksi Status Pinjaman Nasabah
</h3>

<p>
Prediksi Status Pinjaman Menggunakan Metode
<b>Random Forest</b>
</p>

<p>
Program Studi Sistem Informasi • Business Intelligence
</p>

<p>
© 2026
</p>

</div>
""", unsafe_allow_html=True)
