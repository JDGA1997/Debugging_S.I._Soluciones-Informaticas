from Modelos.CategoriaModelo import CategoriaModelo
import ConexionDB

def insertarCategoria(categoria):
    con = ConexionDB.getConnection()
    sqlQuery = """INSERT INTO dbo.[Categorias] (Nombre)
                VALUES (%s)"""
    record = ({categoria.getNombre()})
    cursor = con.cursor()
    cursor.execute(sqlQuery, record)

    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)

def obtenerTodasCategorias():
    con = ConexionDB.getConnection()
    sqlQuery = """SELECT * FROM dbo.[Categorias]"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    filas = cursor.fetchall()

    cursor.close()
    ConexionDB.closeConnection(con)

    categorias = []
    for fila in filas:
        categoriaId = fila[0]
        nombre = fila[1]

        categoria = CategoriaModelo(categoriaId, nombre)
        categorias.append(categoria)

    return categorias

def obtenerCategoria(id): 
    con = ConexionDB.getConnection()
    sqlQuery = f"""SELECT * FROM dbo.[Categorias]
                WHERE CategoriaId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    fila = cursor.fetchone()
    cursor.close()
    ConexionDB.closeConnection(con)

    nombre = fila[1]

    return CategoriaModelo(id, nombre)

def eliminarCategoria(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""DELETE FROM dbo.[Categorias]
                WHERE CategoriaId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    con.commit()
    cursor.close()
    ConexionDB.closeConnection(con)