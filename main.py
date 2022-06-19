import pandas as pd
import encontrar_similitud
import escenarios
#creo un df para grabar los datos en un csv
df = pd.read_csv("resultados.csv",delimiter=';')

#obtengo las rutas de las imagenes del dataset original, solo las originales, las que no llevan _
images=[]
#para cada imagen de las originales
for image in images:
    #obtengo las rutas de todas sus modificaciones
    modificaciones=escenarios.aplicarModificaciones(image)
    #para cada ruta de imagen modificacada
    for modificada in modificaciones:
        #obtengo el tipo de escenario
        tipo_escenario = escenarios.obtenerEscenario(modificada)
        #calculo los resultados de aplicar los metodos entre ella y la imagen original
        resultados=encontrar_similitud.aplicar_metodos(image,modificada)
        #escribo en el csv los resultados
        df.loc[len(df.index)] = [image,modificada,tipo_escenario,resultados[0][1],resultados[1][1],resultados[2][1],resultados[3][1],
        resultados[4][1],resultados[5][1],resultados[6][1],resultados[7][1],resultados[8][1],resultados[9][1],resultados[10][1]]



#exportar el csv
df.to_csv('resultados_acabado.csv')
