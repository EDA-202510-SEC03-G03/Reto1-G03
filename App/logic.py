import time
import csv
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures import array_list as lt

from datetime import datetime
csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {'registros': None}

    catalog["registros"] = lt.new_list()
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    counter = 0
    for register in input_file:
        lt.add_last(catalog["registros"], register)
        counter +=1

    return catalog, counter

# Funciones de consulta sobre el catálogo

def menor_anio(catalog):
    
    menor_anio = int(lt.first_element(catalog["registros"])["year_collection"])
    for i in range(lt.size(catalog["registros"])):
        anio = int(lt.get_element(catalog["registros"], i)["year_collection"])  
        if anio < menor_anio:
            menor_anio = anio  
            
    return menor_anio

def mayor_anio(catalog):
    
    mayor_anio = int(lt.first_element(catalog["registros"])["year_collection"])
    for i in range(lt.size(catalog["registros"])):
        anio = int(lt.get_element(catalog["registros"], i)["year_collection"])  
        if anio > mayor_anio:
            mayor_anio = anio  
            
    return mayor_anio

"""
def primerosYUltimos(catalog):
    primeros = lt.new_list()
    ultimos = lt.new_list()
    
    for i in range(0, 5):
        lt.add_last(primeros, get_data(catalog, i))
        lt.add_last(ultimos, get_data(catalog, len(catalog)-1-i))
        
    return primeros, ultimos
    """

