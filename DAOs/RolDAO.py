from Modelos.RolModelo import RolModelo
import ConexionDB

def obtenerTodosRoles():
    con = ConexionDB.getConnection()
    sqlQuery = """SELECT * FROM dbo.[Roles]"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    filas = cursor.fetchall()

    cursor.close()
    ConexionDB.closeConnection(con)

    roles = []
    for fila in filas:
        rolId = fila[0]
        nombre = fila[1]

        rol = RolModelo(rolId, nombre)
        roles.append(rol)

    return roles

def obtenerRol(id): 
    con = ConexionDB.getConnection()
    sqlQuery = f"""SELECT * FROM dbo.[Roles]
                WHERE RolId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    fila = cursor.fetchone()
    cursor.close()
    ConexionDB.closeConnection(con)

    nombre = fila[1]

    return RolModelo(id, nombre)