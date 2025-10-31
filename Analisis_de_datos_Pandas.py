#Análisis de datos reales con Pandas
import pandas as pd

#Exportamos el archivo CSV que vamos a usar
url= './Recursos/netflix_titles_CLEANED.csv'
tabla = pd.read_csv(url)


#Borra duplicados y filas vacias
tabla = tabla.dropna().drop_duplicates()

#Creamos el diccionar de cabeceras
cabeceras = tabla.head(0)
dic_cabeceras = dict(enumerate(cabeceras))

#Inicializamos la condicion del bucle
inicio = True

#Funciones 

#Permite ver las cabeceras
def ver_cabeceras():
    limpiar_consola()
    for indice, l in enumerate(cabeceras):
        print(indice, l)

#Permite filtrar por cabecera
def filtrar_por_cabecera():
    ver_cabeceras()
    print("----------------------------------------------------------------")
    print("Elija una cabecera")
    try:
        cabecera = int(input("->"))
    except:
        print("Debe ingresar un número válido.")
        return   
    cabeceraElegida = dic_cabeceras.get(int(cabecera),"Cabecera Inexistente")
    if(cabeceraElegida):
        print("----------------------------------------------------------------")       
        print("Ingrese "+cabeceraElegida)
        nombre = input("->")
        print("----------------------------------------------------------------")
        tablaDinamica = tabla[tabla[cabeceraElegida] == nombre]
        print(tablaDinamica)
        print("----------------------------------------------------------------")
        print("Desea exportar a Excel? Y/N")
        resultado = input("->")
        if(resultado.lower() == 'y' ):
            exportar_Excel(tablaDinamica)
        else:
            limpiar_consola() 
    else:
        filtrar_por_cabecera()
 
#Agrupa el contenido de la cabecera
def agrupar_por_cabecera():
    ver_cabeceras()
    print("----------------------------------------------------------------")
    print("Elija una cabecera")
    try:
        cabecera = int(input("->"))
    except:
        print("Debe ingresar un número válido.")
        return   
    print("----------------------------------------------------------------")
    cabeceraElegida = dic_cabeceras.get(cabecera,"Cabecera Inexistente")
    if(cabeceraElegida):
        tablaDinamica = tabla.groupby(cabeceraElegida)[cabeceraElegida].count().reset_index(name='cantidad')   
        print(tablaDinamica)
        print("----------------------------------------------------------------")
        print("Desea exportar a Excel? Y")
        resultado = input("->")
        if(resultado.lower() == 'y' ):
            exportar_Excel(tablaDinamica)
        else:
            limpiar_consola() 
    else:
        limpiar_consola()
        filtrar_por_cabecera()

#Exporta a Excel el CSV completo           
def exportar_Excel(tabla_exportar = tabla, nombre='Resultado.xlsx'):
    tabla_exportar.to_excel(f"./Recursos/{nombre}")
    limpiar_consola()
    print(f"Exportacion finalizada, nombre del archivo: {nombre}")
    print("----------------------------------------------------------------")

#Sale de la Aplicacion
def salir():
    global inicio
    inicio = False      

#Inicializamos el diccionario de las acciones
tabla_acciones = {
        '0': salir,
        '1': ver_cabeceras,
        '2': filtrar_por_cabecera,
        '3': agrupar_por_cabecera,
        '4': exportar_Excel
    }

#Permite ejecutar las funciones del diccionario
def usa_switch(decimal):
    accion = tabla_acciones.get(decimal)
    if accion:
        accion()
    else:
        print("Opcion Invalida")

#Limpia la consola
def limpiar_consola():
    print("\033c", end="")

#Inicia el bucle con las opciones
while inicio == True:
    print("----------------------------------------------------------------")
    print("Elija las opciones:")
    print("----------------------------------------------------------------")
    print("1-Ver Cabeceras")
    print("2-Filtrar por Cabecera")
    print("3-Agrupar por Cabecera")
    print("4-Exportar a Excel")
    print("0-Salir")
    try:
        opcion = input("->")
    except ValueError: 
        print("Debe ingresar un número válido.") 
    print("----------------------------------------------------------------")
    usa_switch(opcion)
