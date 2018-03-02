from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms import validators

#Inicio de Sesion
class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', [validators.data_required(message = "Nombre de usuario")])
    password = PasswordField('Contraseña', [validators.data_required(message = "Ingrese una contraseña")])
    enviar = SubmitField('Ingresar')

#Crear nuevo usuario
class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', [validators.data_required(message = "Ingrese una contraseña")])
    enviar = SubmitField('Registrarse')


#consultas para listar productos y clientes

class Consulta_Cliente(FlaskForm):
    cliente = StringField('Cliente', [validators.data_required(message = "Ingrese producto"), validators.Length(min = 3, message = "Minimo 3 caracteres")])
    busqueda = SubmitField('Buscar')
    
class Consulta_Producto(FlaskForm):
    producto = StringField('Producto', [validators.data_required(message = "Ingrese producto"), validators.Length(min = 3, message = "Minimo 3 caracteres")])
    busqueda = SubmitField('Buscar')


#Cambiar la contraseña de la cuenta usuario

class Nueva_Contrasenia(FlaskForm):

    nContrasenia = PasswordField('Nueva Contraseña',[validators.data_required(),validators.EqualTo("rContrasenia",message = "Debe ingresar la misma contraseña")])
    rContrasenia= PasswordField('Repetir Contraseña', [validators.data_required(message = "Debe ingresar la misma contraseña")])
    submit = SubmitField("Enviar")




