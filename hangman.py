import random
import time

def instrucciones():
    print ("El ordenador va a elegir una palabra al azar. Tú tendrás que adivinar la palabra eligiendo en cada turno una letra.")
    print ("Si la letra es correcta se revelará de la palabra, en caso contrario, se te restará un intento.")
    print ("Si fallas tu muñeco se acercará más a su muerte.")
    
def palabra_elegida():
    número_aleatorio = random.randint(0,4)
    lista_de_palabras = ["hojas","apego","cielo","cajon","lapiz"]
    palabra_elegida = lista_de_palabras[número_aleatorio]
    return palabra_elegida

def letras_palabra_elegida(palabra_elegida):
    letras_elegidas =  list(palabra_elegida)
    return letras_elegidas

def comprobar_repeticiones (input_jugador,repeticiones):
    for repetición in repeticiones:
        if input_jugador == repetición:
            return True

def comprobar_errores (input_jugador):
    if input_jugador.isalpha == True or len(input_jugador) >= 2:
        return True
    
def comprobar_resultado(input_jugador,letras):
    i = 0
    while i < len(letras):
        if input_jugador == letras[i]:
           return i
           i = 7
        i +=1
    if i == 5:
        return -1
       
       
def imagen_juego (turnos_restantes): 
    imagen = ["\n|\n|\n|\n_","\n|--|\n0  |\n   |\n   _","\n|--|\n0  |\n|  |\n  _","\n|--|\n0  |\n|  |\n|  _","\n|--|\n0  |\n|- |\n|  _","\n|--|\nx  |\n|- |\n|  _"]
    indice = 5-turnos_restantes
    return imagen[indice]

def mostrar_resultado (solución,repeticiones,turnos_restantes):
    imagen = imagen_juego(turnos_restantes)
    resultado = """
          {}
          Intentos restantes: {}
          Solución: {}
          Letras utilizadas:{}
                """.format(imagen,turnos_restantes,solución,repeticiones)
    print (resultado)
    
def comprobar_final(error,repitición,posición):
    if error == True:
        return -2
    elif repetición == True:
        return -3
    else:
        return posición
    
turnos_restantes = 5
palabra = palabra_elegida()
letras = letras_palabra_elegida(palabra)
solución = ["* ", "* ", "* ", "* ", "* "]
aciertos = 0
repeticiones = []

instrucciones()
imagen_juego(turnos_restantes)

while turnos_restantes > 0:
     if turnos_restantes == 0:
        mostrar_resultado(solución,repeticiones,turnos_restantes)
        print("Este es tu resultado final. La palabra que buscabas era {}. Gracias por jugar.".format(palabra))
    
     if aciertos == 5:
         mostrar_resultado(solución,repeticiones,turnos_restantes)
         print("¡Felicidades! ¡Lo has conseguido! La palabra era {}".format(palabra))
         exit()
        
     intento = input("Introduce una letra para jugar: ")
     error = comprobar_errores(intento)
     repetición = comprobar_repeticiones(intento,repeticiones)
     posición = comprobar_resultado(intento,letras)
     comprobación_final = comprobar_final(error,repetición,posición)
     
     if comprobación_final == -2:
        print("Algo ha salido mal, vuelve a intentarlo.")
        
     elif comprobación_final == -3:
        print("Esa letra ya la has intentado. Vuelve a probar.")
        
     if comprobación_final >= 0:
       solución[posición] = intento
       repeticiones.append(intento)
       aciertos += 1
       mostrar_resultado(solución,repeticiones,turnos_restantes)
       
     elif comprobación_final == -1: 
       repeticiones.append(intento)
       turnos_restantes -= 1
       mostrar_resultado(solución,repeticiones,turnos_restantes)
    
     
   


