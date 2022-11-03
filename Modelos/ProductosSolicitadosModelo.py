from ProductoModelo import ProductoModelo

class ProductosSolicitadosModelo:

    def __init__(self, producto: ProductoModelo, cantidad = 0):
        self.__producto = producto
        self.__cantidad = cantidad
 
    def getProducto(self):
        return self.__producto
    
    def setProducto(self, value: ProductoModelo):
        self.__producto = value

    def getCantidad(self):
        return self.__cantidad
    
    def setCantidad(self, value):
        self.__cantidad = value