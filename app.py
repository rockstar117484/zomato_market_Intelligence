import streamlit as st
import pandas as pd

st.set_page_config(page_title="Restaurant Market Intelligence", layout="wide")

# Load data
df = pd.read_csv("market_data.csv")

# Clean text again (IMPORTANT)
df['City'] = df['City'].astype(str).str.strip()
df['Locality'] = df['Locality'].astype(str).str.strip()

st.title("🍽️ Restaurant Market Intelligence Dashboard")

# Sidebar
st.sidebar.header("Select Location")

city = st.sidebar.selectbox("City", sorted(df['City'].unique()))

filtered_df = df[df['City'] == city]

locality = st.sidebar.selectbox("Locality", sorted(filtered_df['Locality'].unique()))

result = df[(df['City'] == city) & (df['Locality'] == locality)]

st.subheader("📊 Market Insights")

if not result.empty:
    row = result.iloc[0]

    col1, col2, col3 = st.columns(3)

    col1.metric("⭐ Avg Rating", round(row['rating'], 2))
    col2.metric("📈 Total Demand (Votes)", int(row['votes']))
    col3.metric("💰 Avg Cost", int(row['cost']))

    st.subheader("🧠 Market Type")
    st.info(row['Strategic_Persona'])

    # Recommendation
    if "High Demand" in row['Strategic_Persona']:
        st.success("🚀 Best place for expansion")
    elif "Premium" in row['Strategic_Persona']:
        st.info("💎 Suitable for premium brands")
    elif "Overpriced" in row['Strategic_Persona']:
        st.warning("❌ Market inefficient / overpriced")
    else:
        st.warning("⚠️ Emerging or low visibility area")

else:
    st.error("No data found")