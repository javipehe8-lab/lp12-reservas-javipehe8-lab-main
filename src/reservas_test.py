from reservas import *



def test_lee_reservas():
    print("Leyendo datos...")
    print(f"Se han leído {len(lector)} archivos, imprimiendo...")
    print(lector)

if __name__ == "__main__":
    test_lee_reservas()


def test_total_facturado():
    fecha_info1 = datetime(2022, 12, 31, 1, 0, 0)
    fecha_info12 = datetime(2022, 1, 2, 1, 0, 0 )
    fecha_info2= datetime(2022, 2, 1, 0, 0, 0)
    fecha_info21 = datetime(2022, 2, 28, 0, 0, 0)
    info1 = total_facturado(lector, fecha_info12, fecha_info1 )
    info2 = total_facturado(lector, fecha_info2, fecha_info21)
    print("calculando facturación completa...")
    print(f"En todo el periodo de datos dados, se ha calculador una facturación de {info1} euros")
    print("calculando facturación desde 1 de febrero de 2022 hasta 28 de febrero de 2022...")
    print(f"En todo febrero, se ha calculador una facturación de {info2} euros")

if __name__ == "__main__":
    test_total_facturado()

