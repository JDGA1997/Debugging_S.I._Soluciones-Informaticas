class RolModelo:
    
    def __init__(self, rolId, nombre):
        self.__rolId = rolId
        self.__nombre = nombre

    def getRolId(self):
        return self.__rolId
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, value):
        self.__nombre = value