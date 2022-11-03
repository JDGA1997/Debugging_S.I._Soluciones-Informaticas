class ProductoModelo:

    def __init__(self, productoId, nombre, precio, stock, imagen, vendedor, categoria, 
                estaEnPromo = False, descripcion = ""):
        self.__productoId = productoId
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__imagen = imagen
        self.__estaEnPromo = estaEnPromo
        self.__vendedor = vendedor
        self.__categoria = categoria
    
    def getProductoId(self):
        return self.__productoId
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, value):
        self.__nombre = value
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, value):
        self.__descripcion = value

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, value):
        self.__precio = value

    def getStock(self):
        return self.__stock
    
    def setStock(self, value):
        self.__stock = value

    def getImagen(self):
        return self.__imagen
    
    def setImagen(self, value):
        self.__imagen = value

    def estaEnPromo(self):
        return self.__estaEnPromo
    
    def setEstaEnPromo(self, value):
        self.__estaEnPromo = value

    def getVendedor(self):
        return self.__vendedor
    
    def setVendedor(self, value):
        self.__vendedor = value

    def getCategoria(self):
        return self.__categoria
    
    def setCategoria(self, value):
        self.__categoria = value