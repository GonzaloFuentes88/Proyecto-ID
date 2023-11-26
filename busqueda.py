from conectarDb import db
from registrarActividad import registrarActividad


def buscarPorProv(provName):
    try:
        col_provincias = db['provincias']
        col_climas = db['climas']
        col_localidad = db['localidades']
        prov = col_provincias.find_one({"nombre":provName})
        idProv = prov['_id']
        localidades = col_localidad.find({"provincia.id":idProv})
        nombreProv = prov['nombre']
    
        respLoc = []
        for loc in localidades:
            idLoc = loc['_id']
            clim = col_climas.find_one({"localidadId":idLoc})
            nombreLoc = loc["nombre"]
            cielo=clim["clima"]["cielo"]
            humedad=clim["clima"]["humedad"]
            velocidad_viento=clim["clima"]["velocidad viento"]
            temperatura=clim["clima"]["temperatura"]
            
            respAux =  {
                "nombre":nombreLoc,
                "clima":{
                    "cielo":cielo,
                    "humedad":humedad,
                    "velocidad viento": velocidad_viento,
                    "temperatura":temperatura
                }
            }
            respLoc.append(respAux)
    
        res = {
            "provincia" : nombreProv,
            "localidades": respLoc
        }
    
        registrarActividad("Provincia encontrada: "+str(res))
        print(res)
    except:
        print("Se ha producido un error, verifique el nombre de la provincia")
    
    
def buscarPorLoc(locName):
    try:
        col_localidades = db['localidades']
        col_climas = db['climas']
        loc = col_localidades.find_one({"nombre":locName})
        id = loc['_id']
        clim = col_climas.find_one({"localidadId":id})
    
        nombreLoc = loc["nombre"]
        nombreProv = loc["provincia"]["nombre"]
        cielo=clim["clima"]["cielo"]
        humedad=clim["clima"]["humedad"]
        velocidad_viento=clim["clima"]["velocidad viento"]
        temperatura=clim["clima"]["temperatura"]
    
        resp = {
            "provincia" : nombreProv,
            "localidad" : {
                "nombre":nombreLoc,
                "clima":{
                    "cielo":cielo,
                    "humedad":humedad,
                    "velocidad viento": velocidad_viento,
                    "temperatura":temperatura
                }
            }
        }
    
        registrarActividad("Localidad encontrada: "+str(resp))
        print(resp)
    except:
        print("Se ha producido un error, verifique el nombre de la localidad")