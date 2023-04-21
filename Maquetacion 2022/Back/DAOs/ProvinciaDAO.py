from Modelos.ProvinciaModelo import ProvinciaModelo
import ConexionDB

def obtenerTodasProvincias():
    con = ConexionDB.getConnection()
    sqlQuery = """SELECT * FROM dbo.[Provincias]"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    filas = cursor.fetchall()

    cursor.close()
    ConexionDB.closeConnection(con)

    provincias = []
    for fila in filas:
        provinciaId = fila[0]
        nombre = fila[1]

        categoria = ProvinciaModelo(provinciaId, nombre)
        provincias.append(categoria)

    return provincias

def obtenerProvincia(id): 
    con = ConexionDB.getConnection()
    sqlQuery = f"""SELECT * FROM dbo.[Provincias]
                WHERE ProvinciaId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    fila = cursor.fetchone()
    cursor.close()
    ConexionDB.closeConnection(con)

    nombre = fila[1]

    return ProvinciaModelo(id, nombre)