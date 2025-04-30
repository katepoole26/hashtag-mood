import streamlit as st
from streamlit_autorefresh import st_autorefresh
from utils import append_mood, get_today_moods
import plotly.express as px

st.set_page_config(page_title="Mood Log", layout="centered")
st.title("🪩 Mood of the Queue")

# mood logging
with st.form("mood_log"):
    mood = st.selectbox("How's the mood right now?", ["😊", "😠", "😕", "🎉"])  # drop down selections
    note = st.text_input("Add a note (optional)")
    submitted = st.form_submit_button("Log Mood")

if submitted:
    append_mood(mood, note)
    st.success("✅ Mood logged!")


st.markdown("---")
st.subheader("📊 Today's Mood Trend")
# autorefresh chart 60 second interval
count = st_autorefresh(interval=60000, key="chart_refresh")

# map moods to apt colors
color_map = {
    "😊": "#FFD700",
    "😠": "#FF6347",
    "😕": "#A9A9A9",
    "🎉": "#32CD32"
}

# viz
df = get_today_moods()
if df.empty:
    st.info("No moods logged today yet.")
else:
    mood_counts = df["Mood"].value_counts().reset_index()
    mood_counts.columns = ["Mood", "Count"]
    fig = px.bar(
        mood_counts, 
        x="Mood", 
        y="Count", 
        color="Mood", 
        color_discrete_map=color_map,
        title="Mood Count Today"
    )
    st.plotly_chart(fig)