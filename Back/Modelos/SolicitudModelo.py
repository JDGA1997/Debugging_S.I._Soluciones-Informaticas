import datetime
from ProductosSolicitadosModelo import ProductosSolicitadosModelo

class SolicitudModelo:

    def __init__(self, solicitudId, productosSolicitados: ProductosSolicitadosModelo):
        self.__solicitudId = solicitudId
        self.__productosSolicitados = productosSolicitados
        self.__fecha = datetime.date.today()

    def getSolicitudId(self):
        return self.__solicitudId
    
    def getProductosSolicitados(self):
        return self.__productosSolicitados
    
    def setProductosSolicitados(self, value: ProductosSolicitadosModelo):
        self.__productosSolicitados = value

    def getFecha(self):
        return self.__fecha