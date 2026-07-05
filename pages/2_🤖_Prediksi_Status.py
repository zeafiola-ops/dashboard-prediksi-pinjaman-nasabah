# ==========================================================
# IMPORT LIBRARY
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
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

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
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

    st.markdown(
        """
        <div style="text-align:center;">
        <h2>Dashboard Prediksi</h2>
        <p>Status Pinjaman Nasabah</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
        background:linear-gradient(135deg,#1E88E5,#1565C0);
        padding:18px;
        border-radius:15px;
        color:white;
        ">

        <h4>🤖 Tentang Prediksi</h4>

        <p>

        Halaman ini digunakan
        untuk melakukan prediksi
        status pinjaman nasabah
        menggunakan model
        <b>Random Forest</b>.

        </p>

        <hr>

        ✅ Akurat <br>
        ⚡ Cepat <br>
        💻 Mudah Digunakan

        </div>

        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("© 2026 Dashboard Prediksi")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<h1 style='text-align:center;color:#174EA6;'>
🤖 Prediksi Status Pinjaman Nasabah
</h1>
<p style='text-align:center;
font-size:18px;
color:#555;'>
Masukkan informasi calon nasabah
untuk memperoleh hasil prediksi
status pinjaman menggunakan
<b>Random Forest</b>.

</p>

""", unsafe_allow_html=True)

st.divider()
# ==========================================================
# FORM INPUT DATA NASABAH
# ==========================================================

