from Modelos.VendedorModelo import VendedorModelo
import ConexionDB, ProvinciaDAO

def insertarVendedor(vendedor):
    con = ConexionDB.getConnection()
    sqlQuery = """INSERT INTO dbo.[Vendedores] (Nombre, Apellido, Email, Telefono, Url, Cuit, ProvinciaId)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    record = ({vendedor.getNombre()}, {vendedor.getApellido()}, {vendedor.getEmail()}, 
            {vendedor.getTelefono()}, {vendedor.getUrl()}, {vendedor.getCuit()}, 
            {vendedor.getProvincia().getProvinciaId()})
    cursor = con.cursor()
    cursor.execute(sqlQuery, record)

    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)

def obtenerTodosVendedores():
    con = ConexionDB.getConnection()
    sqlQuery = """SELECT * FROM dbo.[Vendedores]"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    filas = cursor.fetchall()

    cursor.close()
    ConexionDB.closeConnection(con)

    vendedores = []
    provincias = ProvinciaDAO.obtenerTodasProvincias()

    for fila in filas:
        vendedorId = fila[0]
        nombre = fila[1]
        apellido = fila[2]
        email = fila[3]
        tel = fila[4]
        url = fila[5]
        cuit = fila[6]
        provinciaId = fila[7]

        for p in provincias:
            if p.getProvinciaId() == provinciaId:
                provincia = p
                break

        vendedor = VendedorModelo(vendedorId, nombre, email, provincia, cuit, apellido, url, tel)
        vendedores.append(vendedor)

    return vendedores 

def obtenerVendedor(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""SELECT * FROM dbo.[Vendedores]
                WHERE VendedorId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    fila = cursor.fetchone()
    cursor.close()
    ConexionDB.closeConnection(con)

    nombre = fila[1]
    apellido = fila[2]
    email = fila[3]
    tel = fila[4]
    url = fila[5]
    cuit = fila[6]
    provinciaId = fila[7]

    provincia = ProvinciaDAO.obtenerProvincia(provinciaId)

    return VendedorModelo(id, nombre, email, provincia, cuit, apellido, url, tel)


def eliminarVendedor(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""DELETE FROM dbo.[Vendedores]
                WHERE VendedorId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)

def modificarVendedor(vendedor):
    con = ConexionDB.getConnection()
    sqlQuery = f"""UPDATE dbo.[Vendedores] SET 
                Nombre = {vendedor.getNombre()}, 
                Apellido = {vendedor.getApellido()}, 
                Email = {vendedor.getEmail()}, 
                Telefono = {vendedor.getTelefono()}, 
                Url = {vendedor.getUrl()}, 
                Cuit = {vendedor.getCuit()}, 
                ProvinciaId = {vendedor.getProvincia().getProvinciaId()}"""
    
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)