from src.app import app
from flask import request, Response, redirect, url_for
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps
import json
import webbrowser
import src.calls.folium as f
import pandas as pd 
from dotenv import load_dotenv
load_dotenv()
from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth,PolyLine,Element
from folium.plugins import HeatMap
import pandas as pd


 
@app.route('/') 
def welcome():
    HtmlFile = open('src/welcome.html', 'r', encoding='utf-8')
    saludo = HtmlFile.read() 
    return saludo

@app.route("/prediction/direction",methods=["GET","POST"])
def mapa_walking():
    cars=pd.read_csv("./CO2Emissions_vehi.csv")
    fueltypes={"Premium gasoline":"Z", 
            "Regular gasoline":"X",
            "Diesel":"D",
            "Ethanol": "E",
            "Natural gas":"N"
            }
    if request.method=="POST":
        origin=request.form.get('origin')
        destination=request.form.get('destination')
        modo=request.form.get('mode')
        marca=request.form.get('Make')
        modelo=request.form.get("model")
        fueltype=request.form.get("Fuel")
        if fueltype:
            fuel=fueltypes[fueltype]
        else:
            fuel="D"
        
    else:
        origin=request.args.get('origin')
        destination=request.args.get('destination')
        marca=request.args.get('Make')
        modelo=request.args.get("Model")
        fueltype=request.args.get("Fuel")
    if modo=="walking":
        res=f.walk(origin=origin,destination=destination,alternative=modo) 
        distancia=f.hi_google(origin=origin,destination=destination,alternative=modo)
        distancia=distancia[0]
        co2=cars[(cars["Make"]=="HYUNDAI") & (cars["Model"]=="ACCENT") & (cars["Fuel Type"]=="X")]
        corrco2=co2["CO2 Emissions(g/km)"].sum()
        if corrco2==0:
            co2=cars[(cars["Make"]=="HYUNDAI")&(cars["Fuel Type"]=="X")]
            co2=(co2["CO2 Emissions(g/km)"].mean())*distancia
            return res._repr_html_()
    
        else:
            co2=co2
            co2=(co2["CO2 Emissions(g/km)"].mean())*distancia
            return res._repr_html_()

    