st.markdown("""
<div class="section-card">

<h3>📝 Form Input Data Nasabah</h3>

<p>
Silakan lengkapi data calon nasabah pada formulir berikut untuk memperoleh hasil prediksi status pinjaman.
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

# ==========================================================
# INPUT KOLOM KIRI
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
        value=5.0
    )

    pendapatan = st.number_input(
        "💰 Pendapatan Tahunan",
        min_value=0,
        value=50000000,
        step=1000000
    )

    skor_kredit = st.number_input(
        "📊 Skor Kredit",
        min_value=300,
        max_value=900,
        value=650
    )

    lama_riwayat = st.number_input(
        "📅 Lama Riwayat Kredit (Tahun)",
        min_value=0.0,
        value=5.0
    )

    aset_tabungan = st.number_input(
        "🏦 Aset Tabungan",
        min_value=0,
        value=10000000,
        step=500000
    )

    hutang = st.number_input(
        "💳 Hutang Saat Ini",
        min_value=0,
        value=5000000,
        step=500000
    )

# ==========================================================
# INPUT KOLOM KANAN
# ==========================================================

with right:

    gagal_bayar = st.selectbox(
        "❌ Pernah Gagal Bayar",
        ["Tidak", "Ya"]
    )

    tunggakan = st.number_input(
        "📌 Tunggakan 2 Tahun Terakhir",
        min_value=0,
        value=0
    )

    catatan_negatif = st.number_input(
        "📄 Jumlah Catatan Negatif",
        min_value=0,
        value=0
    )

    jumlah_pinjaman = st.number_input(
        "💵 Jumlah Pinjaman",
        min_value=0,
        value=10000000,
        step=1000000
    )

    suku_bunga = st.number_input(
        "📈 Suku Bunga (%)",
        min_value=0.0,
        value=10.0
    )

    status_pekerjaan = st.selectbox(
        "💼 Status Pekerjaan",
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
# BAGIAN 3 - PROSES PREDIKSI
# ==========================================================

st.markdown("""
<div class="section-card">

<h3>🤖 Proses Prediksi</h3>

<p>
Klik tombol di bawah untuk melakukan prediksi status pinjaman berdasarkan data yang telah diinput.
</p>

</div>
""", unsafe_allow_html=True)

if st.button("🔍 Prediksi Status Pinjaman", use_container_width=True):

    # ----------------------------------------
    # Data awal
    # ----------------------------------------

    input_data = {feature: 0 for feature in feature_names}

    # ----------------------------------------
    # Fitur numerik
    # ----------------------------------------

    input_data["usia"] = usia
    input_data["lama_bekerja_tahun"] = lama_bekerja
    input_data["pendapatan_tahunan"] = pendapatan
    input_data["skor_kredit"] = skor_kredit
    input_data["lama_riwayat_kredit_tahun"] = lama_riwayat
    input_data["aset_tabungan"] = aset_tabungan
    input_data["hutang_saat_ini"] = hutang
    input_data["gagal_bayar_tercatat"] = 1 if gagal_bayar == "Ya" else 0
    input_data["tunggakan_2thn_terakhir"] = tunggakan
    input_data["catatan_negatif"] = catatan_negatif
    input_data["jumlah_pinjaman"] = jumlah_pinjaman
    input_data["suku_bunga"] = suku_bunga

    # ----------------------------------------
    # Rasio
    # ----------------------------------------

    if pendapatan > 0:

        input_data["rasio_hutang_terhadap_pendapatan"] = hutang / pendapatan

        input_data["rasio_pinjaman_terhadap_pendapatan"] = jumlah_pinjaman / pendapatan

        input_data["rasio_pembayaran_terhadap_pendapatan"] = (
            jumlah_pinjaman * (suku_bunga / 100)
        ) / pendapatan

    # ----------------------------------------
    # One Hot Encoding
    # ----------------------------------------

    if status_pekerjaan == "Mahasiswa":
        input_data["status_pekerjaan_Mahasiswa"] = 1

    elif status_pekerjaan == "Wiraswasta":
        input_data["status_pekerjaan_Wiraswasta"] = 1

    # Pegawai = baseline

    if tipe_produk == "Kredit Berjalan":
        input_data["tipe_produk_Kredit Berjalan"] = 1

    elif tipe_produk == "Pinjaman Pribadi":
        input_data["tipe_produk_Pinjaman Pribadi"] = 1

    # Kredit Baru = baseline

    if tujuan == "Konsolidasi Hutang":
        input_data["tujuan_pinjaman_Konsolidasi Hutang"] = 1

    elif tujuan == "Medis":
        input_data["tujuan_pinjaman_Medis"] = 1

    elif tujuan == "Pendidikan":
        input_data["tujuan_pinjaman_Pendidikan"] = 1

    elif tujuan == "Pribadi":
        input_data["tujuan_pinjaman_Pribadi"] = 1

    elif tujuan == "Renovasi Rumah":
        input_data["tujuan_pinjaman_Renovasi Rumah"] = 1

    # Kendaraan = baseline

    # ----------------------------------------
    # DataFrame
    # ----------------------------------------

    input_df = pd.DataFrame([input_data])

    input_df = input_df[feature_names]

    # ----------------------------------------
    # Prediksi
    # ----------------------------------------

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    prob_tidak_lancar = probability[0]

    prob_lancar = probability[1]

    # Simpan ke session_state
    st.session_state["prediction"] = prediction
    st.session_state["prob_lancar"] = prob_lancar
    st.session_state["prob_tidak_lancar"] = prob_tidak_lancar

# ===========================================
# WAKTU PREDIKSI
# ===========================================

waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

st.info(f"""
🕒 **Waktu Prediksi**

{waktu}
""")
# ==========================================================
# BAGIAN 4 - HASIL PREDIKSI
# ==========================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]
    prob_lancar = st.session_state["prob_lancar"]
    prob_tidak_lancar = st.session_state["prob_tidak_lancar"]

    st.markdown("""
    <div class="section-card">

    <h3>📊 Hasil Prediksi</h3>

    <p>
    Hasil prediksi status pinjaman berdasarkan
    data yang telah dimasukkan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =============================================
    # CARD HASIL
    # =============================================

    if prediction == 1:

        st.success("🟢 Status Prediksi : LANCAR")

    else:

        st.error("🔴 Status Prediksi : TIDAK LANCAR")

    st.markdown("### 🎯 Tingkat Keyakinan Model")

    if prediction == 1:
        st.progress(float(prob_lancar))
        st.caption(f"Probabilitas Lancar : {prob_lancar:.2%}")
    else:
        st.progress(float(prob_tidak_lancar))
        st.caption(f"Probabilitas Tidak Lancar : {prob_tidak_lancar:.2%}")

    st.divider()

    # =============================================
    # KPI
    # =============================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🟢 Probabilitas Lancar",
            f"{prob_lancar:.2%}"
        )

    with col2:

        st.metric(
            "🔴 Probabilitas Tidak Lancar",
            f"{prob_tidak_lancar:.2%}"
        )

    st.divider()
    
