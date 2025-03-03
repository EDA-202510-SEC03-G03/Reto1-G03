import time
import csv
import DataStructures.array_list as lt
import datetime

csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {'source': None,
               'commodity': None,
               'statical_category': None,
               'unit_measurement': None,
               'location': None,
               'year_collection': None,
               'freq_collection': None,
               'reference_period': None,
               'load_time': None,
               'value': None }

    catalog['source'] = lt.new_list()
    catalog['commodity'] = lt.new_list()
    catalog['statical_category'] = lt.new_list()
    catalog['unit_measurement'] = lt.new_list()
    catalog['location'] = lt.new_list()
    catalog["year_collection"] = lt.new_list()
    catalog["freq_collection"] = lt.new_list()
    catalog["reference_period"] = lt.new_list()
    catalog["load_time"] = lt.new_list()
    catalog["value"] = lt.new_list()
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for register in input_file:
        # Se adiciona el libro a la lista de libros
        lt.add_last(catalog['source'], register["source"])
        lt.add_last(catalog['commodity'], register["commodity"])
        lt.add_last(catalog['statical_category'], register["statical_category"])
        lt.add_last(catalog['unit_measurement'], register["unit_measurement"])
        lt.add_last(catalog['location'], register["location"])
        lt.add_last(catalog['year_collection'], register["year_collection"])
        lt.add_last(catalog['freq_collection'], register["freq_collection"])
        lt.add_last(catalog['reference_period'], register["reference_period"])
        lt.add_last(catalog['load_time'], register["load_time"])
        lt.add_last(catalog['value'], register["value"])
        

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID (posicion en el csv).
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    resp = {"source": catalog['source'][id],
            "commodity": catalog['commodity'][id],
            "statical_category": catalog['statical_category'][id],
            "unit_measurement": catalog['unit_measurement'][id],
            "location": catalog['location'][id],
            "year_collection": catalog['year_collection'][id],
            "freq_collection": catalog['freq_collection'][id],
            "reference_period": catalog['reference_period'][id],
            "load_time": catalog['load_time'][id],
            "value": catalog['value'][id],
            }
    return resp


def req_1(catalog, anioB):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    """""
    fechasUltimoRegistro = ["0", "0", "0"]
    horasUltimoRegistro = ["0", "0", "0"]
    indexUR = -1
    for i in range(0, len(catalog['year_collection'])):
        registro = catalog['load_time'][i]
        fechaRegistro = str(registro[:9])
        fechasRegistro = fechaRegistro.split("-")
        horaRegistro = str(registro[10:])
        horasRegistro = horaRegistro.split(":")
        if int(catalog['year_collection'][i]) == int(anioB):
            if int(fechasRegistro[0]) > int(fechasUltimoRegistro[0]):
                if int(fechasRegistro[1]) > int(fechasUltimoRegistro[1]):
                    if int(fechasRegistro[2]) > int(fechasUltimoRegistro[2]):
                    """
    fechaUltimoRegistro = ["0001-01-01 00:00:00"]
    indexUR = -1
    for i in range(0, len(catalog['year_collection'])):
        if int(catalog['year_collection'][i]) == int(anioB):
            fechaR = catalog['load_time'][i]
            fechaDT = datetime.strptime(fechaR, "%Y-%m-%d %H:%M:%S")
            fechaURDT = datetime.strptime(fechaUltimoRegistro, "%Y-%m-%d %H:%M:%S")
            if fechaDT > fechaURDT:
                fechaUltimoRegistro = fechaR
                indexUR = i
                
    return get_data(catalog, indexUR)


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
