function validarSuscribe() 
{
    let x = document.forms["suscripcion"]["suscribe"].value;
    if (x == "") {
      alert("Debes ingresar una dirección de correo");
      return false;
    }
    else
    {
        alert("Suscripto correctamente");
        return true;
    }
}

function validarLogin() 
{
    let usuario = document.forms["login"]["usuario"].value;
    let contrasena = document.forms["login"]["contrasena"].value;
    if (usuario == "" || contrasena == "") {
      alert("Debes ingresar un usuario y/o contrasena");
      return false;
    }
    else if(usuario.length<8)
    {
        alert("Nombre de usuario muy corto");
        return false;
    }
    else if(contrasena.length<8)
    {
        alert("Contraseña muy corta");
        return false;
    }
    else
    {
        alert("Suscripto correctamente");
        return true;
    }
    
}

function validarRegistro() 
{
    let nombre = document.forms["registro"]["nombre"].value;
    let apellido = document.forms["registro"]["apellido"].value;
    let email = document.forms["registro"]["email"].value;
    let telefono = document.forms["registro"]["telefono"].value;
    let dni = document.forms["registro"]["dni"].value;
    let usuario = document.forms["registro"]["usuario"].value;
    let contrasena = document.forms["registro"]["contrasena"].value;
    let recontrasena = document.forms["registro"]["recontrasena"].value;
    if (usuario == "" || contrasena == "" || recontrasena == "" || nombre == "" || apellido == "" || email == "" || telefono == "" || dni == "") {
      alert("Debe completar todos los campos del formulario");
      return false;
    }
    else if(usuario.length<8)
    {
        alert("Nombre de usuario muy corto, debe tener mínimo 8 caracteres");
        return false;
    }
    else if(contrasena.length<8)
    {
        alert("Contraseña muy corta, debe tener mínimo 8 caracteres");
        return false;
    }
    else if(contrasena != recontrasena)
    {
        alert("Fallo la confirmación de la contraseña");
        return false;
    }
    else if(dni<1000000 || dni>99000000)
    {
        alert("Numero de DNI incorrecto");
        return false;
    }
    else
    {
        alert("Registrado correctamente");
        return true;
    }
    
}