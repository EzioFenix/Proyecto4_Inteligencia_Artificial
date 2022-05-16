from email.mime import image
from importlib.util import module_from_spec
from operator import le, mod
import os
from pyexpat import model
import random
from cv2 import line
import numpy as np # numpy
import cv2  # biblioteca de open cv
import time

"""
Lee una imagen en la dirección que se le de como paramétro y la pasa a un arreglo unidimensional, donde los valores van del 0-255 es decir que estan en blanco y negro
- Parametro:
    Ruta de la imagen
    Ejemplo:
        "carpeta/imagen1.png"
- Return:
    Arreglo unidimensional con valores de 0-255 en escalas de grises, de los pixeles de la imagen
    Ejemplo:
        [255,255,255,0,1,...,244]
"""
def leer_imagen(nombre_archivo:str)->list[int]:
    histograma:list[int]=[]
    dimensionX:int
    dimensionY:int

    img = cv2.imread(nombre_archivo,0) # espacio de color BGr, pero con el 0 es gray´
    #It returns a tuple of the number of rows, columns, and channel
    dimensionY,dimensionX=img.shape

    # acceder a un pixel
    #px =img[10,15] # y=10,x=15
    for j in range(0,dimensionY):
        for i in range(0,dimensionX):
            histograma.append(img[j,i])

    # en caso de ver el resultado activar este código
    """ ac=nombre_archivo.split("\\")[-1]
    nombre,tipo= ac.split(",")
    np.savetxt(nombre + '.csv', histograma,fmt='%s', delimiter=",") """
    
    return histograma


"""
Oscurece la imagen de acuerdo al intervalo dado, si el intervalo es 15, aquellos que tengan menor que el intervalo se volverán negro.
- Por default el valor esta en 30
"""
def oscurecer(histograma:list[int],intervalo:int=48)-> list[int]:
    nuevoHistograma:list[int]=[]

    for px in histograma:
        if px<intervalo:
            nuevoHistograma.append(0)
        elif 255-40<px:
            nuevoHistograma.append(255)
        else:
            nuevoHistograma.append(px)
    return nuevoHistograma

    

    for elemento in histograma:
        if  intervalo< elemento:
            nuevoHistograma.append(255)
        else:
            nuevoHistograma.append(0)

    return nuevoHistograma


"""
Regresa el número de la opción seleccionada del menu
"""
def menu()->int:
    opciones=["Salir","Entrenar modelos","Cargar modelos","Clasificar imagen","Realizar test presición"]
    opcion:str
    opcionValida=False # Para saber si la opción que eleigío es valida

    while not opcionValida:
        for i in range(len(opciones)):
            print('{:<8} {:<20s}'.format(str(i),opciones[i]))

        print("Introduce el número de la opción que deseas ejecutar")
        # introducir opcion
        opcion=input("")

        if not opcion.isdigit():
            print("Tienes que introducir un número, intenta de nuevo")
            time.sleep(1)
            os.system("cls")
        else:
            opcion:int=int(opcion.strip())
            if 0<=opcion and opcion<len(opciones):
                opcionValida=True
                return opcion
            else:
                print("opción no valida,intente de nuevo")
                time.sleep(1)
                os.system("cls")


"""
Genera un modelo de un tipo de imagenes
Parametros:
    - rutaCarpeta: es la dirección donde se encuentran las imagenes con las cuales se entrenará el modelo
        Ejemplo: "../entrenamiento/1"
Return:
    - Regresa un np.ndarray de una dimensión que contiene los valores en escala de grises del 0 al 255,las dimensiones son x por y=z por ejemplo 32x32=1024 [255,255,0,...,0]
 
"""
def crear_modelo(rutaCarpeta:str)->np.ndarray:
    carpeta_actual=os.listdir(rutaCarpeta)
    numImagenes=len(carpeta_actual)
    histogramaPromedio=np.zeros(1024,dtype=np.int8)
    
    for imagen in carpeta_actual:
        rutaImagen=os.path.join(rutaCarpeta,imagen)
        lecturaImagen=leer_imagen(rutaImagen)

        # Convertimos el arreglo a un np.array
        histogramaActual=np.asanyarray(lecturaImagen)

        histogramaPromedio=histogramaPromedio+histogramaActual

    # Para ser pormedio tenemos que dividirlo entre el número de imagenes
    histogramaPromedio= histogramaPromedio/numImagenes 

    #El arreglo ahora es flotante, por tanto vamos a convertirlo a int
    histogramaPromedio=histogramaPromedio.astype(int)
    return histogramaPromedio


