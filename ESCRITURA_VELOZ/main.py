'''Prueba de Escritura Veloz
La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una
oración de manera precisa'''

import tkinter as tk
import time, random

inicio = None
etiqueta_tiempo = None
etiqueta_resultado_correcto = None
etiqueta_resultado_incorrecto = None

#///////////AREA DE FUNCIONES///////////////////////////////////////////
#FUNCION PARA LEER ORACIONES RANDOM DEL ARCHIVO
def oracion_random():
    with open('oraciones.txt', encoding="utf-8") as archivo:
        oraciones = archivo.readlines()
        oracion_random = random.choice(oraciones)
        return oracion_random.strip()
    
#funcion para comparar oracion del usuario con la oracion random
## que devuelva si esta bien o no y el tiempo
def comparar_oracion():
    global etiqueta_resultado_correcto
    global etiqueta_resultado_incorrecto
    oracion_aleatoria = caja_oracion.get("1.0",'end-1c')
    oracion_usuario = caja_texto_usuario.get("1.0",'end-1c')
    if oracion_aleatoria == oracion_usuario:
        mensaje1 = "La oración esta correctamente escrita."
        etiqueta_resultado_correcto= tk.Label(ventana,text=mensaje1,font=("FreeSans",12))
        etiqueta_resultado_correcto.grid(row=5,column=1)
    else:
        mensaje2 = "La oración tiene errores, vuelve a intertarlo."
        etiqueta_resultado_incorrecto = tk.Label(ventana,text=mensaje2,font=("FreeSans",12))
        etiqueta_resultado_incorrecto.grid(row=5,column=1)
        
        
#FUNCIONES Y BOTONES TKINTER
#///////////AREA DE WIDGETS///////////////////////////////////////////

#CREAR VENTANA
ventana = tk.Tk()   
ventana.geometry("900x300")
ventana.title("Prueba de escritura veloz")
ventana.encoding = "utf-8"
verde_pastel = "#b0f2c2"
ventana.grid_columnconfigure(2,weight=1)
ventana.grid_rowconfigure(5,weight=1)
#CREAR ETIQUETA DE INSTRUCCIONES
string_instrucciones = "ESCRIBE LA ORACIÓN EN EL MENOR TIEMPO"
etiqueta_instrucciones =tk.Label(ventana,text=string_instrucciones)
#poner en pantalla
etiqueta_instrucciones.grid(row=0,column=1)

#creamos caja de texto donde se mostrara la oracion random
caja_oracion = tk.Text(ventana,font="FreeSans 14",height=2,wrap="word")
caja_oracion.grid(row=1,column=1, columnspan=2,sticky="we",padx=5)
#creamos la mini funcion asociada a la funcion oracion random
def click_boton_oracion():
    global inicio
    inicio = time.time()
    oracion = oracion_random()
    caja_oracion.insert(tk.END,oracion)
    return inicio

#CREAR BOTON DE GENERAR ORACION ASOCIADO A FUNCION ORACION RANDOM
boton_oracion = tk.Button(ventana,text="GENERAR ORACIÓN",command=click_boton_oracion)
boton_oracion.grid(row=1,column=0)

#CREAR BOTON PARAR, PARA QUE EL USUARIO CONFIRME QUE HA TERMINADO DE ESCRIBIR
#creamos mini funcion que confirmar que ha finalizado de escribir
def parar():
    global etiqueta_tiempo
    if inicio is not None:
        fin = time.time()
        tiempo_total = fin - inicio
        tiempo_redondeado = round(tiempo_total,2)
        mensaje_tiempo = f"Tu tiempo es de: {tiempo_redondeado} seg."
        etiqueta_tiempo = tk.Label(ventana,text=mensaje_tiempo)
        etiqueta_tiempo.grid(row=5,column=0)
  

#CREAMOS EL BOTON PARAR ASOCIADO A LA FUNCION PARAR()
boton_parar = tk.Button(ventana, text="  PARAR  ", command=parar)
boton_parar.grid(row=3,column=0)

#CREAR UN BOTON RESULTADO ASOCIADO A COMPARAR RESULTADOS
boton_resultado = tk.Button(ventana,text="RESULTADO",command=comparar_oracion)
boton_resultado.grid(row=3,column=1)

#funcion para reiniciar la prueba
parar()
def reiniciar():
    caja_texto_usuario.delete(1.0,tk.END)
    caja_oracion.delete(1.0,tk.END)
    global inicio
    inicio = None
    if etiqueta_tiempo:
        etiqueta_tiempo.destroy()
    if etiqueta_resultado_correcto:
        etiqueta_resultado_correcto.destroy()
    if etiqueta_resultado_incorrecto:
        etiqueta_resultado_incorrecto.destroy()


#CREAR UN BOTON DE REINICIO ASOCIADO A FUNCION REINICIAR
boton_reinicio = tk.Button(ventana,text="REINICIAR",command=reiniciar)
boton_reinicio.grid(row=3,column=2)

#CREAR CAJA TEXTO DONDE USUARIO TIPEE LA ORACION
etiqueta_texto_usuario = tk.Label(ventana,text="Escribe aquí: ")
etiqueta_texto_usuario.grid(row=2,column=0,columnspan=1)
caja_texto_usuario = tk.Text(ventana, font="calibri 14",height=2,wrap="word")
caja_texto_usuario.grid(row=2,column=1, columnspan=2,sticky="we",padx=5)

 

#main loop
ventana.mainloop()


