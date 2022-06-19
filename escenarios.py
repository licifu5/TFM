import cv2
import numpy as np
#las modificaciones canalesColor, retocada se han hecho mediante la herramienta photoshop

#aqui se pasa una imagen a los diferentes escenarios a estudiar

def obtenerEscenario(path):
    nombre = path.split("_")
    escenario= nombre.split('.')[0]
    return escenario

#igual
def igual(path):
    original = cv2.imread(path)
    igual = "_igual"
    nombre = path.split(".")
    nuevopath = nombre[0] + igual + ".jpg"
    cv2.imwrite(nuevopath, original)
    return nuevopath

#comprimida
def comprimir(path):
    src = cv2.imread(path)
    # Porcentaje en el que se redimensiona la imagen
    scale_percent = 40
    # calcular el 40 por ciento de las dimensiones originales
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    # cambiar el tamaño de la image
    output = cv2.resize(src, dsize)
    comprimida = "_comprimida"
    nombre = path.split(".")
    nuevopath = nombre[0] + comprimida + ".jpg"
    cv2.imwrite(nuevopath, output)
    return nuevopath


#recortada
def recortar (path):
    img = cv2.imread(path)
    alto = img.shape[0]
    ancho = img.shape[1]
    crop_img = img[int(alto/4):int(3*alto/4),int(ancho/4):int(3*ancho/4)]
    recortado="_recortado"
    nombre=path.split(".")
    nuevopath=nombre[0]+recortado+".jpg"
    cv2.imwrite(nuevopath, crop_img)
    return nuevopath

#rotada
def rotar(path):
    original = cv2.imread(path)
    alto = original.shape[0]
    ancho = original.shape[1]
    M = cv2.getRotationMatrix2D((ancho / 2, alto / 2), 90, 1)
    M[0][2]=0
    M[1][2]=ancho
    new90center = cv2.warpAffine(original, M, (alto, ancho))
    rotado = "_rotado"
    nombre = path.split(".")
    nuevopath = nombre[0] + rotado + ".jpg"
    print(nuevopath)
    cv2.imwrite(nuevopath, new90center)
    return nuevopath




def aplicarModificaciones(path):
    escenarios=[]
    # aplico los cambios que faltan y guardo los path en escenarios
    recortada = recortar(path)
    escenarios.append(recortada)
    rotada = rotar(path)
    escenarios.append(rotada)
    comprimida = comprimir(path)
    escenarios.append(comprimida)
    igualita = igual()
    escenarios.append(igualita)

    #añado los path de las imagenes modificadas via externa
    nombre = path.split(".")
    retocada="_retocada"
    pathRetocada = nombre[0] + retocada + ".jpg"
    escenarios.append(pathRetocada)
    parecida="_parecida"
    pathParecida = nombre[0] + parecida + ".jpg"
    escenarios.append(pathParecida)
    canalesColor="_canalesColor"
    pathCanalesColor= nombre[0] + canalesColor + ".jpg"
    escenarios.append(pathCanalesColor)

    return escenarios