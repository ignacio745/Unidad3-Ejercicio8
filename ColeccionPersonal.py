from Personal import Personal
from Investigador import Investigador
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from PersonalApoyo import PersonalApoyo
from zope.interface import implementer
from IColeccion import IColeccion
from Nodo import Nodo
from IDirector import IDirector
from ITesorero import ITesorero


@implementer(IColeccion, ITesorero, IDirector)
class ColeccionPersonal:
    __comienzo = None
    __actual = None
    __tope = 0

    

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
    
    def insertarElemento(self, unaPersona: Personal, pos: int):
        if not isinstance(pos, int) or pos < 0:
            raise IndexError("Indice invalido")

        unNodo = Nodo(unaPersona)
        if pos == 0:
            unNodo.setSiguiente(self.__comienzo)
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        else:
            i = 1
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                i += 1
                aux = aux.getSiguiente()
            if i == pos:
                unNodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(unNodo)
            else:
                raise IndexError("Indice fuera de rango")
        
        self.__tope += 1
        
            
    
    def agregarElemento(self, unaPersona: Personal):
        unNodo = Nodo(unaPersona)
        
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(unNodo)
        
        self.__tope += 1
    


    def mostrarElemento(self, pos: int):
        if pos < 0 or self.__comienzo == None:
            raise IndexError("Indice invalido")
        
        else:
            i = 0
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                aux = aux.getSiguiente()
                i += 1
            if i == pos:
                unaPersona = aux.getPersona()
                print(unaPersona)
            else:
                raise IndexError("Indice fuera de rango")
            
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Personal:
        
        if self.__actual == None:
            self.__actual = self.__comienzo
            raise StopIteration
        
        else:
            unaPersona = self.__actual.getPersona()
            self.__actual = self.__actual.getSiguiente()
            return unaPersona
    
    
    def ordenarPersonal(self, metodoComparacion):
        
        # La k conserva el primer nodo del ultimo par ordenado para saber si el ordenamiento ha terminado
        # La cota conserva el segundo nodo del ultimo par ordenado para saber si quedan nodos que ordenar en la iteracion actual
        # unNodo es el nodo que se esta ordenando actualmente
        if self.__comienzo != None:
            
            k = None
            cota = None
            
            while k != self.__comienzo:
                
                k = self.__comienzo
                unNodo = self.__comienzo
                while unNodo.getSiguiente() != cota:
                    

                    if metodoComparacion(unNodo.getSiguiente().getPersona()) < metodoComparacion(unNodo.getPersona()):
                        
                        unaPersona = unNodo.getPersona()
                        unNodo.setPersona(unNodo.getSiguiente().getPersona())
                        unNodo.getSiguiente().setPersona(unaPersona)
                        k = unNodo
                    
                    unNodo = unNodo.getSiguiente()
                

                cota = k.getSiguiente()
            

    def getListadoAgentesInvestigadores(self, nombreCarrera: str) -> str:
        """
        Retorna un listado ordenado por nombre con los datos de los agentes que se desempeñan como docentes investigadores en una carrera.

        Parametros
        ----------
        nombreCarrera: str
            El nombre de la carrera
        """

        self.ordenarPersonal(lambda unaPersona: unaPersona.getNombre())
        cadena = "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}\n".format("Cuil", "Apellido", "Nombre", "Categoria incentivos", "Importe extra")
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getCarrera().lower() == nombreCarrera.lower():
                cadena += "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20.2f}\n".format(unaPersona.getCuil(), unaPersona.getApellido(), unaPersona.getNombre(), unaPersona.getCategoriaIncentivos(), unaPersona.getImporteExtra())
        return cadena
    

    def contarDocentesInvestigadores(self, nombreAreaInvestigacion: str) -> tuple:
        """
        Retorna una tupla con la cantidad de docentes investigadores y la cantidad de investigadores de un area de investigacion en ese orden.
        
        Parametros
        ----------
        nombreAreaInvestigacion: str
            El nombre del area de investigacion a contar.
        """

        contadorDocentesInvestigadores = 0
        contadorInvestigadores = 0
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getAreaInvestigacion().lower() == nombreAreaInvestigacion.lower():
                contadorDocentesInvestigadores += 1
            elif isinstance(unaPersona, Investigador) and unaPersona.getAreaInvestigacion().lower() == nombreAreaInvestigacion.lower():
                contadorInvestigadores += 1
        return (contadorDocentesInvestigadores, contadorInvestigadores)
    


    def getListadoPersonal(self):
        self.ordenarPersonal(lambda unaPersona: unaPersona.getApellido())
        cadena = "{0:<20}{1:<20}{2:<25}{3:<20}\n".format("Nombre", "Apellido", "Tipo de agente", "Sueldo")
        for unaPersona in self:
            cadena += "{0:<20}{1:<20}{2:<25}{3:<20}\n".format(unaPersona.getNombre(), unaPersona.getApellido(), unaPersona.getTipo(), unaPersona.getSueldo())
        return cadena
    

    def getListadoDocentesInvestigadores(self, categoria: str):
        cadena = "{0:<23}{1:<23}{2:>20}\n".format("Nombre", "Apellido", "Importe extra")
        total = 0
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getCategoriaIncentivos().lower() == categoria.lower():
                cadena += "{0:<23}{1:<23}{2:20.2f}\n".format(unaPersona.getNombre(), unaPersona.getApellido(), unaPersona.getImporteExtra())
                total += unaPersona.getImporteExtra()
        cadena += "{0:46}{1:20.2f}\n".format("Importe total en concepto de incentivos: ".upper(), total)
        return cadena
    

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            personas = [unaPersona.toJSON() for unaPersona in self]
        )
        return d

    def buscarAgentePorCuil(self, cuil: str):
        """
        Retorna un empleado dado su cuil, en caso de no encontrarlo retorna None
        """

        unNodo = self.__comienzo

        while unNodo.getPersona().getCuil() != cuil and unNodo.getSiguiente() != None:
            unNodo = unNodo.getSiguiente()

        if unNodo.getPersona().getCuil() != cuil:
            unaPersona = None
        else:
            unaPersona = unNodo.getPersona()
        return unaPersona
    

    def gastosSueldoPorEmpleado(self, cuil: str) -> float:

        unaPersona = self.buscarAgentePorCuil(cuil)
        if unaPersona == None:
            gastos = None
        else:
            gastos = unaPersona.getSueldo()
        return gastos
    

    def modificarBasico(self, cuil: str, nuevoBasico: float) -> bool:
        unaPerona = self.buscarAgentePorCuil(cuil)
        if unaPerona == None:
            band = False
        else:
            unaPerona.setSueldoBasico(nuevoBasico)
            band = True
        return band
    

    def modificarCargo(self, cuil: str, nuevoCargo: str) -> bool:
        unaPersona = self.buscarAgentePorCuil(cuil)
        if isinstance(unaPersona, Docente):
            unaPersona.setCargo(nuevoCargo)
            band = True
        else:
            band = False
        return band
    

    def modificarCategoria(self, cuil: str, nuevaCategoria: str) -> bool:
        unaPersona = self.buscarAgentePorCuil(cuil)
        if isinstance(unaPersona, PersonalApoyo):
            unaPersona.setCategoria(nuevaCategoria)
            band = True
        else:
            band = False
        return band
    

    def modificarImporteExtra(self, cuil: str, nuevoImporteExtra: float) -> bool:
        unaPersona = self.buscarAgentePorCuil(cuil)
        if isinstance(unaPersona, DocenteInvestigador):
            unaPersona.setImporteExtra(nuevoImporteExtra)
            band = True
        else:
            band = False
        return band