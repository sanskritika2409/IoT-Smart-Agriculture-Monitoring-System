import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

st.set_page_config(
    page_title="Smart Agriculture Dashboard",
    page_icon="🌱",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

st.markdown("""
<style>
.main {
    background-color:#0f172a;
}
.metric-card {
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
}
.alert-box{
    background:#7f1d1d;
    color:white;
    padding:10px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 IoT Smart Agriculture Monitoring System")

if not os.path.exists("data/sensor_data.csv"):
    st.warning("Run main.py first")
    st.stop()

df = pd.read_csv("data/sensor_data.csv")

if len(df) == 0:
    st.warning("No data found")
    st.stop()

latest = df.iloc[-1]

soil = latest["soil_moisture"]
temp = latest["temperature"]
humidity = latest["humidity"]
water = latest["water_level"]

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("🌿 Soil Moisture", f"{soil}%")

with col2:
    st.metric("🌡 Temperature", f"{temp} °C")

with col3:
    st.metric("💧 Humidity", f"{humidity}%")

with col4:
    st.metric("🚰 Water Level", f"{water}%")

st.divider()

c1,c2 = st.columns(2)

with c1:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=soil,
        title={'text':"Soil Moisture"},
        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':'green'}
        }
    ))

    st.plotly_chart(fig,use_container_width=True)

with c2:

    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=water,
        title={'text':"Water Level"},
        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':'blue'}
        }
    ))

    st.plotly_chart(fig2,use_container_width=True)

st.divider()

st.subheader("📊 Sensor Trends")

fig = px.line(
    df,
    y=["soil_moisture","temperature","humidity","water_level"],
    title="Sensor History"
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("🚨 Alert Center")

alerts=[]

if soil < 40:
    alerts.append("⚠ Low Soil Moisture Detected")

if temp > 35:
    alerts.append("🔥 High Temperature")

if water < 20:
    alerts.append("🚱 Low Water Level")

if alerts:
    for a in alerts:
        st.error(a)
else:
    st.success("✅ All Conditions Normal")

st.divider()

st.subheader("🚿 Pump Status")

if soil < 40:
    st.success("PUMP ON")
else:
    st.info("PUMP OFF")

st.divider()

st.subheader("📥 Download Data")

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    file_name="sensor_data.csv",
    mime="text/csv"
)

st.dataframe(df.tail(20))