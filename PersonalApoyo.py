from Personal import Personal

class PersonalApoyo(Personal):
    __categoria = ""

    def __init__(self, cuil: str, apellido: str, nombre: str, sueldoBasico: float, antiguedad: int, categoria: int) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria
    
    def getCategoria(self) -> int:
        return self.__categoria
    
    def setCategoria(self, nuevaCategoria: str):
        self.__categoria = nuevaCategoria
    
    def getSueldo(self) -> float:
        sueldo = super().getSueldo()
        if 1 <= self.getCategoria() <= 10:
            sueldo += self.getSueldoBasico() * 0.1
        elif 11 <= self.getCategoria() <= 20:
            sueldo += self.getSueldoBasico() * 0.2
        elif 21 <= self.getCategoria() <= 22:
            sueldo += self.getSueldoBasico() * 0.3
        return sueldo
    

    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["categoria"] = self.getCategoria()
        return d
    

    def __str__(self):
        cadena = super().__str__()
        cadena += "Categoria: {0}\n".format(self.__categoria)
        return cadena
    



    @classmethod
    def getTipo(cls) -> str:
        return "Personal de apoyo"