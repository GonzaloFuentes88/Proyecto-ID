from consume import save_provincias, obtener_clima

if __name__=='__main__':
    save_provincias()
    localidad = input("Ingrese la localidad: ")
    obtener_clima(localidad)
    while localidad != "0":
        localidad = input("Ingrese la localidad: ")
        obtener_clima(localidad)
    print("Finalizando...")