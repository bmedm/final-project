import requests
import os
from dotenv import load_dotenv
load_dotenv()
import json
import re
from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth,PolyLine,Element
from folium.plugins import HeatMap

def hi_google(origin,destination,alternative):
    """
    Hace la llamada a la api de Google directions
    """
    load_dotenv()
    apiKey=os.getenv("APIkeyGoogle")
    origin=origin.replace(" ","+")
    destination=destination.replace(" ","+")
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&region=es&mode={alternative}&key={apiKey}"
    res = requests.get(url)
    data = res.json()

    distancia=data["routes"][0]["legs"][0]["distance"]["text"]
    distancia=distancia.split(" km")
    distancia=float(distancia[0])
    destino_coor=data["routes"][0]["legs"][0]["end_location"]
    origen_coor=data["routes"][0]["legs"][0]["start_location"]
    
    trayecto=[]
    for i in data["routes"][0]["legs"][0]["steps"]:
        trayecto.append(i["start_location"])
    trayecto=[(i["lat"],i["lng"]) for i in trayecto]
    trayecto.insert(0,(origen_coor["lat"],origen_coor["lng"]))
    trayecto.append((destino_coor["lat"],destino_coor["lng"]))

    return distancia, origen_coor, destino_coor, trayecto

def walk(origin, destination,alternative="walking"):
    coordenadas=hi_google(origin,destination,alternative)
    distancia=coordenadas[0]
    mapa = Map(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]],zoom_start=12)
    chincheta2 = Marker(location=[coordenadas[1]["lat"],coordenadas[1]["lng"]], tooltip="origen", popup="o")
    chinchetad= Marker(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]], tooltip="destino", popup="d")
    chincheta2.add_to(mapa)
    chinchetad.add_to(mapa)
    PolyLine(coordenadas[3], color="red", weight=2.5, opacity=1).add_to(mapa)  
    return mapa

   

def bicycling(origen,destino,alternativa="bicycling"):
    mapa = Map(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]],zoom_start=12)
    coor=[]
    for i in db.bicimad:
        coor.append(i)
    chincheta2 = Marker(location=[coordenadas[1]["lat"],coordenadas[1]["lng"]], tooltip="origen", popup="o")
    chinchetad= Marker(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]], tooltip="destino", popup="d")
    chincheta2.add_to(mapa)
    return mapa


