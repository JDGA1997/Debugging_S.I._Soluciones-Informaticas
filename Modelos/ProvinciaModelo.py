class ProvinciaModelo:
    
    def __init__(self, provinciaId, nombre):
        self.__provinciaId = provinciaId
        self.__nombre = nombre

    def getProvinciaId(self):
        return self.__provinciaId
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, value):
        self.__nombre = value