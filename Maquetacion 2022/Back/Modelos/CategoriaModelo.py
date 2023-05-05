class CategoriaModelo:
    
    def __init__(self, categoriaId, nombre):
        self.__categoriaId = categoriaId
        self.__nombre = nombre

    def getCategoriaId(self):
        return self.__categoriaId

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, value):
        self.__nombre = value