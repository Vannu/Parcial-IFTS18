import pandas as pd
import csv

#UTILIZO LA LIBRERIA DE PANDAS PARA FACILITAR EL USO DE DATOS

#guardo el orden de las columnas en una variable
head=['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']


def cargar_archivo(farmacia):
    """ Se lee el archivo y lcon el metodo as_matrix retorno las columnas que yo quiero """
    with open('farmacia.csv')as archivo:
         datos=pd.read_csv(archivo)        
         cols = datos.as_matrix(columns=head)
         return cols

#Consulta de productos mas vendidos   
def nproductos(farmacia):
    """ con el método 'groupby()' Agrupo los datos de la columna CODIGO Y PRODUCTO """
    """ com el método 'sort_values()' ordenamos los resultado de mayor a menor de la columna CANTIDAD """
    """ con la funcion de head especifico la cantidad de datos a mostrar """ 
    """ con el metodo as_matrix retorno las columnas """

    df = pd.read_csv('farmacia.csv')   
    datos = df.groupby(by=['CODIGO','PRODUCTO'], as_index=False).sum()
    datos = datos.sort_values(by=['CANTIDAD'], ascending=False)
    datos = datos.head(10)
    datos = datos.as_matrix(columns=['CODIGO', 'PRODUCTO', 'CANTIDAD'])
    return datos

#Consulta de los mejores clientes   
def nclientes(farmacia):
    """ Multiplico los datos del las 2 columnas, los resultados los guardo en lo que va a hacer una nueva columna 'TOTAL' """
    """ los datos de 'TOTAL' son pasados a enteros""" 
    """ Agrupo los datos de la columna CODIGO Y PRODUCTO """
    """ ordenamos los resultado de mayor a menor de la columna 'TOTAL' """
    """ specifico la cantidad de datos a mostrar """
    """  retorno las columnas """
    df = pd.read_csv('farmacia.csv')   
    df['total']= df['CANTIDAD']*df['PRECIO']
    df['total'] = df['total'].astype(int)  
    datos = df.groupby(by=['CODIGO','CLIENTE'], as_index=False).sum()
    datos = datos.sort_values(by=['total'], ascending=False)
    datos = datos.head(10)
    datos = datos.as_matrix(columns=['CODIGO', 'CLIENTE', 'total'])
    return datos

#Consulta de productos por cliente
def productos_por_clientes(Consulta_Cliente):
    """ Comparo si los datos de la columna 'CLIENTE' si es igual a los datos introducidos por medio del formulario forms """
    """ Agrupo los datos de las columnas a mostrar """  
    """  retorno las columnas """
    df = pd.read_csv('farmacia.csv') 
    data_cliente = df[df.CLIENTE == Consulta_Cliente]
    data_cliente = data_cliente.groupby(by=['CODIGO', 'PRODUCTO', 'CLIENTE'], as_index=False).sum()
    data_cliente = data_cliente.as_matrix(columns=['CODIGO', 'PRODUCTO', 'CLIENTE'])
    return data_cliente

#Consulta de clientes por productos
def clientes_por_productos(Consulta_Producto):
    """ Comparo los datos de la columna 'PRODUCTO' si es igual a los datos introducidos por medio del formulario forms """
    """ Agrupo los datos de las columnas a mostrar """  
    """  retorno las columnas """    
    df = pd.read_csv('farmacia.csv') 
    data_producto = df[df.PRODUCTO == Consulta_Producto]
    data_producto = data_producto.groupby(by=['CODIGO', 'PRODUCTO', 'CLIENTE'], as_index=False).sum()
    data_producto = data_producto.as_matrix(columns=['CODIGO', 'PRODUCTO', 'CLIENTE'])
    return data_producto

#listado de clientes y productos

def lista_clientes():
    """ lista de clientes  """    
    df = pd.read_csv('farmacia.csv') 
    listaclientes = df['CLIENTE']
    return  listaclientes

def lista_productos():
    """  lista de productos """    
    df = pd.read_csv('farmacia.csv') 
    listaproductos = df['PRODUCTO']
    return  listaproductos

