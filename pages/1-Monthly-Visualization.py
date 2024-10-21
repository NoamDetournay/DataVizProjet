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

st.write("""
# Energy Consumption Analysis
This streamlit page analyzes gas and electricity consumption data. 
By comparing these energy sources, we can gain insights into consumption patterns, 
seasonal variations, and the overall trends in energy use. 

The following charts will help us visualize these patterns and draw meaningful conclusions.
""")

st.write("""
### Chart 1: Gas Consumption Comparison
This chart compares the gas consumption between GRTgaz and Teréga for the selected year and month. 
By visualizing the consumption trends, we can understand how gas usage varies between these two suppliers.
""")

# Create three columns for the selections
col1, col2, col3 = st.columns(3)

# Column 1: Select year for the first chart (default is 2023)
with col1:
    year1 = st.selectbox('Select a year for GRTgaz vs Teréga comparison', 
                         options=df['date'].dt.year.unique(), index=0)

# Column 2: Select month for the first chart (or 'All' for the entire year)
with col2:
    month1 = st.selectbox('Select a month for GRTgaz vs Teréga comparison', 
                          options=['All'] + list(df['date'].dt.month_name().unique()), index=0)

# Column 3: Checkboxes for variables to display for the first chart
with col3:
    show_gaz_grtgaz = st.checkbox('Show GRTgaz Consumption', value=True)
    show_gaz_terega = st.checkbox('Show Teréga Consumption', value=True)

# Filter data based on the selected year and month
filtered_df1 = df[df['date'].dt.year == year1]

# If the user selects a specific month, filter by that month
if month1 != 'All':
    filtered_df1 = filtered_df1[filtered_df1['date'].dt.month_name() == month1]

# Prepare the list of variables to display based on checkboxes
variables1 = []
if show_gaz_grtgaz:
    variables1.append('consommation_brute_gaz_grtgaz')
if show_gaz_terega:
    variables1.append('consommation_brute_gaz_terega')



# Chart 1: GRTgaz vs Teréga gas consumption comparison
if variables1:
    fig1 = px.line(filtered_df1, x='date', y=variables1, 
                   title=f"Gas Consumption Comparison: GRTgaz vs Teréga in {year1} ({month1 if month1 != 'All' else 'All Year'})")
    st.plotly_chart(fig1)
else:
    st.write("Please select at least one variable for the GRTgaz vs Teréga chart.")

# Placeholder for results interpretation
st.write("### Results Interpretation:")
st.write("""GRTgaz's gas consumption has experienced significant fluctuations throughout the year. 
        It started at a relatively high level in January, then declined to a low point in March before rebounding to a new high in April.
        Overall, GRTgaz's gas consumption is higher than Teréga's
        The fluctuations in gas consumption could be attributed to seasonal factors, such as changes in weather conditions or economic activity. 
        For example, increased heating demand in colder months could lead to higher gas consumption.""")

st.write("""
### Chart 2: Gas vs Electricity Consumption Comparison
This chart compares the total gas consumption to electricity consumption for the selected year and month.
""")
# Create another three columns for the second chart selections
col4, col5, col6 = st.columns(3)

# Column 1: Select year for the second chart (default is 2023)
with col4:
    year2 = st.selectbox('Select a year for Gas vs Electricity comparison', 
                         options=df['date'].dt.year.unique(), index=0)

# Column 2: Select month for the second chart (or 'All' for the entire year)
with col5:
    month2 = st.selectbox('Select a month for Gas vs Electricity comparison', 
                          options=['All'] + list(df['date'].dt.month_name().unique()), index=0)

# Column 3: Checkboxes for variables to display for the second chart
with col6:
    show_gaz_totale = st.checkbox('Show Total Gas Consumption', value=True)
    show_electricite = st.checkbox('Show Electricity Consumption', value=True)

# Filter data based on the selected year and month
filtered_df2 = df[df['date'].dt.year == year2]

# If the user selects a specific month, filter by that month
if month2 != 'All':
    filtered_df2 = filtered_df2[filtered_df2['date'].dt.month_name() == month2]

# Prepare the list of variables to display based on checkboxes
variables2 = []
if show_gaz_totale:
    variables2.append('consommation_brute_gaz_totale')
if show_electricite:
    variables2.append('consommation_brute_electricite_rte')



# Chart 2: Gas vs Electricity consumption comparison
if variables2:
    fig4 = px.line(filtered_df2, x='date', y=variables2, 
                   title=f"Gas vs Electricity Consumption in {year2} ({month2 if month2 != 'All' else 'All Year'})")
    st.plotly_chart(fig4)
else:
    st.write("Please select at least one variable for the Gas vs Electricity chart.")

