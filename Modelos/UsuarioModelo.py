from Modelos import CategoriaModelo, ProvinciaModelo, RolModelo
import datetime

class UsuarioModelo:

    def __init__(self):
        self.usuarioId = -1
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.usuario = ""
        self.contrasenia = ""
        self.fechaNacimiento = datetime.date.min
        self.provincia = ProvinciaModelo()
        self.dni = ""
        self.telefono = ""
        self.categoria = CategoriaModelo()
        self.rol = RolModelo()