st.divider()

st.markdown("## 📌 Informasi Model")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Jumlah Fitur",
        len(feature_names)
    )

with c2:

    st.metric(
        "Jumlah Kelas",
        "2"
    )

with c3:

    st.metric(
        "Metode",
        "Random Forest"
    )
with c3:

    st.metric(
        "Metode",
        "Random Forest"
    )

# =============================================
# BAR CHART
# =============================================

df_prob = pd.DataFrame({

    "Status":[
        "Lancar",
        "Tidak Lancar"
    ],

    "Probabilitas":[
        prob_lancar,
        prob_tidak_lancar
    ]

})

fig = px.bar(...)
        df_prob,

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

# =============================================
# GAUGE CHART
# =============================================
nilai = prob_lancar if prediction == 1 else prob_tidak_lancar

fig2 = go.Figure(

st.plotly_chart(fig2,use_container_width=True)

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

    fig2.update_layout(height=400)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()
st.divider()

st.markdown("## 📋 Ringkasan Data Input")

ringkasan = pd.DataFrame({

    "Variabel":[
        "Usia",
        "Lama Bekerja",
        "Pendapatan",
        "Skor Kredit",
        "Lama Riwayat Kredit",
        "Aset Tabungan",
        "Total Hutang",
        "Status Pekerjaan",
        "Jumlah Pinjaman",
        "Suku Bunga",
        "Tujuan Pinjaman"
    ],

    "Nilai":[
        usia,
        lama_bekerja,
        f"Rp {pendapatan:,}",
        skor_kredit,
        lama_riwayat,
        f"Rp {aset_tabungan:,}",
        f"Rp {hutang:,}",
        status_pekerjaan,
        f"Rp {jumlah_pinjaman:,}",
        f"{suku_bunga} %",
        tujuan
    ]

})

st.dataframe(
    ringkasan,
    use_container_width=True,
    hide_index=True
)

# =============================================
# INTERPRETASI
# =============================================
st.markdown("""

<div class="section-card">

<h3>📝 Interpretasi Hasil</h3>

</div>

""", unsafe_allow_html=True)
    if prediction == 1:

st.success(f"""

Model Random Forest memprediksi bahwa calon
nasabah memiliki **status pinjaman Lancar**
dengan probabilitas **{prob_lancar:.2%}**.

Hal ini menunjukkan bahwa profil nasabah
memiliki tingkat risiko gagal bayar yang rendah.

""")

    else:

        st.error(f"""

Model Random Forest memprediksi bahwa calon
nasabah memiliki **status pinjaman Tidak Lancar**
dengan probabilitas **{prob_tidak_lancar:.2%}**.

Hal ini menunjukkan bahwa profil nasabah
memiliki tingkat risiko gagal bayar yang tinggi.

""")

st.divider()

st.markdown("## 💡 Rekomendasi")

if prediction == 1:

    st.success("""

Nasabah memiliki peluang tinggi memperoleh
persetujuan pinjaman.

Rekomendasi:

• Pertahankan riwayat pembayaran.

• Hindari keterlambatan cicilan.

• Jaga rasio hutang tetap rendah.

""")

else:

    st.warning("""

Risiko gagal bayar relatif tinggi.

Rekomendasi:

• Tingkatkan skor kredit.

• Kurangi total hutang.

• Perbaiki riwayat pembayaran.

• Ajukan kembali setelah kondisi keuangan membaik.

""")

st.divider()

hasil = pd.DataFrame({

    "Status Prediksi":[
        "Lancar" if prediction == 1 else "Tidak Lancar"
    ],

    "Probabilitas Lancar":[
        round(prob_lancar*100,2)
    ],

    "Probabilitas Tidak Lancar":[
        round(prob_tidak_lancar*100,2)
    ],

    "Tanggal Prediksi":[
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
st.divider()

st.markdown("""

<div style="

text-align:center;

color:gray;

padding:15px;

">

Dashboard Prediksi Status Pinjaman Nasabah

<br>

Metode Random Forest

<br>

© 2026 Sistem Informasi - Business Intelligence

</div>

""", unsafe_allow_html=True)
