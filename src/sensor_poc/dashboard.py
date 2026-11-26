import plotly.express as px
import streamlit as st

from sensor_poc.database import get_measurements, init_db

st.set_page_config(
    page_title="Sensor Dashboard",
    layout="wide"
)

st.title("Sensor Monitoring Dashboard")

init_db()

# Automatically refresh this section every second
@st.fragment(run_every="1s")
def dashboard():

    df = get_measurements()

    if df.empty:
        st.info("Waiting for sensor data...")
        return

    # Keep the last 120 measurements
    df = df.tail(120)

    # Latest values
    latest = df.iloc[-1]

    col1, col2, col3 = st.columns(3)

    col1.metric("SpO2", f"{latest['spo2']:.1f} %")
    col2.metric("Heart Rate", f"{latest['heart_rate']:.1f} BPM")
    col3.metric("Pressure", f"{latest['pressure']:.1f} hPa")

    st.divider()

    # Oxymeter
    st.subheader("Oxymeter")

    fig = px.line(
        df,
        x="timestamp",
        y=["spo2", "heart_rate"],
        title="SpO2 and Heart Rate"
    )

    st.plotly_chart(fig, width='stretch')

    # Barometer
    st.subheader("Barometer")

    fig = px.line(
        df,
        x="timestamp",
        y="pressure",
        title="Atmospheric Pressure"
    )

    st.plotly_chart(fig, width='stretch')

    # Accelerometer
    st.subheader("Accelerometer")

    fig = px.line(
        df,
        x="timestamp",
        y=["accel_x", "accel_y", "accel_z"],
        title="Acceleration (m/s²)"
    )

    st.plotly_chart(fig, width='stretch')

dashboard()