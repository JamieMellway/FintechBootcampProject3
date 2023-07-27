import streamlit as st
st.set_page_config(layout="wide")
from utils.MultiApp import MultiApp
import priceindextrends 
import geolocation
import montecarlo
import dataload
import machinelearning
import chatbot
#import unittest

def main():
    app = MultiApp()

    app.add_app("Trends (Ontario)", priceindextrends.render_page)
    #app.add_app("Trends (Regional)", priceindextrendsregional.render_page)
    #app.add_app("Geolocation", geolocation.render_page)
    app.add_app("Monte Carlo", montecarlo.render_page)
    app.add_app("Machine Learning - Data Load", dataload.render_page)
    app.add_app("Machine Learning", machinelearning.render_page)
    app.add_app("Property Value", chatbot.render_page)
    #app.add_app("Unit Tests", unittest.render_page)
    
    # The main app
    app.run()

if __name__ == '__main__':
    main()