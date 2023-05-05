#get Index() -> return View(), por dentro llama al obtenerTodosProductos()
#get/post ComprarProducto(id) -> redirige a la página del Vendedor o a la info de éste.

from DAOs import ProductoDAO
import Vistas

def Index():
    productosEnDb = ProductoDAO.obtenerTodosProductos()
    return Vistas.Home.inicio(productosEnDb)

def ComprarProducto(id):
    producto = ProductoDAO.obtenerProducto(id)
    vendedor = producto.getVendedor()
    return Vistas.Vendedor.MostrarInformación(vendedor)