import streamlit as st

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(page_title="Koundal RF Audit Engine", layout="wide")
st.title("📡 Koundal Global Wireless RF Audit Engine")
st.write("Lead Engineer: **Amit Koundal** | GSM • LTE • NR Diagnostic Suite")
st.divider()

# -----------------------------
# KPI RANGES
# -----------------------------
kpi_ranges = {
    "RSRP": {"good": -90, "average": -105, "bad": -120},
    "RSRQ": {"good": -10, "average": -15, "bad": -20},
    "SINR": {"good": 20, "average": 10, "bad": 0},
    "RSSI": {"good": -60, "average": -80, "bad": -100},
    "RxLev": {"good": -70, "average": -90, "bad": -110},
}

def evaluate_kpi(name, value):
    r = kpi_ranges[name]
    if value >= r["good"]:
        return "✅ Good"
    elif value >= r["average"]:
        return "⚠️ Average"
    else:
        return "❌ Poor"

# -----------------------------
# SIDEBAR
# -----------------------------
tech = st.sidebar.radio("Select Network Technology:", ["NR (5G)", "LTE (4G)", "GSM (2G)"])

# -----------------------------
# NR (5G)
# -----------------------------
if tech == "NR (5G)":
    st.header("NR (5G) Primary Serving Cell Audit")
    t1, t2 = st.tabs(["Band & Frequency", "Signal & Beam"])
    with t1:
        c1, c2 = st.columns(2)
        c1.text_input("NR Band Type", "n78 (C-Band)")
        c1.number_input("NR DL ARFCN", value=627312)
        c2.number_input("GSCN", value=7711)
        c2.number_input("Point A Frequency (MHz)", value=3500.0)
    with t2:
        c1, c2 = st.columns(2)
        rsrp = c1.number_input("SS-RSRP (dBm)", value=-105.0)
        rsrq = c1.number_input("SS-RSRQ (dB)", value=-12.0)
        sinr = c2.number_input("SINR (dB)", value=10.0)
        c2.text_input("Rx Beam ID", "Beam_01")

    st.write("RSRP Status:", evaluate_kpi("RSRP", rsrp))
    st.write("RSRQ Status:", evaluate_kpi("RSRQ", rsrq))
    st.write("SINR Status:", evaluate_kpi("SINR", sinr))

# -----------------------------
# LTE (4G)
# -----------------------------
elif tech == "LTE (4G)":
    st.header("LTE (4G) Serving Cell Detail Audit")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Layer 1/2 Info")
        st.text_input("LTE Serving Band", "Band 3 (1800)")
        st.number_input("EARFCN (DL)", value=1300)
        st.number_input("EARFCN (UL)", value=19300)
        st.number_input("LTE PCI", value=124)
    
    with col2:
        st.subheader("Network Info")
        st.number_input("Tracking Area Code (TAC)", value=4501)
        st.number_input("Global Cell ID", value=128945)
        st.selectbox("Duplex", ["FDD", "TDD"])
        st.number_input("DL Bandwidth (MHz)", value=20)
        
    with col3:
        st.subheader("Radio KPIs")
        rsrp = st.number_input("RSRP (dBm)", value=-95.0)
        rsrq = st.number_input("RSRQ (dB)", value=-12.0)
        sinr = st.number_input("SINR (dB)", value=10.0)
        rssi = st.number_input("RSSI (dBm)", value=-65.0)

    st.write("RSRP Status:", evaluate_kpi("RSRP", rsrp))
    st.write("RSRQ Status:", evaluate_kpi("RSRQ", rsrq))
    st.write("SINR Status:", evaluate_kpi("SINR", sinr))
    st.write("RSSI Status:", evaluate_kpi("RSSI", rssi))

# -----------------------------
# GSM (2G)
# -----------------------------
elif tech == "GSM (2G)":
    st.header("GSM (2G) Legacy Audit")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Frequency Info")
        st.number_input("BCCH ARFCN", value=62)
        st.number_input("BSIC", value=34)
        st.number_input("TSC (Training Seq Code)", value=5)
    
    with c2:
        st.subheader("Identity")
        st.number_input("LAC (Location Area Code)", value=1023)
        st.number_input("Cell ID", value=5521)
        st.selectbox("Band", ["900", "1800"])
        
    with c3:
        st.subheader("Quality")
        rxlev = st.number_input("RxLev (dBm)", value=-85.0)
        rxqual = st.slider("RxQual (0-7)", 0, 7, 2)
        
    st.write("RxLev Status:", evaluate_kpi("RxLev", rxlev))
    if rxqual > 4:
        st.error("🚨 High BER (Bit Error Rate). Likely co-channel interference.")

# -----------------------------
# FOOTER
# -----------------------------
st.divider()
st.info("💡 **Amit's Leadership Vision:** Unified RF KPI baseline for 2G, 4G, and 5G.")
