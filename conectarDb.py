import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

try:
    cliente=pymongo.MongoClient(MONGO_URI)
    print("Conexion exitosa")
    db = cliente['argentina']
    db.drop_collection('provincias')
    db.drop_collection('localidades')
    db.drop_collection('climas')
except:
    print("Error al conectar")
