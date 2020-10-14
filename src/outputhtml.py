
import pandas as pd

def html_normal(res,co2,mood):
    aviones=pd.read_csv("./aviones.csv")
    travel=aviones[aviones["Estilo"]==mood]
    travel=travel.sample(3)
    avco2=[i for i in travel["CO2/pass"]]
    avurl=[i for i in travel["url"]]
    avdest=[i for i in travel["Destino"]]
  

    return f"""<!DOCTYPE html>
            <html lang="es">
            <head>
            <meta charset="utf-8">
            <title>PiggyCO2bank</title>
            <link rel="icon"type="image/png" href="https://cdn4.iconfinder.com/data/icons/business-economy-market-company-filling-wiht-beaut/283/69-512.png">
            </head>
           <body style="margin:50px;text-align:center; background:#cff6fd; 
            background-image:url('https://i.pinimg.com/originals/39/dd/63/39dd637ade2a7f5d4a3b74c0664be29a.jpg');
            background-repeat:no-repeat ;
            background-size: 100% 100%;
            color:#000000;
            font-family:monospace,arial,helvética; ">
                    <h1 style="color:#eeb8ec;font-family:copperplate; font-size: 50px; "><code>Piggy<big>|CO2|</big>bank</code></h1>
                </td>
            </tr>
            <tr>
                <td colspan="2" style="padding:4px; background-color:whitesmoke; text-align:center;">
                    <p><b>How much are you going to save the planet?</b></p>
                </td>
            </tr>
            </table>
            <div style="text-align:center;">
                <table style="margin: 0 auto;" cellspacing="100">
                    <tr>
                        <td>
                            <h1>You save:{co2} g of CO2<h1>
                        </td>
                        <td>
                            <h1>{res._repr_html_()}<h1>
                        </td>
                    </tr>
            </table>
    
            <h1 style="color:#e2748c;font-family:arial; font-size: 50px; ">You might be interested in traveling to...</h1>
            <table style="margin: 0 auto;" cellspacing="40">
                <tr>
                    <td>
                        <h1 style="color:#f1c40f;font-family:arial; font-size: 50px;">{avdest[0]}<h1>
                    </td>
                    <td>
                        <h1 style="color:#f1c40f;font-family:arial font-size: 50px;" >{avdest[1]}<h1>
                    </td>
                    <td>
                        <h1 style="color:#f1c40f;font-family:arial; font-size: 50px; ">{avdest[2]}<h1>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img width="300" height="300" src="{avurl[0]}" alt="travel">
                    </td>
                    <td>
                        <img width="300" height="300" src="{avurl[1]}" alt="travel">
                    </td>
                    <td>
                        <img width="300" height="300" src="{avurl[2]}" alt="travel">
                    </td>
                </tr>
                <tr>
                    <td>
                        <h2 style="color:#252525;font-family:arial; font-size: 20px;" >Equivale a {int((avco2[0]/co2)+1)} veces este mismo trayecto en gasto de CO2 en avión<h2>
                    </td>
                    <td>
                        <h2 style="color:#252525;font-family:arial; font-size: 20px;" >Equivale a {int((avco2[1]/co2)+1)} veces este mismo trayecto en gasto de CO2 en avión<h2>
                    </td>
                    <td>
                        <h2 style="color:#252525;font-family:arial; font-size: 20px;" >Equivale a {int((avco2[2]/co2)+1)} veces este mismo trayecto en gasto de CO2 en avión<h2>
                    </td>
                </tr>
            </table>
            </div>
            </body>
            </html>"""

def html_driving(res,co2,mood):
    aviones=pd.read_csv("./aviones.csv")
    travel=aviones[aviones["Estilo"]==mood]
    travel=travel.sample(3)
    avco2=[i for i in travel["CO2/pass"]]
    avurl=[i for i in travel["url"]]
    avdest=[i for i in travel["Destino"]]
  

    return f"""<!DOCTYPE html>
            <html lang="es">
            <head>
            <meta charset="utf-8">
            <title>PiggyCO2bank</title>
            <link rel="icon"type="image/png" href="https://cdn4.iconfinder.com/data/icons/business-economy-market-company-filling-wiht-beaut/283/69-512.png">
            </head>
           <body style="margin:50px;text-align:center; background:#cff6fd; 
            background-image:url('https://i.pinimg.com/originals/39/dd/63/39dd637ade2a7f5d4a3b74c0664be29a.jpg');
            background-repeat:no-repeat ;
            background-size: 100% 100%;
            color:#000000;
            font-family:monospace,arial,helvética; ">
                    <h1 style="color:#eeb8ec;font-family:copperplate; font-size: 50px; "><code>Piggy<big>|CO2|</big>bank</code></h1>
                </td>
            </tr>
            <tr>
                <td colspan="2" style="padding:4px; background-color:whitesmoke; text-align:center;">
                    <p><b>How much are you going to save the planet?</b></p>
                </td>
            </tr>
            </table>
            <div style="text-align:center;">
                <table style="margin: 0 auto;" cellspacing="100">
                    <tr>
                        <td>
                            <h1>ARE YOU SURE???: you are emitting {co2}g of CO2 to the planet</h1>
                        </td>
                        <td>
                            <h1>{res._repr_html_()}<h1>
                        </td>
                    </tr>
            </table>
    
            <h1 style="color:#e2748c;font-family:arial; font-size: 50px; ">You might be interested in traveling to...</h1>
            <table style="margin: 0 auto;" cellspacing="40">
                <tr>
                    <td>
                        <h1 style="color:#f1c40f;font-family:arial; font-size: 50px;">{avdest[0]}<h1>
                    </td>
                    <td>
                        <h1 style="color:#f1c40f;font-family:arial font-size: 50px;" >{avdest[1]}<h1>
                    </td>
                    <td>
                        <h1 style="color:#f1c40f;font-family:arial; font-size: 50px; ">{avdest[2]}<h1>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img width="300" height="300" src="{avurl[0]}" alt="travel">
                    </td>
                    <td>
                        <img width="300" height="300" src="{avurl[1]}" alt="travel">
                    </td>
                    <td>
                        <img width="300" height="300" src="{avurl[2]}" alt="travel">
                    </td>
                </tr>
                <tr>
                    <td>
                        <h2 style="color:#252525;font-family:arial; font-size: 20px;" >Equivale a {int((avco2[0]/co2)+1)} veces este mismo trayecto en gasto de CO2 en avión<h2>
                    </td>
                    <td>
                        <h2 style="color:#252525;font-family:arial; font-size: 20px;" >Equivale a {int((avco2[1]/co2)+1)} veces este mismo trayecto en gasto de CO2 en avión<h2>
                    </td>
                    <td>
                        <h2 style="color:#252525;font-family:arial; font-size: 20px;" >Equivale a {int((avco2[2]/co2)+1)} veces este mismo trayecto en gasto de CO2 en avión<h2>
                    </td>
                </tr>
            </table>
            </div>
            </body>
            </html>"""