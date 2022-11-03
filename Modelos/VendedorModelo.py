class VendedorModelo:

    def __init__(self, vendedorId, nombre, email, provincia, cuit, 
                apellido = "", url = "", telefono = 0):
        self.__vendedorId = vendedorId
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__provincia = provincia
        self.__cuit = cuit
        self.__telefono = telefono
        self.__url = url

    def getUsuarioId(self):
        return self.__vendedorId
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, value):
        self.__nombre = value
    
    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, value):
        self.__apellido = value

    def getEmail(self):
        return self.__email
    
    def setEmail(self, value):
        self.__email = value

    def getProvincia(self):
        return self.__provincia
    
    def setProvincia(self, value):
        self.__provincia = value

    def getCuit(self):
        return self.__cuit
    
    def setCuit(self, value):
        self.__cuit = value

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, value):
        self.__telefono = value

    def getUrl(self):
        return self.__url
    
    def setUrl(self, value):
        self.__url = value