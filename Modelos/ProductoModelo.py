from Modelos import CategoriaModelo, VendedorModelo

class ProductoModelo:

    def __init__(self):
        self.productoId = -1
        self.nombre = ""
        self.descripcion = ""
        self.precio = 0.0
        self.stock = 0
        self.imagen = "../Base_de_datos/default-image.png"
        self.estaEnPromo = False
        self.vendedor = VendedorModelo()
        self.categoria = CategoriaModelo()