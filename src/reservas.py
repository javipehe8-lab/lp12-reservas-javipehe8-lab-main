import csv
from typing import NamedTuple
from datetime import datetime, date

Reserva = NamedTuple("Reserva", 
                     [("nombre", str),
                      ("dni", str),
                      ("fecha_entrada", date),
                      ("fecha_salida", date),
                      ("tipo_habitacion", str),
                      ("num_personas", int),
                      ("precio_noche", float),
                      ("servicios_adicionales", list[str])
                    ])

def lee_reservas(ruta):
    res = []
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales in lector:
            fecha_entrada_obj = datetime.strptime(fecha_entrada, '%Y-%m-%d').date()
            fecha_salida_obj = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            servicios_adicionales_pars = servicios_adicionales.split(',')
            t= Reserva(nombre, dni, fecha_entrada_obj, fecha_salida_obj, tipo_habitacion, num_personas, precio_noche, servicios_adicionales_pars)
            res.append(t)
        return res

lector = lee_reservas(r"data\reservas.csv")


def total_facturado(lector, fecha1, fecha2):
    contador = 0
    for a in lector:
        calculador_dias = (a.fecha_salida - a.fecha_entrada).days
        if fecha1.date() <= a.fecha_entrada <= fecha2.date():
            contador += calculador_dias * a.precio_noche
    return contador

def reserva_mas_larga_auxiliar(reservas, n):
    lista = []
    for a in reservas:
        contador_dias = (a.fecha_salida - a.fecha_entrada).days
        tupla_duracion = (contador_dias, a.nombre, a.fecha_entrada)
        lista.append(tupla_duracion)
    return sorted(lista, key=lambda x: x[0], reverse=True)[:n]

    
def reserva_mas_larga(reservas, n):
    tuplas_con_duracion = reserva_mas_larga_auxiliar(reservas, n)
    resultado = []
    for a in tuplas_con_duracion:
        nombre = a[1]
        fecha_entrada = a[2]
        tupla_final = (nombre, fecha_entrada)
        resultado.append(tupla_final)
    return resultado


def cliente_mayor_facturacion(reservas, servicios):
    dic = {}
    res = []
    for a in reservas:
        if any(servicio in servicios for servicio in a.servicios_adicionales):
            calculador_facturacion= (a.fecha_salida - a.fecha_entrada).days * a.precio_noche
            if a.dni not in dic:
                dic[a.dni] = calculador_facturacion
            else:
                dic[a.dni] += calculador_facturacion
    for dni, facturacion in dic.items():
        res.append((dni, facturacion))
    return sorted(res, key=lambda x: x[1], reverse=True)[0]

print(cliente_mayor_facturacion(lector, {"Parking"}))

#def servicios_estrella_por_mes(registros, tipos_habitacion):


        













    



     
