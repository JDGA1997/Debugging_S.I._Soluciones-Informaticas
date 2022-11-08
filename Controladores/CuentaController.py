# get Index() -> returns View() --> Home/Account
# post RegistrarCuenta(info) -> si todo ok, redirige al Index()
# ValidarDatos(info) -> return bool (método privado para Login())
# get Login(usuario, contrasenia) -> returns View() --> la vista Home/Index
# get Logout(Usuario) -> returns View() --> la vista Home/Index

from DAOs import UsuarioDAO, ProductoDAO
import Vistas

def Index():
    return Vistas.Cuenta.inicio()

def RegistrarCuenta(infoUsuario):
    if ValidarDatos(infoUsuario.email, infoUsuario.usuario, infoUsuario.contrasenia, infoUsuario.repetirContrasenia):
        UsuarioDAO.insertarUsuario(infoUsuario)
        return Vistas.Home.inicio()
    else:
        return Vistas.Cuenta.mensajeError()   

def ValidarDatos(email, usuario, contrasenia, repetirContrasenia):
    if (contrasenia == repetirContrasenia):
        u = UsuarioDAO.obtenerUsuarioPorNombreUsuario(usuario)
        return u is not None and u.getEmail().__eq__(email)
    else:
        return False