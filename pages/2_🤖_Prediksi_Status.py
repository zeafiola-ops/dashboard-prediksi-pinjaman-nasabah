# ==========================================================
# IMPORT LIBRARY
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

import plotly.express as px
import plotly.graph_objects as go

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

with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
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

    st.markdown("""
    <div style="text-align:center;">

    <h2 style="color:white;">
    Dashboard Prediksi
    </h2>

    <p style="color:white;">
    Status Pinjaman Nasabah
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#1976D2,#0D47A1);
    padding:18px;
    border-radius:15px;
    color:white;
    ">

    <h4>🤖 Tentang Prediksi</h4>

    <p>

    Halaman ini digunakan
    untuk memprediksi
    status pinjaman nasabah
    menggunakan metode
    <b>Random Forest</b>.

    </p>

    <hr>

    ✔ Prediksi Cepat<br>
    ✔ Akurat<br>
    ✔ Mudah Digunakan

    </div>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("© 2026 Dashboard Prediksi")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<h1 style="text-align:center;
color:#174EA6;">
🤖 Prediksi Status Pinjaman Nasabah
</h1>
<p style="text-align:center;
font-size:18px;
color:#555;">
Masukkan informasi calon nasabah pada formulir berikut
untuk memperoleh hasil prediksi status pinjaman
menggunakan metode <b>Random Forest</b>.

</p>

""", unsafe_allow_html=True)

st.divider()
# ==========================================================
# FORM INPUT NASABAH
# ==========================================================

