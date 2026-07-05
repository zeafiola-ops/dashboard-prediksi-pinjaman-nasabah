# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

import streamlit as st
from pathlib import Path

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Informasi Penelitian",
    page_icon="📚",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

LOGO_PATH = BASE_DIR / "assets" / "logo.png"

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

box-shadow:0px 6px 20px rgba(0,0,0,.08);

margin-bottom:25px;

transition:0.3s;

}

.card:hover{

transform:translateY(-3px);

}

/* Title */

.title{

font-size:44px;

font-weight:bold;

text-align:center;

color:#1848A
