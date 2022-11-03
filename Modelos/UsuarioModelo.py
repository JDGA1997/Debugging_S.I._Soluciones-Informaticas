import datetime
from RolModelo import RolModelo
from CategoriaModelo import CategoriaModelo
from ProvinciaModelo import ProvinciaModelo

class UsuarioModelo:

    def __init__(self, usuarioId, nombre, apellido, email, usuario, contrasenia, dni, 
                provincia: ProvinciaModelo, telefono = 0, rol = RolModelo(0, "user"), 
                prefencia = CategoriaModelo(0, "todas"), fechaNacimiento = datetime.date.min):
        self.__usuarioId = usuarioId
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.__fechaNac = fechaNacimiento
        self.__provincia = provincia
        self.__dni = dni
        self.__telefono = telefono
        self.__categoria = prefencia
        self.__rol = rol

    def getUsuarioId(self):
        return self.__usuarioId
    
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

    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self, value):
        self.__usuario = value

    def getContrasenia(self):
        return self.__contrasenia
    
    def setContrasenia(self, value):
        self.__contrasenia = value

    def getFechaNac(self):
        return self.__fechaNac
    
    def setFechaNac(self, value):
        self.__fechaNac = value

    def getProvincia(self):
        return self.__provincia
    
    def setProvincia(self, value: ProvinciaModelo):
        self.__provincia = value

    def getDni(self):
        return self.__dni
    
    def setDni(self, value):
        self.__dni = value

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, value):
        self.__telefono = value

    def getCategoria(self):
        return self.__categoria
    
    def setCategoria(self, value: CategoriaModelo):
        self.__categoria = value

    def getRol(self):
        return self.__rol
    
    def setRol(self, value: RolModelo):
        self.__rol = value