"""
Genera los modelos entrenados en la carpeta de entrenados
Return:
    - lista con las direcciones de los archivos generados
    Ejemplo: ["../entrenado/img1.png","../entrenado/img2.png"]
"""
def generarModelos()->list[str]:
    direccionModelos:list[str]=[]

    entrenamientoPath=os.path.join("..","entrenamiento")
    # Leemos los archivos de entrenamiento
    carpetas=os.listdir(entrenamientoPath)
    # Leemos cada uno de los modelos de entrenamiento
    for subcarpeta in carpetas:
        ruta=os.path.join(entrenamientoPath,subcarpeta)

        modelo=crear_modelo(ruta)

        """# Guardamos el modelo entrenado en un cvs
        nombre_modelo="{0}en.csv".format(subcarpeta)
        np.savetxt(nombre_modelo, modelo,fmt='%s', delimiter=",")
            with open(nombre_modelo, "w") as f:
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
        nombreNuevo=os.path.join("..","entrenado",subcarpeta+".jpg")
        cv2.imwrite(nombreNuevo,imagen)

        #agregamos a la lista de archivos
        direccionModelos.append(nombreNuevo)
    return direccionModelos


def cargarImagen()->str:
    rutaInput=os.path.join("..","input")
    archivos=os.listdir(rutaInput)
    opcion:str
    opcionValida=False # Para saber si la opción que eleigío es valida

    # mostar imagenes
    while not opcionValida:
        for i in range(len(archivos)):
            print('{:<8} {:<20s}'.format(str(i),archivos[i]))

        print("Introduce el número de la imagen")
        # introducir opcion
        opcion=input("")

        if not opcion.isdigit():
            print("Tienes que introducir un número, intenta de nuevo")
            time.sleep(1)
            os.system("cls")
        else:
            opcion:int=int(opcion.strip())
            if 0<=opcion and opcion<len(archivos):
                opcionValida=True
                return os.path.join(rutaInput,archivos[opcion])
            else:
                print("opción no valida,intente de nuevo")
                time.sleep(1)
                os.system("cls")
    

def cargarModelos()->list[str]:
    rutaEntrenados=os.path.join("..","entrenado")
    archivos=os.listdir(rutaEntrenados)
    archivosValidos:list[str]=[] # Archivos que si son .jpg

    # Agregamos las rutas de los archivos de modelo validos en la carpeta de entrenamiento
    for archivo in archivos:
        if archivo.endswith(".jpg"):
            ruta=os.path.join(rutaEntrenados,archivo)
            archivosValidos.append(ruta)
    return archivosValidos
    
"""
Calcula la probabilidad a posterior de los pixeles de una imagen
Parametros:
    - Modelo: es la imagen de modelo, en este caso esta leido de una imagen con openCv en una un arreglo de 1 dimensión
    - Imagen: es un imagen leida con openCv en arreglo de 1 dimensión
