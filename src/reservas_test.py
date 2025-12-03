from reservas import *



def test_lee_reservas():
    print("Leyendo datos...")
    print(f"Se han leído {len(lector)} archivos, imprimiendo...")
    print(lector)

if __name__ == "__main__":
    test_lee_reservas()


print("------------------------------------------------------------------------------------")


def test_total_facturado(lector: list[Reserva], fecha1: date, fecha2: date):
    info2 = total_facturado(lector, fecha1, fecha2)
    print(f"Entre {fecha1} y {fecha2}, se ha calculado una facturación de {info2} euros")

if __name__ == "__main__":
    fecha_info1 = date(2022, 12, 31)
    fecha_info12 = date(2022, 1, 2)
    fecha_info2= date(2022, 2, 1)
    fecha_info21 = date(2022, 2, 28)
    test_total_facturado(lector, fecha_info1, fecha_info12)
    test_total_facturado(lector, fecha_info2, fecha_info21)

print("-----------------------------------------------------------------------------------------")

def test_cliente_mayor_facturacion(reserva: list[Reserva], servicios: list[str]):
    info = cliente_mayor_facturacion(lector, servicios)
    print(f"Sin filtrar por servicios: {info}")

