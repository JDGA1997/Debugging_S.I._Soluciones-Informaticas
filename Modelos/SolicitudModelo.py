from Modelos import ProductoModelo
import datetime

class SolicitudModelo:

    def __init__(self):
        self.solicitudId = -1
        self.producto = ProductoModelo()
        self.fecha = datetime.date.today()
        self.cantidad = 0