"""
def obtenerProbabilidadPosteri(modelo:list[int],imagen:list[int]):
    resta:list[int]=[]
    probabilidad:float=0.0
    for i in range(len(modelo)):
        resta.append(abs(modelo[i]-imagen[i]))

    for i in resta:
        probabilidad+=1 -i/255

    return probabilidad /len(modelo)



def clasificarImagen(direccionImagen:str,direccionesModelos:list[str])->str:
    modeloActual:list[int]

    for direccion in direccionesModelos:
        img=cv2.imread(direccionImagen)
        dimensionY=img.shape[0]
        dimensionX=img.shape[1]
        redimensionar(direccion,dimensionX,dimensionY)

    
    imagenActual:list[int]=leer_imagen(direccionImagen)
    imagenActual=oscurecer(imagenActual)
    probabilidadMayor=0.0
    probababilidadesModelos=[int]

    probabilidadApriori:float=1/len(direccionesModelos)


    for direccion in direccionesModelos:
        modeloActual=leer_imagen(direccion)
        modeloActual=oscurecer(modeloActual)
        probabilidadActual=obtenerProbabilidadPosteri(modeloActual,imagenActual) 
        probababilidadesModelos.append(probabilidadActual)

        if probabilidadMayor<=probabilidadActual:
            probabilidadMayor=probabilidadActual

    # Mostrar resultado
    indiceResultado=probababilidadesModelos.index(probabilidadMayor)
    nombreResultado=direccionesModelos[indiceResultado-1]
    print(f"Tu imagen es: {nombreResultado}")
    print(f"La probabilidad es: {probabilidadMayor *probabilidadApriori}")
    print(f"La probabilidad de coincidencia es :{probabilidadMayor}")

    return nombreResultado
        

def redimensionar(direccionImagen:str,nuevoX:int,nuevoY:int)->None:
    img=cv2.imread(direccionImagen)
    dimensionX,dimensiony,ne= img.shape
    if not(dimensionX==nuevoX and dimensiony==nuevoY):
        res= cv2.resize(img, dsize=(nuevoX, nuevoY), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(direccionImagen,res)
        print("cambio tamaño completado ...")


def sublista_Aleatoria(lista:list[str],numSeleccionados:int)->list[str]:
    num=len(lista)-1
    listaResultado=[]
    
    while len(listaResultado) <numSeleccionados:
        numAleatorio=random.randint(0,num)
        listaResultado.append(lista.pop(numAleatorio))
        num-=1

    return listaResultado  
    



def crear_modeloPrecicion(rutaCarpeta:str,casosEntrenamiento:int,casosPractica:int)->list[np.ndarray,list[str]]:
    carpeta_actual=os.listdir(rutaCarpeta)
    numImagenes=len(carpeta_actual)
    histogramaPromedio=np.zeros(1024,dtype=np.int8)
    
    imagenesPrueba=sublista_Aleatoria(carpeta_actual,casosPractica)
    aux=sublista_Aleatoria(carpeta_actual,casosEntrenamiento)
    carpeta_actual=aux.copy()
    imagenesPrueba_Direccion:list[str]=[]

    # Convertir el nombre de las imagenes en una dirección absoluta
    for imagen in imagenesPrueba:
        imagenesPrueba_Direccion.append(os.path.join(rutaCarpeta,imagen))

    for imagen in carpeta_actual:
        rutaImagen=os.path.join(rutaCarpeta,imagen)
        lecturaImagen=leer_imagen(rutaImagen)

        # Convertimos el arreglo a un np.array
        histogramaActual=np.asanyarray(lecturaImagen)

        histogramaPromedio=histogramaPromedio+histogramaActual

    # Para ser pormedio tenemos que dividirlo entre el número de imagenes
    histogramaPromedio= histogramaPromedio/numImagenes 

    #El arreglo ahora es flotante, por tanto vamos a convertirlo a int
    histogramaPromedio=histogramaPromedio.astype(int)
    return [histogramaPromedio,imagenesPrueba_Direccion]

def generarModeloPrecision(casosEntrenamiento:int,casosPractica:int)->list[list[str],list[str]]:
    direccionModelos:list[str]=[]
    direccionesImagenes:list[str]=[]

    entrenamientoPath=os.path.join("..","entrenamiento")
    # Leemos los archivos de entrenamiento
    carpetas=os.listdir(entrenamientoPath)
    # Leemos cada uno de los modelos de entrenamiento
    for subcarpeta in carpetas:
        ruta=os.path.join(entrenamientoPath,subcarpeta)

        modelo,direcciones=crear_modeloPrecicion(ruta,casosEntrenamiento,casosPractica)

        # Direcciones de imagenes por cada carpeta
        direccionesImagenes.extend(direcciones)
        
        # crear imagen
        # dimensiones y,x
        imagen=np.zeros((32,32),dtype=np.intc)
        modelo=list(modelo)
        for j in range (32):
            for i in range(32):
                imagen[j,i]=modelo.pop(0)
        
        # Creamos imagen
        nombreNuevo=os.path.join("..","entrenado",subcarpeta+".jpg")
        cv2.imwrite(nombreNuevo,imagen)

        #agregamos a la lista de archivos
        direccionModelos.append(nombreNuevo)
    return [direccionModelos,direccionesImagenes]


def testPrecision(casosEntrenamiento:int,casosPractica: int)->None:
    direccionImagenes:list[str]=[]
    direccionModelos:list[str]=[]
    numVerdadero=0

    direccionModelos,direccionImagenes=generarModeloPrecision(casosEntrenamiento,casosPractica)

    print(f"Num: {len(direccionImagenes)}")

    for imagen in direccionImagenes:
        n2=clasificarImagen(imagen,direccionModelos)
        n2=n2.split("\\")[-1]
        n2=n2.split(".")[-2]

        n1=imagen.split("\\")[-2]
        print(f"realidad: {n1} -- prediccion :{n2} resultado {n2==n1}")
        if n2==n1:
            numVerdadero+=1
        
    print(f"La precisión es de : {100 *(numVerdadero/len(direccionImagenes))}%")
    return 100 *(numVerdadero/len(direccionImagenes))

        

def main():
    # variables globales 
    modelosCargados:list[str]=cargarModelos()
    isModelosCargados:bool = 0<len(modelosCargados)# saber si los modelos estan cargados
    imagenCargada:list
    isImagenCargada:bool=False
    direccionImagenCargada:str=""
    opcion=1

    while opcion!=0:
        opcion=menu()
        if opcion==0:
            print("Hasta luego")
            time.sleep(1)
        elif opcion==1:
            print("Entrenanando modelos...")
            if isModelosCargados:
                print("Deseas volver a generar los modelos")
                respuesta=input("s=si,n=no   ")
                respuesta=respuesta.strip()
                if respuesta=="s":
                    modelosCargados=generarModelos()
                    isModelosCargados=True
                    print("Modelos entrenados correctamente")
                elif respuesta=="n":
                    print("esta bien")
                    time.sleep(1)
                else:
                    print("tu respuesta es incorrecta, vuelve a intentar")
                    time.sleep(1)
            else:
                modelosCargados=generarModelos()
                print("Modelos entrenados correctamente")
        elif opcion==2:
            print("Cargar Modelos")
            dirrecciones=cargarModelos()
            if len(dirrecciones)==0:
                print("No habia modelos")
            else:
                print("Se cargarón perfectamente los modelos")
                modelosCargados=dirrecciones
                isModelosCargados=True 
        elif opcion==3:
            print("Clasificar una imagen")
            if isModelosCargados:
                if isImagenCargada:
                    respuesta=input("Desea cargar otra imagen s=si,n=no ")
                    respuesta=respuesta.strip()
                    if respuesta=="s":
                        isImagenCargada=False
                    else:
                        print(f"imagen :{direccionImagenCargada}")
                        inicio=time.process_time()
                        clasificarImagen(direccionImagenCargada,modelosCargados)
                        fin=time.process_time()
                        print(f"El tiempo fue:{fin-inicio} segundos")
                if not isImagenCargada:
                    direccionImagenCargada=cargarImagen()
                    isImagenCargada=True
                    inicio=time.process_time()
                    clasificarImagen(direccionImagenCargada,modelosCargados)
                    fin=time.process_time()
                    print(f"El tiempo fue:{fin-inicio} segundos")
        elif opcion==4:
            print("Realizar test precisión")
            test=[]
            inicio=time.process_time()
            test.append(testPrecision(4,1))
            test.append(testPrecision(5,2))
            test.append(testPrecision(7,3))
            test.append(testPrecision(10,4))
            print(test)
            fin=time.process_time()
            print(f"El tiempo fue:{fin-inicio} segundos")

if __name__ == "__main__":
    #leer_directorio(True)
    # menu()
    main()
    #^