st.markdown("""
<div class="section-card">

<h3>📝 Form Input Data Nasabah</h3>

<p>
Silakan lengkapi data calon nasabah pada formulir berikut
untuk memperoleh hasil prediksi status pinjaman.
</p>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ==========================================================
# KOLOM KIRI
# ==========================================================

with col1:

    st.subheader("👤 Informasi Pribadi")

    usia = st.number_input(
        "Usia",
        min_value=18,
        max_value=100,
        value=30
    )

    lama_bekerja = st.number_input(
        "Lama Bekerja (Tahun)",
        min_value=0,
        value=5
    )

    pendapatan = st.number_input(
        "Pendapatan Tahunan (Rp)",
        min_value=0,
        value=50000000,
        step=1000000
    )

    skor_kredit = st.number_input(
        "Skor Kredit",
        min_value=300,
        max_value=900,
        value=650
    )

    lama_riwayat = st.number_input(
        "Lama Riwayat Kredit (Tahun)",
        min_value=0,
        value=5
    )

    aset_tabungan = st.number_input(
        "Aset Tabungan (Rp)",
        min_value=0,
        value=10000000,
        step=1000000
    )

    hutang = st.number_input(
        "Total Hutang (Rp)",
        min_value=0,
        value=5000000,
        step=500000
    )

# ==========================================================
# KOLOM KANAN
# ==========================================================

with col2:

    st.subheader("🏦 Informasi Pinjaman")

    gagal_bayar = st.selectbox(
        "Pernah Gagal Bayar",
        [
            "Tidak",
            "Ya"
        ]
    )

    tunggakan = st.number_input(
        "Jumlah Tunggakan",
        min_value=0,
        value=0
    )

    catatan_negatif = st.number_input(
        "Catatan Negatif",
        min_value=0,
        value=0
    )

    jumlah_pinjaman = st.number_input(
        "Jumlah Pinjaman (Rp)",
        min_value=0,
        value=10000000,
        step=1000000
    )

    suku_bunga = st.number_input(
        "Suku Bunga (%)",
        min_value=0.0,
        value=10.0,
        step=0.1
    )

    status_pekerjaan = st.selectbox(
        "Status Pekerjaan",
        [
            "Pegawai",
            "Mahasiswa",
            "Wiraswasta"
        ]
    )

    tipe_produk = st.selectbox(
        "Tipe Produk",
        [
            "Kredit Baru",
            "Kredit Berjalan",
            "Pinjaman Pribadi"
        ]
    )

    tujuan = st.selectbox(
        "Tujuan Pinjaman",
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
# BAGIAN 3
# PROSES PREDIKSI
# ==========================================================

st.markdown("""
<div class="section-card">

<h3>🤖 Proses Prediksi</h3>

<p>
Klik tombol di bawah untuk melakukan prediksi status pinjaman
berdasarkan data yang telah dimasukkan.
</p>

</div>
""", unsafe_allow_html=True)

prediksi = st.button(
    "🔍 Prediksi Status Pinjaman",
    use_container_width=True
)

if prediksi:

    # ============================================
    # Membuat dictionary seluruh feature = 0
    # ============================================

    input_data = {}

    for feature in feature_names:
        input_data[feature] = 0

    # ============================================
    # FEATURE NUMERIK
    # ============================================

    if "usia" in input_data:
        input_data["usia"] = usia

    if "lama_bekerja_tahun" in input_data:
        input_data["lama_bekerja_tahun"] = lama_bekerja

    if "pendapatan_tahunan" in input_data:
        input_data["pendapatan_tahunan"] = pendapatan

    if "skor_kredit" in input_data:
        input_data["skor_kredit"] = skor_kredit

    if "lama_riwayat_kredit_tahun" in input_data:
        input_data["lama_riwayat_kredit_tahun"] = lama_riwayat

    if "aset_tabungan" in input_data:
        input_data["aset_tabungan"] = aset_tabungan

    if "hutang_saat_ini" in input_data:
        input_data["hutang_saat_ini"] = hutang

    if "tunggakan_2thn_terakhir" in input_data:
        input_data["tunggakan_2thn_terakhir"] = tunggakan

    if "catatan_negatif" in input_data:
        input_data["catatan_negatif"] = catatan_negatif

    if "jumlah_pinjaman" in input_data:
        input_data["jumlah_pinjaman"] = jumlah_pinjaman

    if "suku_bunga" in input_data:
        input_data["suku_bunga"] = suku_bunga

    # ============================================
    # GAGAL BAYAR
    # ============================================

    if "gagal_bayar_tercatat" in input_data:

        input_data["gagal_bayar_tercatat"] = 1 if gagal_bayar == "Ya" else 0

    # ============================================
    # RASIO
    # ============================================

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
                (jumlah_pinjaman * (suku_bunga / 100)) / pendapatan
            )

    # ============================================
    # ONE HOT ENCODING
    # ============================================

    nama = f"status_pekerjaan_{status_pekerjaan}"

    if nama in input_data:
        input_data[nama] = 1

    nama = f"tipe_produk_{tipe_produk}"

    if nama in input_data:
        input_data[nama] = 1

    nama = f"tujuan_pinjaman_{tujuan}"

    if nama in input_data:
        input_data[nama] = 1

    # ============================================
    # DATAFRAME
    # ============================================

    input_df = pd.DataFrame(
        [input_data]
    )

    input_df = input_df.reindex(
        columns=feature_names,
        fill_value=0
    )

    # ============================================
    # PREDIKSI
    # ============================================

    try:

        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0]

        st.session_state["prediction"] = prediction

        st.session_state["prob_lancar"] = probability[1]

        st.session_state["prob_tidak_lancar"] = probability[0]

        st.success("✅ Prediksi berhasil dilakukan.")

    except Exception as e:

        st.error(f"Terjadi kesalahan saat prediksi : {e}")
    # ==========================================================
# BAGIAN 4
# HASIL PREDIKSI
# ==========================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]
    prob_lancar = st.session_state["prob_lancar"]
    prob_tidak_lancar = st.session_state["prob_tidak_lancar"]

    st.divider()

    st.markdown("""
    <div class="section-card">

    <h2 style="text-align:center;color:#174EA6;">
    📊 Hasil Prediksi Status Pinjaman
    </h2>

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # CARD HASIL
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:

        if prediction == 1:

            st.success("## 🟢 LANCAR")

        else:

            st.error("## 🔴 TIDAK LANCAR")

    with col2:

        st.metric(

            "Probabilitas Lancar",

            f"{prob_lancar*100:.2f}%"

        )

    with col3:

        st.metric(

            "Probabilitas Tidak Lancar",

            f"{prob_tidak_lancar*100:.2f}%"

        )

    st.divider()

    # ==========================================
    # PROGRESS BAR
    # ==========================================

    st.subheader("📈 Tingkat Keyakinan Model")

    if prediction == 1:

        st.progress(float(prob_lancar))

        st.caption(
            f"Model yakin sebesar {prob_lancar*100:.2f}% bahwa pinjaman akan Lancar."
        )

    else:

        st.progress(float(prob_tidak_lancar))

        st.caption(
            f"Model yakin sebesar {prob_tidak_lancar*100:.2f}% bahwa pinjaman Tidak Lancar."
        )

    st.divider()

    # ==========================================
    # BAR CHART
    # ==========================================

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

        text_auto=".2%",

        color="Status",

        title="Perbandingan Probabilitas Prediksi"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        title_x=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ==========================================
    # GAUGE CHART
    # ==========================================

    nilai = prob_lancar if prediction == 1 else prob_tidak_lancar

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=nilai*100,

            number={"suffix":"%"},

            title={"text":"Tingkat Keyakinan Model"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"royalblue"}

            }

        )

    )

    gauge.update_layout(

        height=420

    )

    st.plotly_chart(

        gauge,

        use_container_width=True

    )

    st.divider()

    # ==========================================
    # INTERPRETASI
    # ==========================================

    st.markdown("""
    <div class="section-card">

    <h3>📝 Interpretasi Hasil</h3>

    </div>
    """, unsafe_allow_html=True)

    if prediction == 1:

        st.success(f"""

Model Random Forest memprediksi bahwa calon nasabah memiliki **status pinjaman Lancar**.

Probabilitas prediksi sebesar **{prob_lancar*100:.2f}%** menunjukkan bahwa calon nasabah memiliki tingkat risiko gagal bayar yang rendah.

""")

   else:

    st.error(f"""

Model Random Forest memprediksi bahwa calon nasabah memiliki **status pinjaman Tidak Lancar**.

Probabilitas prediksi sebesar **{prob_tidak_lancar*100:.2f}%** menunjukkan bahwa calon nasabah memiliki tingkat risiko gagal bayar yang lebih tinggi.

""")
# ==========================================================
# BAGIAN 5
# RINGKASAN DATA INPUT
# ==========================================================

