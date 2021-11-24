"""
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:
nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa),
Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada),
volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y
devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.    
"""
#Importación de librearías necesarias
import pandas as pd
from io import open
import matplotlib.pyplot as plt

#Incorporamos el fichero cotizacion.csv a la variable fichero y la leemos con el comando fichero.read()
fichero = open("C:\\Users\\Fran\\Desktop\\Formacion\\python\\Programas de clase\\Pandas\\cotizacion.csv")
texto = fichero.read()

#definimos las variable globales necesarias
df = {}
cabeceras = []
datos=[]
datos_nuevos =[]
lista_total=[]
lista_nombre =[]
lista_final=[]
lista_maximo=[]
lista_minimo=[]
lista_volumen=[]
lista_efectivo=[]

#split para separar las cabeceras de los datos
cabecera_datos = texto.split("\n")
cabecera = cabecera_datos[0].split(";")

#quitamos las cabeceras de los datos
cabecera_datos.remove(cabecera_datos[0])

#separamos los datos en ;
for a in cabecera_datos:
    datos_nuevos.append(a.split(";"))

#generamos una elemento [] dentro de los datos por cada linea en el fichero de datos_nuevos
for t in datos_nuevos:
    lista_nombre.append(t[0])
    lista_final.append(t[1])
    lista_maximo.append(t[2])
    lista_minimo.append(t[3])
    lista_volumen.append(t[4])
    lista_efectivo.append(t[5])
    
#eliminamos la notacion inglesa
for i in range(len(lista_final)):
    lista_final[i] = lista_final[i].replace(",",".")
    lista_maximo[i] = lista_maximo[i].replace(",",".")
    lista_minimo[i] = lista_minimo[i].replace(",",".")
    lista_volumen[i] = lista_volumen[i].replace(".","")
    lista_efectivo[i] = lista_efectivo[i].replace(",",".")

#parseamos string a float e int según necesidad
lista_final_final = [float(i) for i in lista_final]
lista_final_maximo = [float(i) for i in lista_maximo]
lista_final_minimo = [float(i) for i in lista_minimo]
lista_final_volumen = [int(i) for i in lista_volumen]
lista_final_efectivo = [float(i) for i in lista_efectivo]

#añadimos las listas con los datos a la lista total que será el valor del diccionario general
lista_total.append(lista_nombre)
lista_total.append(lista_final_final)
lista_total.append(lista_final_maximo)
lista_total.append(lista_final_minimo)
lista_total.append(lista_final_volumen)
lista_total.append(lista_final_efectivo)

#creamos el diccionario general que tendrá por clave las cabeceras del fichero y como valor las listas procesadas 
for r in range(len(cabecera)):
    df[cabecera[r]]=lista_total[r]

#Creamos DataFrame
df_bueno = pd.DataFrame(df)


#Pintamos gráfica de puntos
fig, ax= plt.subplots(figsize=(50,6))
#Aqui metemos las columnas del datagrama que saldran en el diagrama
ax.scatter( x = df["Nombre"], y = df["Volumen"])
plt.title("Relación empresa/volumen")
fig.subplots_adjust(bottom=0.5)
plt.xticks(rotation = 75)
#Aqui introducimos el nombre de las variables x,y
plt.xlabel("Empresa")
plt.ylabel("Volumen")
#Lo mostramos
plt.show()
