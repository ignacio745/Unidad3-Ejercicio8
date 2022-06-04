from zope.interface import Interface

class IDirector(Interface):

    def modificarBasico(cuil:str, nuevoBasico:float) -> bool:
        """
        Modifica el sueldo basico de un agente dado su cuil,
        retorna True si se pudo realizar la modificacion, False en caso contrario
        """

        pass


    def modificarCargo(cuil: str, nuevoCargo: str) -> bool:
        """
        Modifica el porcentaje por cargo de un docente dado su cuil,
        retorna True si se pudo realizar la modificacion, False en caso contrario
        """

        pass


    def modificarCategoria(cuil: str, nuevaCategoria: str) -> bool:
        """
        Modifica la categoria de un personal de apoyo dado su cuil,
        retorna True si se pudo realizar la modificacion, False en caso contrario
        """

        pass


    def modificarImporteExtra(self, cuil: str, nuevoImporteExtra: float) -> bool:
        """
        Modifica el extra que corresponde a un agente dado su cuil,
        retorna True si se pudo realizar la modificacion, False en caso contrario
        """

        pass