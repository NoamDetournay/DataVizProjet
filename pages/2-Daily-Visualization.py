import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

@st.cache_data  
def load_data(url):
    df = pd.read_csv(url, delimiter=';')
    # Convert the 'Date/Time' column to datetime format
    df = df.dropna(subset=['consommation_brute_gaz_grtgaz'])
    df = df.reset_index(drop=True)
    
    df['date'] = pd.to_datetime(df['date'])
    df['date_heure'] = pd.to_datetime(df['date_heure'])
    df['heure'] = pd.to_datetime(df['heure'], format='%H:%M').dt.hour
    return df


df = load_data(
    "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/consommation-quotidienne-brute/exports/csv")


st.write("""# Daily Energy Consumption Analysis: Gas vs Electricity Trends
In this page, we analyze the consumption patterns of gas and electricity across different hours, days, and months. 
Our analysis includes hourly and daily comparisons, highlighting key insights such as peak consumption times, seasonal dependencies, and the relationship between gas and electricity consumption.
""")

# List of months
months = list(calendar.month_name[1:])  # Month names from January to December

# Create a selectbox for each chart to choose the month
st.write("""### Hourly Gas and Electricity Consumption
This chart shows the hourly consumption of gas and electricity. It's interesting because we can observe a peak in gas usage at 7 a.m., followed by a gradual decrease until 5 p.m. before dropping further during the night. 
         
For electricity, there is less variation overall, but we notice a significant drop between 1 a.m. and 6 a.m.
""")
# Line chart section for hourly gas and electricity consumption
selected_month_for_hourly = st.selectbox("Select a month for Hourly Consumption Chart:", months)
selected_month_index = months.index(selected_month_for_hourly) + 1  # Get month number (1 for Jan, etc.)

# Filter data for the selected month
month_data = df[df['date'].dt.month == selected_month_index]

if month_data.empty:
    st.write(f"No data available for {selected_month_for_hourly}.")
else:
    # Group by the 'heure' (which is already converted to hour integer)
    hourly_gas_data = month_data.groupby('heure')['consommation_brute_gaz_totale'].sum()
    hourly_electricity_data = month_data.groupby('heure')['consommation_brute_electricite_rte'].sum()

    # Plot gas consumption per hour
    if not hourly_gas_data.empty:
        fig_hourly_gas = px.bar(hourly_gas_data, 
                                labels={'x': "Hour of Day", 'y': "Total Gas Consumption (MWh)"},
                                title=f"Hourly Gas Consumption for {selected_month_for_hourly}")
        st.plotly_chart(fig_hourly_gas)
    else:
        st.write(f"No gas data available for {selected_month_for_hourly}.")

    # Plot electricity consumption per hour
    if not hourly_electricity_data.empty:
        fig_hourly_electricity = px.bar(hourly_electricity_data, 
                                        labels={'x': "Hour of Day", 'y': "Total Electricity Consumption (MWh)"},
                                        title=f"Hourly Electricity Consumption for {selected_month_for_hourly}")
        st.plotly_chart(fig_hourly_electricity)
    else:
        st.write(f"No electricity data available for {selected_month_for_hourly}.")

st.write("""### Result interpretation
The gas usage follows a typical daily pattern with high consumption in the morning and gradual decrease. 
         
The electricity consumption is steadier but shows a notable decrease in the early morning hours.
""")

st.write("""### Daily Gas and Electricity Consumption Comparison
This chart compares daily gas and electricity consumption. We can observe that during the summer, gas consumption is much lower than electricity. 

However, gas consumption tends to surpass electricity consumption overall. Noticeable drops occur on significant event days like July 14 and December 25.
""")

# Stacked chart for daily gas and electricity consumption
selected_month_for_daily = st.selectbox("Select a month for Daily Stacked Chart:", months)

# Filter data for the selected month
selected_month_index = months.index(selected_month_for_daily) + 1
month_data = df[df['date'].dt.month == selected_month_index]

if not month_data.empty:
    daily_gas = month_data.groupby(month_data['date'].dt.day)['consommation_brute_gaz_totale'].sum()
    daily_electricity = month_data.groupby(month_data['date'].dt.day)['consommation_brute_electricite_rte'].sum()

    if not daily_gas.empty and not daily_electricity.empty:
        fig_stacked = px.area(x=daily_gas.index, 
                              y=[daily_gas.values, daily_electricity.values],
                              labels={'x': "Day of Month", 'y': "Total Consumption (MWh)"},
                              title=f"Daily Energy Consumption (Gas vs Electricity) for {selected_month_for_daily}")
        fig_stacked.update_layout(legend_title="Energy Source", showlegend=True)
        st.plotly_chart(fig_stacked)
    else:
        st.write(f"No data available for gas and electricity in {selected_month_for_daily}.")
else:
    st.write(f"No data available for {selected_month_for_daily}.")

st.write("""### Result interpretation
The data reveals the strong impact of seasonal events on energy consumption, particularly with large drops in both gas and electricity use during major holidays like July 14 and December 25.
""")

st.write("""### Gas to Electricity Ratio
This chart highlights the ratio between gas and electricity consumption. 
It provides better insight into gas usage during colder months, as people tend to use more gas during colder weather.
""")


# Ratio chart for gas to electricity consumption
selected_month_for_ratio = st.selectbox("Select a month for Gas to Electricity Ratio Chart:", months)

# Filter data for the selected month
selected_month_index = months.index(selected_month_for_ratio) + 1
month_data = df[df['date'].dt.month == selected_month_index]

if not month_data.empty:
    # Calculate the ratio of gas to electricity consumption
    month_data['gas_to_electricity_ratio'] = month_data['consommation_brute_gaz_totale'] / month_data['consommation_brute_electricite_rte']
    daily_ratio = month_data.groupby(month_data['date'].dt.day)['gas_to_electricity_ratio'].mean()

    if not daily_ratio.empty:
        fig_ratio = px.line(daily_ratio, 
                            labels={'x': "Day of Month", 'y': "Gas to Electricity Ratio"},
                            title=f"Daily Gas to Electricity Consumption Ratio for {selected_month_for_ratio}")
        st.plotly_chart(fig_ratio)
    else:
        st.write(f"No data available for gas to electricity ratio in {selected_month_for_ratio}.")
else:
    st.write(f"No data available for {selected_month_for_ratio}.")

st.write("""### Result interpretation
The ratio chart clearly shows the increased use of gas compared to electricity during colder months, reflecting the demand for heating in such conditions.
""")