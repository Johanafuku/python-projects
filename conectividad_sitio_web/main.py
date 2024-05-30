'''crear un programa que pruebe la conectividad de sitios web.'''

import tkinter as tk
import urllib
import urllib.error
import urllib.request

etiqueta_mensaje1 = None
etiqueta_mensaje2 = None

#FUNCION PARA COMPROBAR CONECTIVIDAD
def conectividad():
    global etiqueta_mensaje1
    global etiqueta_mensaje2
    #trae el url ingresado por el usuario en la caja de texto
    url = url_usuario.get("1.0","end-1c")
    
    try:
        prueba_conexion = urllib.request.urlopen(url).getcode()
        if prueba_conexion == 200:
            etiqueta_mensaje1 = tk.Label(ventana,text="LA PÁGINA WEB ESTA DISPONIBLE", fg="green")
            etiqueta_mensaje1.grid(row=3,column=0,sticky="w",padx=5,pady=5)
        
    except urllib.error.URLError:
            etiqueta_mensaje2 = tk.Label(ventana,text="LA PÁGINA WEB NO ESTA DISPONIBLE",fg="red")
            etiqueta_mensaje2.grid(row=3,column=0,sticky="w",padx=5,pady=5)
    except ValueError:
            etiqueta_mensaje2 = tk.Label(ventana,text="LA PÁGINA WEB NO ESTA DISPONIBLE",fg="red")
            etiqueta_mensaje2.grid(row=3,column=0,sticky="w",padx=5,pady=5)
        
#CREAR FUNCION DE REINICIO:
def reiniciar():
    global etiqueta_mensaje1
    global etiqueta_mensaje2

#Borramos la caja de texto y las etiquetas
    url_usuario.delete(1.0,tk.END)
    if etiqueta_mensaje1:
        etiqueta_mensaje1.destroy()
        etiqueta_mensaje1 = None
    if etiqueta_mensaje2:
        etiqueta_mensaje2.destroy()
        etiqueta_mensaje2 = None
    

#CREAR VENTANA
ventana = tk.Tk()   
ventana.geometry("820x200")
ventana.title("Comprador de conectividad")
ventana.encoding = "utf-8"
ventana.grid_columnconfigure(2,weight=1)
ventana.grid_rowconfigure(5,weight=1)

#CREAR ETIQUETA DE INSTRUCCIONES
string_instrucciones = "PEGA EL URL DEL SITIO WEB:"
etiqueta_instrucciones =tk.Label(ventana,text=string_instrucciones)
#poner en pantalla
etiqueta_instrucciones.grid(row=0,column=0,sticky="w",padx=5,pady=5)

#creamos caja de texto donde se pegará el URL
url_usuario = tk.Text(ventana,height=2,wrap="word",font=("FreeSans",12))
url_usuario.grid(row=1,column=0, columnspan=2,sticky="we",padx=5,pady=10)

#CREAR BOTON DE COMPROBACION DE CONEXIÓN
boton_comprobar = tk.Button(ventana,text="COMPROBAR CONECTIVIDAD",command=conectividad)
boton_comprobar.grid(row=2,column=0,sticky="w",padx=5,pady=10)

#CREAR BOTON REINICIO
boton_reiniciar = tk.Button(ventana,text=" REINICIAR ",command=reiniciar)
boton_reiniciar.grid(row=2,column=1,sticky="e",padx=5,pady=10)
#main loop
ventana.mainloop()