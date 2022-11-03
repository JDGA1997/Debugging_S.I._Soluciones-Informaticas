import datetime

class SolicitudModelo:

    def __init__(self, solicitudId, productosSolicitados):
        self.__solicitudId = solicitudId
        self.__productosSolicitados = productosSolicitados
        self.__fecha = datetime.date.today()

    def getSolicitudId(self):
        return self.__solicitudId
    
    def getProductosSolicitados(self):
        return self.__productosSolicitados
    
    def setProductosSolicitados(self, value):
        self.__productosSolicitados = value

    def getFecha(self):
        return self.__fecha