import os
from IDirector import IDirector
from IngresadorTeclado import IngresadorTeclado


class MenuDirector:
    __switcher = None
    __ingresador = None
    __menuTesorero = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                          }
        self.__ingresador = IngresadorTeclado()

            
    def opcion(self, unaColeccionPersonal: IDirector,op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op in ('1', '2', '3', '4'):
            func(unaColeccionPersonal)
        else:
            func()


    def opcion1(self, unaColeccionPersonal: IDirector):
        cuil = self.__ingresador.inputRegularExpression("Ingrese el cuil del agente cuyo sueldo desea modificar: ", "[0-9]{2,2}-[0-9]{8,8}-[0-9]","CUIL invalido, reintente: ")
        sueldoBasico = self.__ingresador.inputFloat("Ingrese el nuevo sueldo basico, en caso de incluir decimales usar un punto: ", "Sueldo invalido, reintente: ")
        resultado = unaColeccionPersonal.modificarBasico(cuil, sueldoBasico)
        if resultado:
            print("Sueldo cambiado")
        else:
            print("[ERROR] No se encontro un agente con cuil {0}".format(cuil))
        
    
    def opcion2(self, unaColeccionPersonal: IDirector):
        cuil = self.__ingresador.inputRegularExpression("Ingrese el cuil del docente cuyo cargo desea modificar: ", "[0-9]{2,2}-[0-9]{8,8}-[0-9]", "CUIL invalido, reintente: ")
        nuevoCargo = self.__ingresador.inputOpcion("Seleccione el nuevo cargo", ["Simple", "Semiexclusivo", "Exclusivo"])
        resultado = unaColeccionPersonal.modificarCargo(cuil, nuevoCargo)
        if resultado:
            print("Cargo modificado")
        else:
            print("[ERROR] No se encontro un docente con cuil {0}".format(cuil))
    

    def opcion3(self, unaColeccionPersonal: IDirector):
        cuil = self.__ingresador.inputRegularExpression("Ingrese el cuil del personal de apoyo cuya categoria desea modificar: ", "[0-9]{2,2}-[0-9]{8,8}-[0-9]", "CUIL invalido, reintente: ")
        categoria = self.__ingresador.inputInt("Ingrese la nueva categoria, un numero del 1 al 22: ", "Categoria invalida, reintente: ")
        while not (1 <= categoria <= 22):
            categoria = self.__ingresador.inputInt("Categoria invalida, reintente: ", "Categoria invalida, reintente: ")
        resultado = unaColeccionPersonal.modificarCategoria(cuil, categoria)
        if resultado:
            print("Categoria cambiada")
        else:
            print("[ERROR] No se encontro un personal de apoyo con cuil {0}".format(cuil))
    
    
    def opcion4(self, unaColeccionPersonal: IDirector):
        cuil = self.__ingresador.inputRegularExpression("Ingrese el cuil del docente-investigador cuyo importe desea cambiar: ", "[0-9]{2,2}-[0-9]{8,8}-[0-9]", "CUIL invalido, reintente: ")
        nuevoExtra = self.__ingresador.inputFloat("Ingrese el nuevo extra, en caso de incluir decimales use un punto: ", "Extra invalido, reintente: ")
        resultado = unaColeccionPersonal.modificarImporteExtra(cuil, nuevoExtra)
        if resultado:
            print("Extra cambiado")
        else:
            print("[ERROR] No se encontro un docente-investigador con cuil {0}".format(cuil))



    def salir(self):
        print('Sesion cerrada')




    def ejecutarMenu(self, unaColeccionPersonal: IDirector):
            opcion = "0"
            os.system("clear")
            while opcion != "5":
                print("Ingrese la opcion deseada")
                print("[1] Modificar el sueldo basico de un agente")
                print("[2] Modificar el cargo de un docente")
                print("[3] Modificar la categoria de un personal de apoyo")
                print("[4] Modificar el importe extra que se paga a un docente investigador")
                print("[5] Cerrar sesion")
                opcion = input("--> ")
                os.system("clear")
                self.opcion(unaColeccionPersonal, opcion)
                input("Presione enter para continuar")
                os.system("clear")