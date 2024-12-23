# -*- coding: utf-8 -*-

# Definimos el TDA para la información de cada vuelta
class TDA_Vuelta:
    def __init__(self, pnumero_vuelta, ptiempo_vuelta, plitros_combustible):
        self.numero_vuelta = pnumero_vuelta
        self.tiempo_vuelta = ptiempo_vuelta
        self.litros_combustible = plitros_combustible
    
    def __str__(self):
        return f"nro_vuelta: {self.numero_vuelta}, litros_combustible: {self.litros_combustible}, tiempo_vuelta: {self.tiempo_vuelta}"

# Función para mostrar el menú
def udf_mi_menu():
    print("\n--- Menú ---")
    print("1) Registro de tiempos")
    print("2) Informe de performance")
    print("3) Salir")

    opcion = input("Elige una opción: ")

    return opcion

def reg_tiempos(reg_list: list) -> None:
    CARGA_MINIMA = 250
    VUELTAS = 5
    GASTO_POR_VUELTA = 50

    while True:
        try:
            combustible_inicial = int(input("con cuantos litros de combustible se arranca?: "))
            if combustible_inicial < CARGA_MINIMA:
                raise Exception(f"la carga minima es de {CARGA_MINIMA}")
            break
        except ValueError:
            print("solo numeros enteros.")
        except Exception as e:
            print(e)

    for nro_vuelta in range(VUELTAS):
        while True:
            try:
                vuelta_tiempo = int(input(f"cuantos segundos tardo en la vuelta nro {nro_vuelta+1}?: "))
                if vuelta_tiempo < 0:
                    raise Exception("ERROR: es imposible que sea el tiempo de la vuelta sea negativo")
                break
            except ValueError:
                print("solo numeros")
            except Exception as e:
                print(e)

        if nro_vuelta == 0:
            reg_list.append(TDA_Vuelta(nro_vuelta+1,vuelta_tiempo,combustible_inicial-GASTO_POR_VUELTA))
        else:
            reg_list.append(TDA_Vuelta(nro_vuelta+1,vuelta_tiempo,reg_list[-1].litros_combustible-GASTO_POR_VUELTA))

def gen_informe(reg_list: list) -> None:
    mejor_vuelta = reg_list[0]

    print("resumen de las vueltas: \n")
    for vuelta in reg_list:
        print("\t",vuelta)
        if mejor_vuelta.tiempo_vuelta < vuelta.tiempo_vuelta:
            mejor_vuelta = vuelta
    
    print(f"la mejor vuelta es {mejor_vuelta.numero_vuelta} con un timpo de {mejor_vuelta.tiempo_vuelta}")
    print(f"en la ultima vuelta quedo {reg_list[-1].litros_combustible}")

# Función principal (main)
def udf_mi_main():
    lis_vueltas = ["as"]
    while True:
        opcion = udf_mi_menu()
        if opcion == "1":
            print("Opción 1 seleccionada: Registro de tiempos.")

            if len(lis_vueltas) > 0:    
                try:
                    res = input("deseas sobreescribir el registro actual? 1 (si) 2 (no): ")
                except:
                    print("ocurrio un error, ingresa solo el numero.")

                match res:
                    case "1": reg_tiempos(lis_vueltas); continue
                    case _: continue

            reg_tiempos(lis_vueltas)
        elif opcion == "2":
            print("Opción 2 seleccionada: Informe de performance.")
            if len(lis_vueltas):
                gen_informe(lis_vueltas)
                continue
            print("no se encuentran registros de vueltas")
        elif opcion == "3":
            print("Opción 3 seleccionada: Salir del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

# Ejecutar el programa
udf_mi_main()