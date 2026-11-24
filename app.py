import streamlit as st
import pandas as pd

st.title("📊 Student Academic Performance - Statistical Analysis")
df = pd.read_csv("student_data.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Mean Marks", f"{df['Marks'].mean():.2f}")
col2.metric("Correlation (r)", "0.9261")
col3.metric("R-Squared", "0.8576")

st.subheader("Visualizations")
st.image(["1_histogram.png", "2_boxplot.png", "3_scatterplot.png"])

st.subheader("Dataset Preview")
st.dataframe(df)