def get_data(catalog, id):
    """
    Retorna un dato por su ID (posicion en el csv).
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    resp = lt.get_element(catalog["registros"], id)
    return resp


def req_1(catalog, anioB):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    inicio = get_time()
    fechaUltimoRegistro = None
    indexUR = -1
    for i in range(0, lt.size(catalog['registros'])):
        anio = int(lt.get_element(catalog["registros"], i)["year_collection"])  
        if anio == int(anioB):
            fechaR = lt.get_element(catalog["registros"], i)["load_time"]
            if fechaUltimoRegistro == None:
                fechaUltimoRegistro = fechaR
                indexUR = i
            else:
                fechaDT = datetime.strptime(fechaR, "%Y-%m-%d %H:%M:%S")
                fechaURDT = datetime.strptime(fechaUltimoRegistro, "%Y-%m-%d %H:%M:%S")
                if fechaDT > fechaURDT:
                    fechaUltimoRegistro = fechaR
                    indexUR = i
    fin = time.time()
    tiempo_ejecucion = (fin - inicio)  # Convertir a milisegundos
    return indexUR, tiempo_ejecucion


def req_2(catalog, depB):
    """
    Retorna el resultado del requerimiento 2
    """
    inicio = get_time()
    fechaUltimoRegistro = None
    indexUR = -1
    for i in range(0, lt.size(catalog['registros'])):
        departamento = lt.get_element(catalog["registros"], i)["location"] 
        if departamento == depB:
            fechaR = lt.get_element(catalog["registros"], i)["load_time"]
            if fechaUltimoRegistro == None:
                fechaUltimoRegistro = fechaR
                indexUR = i
            else:
                fechaDT = datetime.strptime(fechaR, "%Y-%m-%d %H:%M:%S")
                fechaURDT = datetime.strptime(fechaUltimoRegistro, "%Y-%m-%d %H:%M:%S")
                if fechaDT > fechaURDT:
                    fechaUltimoRegistro = fechaR
                    indexUR = i
    fin = time.time()
    tiempo_ejecucion = (fin - inicio) # Convertir a milisegundos
    return indexUR, tiempo_ejecucion


def req_3(catalog, nombre_departamento, year_inicio, year_final):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    registros_copilados = []
    total_registros = 0
    total_survey = 0
    total_census = 0 
    
    
    for i in range(lt.size(catalog["registros"])):
        registro = lt.get_element(catalog["registros"], i) 
        #survey = registro["source"]["SURVEY"]
       # census = registro["source"]["CENSUS"]
        departamento = registro["state_name"]
        if departamento == nombre_departamento:
            year = int(registro["year_collection"])
            
            if year_inicio <= year <= year_final:
                total_registros +=1
                
                if registro["source"] == "CENSUS":
                    tipo_fuente = "CENSUS"
                    total_census += 1
                elif registro["source"] == "SURVEY":
                    tipo_fuente = "SURVEY"
                    total_survey += 1
                fecha_carga = registro["load_time"]
                fecha_carga = datetime.strptime(fecha_carga, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                registros = {
                    "Fuente": tipo_fuente,  
                    "Año_Recopilacion": year,
                    "Fecha_Carga": fecha_carga,
                    "Frecuencia": registro["freq_collection"],
                    "Tipo de Producto": registro["commodity"],
                    "Unidad": registro["unit_measurement"]
                }
                registros_copilados.append(registros)
                
    if len(registros_copilados) > 20:
        registros_filtrados = registros_copilados[:5] + registros_copilados[-5:]
    end_time = get_time() 
    tiempo_ejecucion = delta_time(start_time, end_time)
    
    return {
        "Tiempo de ejecución": tiempo_ejecucion,
        "Total registros filtrados": total_registros,
        "Total registros (SURVEY)": total_survey,
        "Total registros (CENSUS)": total_census,
        "Registros": registros_filtrados
    }

        

def req_4(catalog, producto, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    inicio = get_time()
    
    registros_filtrados = []
    total_survey = 0
    total_census = 0
    
    
    # Iterate over dictionary values
    for i in range(lt.size(catalog["registros"])):
        registro = lt.get_element(catalog["registros"], i) 
        if registro["commodity"] == producto and anio_inicio <= int(registro["year_collection"]) <= anio_fin:
            registros_filtrados.append({
                "Fuente": registro["source"],
                "Año_Recopilacion": registro["year_collection"],
                "Fecha_Carga": registro["load_time"],
                "Frecuencia": registro["freq_collection"],
                "Departamento": registro["location"],
                "Unidad": registro["unit_measurement"]
            })
            
            if registro["source"] == "SURVEY":
                total_survey += 1
            elif registro["source"] == "CENSUS":

                total_census += 1
    
    total_registros = len(registros_filtrados)
    
    fin = time.time()
    tiempo_ejecucion = (fin - inicio)  # Convertir a milisegundos
    
    return {
        "Tiempo de ejecución (ms)": tiempo_ejecucion,
        "Total registros": total_registros,
        "Total SURVEY": total_survey,
        "Total CENSUS": total_census,
        "Registros": registros_filtrados
    }



def req_5(catalog, stat_category, anioI, anioF):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    inicio = get_time()
    resp_index = lt.new_list()
    surveys = 0
    census = 0
    for i in range(0, lt.size(catalog['registros'])):
        statC = lt.get_element(catalog["registros"], i)["statical_category"]
        if stat_category == statC:
            anio = int(lt.get_element(catalog["registros"], i)["year_collection"])  
            if (int(anio) <= int(anioF)) and (int(anio) >= int(anioI)):
                lt.add_last(resp_index, i)
                if lt.get_element(catalog["registros"], i)["source"] ==  "CENSUS":
                    census += 1
                else: surveys +=1
    tamanio_resp = lt.size(resp_index)
    fin = time.time()
    tiempo_ejecucion = (fin - inicio)  # Convertir a milisegundos
    return resp_index, tamanio_resp, census, surveys, tiempo_ejecucion

def req_6(catalog, nombre_departamento, initial_date, final_date):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    registros_filtrados = []
    total_registros = 0
    total_survey = 0
    total_census = 0
    census = catalog["source"]["CENSUS"]
    survey = catalog["source"]["SURVEY"]
    
    for registro in catalog:
        departamento = registro["state_name"]
        
        if departamento == nombre_departamento:
            date = int(registro["load_time"]).strftime("%Y-%m-%d")
            
            if initial_date <= date <= final_date:
                total_registros +=1
                
                if registro["source"] == census:
                    tipo_fuente = "CENSUS"
                    total_census += 1
                elif registro["source"] == survey:
                    tipo_fuente = "SURVEY"
                    total_survey += 1
                
                registros = {
                    "Fuente": tipo_fuente,  
                    "Año_Recopilacion": date,
                    "Fecha_Carga": registro["load_time"].strftime("%Y-%m-%d"),
                    "Frecuencia": registro["freq_collection"],
                    "Tipo de Producto": registro["product_type"],
                    "Unidad": registro["unit_measurement"]
                }
                registros_filtrados.append(registros)
    if len(registros_filtrados) > 20:
        registros_filtrados = registros_filtrados[:5] + registros_filtrados[-5:]
        
    end_time = get_time()  
    tiempo_ejecucion = delta_time(start_time, end_time)

    return {
        "Tiempo de ejecución": tiempo_ejecucion,
        "Total registros filtrados": total_registros,
        "Total registros (SURVEY)": total_survey,
        "Total registros (CENSUS)": total_census,
        "Registros": registros_filtrados
    }


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