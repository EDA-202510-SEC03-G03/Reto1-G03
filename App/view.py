import sys
from App import logic as l
from DataStructures import array_list as lt


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog = l.new_logic() 
    
    return catalog

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data, counter = l.load_data(control, "Data/agricultural-20.csv") 
    print("Carga de datos completada.")
    print("")
    print("Total de registros cargados: " + str(counter))
    print("Menor año de recoleccion: " + str(l.menor_anio(control)))
    print("Mayor anio de recoleccion: " + str(l.mayor_anio(control)))
    print("")
    print("")
    print("La información de los primeros 5 registros son: ")
    print("")
    for i in range(5):
        print_data(control, i)
        print("")
        
    print("")
    print("")
    print("La información de los últimos 5 registros son: ")
    print("")
    for i in range(5):
        print_data(control, counter - 1 - i)
        print("")
    #primeros, ultimos = l.primerosYUltimos(control)
    #for regsitro in primeros:
    #    print_data(control, )
    
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    e = l.get_data(control, id)
    print("Para el registro indicado la informacion es: ")
    print("El anio de recolección fue: " + e["year_collection"])
    print("La fecha de carga del registro fue: " + e["load_time"])
    print("La frecuencia de recopilación del registro fue: " + e["freq_collection"])
    print("El nombre del departamento del registro fue: " + e["state_name"])
    print("El tipo de fuente/origen del registro fue: " + e["source"])
    print("La unidad de medición del registro es: " + e["unit_measurement"])
    print("El valor de la medición del registro es: " + e["value"])
    print("El tipo de producto del registro es : " + e["commodity"])
    

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    anio_buscado = input('Ingrese el anio buscado: ')
    i_resp, tiempo = l.req_1(control, anio_buscado)
    if i_resp == -1:
        print("Anio no encontrado.")
    else:
        print_data(control, i_resp)
        print("El tiempo de ejecución en milisegundo fue de: " + str(round(tiempo, 3)))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    dep_buscado = input('Ingrese el departamento buscado: ')
    i_resp, tiempo = l.req_2(control, dep_buscado)
    if i_resp == -1:
        print("Anio no encontrado.")
    else:
        print_data(control, i_resp)
        print("El tiempo de ejecución en milisegundo fue de: " + str(round(tiempo, 3)))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    nombre_departamento = input("Ingrese el nombre del departamento: ")
    year_inicio = int(input("Ingrese el año de inicio: "))
    year_final = int(input("Ingrese el año de final: "))
    
    registros = l.req_3(control, nombre_departamento, year_inicio, year_final)
    print("Tiempo de ejecución:", "tiempo_ejecucion")
    print("Total registros:", "total_registros")
    print("Total SURVEY:", "total_survey")
    print("Total CENSUS:", "total_census")
    print("Registros:")
    for registro in registros["Registros"]:
        print(registro)

    

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    producto = input("Ingrese el tipo de producto: ")
    anio_inicio = int(input("Ingrese el año de inicio: "))
    anio_fin = int(input("Ingrese el año de fin: "))
    
    resultado = l.req_4(control, producto, anio_inicio, anio_fin)
    
    print("Tiempo de ejecución (ms):", round(resultado["Tiempo de ejecución (ms)"], 3))
    print("Total registros:", resultado["Total registros"])
    print("Total SURVEY:", resultado["Total SURVEY"])
    print("Total CENSUS:", resultado["Total CENSUS"])
    print("Registros:")
    for registro in resultado["Registros"][:5] + resultado["Registros"][-5:] if len(resultado["Registros"]) > 20 else resultado["Registros"]:
        print(registro)

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    cat = input("Ingrese la categoría estadística buscada: ")
    anioI = input("Ingrese el año inicial del periodo a consultar: ")
    anioF = input("Ingrese el año final del periodo a consultar: ")
    lista_indices, tamanio, census, surveys, tiempo = l.req_5(control, cat, anioI, anioF)
    print("")
    print("El número total de registros es: " + str(tamanio))
    print("")
    print("El número total de registros SURVEY es: " + str(surveys))
    print("")
    print("El número total de registros CENSUS es: " + str(census))
    print("")
    
    if tamanio > 20: 
         print("La información de los primeros 5 registros son: ")
         print("")
         for i in range(5):
            print_data(control, lt.get_element(lista_indices, i))
            print("")
        
         print("")
         print("")
         print("La información de los últimos 5 registros son: ")
         print("")
         for i in range(5):
            print_data(control, lt.get_element(lista_indices, tamanio - 1 - i))
            print("")
    else:
        for i in range(tamanio):
            print_data(lista_indices, i)
            
    print("El tiempo de ejecución en milisegundo fue de: " + str(round(tiempo, 3)))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    nombre_departamento = input("Ingrese el nombre de un departamento: ")
    initial_date = int(input("Ingrese la fecha inicial: "))
    final_date = int(input("Ingrese la fecha final: "))
    
    registros = l.req_6(control, nombre_departamento, initial_date, final_date)
    
    print("Tiempo de ejecución (ms):", registros["Tiempo de ejecución (ms)"])
    print("Total registros:", registros["Total registros"])
    print("Total SURVEY:", registros["Total SURVEY"])
    print("Total CENSUS:", registros["Total CENSUS"])
    print("Registros:")
    for registro in registros["Registros"]:
        print(registro)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    departamento = input("Ingrese el nombre de un departamento: ")
    initial_date = int(input("Ingrese la fecha inicial: "))
    final_date = int(input("Ingrese la fecha final: "))

    resultado = l.req_7(control, departamento, initial_date, final_date)

    print("\nTiempo de ejecución (ms):", resultado["execution_time_ms"])
    print("Número total de registros que cumplieron el filtro:", resultado["total_records"])
    print("Número de registros con unidad de medida no válida:", resultado["invalid_unit_count"])
    print("Número de registros con fuente 'SURVEY':", resultado["survey_count"])
    print("Número de registros con fuente 'CENSUS':", resultado["census_count"])

    print("\n🔹 Período con MAYOR ingreso:")
    print("Año de recopilación:", resultado["max_income_period"]["year"])
    print("Tipo de período: MAYOR")
    print("Valor de ingresos:", resultado["max_income_period"]["income"])

    print("\n🔹 Período con MENOR ingreso:")
    print("Año de recopilación:", resultado["min_income_period"]["year"])
    print("Tipo de período: MENOR")
    print("Valor de ingresos:", resultado["min_income_period"]["income"])


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(data)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
