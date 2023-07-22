# importing libraries
import streamlit as st
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
from pathlib import Path
import hvplot.pandas
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import time
import holoviews as hv
hv.extension('bokeh', logo=False)

def render_page():
   #Import Regional Data
    region01 = pd.read_csv(Path("../Resources/BANCROFT_AND_AREA.csv"))
    region02 = pd.read_csv(Path("../Resources/BARRIE_AND_DISTRICT.csv"))
    region03 = pd.read_csv(Path("../Resources/BRANTFORD_REGION.csv"))
    region04 = pd.read_csv(Path("../Resources/CAMBRIDGE.csv"))
    region05 = pd.read_csv(Path("../Resources/GREATER_TORONTO.csv"))
    region06 = pd.read_csv(Path("../Resources/GREY_BRUCE_OWN_SOUND.csv"))
    region07 = pd.read_csv(Path("../Resources/GUELPH_AND_DISTRICT.csv"))
    region08 = pd.read_csv(Path("../Resources/HAMILTON_BURLINGTON.csv"))
    region09 = pd.read_csv(Path("../Resources/HURON_PERTH.csv"))
    region10 = pd.read_csv(Path("../Resources/KAWARTHA_LAKES.csv"))
    region11 = pd.read_csv(Path("../Resources/KINGSTON_AND_AREA.csv"))
    region12 = pd.read_csv(Path("../Resources/KITCHENER_WATERLOO.csv"))
    region13 = pd.read_csv(Path("../Resources/LAKELANDS.csv"))
    region14 = pd.read_csv(Path("../Resources/LONDON_ST_THOMAS.csv"))
    region15 = pd.read_csv(Path("../Resources/MISSISSAUGA.csv"))
    region16 = pd.read_csv(Path("../Resources/NIAGARA_REGION.csv"))
    region17 = pd.read_csv(Path("../Resources/NORTHUMBERLAND_HILLS.csv"))
    region18 = pd.read_csv(Path("../Resources/NORTH_BAY.csv"))
    region19 = pd.read_csv(Path("../Resources/OAKVILLE_MILTON.csv"))
    region20 = pd.read_csv(Path("../Resources/OTTAWA.csv"))
    region21 = pd.read_csv(Path("../Resources/PETERBOROUGH_AND_KAWARTHAS.csv"))
    region22 = pd.read_csv(Path("../Resources/QUINTE_AND_DISTRICT.csv"))
    region23 = pd.read_csv(Path("../Resources/RIDEAU_ST_LAWRENCE.csv"))
    region24 = pd.read_csv(Path("../Resources/SAULT_STE_MARIE.csv"))
    region25 = pd.read_csv(Path("../Resources/SIMCOE_AND_DISTRICT.csv"))
    region26 = pd.read_csv(Path("../Resources/SUDBURY.csv"))
    region27 = pd.read_csv(Path("../Resources/TILLSONBURG_DISTRICT.csv"))
    region28 = pd.read_csv(Path("../Resources/WINDSOR_ESSEX.csv"))
    region29 = pd.read_csv(Path("../Resources/WOODSTOCK_INGERSOLL.csv"))

    #Take the last (Feb 2023) value for Composite Benchmark
    R01 = region01.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R02 = region02.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R03 = region03.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R04 = region04.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R05 = region05.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R06 = region06.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R07 = region07.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R08 = region08.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R09 = region09.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R10 = region10.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R11 = region11.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R12 = region12.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R13 = region13.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R14 = region14.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R15 = region15.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R16 = region16.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R17 = region17.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R18 = region18.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R19 = region19.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R20 = region20.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R21 = region21.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R22 = region22.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R23 = region23.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R24 = region24.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R25 = region25.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R26 = region26.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R27 = region27.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R28 = region28.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)
    R29 = region29.dropna().loc[:, ['Composite_Benchmark_SA']].tail(1)

    #Concatinate regional data
    all_regions = pd.concat([R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R16, R17, R18 ,R19, R20, R21, R22, R23, R24 ,R25, R26, R27, R28, R29], axis=0, keys=['R01','R02', 'R03', 'R04', 'R05', 'R06', 'R07','R08', 'R09', 'R10', 'R11', 'R12', 'R13','R14', 'R15', 'R16', 'R17', 'R18', 'R19','R20', 'R21', 'R22', 'R23', 'R24', 'R25', 'R26', 'R27', 'R28', 'R29'])
    all_regions.reset_index(drop=True, inplace=True)
    all_regions

    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")

    #Array of regional locations
    locations = [
        ["Bancroft, ontario", "Bancroft and Area"],
        ["Barrie, Ontario", "Barrie And District"], 
        ["Brantford, Ontario", "Brantford"], 
        ["Cambridge, Ontario", "Cambridge"], 
        ["Toronto, Ontario", "Greater Toronto"], 
        ["Owen Sound, Ontario", "Grey Bruce Owen Sound"], 
        ["Guelph, Ontario", "Guelph And District"], 
        ["Hamilton, Ontario", "Hamilton Burlington"], 
        ["Huron, Ontario", "Huron Perth"], 
        ["Kawartha Lakes, Ontario", "Kawartha Lakes"], 
        ["Kingston, Ontario", "Kingston And Area"], 
        ["Waterloo, Ontario", "Kitchener Waterloo"], 
        ["Muskoka, Ontario", "Lakelands"], 
        ["London, Ontario", "London St Thomas"], 
        ["Mississauga, Ontario", "Mississauga"], 
        ["Niagara region, Ontario", "Niagara Region"], 
        ["Northumberland Hills, Ontario", "Northumberland Hills"], 
        ["North Bay, Ontario", "North Bay"], 
        ["Oakville, Ontario", "Oakville Milton"], 
        ["Ottawa, Ontario", "Ottawa"], 
        ["Peterborough, Ontario", "Peterborough And Kawarthas"], 
        ["Quinte, Ontario", "Quinte And District"], 
        ["Rideau, Ontario", "Rideau St Lawrence"], 
        ["Sault Ste Marie, Ontario", "Sault Ste Marie"], 
        ["Norfolk General Hospital, Simcoe, Ontario", "Simcoe And District"], 
        ["Sudbury, Ontario", "Sudbury"],
        ["Tillsonburg, Ontario", "Tillsonburg District"] ,
        ["Windsor, Ontario", "Windsor Essex"] ,
        ["Woodstock, Ontario", "Woodstock Ingersoll"]
    ]

    # location_array = []
    # for l in locations:
    #     getLoc = loc.geocode(l[0], timeout=None)
    #     #print(getLoc.address)
    #     #print(l[1] + "," + str(getLoc.latitude) + "," + str(getLoc.longitude))
    #     location_array.append([l[1], float(getLoc.latitude), float(getLoc.longitude)])
    #     time.sleep(2.5)

    location_array = [['Bancroft and Area', 45.0570769, -77.8537127],
    ['Barrie And District', 44.3893113, -79.6901736],
    ['Brantford', 43.1408157, -80.2631733],
    ['Cambridge', 43.3600536, -80.3123023],
    ['Greater Toronto', 43.6534817, -79.3839347],
    ['Grey Bruce Owen Sound', 44.5678105, -80.9430094],
    ['Guelph And District', 43.5460516, -80.2493276],
    ['Hamilton Burlington', 43.2560802, -79.8728583],
    ['Huron Perth', 43.6406639, -81.4793923],
    ['Kawartha Lakes', 44.575616, -78.8486034],
    ['Kingston And Area', 44.230687, -76.481323],
    ['Kitchener Waterloo', 43.4652699, -80.5222961],
    ['Lakelands', 45.1307013, -79.3839611],
    ['London St Thomas', 42.9832406, -81.243372],
    ['Mississauga', 43.5896231, -79.6443879],
    ['Niagara Region', 43.0631891, -79.3098089],
    ['Northumberland Hills', 44.2156131, -77.9771027],
    ['North Bay', 46.3092115, -79.4607617],
    ['Oakville Milton', 43.447436, -79.666672],
    ['Ottawa', 45.4208777, -75.6901106],
    ['Peterborough And Kawarthas', 44.3048009, -78.3199496],
    ['Quinte And District', 44.1884744, -77.3403039],
    ['Rideau St Lawrence', 45.4263154, -75.6914553],
    ['Sault Ste Marie', 46.52391, -84.320068],
    ['Simcoe And District', 42.8353002, -80.31389770907487],
    ['Sudbury', 46.49272, -80.991211],
    ['Tillsonburg District', 42.859494, -80.7265015],
    ['Windsor Essex', 42.3167397, -83.0373389],
    ['Woodstock Ingersoll', 43.1301111, -80.7562977]]

    #location_numpy_array = np.array(location_array)
    ontario_regions_df = pd.DataFrame(location_array, columns=['Region', 'Lat', 'Long'])
    ontario_regions_df

    #Merge regional data with geolocations
    all_regions_with_coords = pd.merge(ontario_regions_df, all_regions, left_index=True, right_index=True)
    all_regions_with_coords

    #Plot most recent regional data on Ontario map
    map_plot = all_regions_with_coords.hvplot.points(
        'Long', 
        'Lat', 
        geo=True, 
        size = 'Composite_Benchmark_SA',
        scale = 0.02,
        color='Region',
        alpha=0.8,
        tiles='OSM',
        frame_width = 1000,
        frame_height = 700,
        hover_cols='all',
        title='Ontario Benchmark by Region Feb 2023',
        xlabel='Longitude',
        ylabel='Latitude'
        )

    map_plot
    st.write(hv.render(map_plot, backend='bokeh'))
