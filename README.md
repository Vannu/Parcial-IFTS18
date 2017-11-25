# Parcial - IFTS18
Informe
==========


Aplicación web creada para la consulta de base de datos de la droguería FarmaSoft.

FLUJO DEL PROGRAMA:
-------------------
El sistema cuenta con una página inicio y un menú para acceder a la cuenta o la creación del mismo. Una vez ingresado se accede a una página en donde podrás hacer diferentes consultas al sistema y visualizar la base de datos de la empresa.

ESTRUCTURA DE LA INFORMACION:
-----------------------------
Consta de dos archivos CSV en donde contiene los datos de la base de datos y los nombres de usuarios con sus respectivas contraseñas.
La aplicación consta de distintos archivos .py (app.py, archivo.py, forms.py pruebas.py), en la carpeta templates están contenidos los archivos .html (para la visualización del programa) y dentro de la carpeta static que contiene la hoja de estilo.

UTILIZACION EL PROGRAMA:
------------------------
Atreves de la página de inicio el usuario se puede logearse (Ingresar) o si no tiene cuenta, puede crear uno (Registrarse), las opciones son visibles desde el menú superior.
Una vez que allá accedido se redirecciona a nueva página, en esta se visualizará otro menú, en donde el usuario podrá realizar distintas consultas.
Las consultas le permitirán al usuario a visualizar la base de datos de la empresa, hacer búsqueda de clientes por productos, búsqueda de productos por clientes, ver los mejores clientes y c los productos más vendidos.
El programa también cuenta con la opción de salir del sistema.


CLASES UTILIZADAS:
------------------
En el programa se utilizan seis clases; dos clases son utilizadas para el login (RegistrarForm) y registración del usuario (LoginForm), dos clases para la búsqueda de clientes (Consulta_Cliente) y búsqueda de productos (Consulta_Producto) y otras dos clases para la excepcion (CSVError) y para validar los errores del archivo (validarCSV).
