import streamlit as st
import pandas as pd
from pathlib import Path
import csv
import requests
from io import StringIO

def load_csv(name):
    url = 'https://raw.githubusercontent.com/JamieMellway/FintechBootcampProject3/main/streamlit/Resources/' + name
    response = requests.get(url)
    data = StringIO(response.text)
    return pd.read_csv(data)

def get_data_by_region_bldg_date(data, region, bldg, date=None):
    new_bldg = bldg.replace(' ', '_')
    new_region = region.upper().replace(' ', '_')

    feature = f'PRED_{new_bldg}_Benchmark_SA_{new_region}'

    return feature

def render_page():
    total_chart = load_csv('total_chart_regional_save.csv')
    total_chart = total_chart.set_index('date')

    locations = ["Bancroft and Area", "Barrie And District", "Brantford Region", "Cambridge", "Greater Toronto", "Grey Bruce Owen Sound", "Guelph And District", "Hamilton Burlington", "Huron Perth", "Kawartha Lakes", "Kingston And Area", "Kitchener Waterloo", "Lakelands", "London St Thomas", "Mississauga", "Niagara Region", "Northumberland Hills", "North Bay", "Oakville Milton", "Ottawa", "Peterborough And Kawarthas", "Quinte And District", "Rideau St Lawrence", "Sault Ste Marie", "Simcoe And District", "Sudbury", "Tillsonburg District" , "Windsor Essex" , "Woodstock Ingersoll"]
    building_types = ['Composite', 'Single Family', 'One Storey', 'Two Storey', 'Townhouse', 'Apartment']
    dates = total_chart.index.to_numpy()
    sorted_dates = sorted(dates, reverse=True)

    locations_selected = st.selectbox("Location", locations)
    building_types_selected = st.selectbox("Building Type", building_types)
    date_selected = st.selectbox("Date", sorted_dates)

    if st.button("Generate Chart"):
        if building_types_selected and locations_selected:
            selection = get_data_by_region_bldg_date(total_chart, locations_selected, building_types_selected)
            try:
                chart = total_chart[selection]
                value = round(chart.loc[date_selected],2)
                st.write(f"The price of a {building_types_selected} in {locations_selected} is \${value:,.2f}")
            except:
                st.write(f"Information on a {building_types_selected} is not available in {locations_selected}.")    
