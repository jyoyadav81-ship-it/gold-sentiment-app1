import streamlit as st
import pandas as pd

df = pd.read_csv("final_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.title("📊 Gold Price + Sentiment App")

date_input = st.date_input("Select Date")

if st.button("Get Result"):

    result = df[df['Date'] == pd.to_datetime(date_input)]

    if not result.empty:
        price = result['Price'].values[0]
        sentiment = result['sentiment_num'].values[0]

        if sentiment > 0:
            label = "😊 Positive"
        elif sentiment < 0:
            label = "😡 Negative"
        else:
            label = "😐 Neutral"

        st.success(f"💰 Gold Price: {price}")
        st.info(f"📊 Sentiment Score: {sentiment}")
        st.write(f"🧠 Market Mood: {label}")
    else:
        st.error("No data found")