st.write("### Results Interpretation:")
st.write("""
The total gas consumption is significantly higher than the total electricity consumption.
         
Both gas and electricity consumption fluctuate throughout the year. There are peaks and troughs in both consumption patterns, but the overall trend for gas consumption is higher than that of electricity.
         
The months of January and February show the highest consumption of both gas and electricity. Consumption tends to decrease in the spring and summer months, before increasing again in the autumn and winter.
""")

# Monthly average consumption chart
monthly_avg = df.groupby(df['date'].dt.month)[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte']].mean().reset_index()
monthly_avg['date'] = monthly_avg['date'].apply(lambda x: calendar.month_name[x])

st.write("""
### Chart 3 : Monthly Average Consumption Chart
This bar chart illustrates the monthly average consumption of gas and electricity, allowing for a quick comparison 
of energy usage throughout the year.
""")

fig_avg = px.bar(monthly_avg, x='date', y=['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte'],
                 title='Monthly Average Consumption of Gas and Electricity')
st.plotly_chart(fig_avg)

st.write("### Results Interpretation:")
st.write("""
         The gas consumption peaks in January and February, likely due to colder temperatures requiring more heating. It remains relatively high throughout the winter months but decreases significantly during the summer.

         The electricity consumption is relatively stable throughout the year.

         Gas is commonly used for heating, which is a major energy consumer during colder months.

         Electricity is used for a variety of purposes, including lighting, appliances, and electronics. Its consumption is more consistent throughout the year.
         """)

st.write("""
### Box Plot of Gas and Electricity Consumption
The box plot provides a visual summary of the distribution of gas and electricity consumption. 
It highlights the median, quartiles, and potential outliers in the data.""")

fig_box = px.box(df, y=['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte'],
                 title='Box Plot of Gas and Electricity Consumption')
st.plotly_chart(fig_box)

st.write("""### Interpretation of Results: 
The median gas consumption is notably higher, indicating that a majority of households consume more gas than electricity. The outliers suggest a few households consume significantly more gas than the general population.

The electricity consumption data appears more concentrated around the median, with a smaller IQR. This suggests a more consistent pattern of electricity consumption among households.
    """)

st.write("""
### Proportion of Gas and Electricity Consumption
This pie chart gives an overview of the total proportion of gas versus electricity consumption. """)

total_consumption = df[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte']].sum()
fig_pie = px.pie(values=total_consumption, names=total_consumption.index, title='Proportion of Gas and Electricity Consumption')
st.plotly_chart(fig_pie)

st.write("""### Interpretation of Results:
Throught the all the years, the proportion of gas and electricity are equal.
""")

st.write("""
### Annual Gas and Electricity Consumption Trends
The line chart below highlights the trends in energy consumption over the years. You can easily observe how gas and electricity consumption have evolved over the years.
""")
# Annual Trends for Gas and Electricity
annual_trends = df.groupby(df['date'].dt.year)[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte']].sum().reset_index()

fig_annual_trends = px.line(annual_trends, x='date', y=['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte'], 
                             title='Annual Gas and Electricity Consumption Trends')
st.plotly_chart(fig_annual_trends)

st.write("""### Interpretation of Results:
The chart shows a notable decline in both gas and electricity consumption starting around 2020, which aligns with the onset of the COVID-19 pandemic. During this period, lockdowns and reduced industrial activity would have contributed to lower energy demand, especially in sectors like manufacturing, transportation, and commercial real estate. Many businesses closed or operated at reduced capacity, and fewer people commuted, which likely drove down both gas and electricity usage.

In addition to the pandemic, post-2020 efforts toward greener energy sources and greater efficiency could also contribute to the continued decline in fossil fuel consumption like gas, along with better optimization of electricity use.
""")

df['date'] = pd.to_datetime(df['date'])

st.write("""
### Monthly Electricity Consumption Breakdown
This section provides a monthly breakdown of gas and electricity consumption. It is split into two pie charts to help visualize how energy usage varies across different months of the year.
""")


# Create a mapping of month numbers to month names
month_names = pd.Series(pd.date_range('2021-01-01', periods=12, freq='M')).dt.month_name()

# Monthly Consumption Breakdown for Gas
monthly_gas_consumption = df.groupby(df['date'].dt.month)['consommation_brute_gaz_totale'].sum()
fig_pie_gas = px.pie(values=monthly_gas_consumption, names=month_names[monthly_gas_consumption.index - 1], title='Monthly Gas Consumption Breakdown')
st.plotly_chart(fig_pie_gas)

# Monthly Consumption Breakdown for Electricity
monthly_electricity_consumption = df.groupby(df['date'].dt.month)['consommation_brute_electricite_rte'].sum()
fig_pie_electricity = px.pie(values=monthly_electricity_consumption, names=month_names[monthly_electricity_consumption.index - 1], title='Monthly Electricity Consumption Breakdown')
st.plotly_chart(fig_pie_electricity)

