import os
from datetime import datetime

def registrarActividad(actividad): 
    archivo = open(os.getcwd() + './actividad.txt', 'a', encoding = 'utf-8')
    archivo.write(f"- {datetime.now()}: " + actividad + "\n")
    archivo.close()

registrarActividad('Hola')