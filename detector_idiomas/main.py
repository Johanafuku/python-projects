'''utilizar modulo langdetect para identificar idioma ingresado'''
import tkinter as tk
from langdetect import detect
from langdetect import DetectorFactory

DetectorFactory.seed = 0

etiqueta_idioma = None
#función para mostrar el idioma de las abreviaciones
def idioma_completo(dato):
    match dato:
        case "af":
            return "afrikáans"
        case "ar":
            return "árabe"
        case "bg":
            return "búlgaro"
        case "bn":
            return "bengalí"
        case "ca":
            return "catalán"
        case "cs":
            return "checo"
        case "cy":
            return "galés"
        case "da":
            return "danés"
        case "de":
            return "alemán"
        case "el":
            return "griego (moderno)"
        case "en":
            return "inglés"
        case "es":
            return "español"
        case "et":
            return "estonio"
        case "fa":
            return "persa"
        case "fi":
            return "finés o finlandés"
        case "fr":
            return "francés"
        case "gu":
            return "guyaratí (o gujaratí)" 
        case "he":
            return "hebreo"  
        case "hi":
            return "hindi (hindú)"
        case "hr":
            return "croata"    
        case "hu":
            return "húngaro"
        case "id":
            return "indonesio" 
        case "it":
            return "italiano"
        case "ja":
            return "japonés"
        case "kn":
            return "canarés"
        case "ko":
            return "coreano"
        case "lt":
            return "lituano"
        case "lv":
            return "letón"
        case "mk":
            return "macedonio"
        case "ml":
            return "malayalam"
        case "mr":
            return "maratí"
        case "ne":
            return "nepalí"
        case "nl":
            return "neerlandés (u holandés)"
        case "no":
            return "noruego"
        case "pa":
            return "panyabí (o penyabi)"
        case "pl":
            return "polaco"
        case "pt":
            return "portugués"
        case "ro":
            return "rumano"
        case "ru":
            return "ruso"
        case "sk":
            return "eslovaco"
        case "sl":
            return "esloveno"
        case "so":
            return "somalí"
        case "sq":
            return "albanés"
        case "sv":
            return "sueco"
        case "sw":
            return "suajili"
        case "ta":
            return "tamil"
        case "te":
            return "télugu"
        case "th":
            return "tailandés"
        case "tl":
            return "tagalo"
        case "tr":
            return "turco"
        case "uk":
            return "ucraniano"
        case "ur":
            return "urdu"
        case "vi":
            return "vietnamita"
        case "zh-cn":
            return "chino"
        case "zh-tw":
            return "chino (taiwán)"
        case _:
            return "Idioma no detectado"
        
#CREAR FUNCION DETECTA IDIOMA:
##comentario: langdetect es más eficiente cuando se ingresa frases mas largas
## con palabras o frases cortas, puede generar un resultado no esperado
def detectar_idioma():
    global etiqueta_idioma
    texto_ingresado = texto_usuario.get("1.0","end-1c")
    resultado = detect(texto_ingresado).strip()
    resultado_completo = idioma_completo(resultado)
    etiqueta_idioma = tk.Label(ventana,text=resultado_completo, fg="blue")
    etiqueta_idioma.grid(row=3,column=0,sticky="w",padx=5,pady=5)

#CREAR FUNCION DE REINICIO:
def reiniciar():
    global etiqueta_idioma

#Borramos la caja de texto y las etiquetas
    texto_usuario.delete(1.0,tk.END)
    if etiqueta_idioma:
        etiqueta_idioma.destroy()
        etiqueta_idioma = None
           

#CREAR VENTANA
ventana = tk.Tk()   
ventana.geometry("820x200")
ventana.title("DETECTOR DE IDIOMAS")
ventana.encoding = "utf-8"
ventana.grid_columnconfigure(2,weight=1)
ventana.grid_rowconfigure(5,weight=1)

#CREAR ETIQUETA DE INSTRUCCIONES
string_instrucciones = "INGRESA UNA FRASE (debe ser más de 3 palabras):"
etiqueta_instrucciones =tk.Label(ventana,text=string_instrucciones)
#poner en pantalla
etiqueta_instrucciones.grid(row=0,column=0,sticky="w",padx=5,pady=5)

#creamos caja de texto donde el usuario ingresara el texto
texto_usuario = tk.Text(ventana,height=2,wrap="word",font=("FreeSans",12))
texto_usuario.grid(row=1,column=0, columnspan=2,sticky="we",padx=5,pady=10)

#CREAR BOTON DE DETECTAR IDIOMA
boton_comprobar = tk.Button(ventana,text="DETECTAR IDIOMA",command=detectar_idioma)
boton_comprobar.grid(row=2,column=0,sticky="w",padx=5,pady=10)

#CREAR BOTON REINICIO
boton_reiniciar = tk.Button(ventana,text="  BORRAR  ",command=reiniciar)
boton_reiniciar.grid(row=2,column=0,sticky="w", padx=200,pady=10)
#main loop
ventana.mainloop()