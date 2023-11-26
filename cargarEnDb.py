import requests
from conectarDb import db
from registrarActividad import registrarActividad


KEY = "2413980055a8cf0ac036aab4997a7798"
URL_PROVINCIA = "https://apis.datos.gob.ar/georef/api/provincias"
URL_LOCALIDAD="https://apis.datos.gob.ar/georef/api/municipios?provincia"
URL_CLIMA = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid="+KEY+"&units=metric&lang=es"

def save_localidades(provincia):
    #creo una coleccion con las los municipios asociado a cada provinca en la url
    col_localidades = db['localidades']
    url = URL_LOCALIDAD+'='+provincia
    list_localidades = []
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        for localidad in respuesta_json['municipios']:
            lat = localidad['centroide']['lat']
            lon = localidad['centroide']['lon']
            id = localidad['id']
            nombre = localidad['nombre']
            idProv = localidad['provincia']['id']
            nombreProv= localidad['provincia']['nombre']
            list_localidades.append({"_id": id,"nombre": nombre,"centroide": {"lat": lat,"lon": lon},"provincia": {"id": idProv,"nombre": nombreProv}})
        
        if len(list_localidades)> 0:
            col_localidades.insert_many(list_localidades)
            registrarActividad("Se insertaron las Localidades de la provincia "+provincia+" en la Base de datos")
    for documento in list_localidades:
        save_clima_in_DB(documento)

def save_provincias():
    col_provincias = db['provincias']
    respuesta = requests.get(URL_PROVINCIA)
    list_provincias = []
    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        for provincia in respuesta_json["provincias"]:
            id = provincia['id']
            nombre = provincia['nombre']
            lat = provincia['centroide']['lat']
            lon = provincia['centroide']['lon']
            list_provincias.append({'_id': id,'nombre':nombre, 'centroide':{'lat':lat,'lon':lon}})
        col_provincias.insert_many(list_provincias)
    registrarActividad("Se insertaron las Provincias en la Base de datos : Total "+str(len(list_provincias)))
    for documento in list_provincias:
        save_localidades(documento['nombre'])
            
    
def save_clima_in_DB(documento):
    col_clima = db['climas']
    lat = documento["centroide"]["lat"]
    lon= documento["centroide"]["lon"]
    
    respuesta = requests.get(URL_CLIMA.format(lat,lon))
    if(respuesta.status_code==200):        
        data = respuesta.json()
        temp = data["main"]["temp"]
        vel_viento = data["wind"]["speed"]
        descripcion = data["weather"][0]["description"]
        humedad = data['main']['humidity']
        temperatura = {'localidadId':documento['_id'], 'clima':{'cielo':descripcion,'humedad':humedad,'velocidad viento':vel_viento,'temperatura':temp}}
        col_clima.insert_one(temperatura)
        registrarActividad("Se insertaron el clima de la localidad "+documento["nombre"])
    
    
        

