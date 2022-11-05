"""


"""

import os
import json
import fiona
import folium
import pandas as pd
import branca as bc
import seaborn as sns
import geopandas as gpd
from datetime import date
from folium import plugins


def add_lyr_aprm(path):
    # Input
    gdf = gpd.read_file(os.path.join(path, '01_aprm.gpkg'))
    gdf = gdf.to_crs(epsg=4326)

    # Popup
    #gdf['popup'] = gdf.apply(popup_html_est_aut_empresas, axis=1)

    # Layer
    lyr = folium.GeoJson(
        gdf,
        name='APRMs',
        smooth_factor=1.0,
        style_function=lambda x: {
            'fillColor': '#DC143C',
            'color': '#DC143C',
            'weight': 1,
            'fillOpacity': 0.3,
        },
        highlight_function=lambda x: {
            'weight': 3,
            'fillOpacity': 0.6,
        },
        # popup=folium.GeoJsonPopup(
        #     ['popup'],
        #     parse_html=False,
        #     max_width='400',
        #     show=False,
        #     labels=False,
        #     sticky=True,
        # ),
        # marker=folium.Marker(
        #     icon=folium.Icon(
        #         color='lightgray',
        #         icon_color='#FFFF00',
        #         #icon='leaf',
        #     ),
        # ),
        tooltip=folium.GeoJsonTooltip(
            fields=['Manancial'],
            aliases=['Manancial'],
            sticky=True,
            opacity=0.9,
            direction='right',
        ),
        embed=False,
        zoom_on_click=False,
        control=True,
        show=True,
    )
    return lyr


# PopUp
def popup_html_est_aut_empresas(row):
    # Data
    nome = row['Nome']
    posto = row['Posto']
    url_1 = row['url']
    url_2 = row['url_mapa']
    url_3 = row['url_infoposto']

    # Infos
    return f"""
    <div>
    <h5>{nome}</h5>
    <br>Posto: <b>{posto}</b>
    <br><a href="{url_1}" target="_blank">url - dados</a></b>
    <br><a href="{url_2}" target="_blank">url - mapa</a></b>
    <br><a href="{url_3}" target="_blank">url - infoposto</a></b>
    </div>
    """



if __name__ == '__main__':
    pass
