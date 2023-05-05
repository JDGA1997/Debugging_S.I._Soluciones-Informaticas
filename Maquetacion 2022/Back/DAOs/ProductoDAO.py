from Modelos.ProductoModelo import ProductoModelo
import ConexionDB, CategoriaDAO, VendedorDAO

def insertarProducto(producto):
    con = ConexionDB.getConnection()
    sqlQuery = """INSERT INTO dbo.[Productos] (Nombre, Descripcion, Precio, Stock, Imagen, VendedorId, CategoriaId, EstaEnPromo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    record = ({producto.getNombre()}, {producto.getDescripcion()}, {producto.getPrecio()}, 
            {producto.getStock()}, {producto.getImagen()}, {producto.getVendedor().getVendedorId()}, 
            {producto.getCategoria().getCategoriaId()}, {producto.estaEnPromo()})
    cursor = con.cursor()
    cursor.execute(sqlQuery, record)
    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)

def obtenerTodosProductos():
    con = ConexionDB.getConnection()
    sqlQuery = """SELECT * FROM dbo.[Productos]"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    filas = cursor.fetchall()

    cursor.close()
    ConexionDB.closeConnection(con)

    productos = []
    categorias = CategoriaDAO.obtenerTodasCategorias()
    vendedores = VendedorDAO.obtenerTodosVendedores()

    for fila in filas:
        productoId = fila[0]
        nombre = fila[1]
        descripcion = fila[2]
        precio = fila[3]
        stock = fila[4]
        imagen = fila[5]
        vendedorId = fila[6]
        categoriaId = fila[7]
        estaEnPromo = fila[8]

        for c in categorias:
            if c.getCategoriaId() == categoriaId:
                categoria = c
                break
        for v in vendedores:
            if v.getVendedorId() == vendedorId:
                vendedor = v
                break

        producto = ProductoModelo(productoId, nombre, precio, stock, imagen, vendedor, categoria, estaEnPromo, descripcion)
        productos.append(producto)

    return productos 

def obtenerProducto(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""SELECT * FROM dbo.[Productos]
                WHERE ProductoId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    fila = cursor.fetchone()
    cursor.close()
    ConexionDB.closeConnection(con)

    nombre = fila[1]
    descripcion = fila[2]
    precio = fila[3]
    stock = fila[4]
    imagen = fila[5]
    vendedorId = fila[6]
    categoriaId = fila[7]
    estaEnPromo = fila[8]

    categoria = CategoriaDAO.obtenerCategoria(categoriaId)
    vendedor = VendedorDAO.obtenerVendedor(vendedorId)

    return ProductoModelo(id, nombre, precio, stock, imagen, vendedor, categoria, estaEnPromo, descripcion)


def eliminarProducto(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""DELETE FROM dbo.[Productos]
                WHERE ProductoId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)

def modificarProducto(producto):
    con = ConexionDB.getConnection()
    sqlQuery = f"""UPDATE dbo.[Productos] SET 
                Nombre = {producto.getNombre()}, 
                Descripcion = {producto.getDescripcion()}, 
                Precio = {producto.getPrecio()}, 
                Stock = {producto.getStock()}, 
                Imagen = {producto.getImagen()}, 
                VendedorId = {producto.getVendedor().getVendedorId()}, 
                CategoriaId = {producto.getCategoria().getCategoriaId()}, 
                EstaEnPromo = {producto.estaEnPromo()}
                WHERE ProductoId = {producto.getProductoId()}"""
    
    cursor = con.cursor()
    cursor.execute(sqlQuery)
    
    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)