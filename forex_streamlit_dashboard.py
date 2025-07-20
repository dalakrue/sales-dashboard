
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Forex_Trading_Summary_Data.csv")

# Set page config
st.set_page_config(page_title="Forex Trading Dashboard", layout="wide")

# Title
st.title("📈 Forex Trading Performance Dashboard")

# KPI Section
st.header("🔹 Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Gross Profit", f"${df[df['Metric']=='Gross Profit']['Value'].values[0]:.2f}")
kpi2.metric("Gross Loss", f"${df[df['Metric']=='Gross Loss']['Value'].values[0]:.2f}")
kpi3.metric("Netto P/L", f"${df[df['Metric']=='Netto P/L']['Value'].values[0]:.2f}")
kpi4.metric("Profit Factor", f"{df[df['Metric']=='Profit Factor']['Value'].values[0]:.2f}")

kpi5, kpi6, kpi7, kpi8 = st.columns(4)
kpi5.metric("Sharpe Ratio", f"{df[df['Metric']=='Sharpe Ratio']['Value'].values[0]:.2f}")
kpi6.metric("Recovery Factor", f"{df[df['Metric']=='Recovery Factor']['Value'].values[0]:.2f}")
kpi7.metric("Max Drawdown %", f"{df[df['Metric']=='Max Drawdown %']['Value'].values[0]:.2f}%")
kpi8.metric("Deposit Load %", f"{df[df['Metric']=='Max Deposit Load %']['Value'].values[0]:.2f}%")

# Bar Chart: Long vs Short Trades
st.header("🔹 Long vs Short Trade Analysis")
long_short_data = {
    'Type': ['Trades', 'Win Trades', 'Average P/L', 'Average Profit'],
    'Long': [
        df[df['Metric'] == 'Trades (Long)']['Value'].values[0],
        df[df['Metric'] == 'Win Trades (Long)']['Value'].values[0],
        df[df['Metric'] == 'Average P/L (Long)']['Value'].values[0],
        df[df['Metric'] == 'Average Profit (Long)']['Value'].values[0]
    ],
    'Short': [
        df[df['Metric'] == 'Trades (Short)']['Value'].values[0],
        df[df['Metric'] == 'Win Trades (Short)']['Value'].values[0],
        df[df['Metric'] == 'Average P/L (Short)']['Value'].values[0],
        df[df['Metric'] == 'Average Profit (Short)']['Value'].values[0]
    ]
}
df_long_short = pd.DataFrame(long_short_data)

fig = px.bar(df_long_short, x='Type', y=['Long', 'Short'], barmode='group',
             title='📊 Long vs Short Trade Comparison')
st.plotly_chart(fig)

# Footer
st.caption("Built with ❤️ in Streamlit")
