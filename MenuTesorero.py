import os
from ITesorero import ITesorero
from IngresadorTeclado import IngresadorTeclado

class MenuTesorero:
    __switcher = None
    __ingresador = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.salir
                          }
        self.__ingresador = IngresadorTeclado()
        
    

    def opcion(self, unaColeccionPersonal: ITesorero, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1':
            func(unaColeccionPersonal)
        else:
            func()
        
    def opcion1(self, unaColeccionPersonal: ITesorero):
        cuil = input("Ingrese el cuil: ")
        gasto = unaColeccionPersonal.gastosSueldoPorEmpleado(cuil)
        if gasto != None:
            print("El gasto en concepto de sueldo para el empleado de cuil {0} es ${1:.2f}".format(cuil, gasto))
        else:
            print("No se encontro al agente de cuil {0}".format(cuil))


    
    def salir(self):
        print('Sesion cerrada')
    

    def ejecutarMenu(self, unaColeccionPersonal: ITesorero):
            opcion = "0"
            while opcion != "2":
                print("Ingrese la opcion deseada")
                print("[1] Consultar el gasto en concepto de sueldo de un empleado")
                print("[2] Cerrar sesion")
                opcion = input("--> ")  
                self.opcion(unaColeccionPersonal, opcion)
                input("Presione Enter para continuar")
                os.system("clear")