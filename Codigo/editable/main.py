from operator import mod
import os
from pyexpat import model
import numpy as np # numpy
import cv2  # biblioteca de open cv


def leer_directorio(isTraining:bool):

    if isTraining:
        entrenamientoPath=os.path.join("..","entrenamiento")
        # Leemos los archivos de entrenamiento
        carpetas=os.listdir(entrenamientoPath)
        # Leemos cada uno de los modelos de entrenamiento
        print(carpetas)
        for subcarpeta in carpetas:
            ruta=os.path.join(entrenamientoPath,subcarpeta)

            print(ruta)
            modelo=crear_modelo(ruta)
            print(modelo.shape)

            # Guardamos el modelo entrenado en un cvs
            nombre_modelo="{0}en.csv".format(subcarpeta)
            np.savetxt(nombre_modelo, modelo,fmt='%s', delimiter=",")
            """ with open(nombre_modelo, "w") as f:
                #f.write(b'ImageId,Label\n')
                numpy.savetxt(f, result, fmt='%s', delimiter=",") """
            
            # crear imagen
            # dimensiones y,x
            imagen=np.zeros((32,32),dtype=np.intc)
            modelo=list(modelo)
            for j in range (32):
                for i in range(32):
                    imagen[j,i]=modelo.pop(0)
            
            # Creamos imagen
            cv2.imwrite("ne1.jpg",imagen)


        
        
def leer_imagen(nombre_archivo:str)->list[int]:
    print(nombre_archivo)
    img = cv2.imread(nombre_archivo,0) # espacio de color BGr, pero con el 0 es gray
    dimensionY,dimensionX=img.shape
    dimension=dimensionX * dimensionY
    histograma:list[int]=[]

    

    # funcion shape
    #It returns a tuple of the number of rows, columns, and channel
    # y,x,canal

    # acceder a un pixel
    #px =img[10,15] # y=10,x=15
    for j in range(0,dimensionY):
        for i in range(0,dimensionX):
            histograma.append(img[j,i])

    ac=nombre_archivo.split("\\")[-1]
    np.savetxt("p"+ac + '.csv', histograma,fmt='%s', delimiter=",")
    
    return histograma


def crear_modelo(rutaCarpeta:str):
    carpeta_actual=os.listdir(rutaCarpeta)
    #print(carpeta_actual)
    numImagenes=len(carpeta_actual)
    histogramaPromedio=np.zeros(1024,dtype=np.int8)
    
    for imagen in carpeta_actual:
        rutaImagen=os.path.join(rutaCarpeta,imagen)
        print(rutaImagen)
        lecturaImagen=leer_imagen(rutaImagen)

        print(lecturaImagen[0])
        # Convertimos el arreglo a un np.array
        histogramaActual=np.asanyarray(lecturaImagen)
        print(histogramaActual)

        histogramaPromedio=histogramaPromedio+histogramaActual

    # Para ser pormedio tenemos que dividirlo entre el número de imagenes
    print(histogramaPromedio)

    histogramaPromedio= histogramaPromedio/numImagenes 

    #El arreglo ahora es flotante, por tanto vamos a convertirlo a int
    histogramaPromedio=histogramaPromedio.astype(int)
    return histogramaPromedio



def main():
    pass

if __name__ == "__main__":
    leer_directorio(True)