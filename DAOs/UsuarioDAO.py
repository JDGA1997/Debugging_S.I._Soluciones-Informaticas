from Modelos.UsuarioModelo import UsuarioModelo
import ConexionDB, ProvinciaDAO, CategoriaDAO, RolDAO

def insertarUsuario(usuario):
    con = ConexionDB.getConnection()
    sqlQuery = """INSERT INTO dbo.[Usuarios] (Nombre, Apellido, Email, Usuario, Contrasenia, FechaNacimiento, ProvinciaId, Dni, Telefono, CategoriaId, RolId)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    record = ({usuario.getNombre()}, {usuario.getApellido()}, {usuario.getEmail()}, 
            {usuario.getUsuario()}, {usuario.getContrasenia()}, {usuario.getFechaNac()}, 
            {usuario.getProvincia().getProvinciaId()}, {usuario.getDni()}, {usuario.getTelefono()},
            {usuario.getCategoria().getCategoriaId()}, {usuario.getRol().getRolId()})
    cursor = con.cursor()
    cursor.execute(sqlQuery, record)
    cursor.close()
    ConexionDB.closeConnection(con)

def obtenerTodosUsuarios():
    con = ConexionDB.getConnection()
    sqlQuery = """SELECT * FROM dbo.[Usuarios]"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    filas = cursor.fetchall()

    cursor.close()
    ConexionDB.closeConnection(con)

    usuarios = []
    provincias = ProvinciaDAO.obtenerTodasProvincias()
    categorias = CategoriaDAO.obtenerTodasCategorias()
    roles = RolDAO.obtenerTodosRoles()

    for fila in filas:
        usuarioId = fila[0]
        nombre = fila[1]
        apellido = fila[2]
        email = fila[3]
        usuario = fila[4]
        contrasenia = fila[5]
        fechaNac = fila[6]
        provinciaId = fila[7]
        dni = fila[8]
        tel = fila[9]
        categoriaId = fila[10]
        rolId = fila[11]

        for p in provincias:
            if p.getProvinciaId() == provinciaId:
                provincia = p
                break
        for c in categorias:
            if c.getCategoriaId() == categoriaId:
                categoria = c
                break
        for r in roles:
            if r.getRolId() == rolId:
                rol = r
                break
        usuario = UsuarioModelo(usuarioId, nombre, apellido, email, usuario, contrasenia, dni, provincia, tel, rol, categoria, fechaNac)
        usuarios.append(usuario)

    return usuarios 

def obtenerUsuario(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""SELECT * FROM dbo.[Usuarios]
                WHERE UsuarioId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    fila = cursor.fetchone()
    cursor.close()
    ConexionDB.closeConnection(con)

    nombre = fila[1]
    apellido = fila[2]
    email = fila[3]
    usuario = fila[4]
    contrasenia = fila[5]
    fechaNac = fila[6]
    provinciaId = fila[7]
    dni = fila[8]
    tel = fila[9]
    categoriaId = fila[10]
    rolId = fila[11]

    provincia = ProvinciaDAO.obtenerProvincia(provinciaId)
    categoria = CategoriaDAO.obtenerCategoria(categoriaId)
    rol = RolDAO.obtenerRol(rolId)

    return UsuarioModelo(id, nombre, apellido, email, usuario, contrasenia, dni, provincia, tel, rol, categoria, fechaNac)


def eliminarUsuario(id):
    con = ConexionDB.getConnection()
    sqlQuery = f"""DELETE FROM dbo.[Usuarios]
                WHERE UsuarioId = {id}"""
    cursor = con.cursor()
    cursor.execute(sqlQuery)

    cursor.close()
    ConexionDB.closeConnection(con)

def modificarUsuario(usuario):
    con = ConexionDB.getConnection()
    sqlQuery = f"""UPDATE dbo.[Usuarios] SET 
                Nombre = {usuario.getNombre()}, 
                Apellido = {usuario.getApellido()}, 
                Email = {usuario.getEmail()}, 
                Usuario = {usuario.getUsuario()},
                Contrasenia = {usuario.getContrasenia()},
                FechaNacimiento = {usuario.getFechaNac()},
                ProvinciaId = {usuario.getProvincia().getProvinciaId()},
                Dni = {usuario.getDni()}, 
                Telefono = {usuario.getTelefono()}, 
                CategoriaId = {usuario.getCategoria().getCategoriaId()}, 
                RolId = {usuario.getRol().getRolId()}"""
    
    cursor = con.cursor()
    cursor.execute(sqlQuery)
    cursor.close()
    ConexionDB.closeConnection(con)