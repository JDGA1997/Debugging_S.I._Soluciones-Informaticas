from Modelos import ProvinciaModelo

class VendedorModelo:

    def __init__(self):
        self.usuarioId = -1
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.provincia = ProvinciaModelo()
        self.cuit = ""
        self.telefono = ""
        self.url = ""