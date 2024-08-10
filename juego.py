import random

def chequear_palabra(palabra, correcta):
    ret = [[l] for l in palabra] # Ej.: [["h", 0], ["o", 1], ["l", 0], ["a", 2]] - 0: gris, 1: amarillo, 2: verde
    for i in range(5): # Chequear verdes
        if palabra[i] == correcta[i]:
            ret[i].append(2)
            correcta = correcta[:i] + "_" + correcta[i+1:]
    for i in range(5): # Chequear amarillos
        if len(ret[i]) == 2:
            continue
        if palabra[i] in correcta:
            ret[i].append(1)
            correcta = correcta.replace(palabra[i], "_", 1)
    for i in range(5): # Chequear grises
        if len(ret[i]) == 1:
            ret[i].append(0)
    return ret

def recibir_palabra():
    import re
    def limpiar_texto(text):
        # Reemplaza las vocales con tildes por sus equivalentes sin tildes
        replacements = {
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u',
            'Á': 'A',
            'É': 'E',
            'Í': 'I',
            'Ó': 'O',
            'Ú': 'U',
            'ü': 'u'
        }
        
        # Usa una expresión regular para encontrar y reemplazar cada vocal con tilde
        pattern = re.compile('|'.join(re.escape(key) for key in replacements.keys()))
        text_without_accents = pattern.sub(lambda x: replacements[x.group()], text)
        
        return text_without_accents.lower()
    def is_alpha(text):
        # Expresión regular para buscar solo letras alfabéticas, incluyendo la "ñ"
        return bool(re.fullmatch(r'[^\W\d_]+', text))
    
    ### ADAPTAR ESTA FUNCIÓN PARA RECIBIR EL INPUT DE UN MENSAJE DE WPP ###
    es_valida = False
    with open ("palabras_esp.csv") as archivo:
        palabras = archivo.readlines()

    while not es_valida:
        palabra = limpiar_texto(input("Ingrese una palabra: ")) # CAMBIAR POR EL INPUT DE WPP
        if len(palabra) != 5:
            print("La palabra debe tener 5 letras.")
        elif not is_alpha(palabra):
            print("La palabra debe contener solo letras.")
        elif palabra+"\n" not in palabras:
            print("La palabra no es válida.")
        else:
            es_valida = True
    return palabra

def juego():
    with open("palabras_esp.csv") as archivo:
        correcta = random.choice(archivo.readlines()).strip("\n")
    intentos = []
    while len(intentos) < 6:
        palabra_usr = recibir_palabra()
        print(chequear_palabra(palabra_usr, correcta))

juego()