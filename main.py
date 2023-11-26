from cargarEnDb import save_provincias
from conectarDb import cliente
from busqueda import buscarPorProv,buscarPorLoc
from registrarActividad import registrarActividad

if __name__=='__main__':
    print("El programa va a cargar los datos a la base de datos")
    print("Esto puede demorar un tiempo")
    
    registrarActividad("Se inicia el programa...")
    
    save_provincias()
    
    opcion = "-1"
    while opcion != "0" :
        print("Opcion 0 para finalizar ejecucion")
        print("Opcion 1 para finalizar obtener por provincia")
        print("Opcion 2 para finalizar obtener por localidad")
        opcion = input("Ingrese la opcion: ")
    
        if opcion == "1" :
            provName = input("Ingrese la provincia: ")
            buscarPorProv(provName)
        elif opcion == "2" :
            locName = input("Ingrese la localidad: ")
            buscarPorLoc(locName)
        elif opcion == "0" :
            cliente.close()
            print("Finalizando ejecucion....")
        else : 
            print("Opcion invalida")
    #btener_clima(localidad)
    #while localidad != "0":
     #   localidad = input("Ingrese la localidad: ")
      #  obtener_clima(localidad)
    #print("Finalizando...")