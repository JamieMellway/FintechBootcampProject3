import streamlit as st
st.set_page_config(layout="wide")
from utils.MultiApp import MultiApp
import priceindextrends 
import geolocation
import montecarlo
import dataload

# def priceindextrends():
#     st.header("Trends")

# def geolocation():
#     st.header("Geolocation")

# def montecarlo():
#     st.header("Monte Carlo")

def machinelearning():
    st.header("Machine Learning")

def chatbot():
    st.header("Chat bot")

def main():
    app = MultiApp()

    app.add_app("Trends (Ontario)", priceindextrends.render_page)
    #app.add_app("Trends (Regional)", priceindextrendsregional.render_page)
    app.add_app("Geolocation", geolocation.render_page)
    app.add_app("Monte Carlo", montecarlo.render_page)
    app.add_app("Machine Learning - Data Load", dataload.render_page)
    app.add_app("Machine Learning", machinelearning)
    app.add_app("Chat Bot", chatbot)
    
    # The main app
    app.run()

if __name__ == '__main__':
    main()