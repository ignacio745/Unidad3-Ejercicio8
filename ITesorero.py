from zope.interface import Interface

class ITesorero(Interface):

    def gastosSueldoPorEmpleado(self, cuil:str) -> float:
        """
        Retorna el gasto en sueldo de un agente dado su cuil, en caso de no encontrarlo retorna None
        """
        
        pass