if "prediction" in st.session_state:

    st.divider()

    st.markdown("""
    <h2 style="text-align:center;color:#174EA6;">
    📋 Ringkasan Data Nasabah
    </h2>
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
            pendapatan,
            skor_kredit,
            lama_riwayat,
            aset_tabungan,
            hutang,
            gagal_bayar,
            tunggakan,
            catatan_negatif,
            jumlah_pinjaman,
            suku_bunga,
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

    # =====================================
    # DOWNLOAD HASIL
    # =====================================

    status = "Lancar" if prediction == 1 else "Tidak Lancar"

    hasil = pd.DataFrame({

        "Status Prediksi":[status],

        "Probabilitas Lancar (%)":[round(prob_lancar*100,2)],

        "Probabilitas Tidak Lancar (%)":[round(prob_tidak_lancar*100,2)]

    })

    csv = hasil.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Hasil Prediksi",

        data=csv,

        file_name="hasil_prediksi.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.divider()

    # =====================================
    # FOOTER
    # =====================================

    st.markdown("""

    <div style="

    background:#F4F8FF;

    padding:20px;

    border-radius:15px;

    text-align:center;

    ">

    <h4 style="color:#174EA6;">

    Dashboard Prediksi Status Pinjaman Nasabah

    </h4>

    <p>

    Sistem prediksi menggunakan metode
    <b>Random Forest</b>.

    </p>

    <p>

    © 2026 | Sistem Informasi - Business Intelligence

    </p>

    </div>

    """, unsafe_allow_html=True)
