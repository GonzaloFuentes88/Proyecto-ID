import requests
from data import db,cliente

KEY = "2413980055a8cf0ac036aab4997a7798"
URL_PROVINCIA = "https://apis.datos.gob.ar/georef/api/provincias"
URL_LOCALIDAD="https://apis.datos.gob.ar/georef/api/municipios?provincia"
URL_CLIMA = "https://api.openweathermap.org/data/2.5/weather?q={}&appid="+KEY+"&units=metric&lang=es"

def save_localidades(provincia):
    url = URL_LOCALIDAD+'='+provincia
    respuesta = requests.get(url)
    list_localidades = []
    #creo una coleccion con las los municipios asociado a cada provinca en la url
    col_localidades = db['localidades']
    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        for localidad in respuesta_json["municipios"]:
            list_localidades.append(localidad)
            
        #verifico que se hayan encontrado localidades
        if len(list_localidades)> 0:
            col_localidades.insert_many(list_localidades)

def save_provincias():
    respuesta = requests.get(URL_PROVINCIA)
    #creo una coleccion con las provincias obtenidas en la url
    col_provincias = db['provincias']
    list_provincias = []
    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        for provincia in respuesta_json["provincias"]:
            list_provincias.append(provincia)
        col_provincias.insert_many(list_provincias)
        
    for documento in col_provincias.find({}):
            save_localidades(documento['nombre'])
            
    
def save_clima_in_DB(localidad):
    respuesta = requests.get(URL_CLIMA.format(localidad))
    #creo una coleccion con las provincias obtenidas en la url
    col_clima = db['clima']
    list_clima = []
    if respuesta.status_code == 200:
        data = respuesta.json()
        temp = data["main"]["temp"]
        list_clima.append(temp)
        col_clima.insert_many(temp)
        

def obtener_clima(localidad):
    query="{\"provincia.nombre\":\""+localidad+"\"}"
    col = cliente["provincias"]
    doc = col.find(query)
    for x in doc:
        print(x)
    if(localidad):
        print("is not valid")
    
    respuesta = requests.get(URL_CLIMA.format(localidad))
    if(respuesta.status_code==200):        
        data = respuesta.json()
        temp = data["main"]["temp"]
        vel_viento = data["wind"]["speed"]

        latitud = data["coord"]["lat"]
        longitud = data["coord"]["lon"]

        descripcion = data["weather"][0]["description"]

        print("Tempreratura: ", temp)
        print("Velocidad del viento: {} m/s".format(vel_viento))
        print("Latitud: {}".format(latitud))
        print("Longitud: {}".format(longitud))
        print("Descripción: {}".format(descripcion))
    else:
        print(respuesta.status_code)



