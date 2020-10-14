import requests
import os
from dotenv import load_dotenv
load_dotenv()
import json
import re
from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth,PolyLine,Element
from folium.plugins import HeatMap
from src.database import db
from bson.json_util import dumps



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

def walk(origin, destination,alternative):
    """
    Recoge las cordenadas y dibuja el mapa con direcciones
    (andando)
    """
    coordenadas=hi_google(origin,destination,alternative)
    distancia=coordenadas[0]
    mapa = Map(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]],zoom_start=14)
    chincheta2 = Marker(location=[coordenadas[1]["lat"],coordenadas[1]["lng"]], tooltip="origen", popup="o")
    chinchetad= Marker(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]], tooltip="destino", popup="d")
    chincheta2.add_to(mapa)
    chinchetad.add_to(mapa)
    PolyLine(coordenadas[3], color="red", weight=2.5, opacity=1).add_to(mapa)  
    return mapa

    
def waypoints(origin,destination,alternative):
    
    """
    Hace la llamada a la api de Google directions
    """
    
    address=hi_google(origin,destination,alternative="bicycling")
    stopsdest=db.bicimad.find({"coordinates": {"$geoWithin": { "$centerSphere":  [ [address[2]["lng"],address[2]["lat"]], 0.00007885743614075527 ]}}}).limit(1)
    stopsorig=db.bicimad.find({"coordinates": {"$geoWithin": { "$centerSphere":  [ [address[1]["lng"],address[1]["lat"]], 0.00007885743614075527 ]}}}).limit(1)
    wpsneardest=[]
    wpsnearorig=[]
    for i in stopsdest:
        wpsneardest.append(i)
    for i in stopsorig:
        wpsnearorig.append(i)
    wpsneardest=wpsneardest[0]["address"]
    wpsnearorig=wpsnearorig[0]["address"]

    load_dotenv()
    apiKey=os.getenv("APIkeyGoogle")
    origin=origin.replace(" ","+")
    destination=destination.replace(" ","+")
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&region=es&mode=bicycling&waypoints=via:{wpsnearorig}|via:{wpsneardest}&key={apiKey}"
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

    
def bicycling(origin,destination,alternative="bicycling"):
    
    """
    Recoge las cordenadas y dibuja el mapa con direcciones
    (en bici)
    """ 
    
    coordenadas=waypoints(origin=origin,destination=destination,alternative="bicycling")
    stopsdest=db.bicimad.find({"coordinates": {"$geoWithin": { "$centerSphere":  [ [coordenadas[2]["lng"],coordenadas[2]["lat"]], 0.00007885743614075527 ]}}}).limit(1)
    stopsorig=db.bicimad.find({"coordinates": {"$geoWithin": { "$centerSphere":  [ [coordenadas[1]["lng"],coordenadas[1]["lat"]], 0.00007885743614075527 ]}}}).limit(1)
    wpsneardest=[]
    wpsnearorig=[]
    for i in stopsdest:
        wpsneardest.append(i)
    for i in stopsorig:
        wpsnearorig.append(i)
    wpsneardest=wpsneardest[0]["coordinates"]
    wpsnearorig=wpsnearorig[0]["coordinates"]
    mapa = Map(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]],zoom_start=14)
    chincheta2 = Marker(location=[coordenadas[1]["lat"],coordenadas[1]["lng"]], tooltip="origen", popup="o")
    chinchetad= Marker(location=[coordenadas[2]["lat"],coordenadas[2]["lng"]], tooltip="destino", popup="d")
    bicimador=Marker(location=[wpsnearorig[1],wpsnearorig[0]], tooltip="orbici", popup="bo",icon=Icon(icon='heart',color='#f7b5f5'))
    bicimaddest=Marker(location=[wpsneardest[1],wpsneardest[0]], tooltip="destbici", popup="bd",icon=Icon(icon="heart",color="#f7b5f5"))
    chincheta2.add_to(mapa)
    chinchetad.add_to(mapa)
    bicimador.add_to(mapa)
    bicimaddest.add_to(mapa)
    PolyLine(coordenadas[3], color="red", weight=2.5, opacity=1).add_to(mapa)
    return mapa
    




