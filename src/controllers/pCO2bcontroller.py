from src.app import app
from flask import request, Response, redirect, url_for
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
import src.outputhtml as so
from bson.json_util import dumps
import json
import src.calls.folium as f
import pandas as pd 
from dotenv import load_dotenv
load_dotenv()
from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth,PolyLine,Element
from folium.plugins import HeatMap
import requests
from bs4 import BeautifulSoup



 
@app.route('/') 
def welcome():
    HtmlFile = open('src/welcome.html', 'r', encoding='utf-8')
    saludo = HtmlFile.read() 
    return saludo

@app.route("/prediction/direction",methods=["GET","POST"])
def mapa_walking():
    cars=pd.read_csv("./CO2Emissions_vehi.csv")
    url = 'https://gasolinabarata.info/precio-gasolina/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    tag=soup.select('.bloqueGasolina div')
    regular_gasoline= float(tag[2].text.strip().strip("€/l"))
    premium_gasoline=float(tag[5].text.strip().strip("€/l"))
    diesel=float(tag[8].text.strip().strip("€/l"))
    ethanol=float(tag[20].text.strip().strip("€/l"))
    gas_natural=float(tag[23].text.strip().strip("€/l"))

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
        mood=request.form.get('mood')
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
        mood=request.args.get('mood')
    
    prices={"X":regular_gasoline,
            "Z":premium_gasoline,
            "D":diesel,
            "E":ethanol,
            "N":gas_natural}

    if modo=="walking":
        res=f.walk(origin=origin,destination=destination,alternative=modo) 
        distancia=f.hi_google(origin=origin,destination=destination,alternative="driving")
        distancia=distancia[0]
        co2=cars[(cars["Make"]==marca) & (cars["Model"]==modelo) & (cars["Fuel Type"]==fuel)]
        save=round((co2["Fuel Consumption City (L/100 km)"].mean()/100)*prices[fuel]*distancia,2)
        corrco2=co2["CO2 Emissions(g/km)"].sum()
        if corrco2==0:
            co2=cars[(cars["Make"]==marca)&(cars["Fuel Type"]==fuel)]
            co2=round((co2["CO2 Emissions(g/km)"].mean())*distancia,3)
            return so.html_walk(res=res,co2=co2,mood=mood,fuel=save)
    
        else:
            co2=co2
            co2=round((co2["CO2 Emissions(g/km)"].mean())*distancia,3)
            return so.html_walk(res=res,co2=co2,mood=mood,fuel=save)

    if modo=="driving":
        res=f.walk(origin=origin,destination=destination,alternative=modo) 
        distancia=f.hi_google(origin=origin,destination=destination,alternative="driving")
        distancia=distancia[0]
        co2=cars[(cars["Make"]==marca) & (cars["Model"]==modelo) & (cars["Fuel Type"]==fuel)]
        save=round((co2["Fuel Consumption City (L/100 km)"].mean()/100)*prices[fuel]*distancia,2)
        corrco2c=co2["CO2 Emissions(g/km)"].sum()
        if corrco2c==0:
            co2=cars[(cars["Make"]==marca)&(cars["Fuel Type"]==fuel)]
            co2=round((co2["CO2 Emissions(g/km)"].mean())*distancia,3)
            return so.html_driving(res=res,co2=co2,mood=mood,fuel=save)
    
        else:
            co2=co2
            co2=round((co2["CO2 Emissions(g/km)"].mean())*distancia,3)
            return so.html_driving(res=res,co2=co2,mood=mood,fuel=save)
    if modo=="bicycling":
        res=f.bicycling(origin=origin,destination=destination,alternative=modo) 
        distancia=f.hi_google(origin=origin,destination=destination,alternative="driving")
        distancia=distancia[0]
        co2=cars[(cars["Make"]==marca) & (cars["Model"]==modelo) & (cars["Fuel Type"]==fuel)]
        save=round((co2["Fuel Consumption City (L/100 km)"].mean()/100)*prices[fuel]*distancia,2)
        corrco2=co2["CO2 Emissions(g/km)"].sum()

        if corrco2==0:
            co2=cars[(cars["Make"]==marca)&(cars["Fuel Type"]==fuel)]
            co2=round((co2c["CO2 Emissions(g/km)"].mean())*distancia,3)
            return so.html_bike(res=res,co2=co2,mood=mood,fuel=save)
    
        else:
            co2=co2
            co2=round((co2["CO2 Emissions(g/km)"].mean())*distancia,3)
            return so.html_bike(res=res,co2=co2,mood=mood,fuel=save)
        
        



    


