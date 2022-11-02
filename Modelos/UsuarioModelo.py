from Modelos import CategoriaModelo, ProvinciaModelo, RolModelo

class UsuarioModelo:

    def __init__(self):
        self.usuarioId = -1
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.usuario = ""
        self.contrasenia = ""
        self.fechaNacimiento = ""
        self.provincia = ProvinciaModelo()
        self.dni = ""
        self.telefono = ""
        self.categoria = CategoriaModelo()
        self.rol = RolModelo()
