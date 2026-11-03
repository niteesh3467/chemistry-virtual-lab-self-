
import streamlit as st

st.set_page_config(
    page_title="Chemistry Virtual Lab",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Chemistry Virtual Lab")

st.subheader(
    "Welcome to Your Interactive Chemistry Laboratory"
)

st.write(
    "Explore chemistry through interactive "
    "2D experiments and simulations."
)

st.success("Your Chemistry Virtual Lab project has started!")

st.markdown("### Our Experiments")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧫 pH Testing")

with col2:
    st.info("⚗️ Acid-Base Reaction")

with col3:
    st.info("💧 Solubility Experiment")

