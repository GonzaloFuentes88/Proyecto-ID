import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    print("Conexion exitosa")
    db = cliente['argentina']
    db.drop_collection('provincias')
    db.drop_collection('localidades')
    db.drop_collection('clima')
    cliente.close
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo de error"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Connection failure"+errorConexion)
