import pandas as pd
import encontrar_similitud
import escenarios
#creo un df para grabar los datos en un csv
df = pd.read_csv("resultados.csv",delimiter=';')

#cojo una imagen y le aplico los 5 escenarios, se me devuelve un vector con los 5 path

#para cada imagen en el path:

#ejemplo entre un par- hay que expandirlo a n comparativas
path1='imagenes\img1.jpg'
path2='imagenes\img4.jpg'
tipo_escenario=escenarios.obtenerEscenario(path2)
#aplico todos los métodos de similitud entre las dos imagenes
resultados=encontrar_similitud.aplicar_metodos(path1,path2)
#escribo los resultados de este experimento en el csv
df.loc[len(df.index)] = [path1,path2,tipo_escenario,resultados[0][1],resultados[1][1],resultados[2][1],resultados[3][1],
resultados[4][1],resultados[5][1],resultados[6][1],resultados[7][1],resultados[8][1],resultados[9][1],resultados[10][1]]





#exportar el csv
df.to_csv('resultados_acabado.csv')
