import streamlit as st

st.set_page_config(
    page_title="Chemistry Virtual Lab",
    page_icon="🧪",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
[data-testid="stSidebar"] {
    background-color: #182438;
}
</style>
""", unsafe_allow_html=True)

st.title("🧪 Chemistry Virtual Lab")
st.write("An interactive 2D learning experience for chemistry students.")

st.sidebar.title("Laboratory Menu")
page = st.sidebar.radio(
    "Choose a section",
    ["Home", "pH Simulator", "Acid-Base Simulator",
     "Solubility Simulator", "Chemistry Quiz"]
)

if page == "Home":
    st.header("Welcome to Your Virtual Laboratory")
    st.write("Learn chemistry through simple educational simulations.")

    col1, col2, col3 = st.columns(3)

    col1.info("🧫 **pH Testing**\n\nExplore acidity and alkalinity.")
    col2.info("⚗️ **Acid-Base**\n\nUnderstand neutralisation.")
    col3.info("💧 **Solubility**\n\nExplore dissolving and temperature.")

    st.success("Select an experiment from the menu on the left.")

elif page == "pH Simulator":
    st.header("🧫 pH Simulator")
    st.write("Move the slider to explore the pH scale.")

    ph = st.slider("Select pH value", 0.0, 14.0, 7.0, 0.5)

    if ph < 7:
        st.error(f"pH {ph} — Acidic")
    elif ph > 7:
        st.info(f"pH {ph} — Basic (alkaline)")
    else:
        st.success("pH 7 — Neutral")

    st.progress(int(ph / 14 * 100))
    st.caption("Educational pH scale: 0 = strongly acidic, 7 = neutral, 14 = strongly basic.")

elif page == "Acid-Base Simulator":
    st.header("⚗️ Acid-Base Simulator")
    st.write("Explore a simplified neutralisation model.")

    acid = st.slider("Acid amount (illustrative units)", 0, 100, 50)
    base = st.slider("Base amount (illustrative units)", 0, 100, 50)

    difference = acid - base

    if difference == 0:
        st.success("Balanced model: neutralisation point!")
    elif difference > 0:
        st.warning("The model has excess acid.")
    else:
        st.info("The model has excess base.")

    st.write(f"Acid amount: {acid}")
    st.write(f"Base amount: {base}")

elif page == "Solubility Simulator":
    st.header("💧 Solubility Simulator")
    st.write("Explore an illustrative model of how temperature can affect dissolving.")

    temperature = st.slider("Temperature (°C)", 0, 100, 25)

    solubility = 20 + temperature * 0.8

    st.metric("Illustrative solubility", f"{solubility:.1f} units")
    st.caption("This is a simplified teaching model, not measured data for a real substance.")

elif page == "Chemistry Quiz":
    st.header("📝 Chemistry Quiz")

    answer = st.radio(
        "What is the pH value of a neutral solution?",
        ["0", "7", "14", "10"]
    )

    if st.button("Check Answer"):
        if answer == "7":
            st.success("Correct! A neutral solution has pH 7.")
        else:
            st.error("Not quite. Try again!")
 
 
