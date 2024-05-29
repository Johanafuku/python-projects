import tkinter as tk
from tkinter import filedialog
from io import open
import fitz  # PyMuPDF
from odf.opendocument import load as load_odt
from odf.text import P
import openpyxl
import docx

# Variable para almacenar ruta de un documento
ruta = ""

# Crear funciones
def nuevo():
    global ruta
    mensaje.set("Nuevo documento")
    ruta = ""
    texto_usuario.delete("1.0", "end")
    ventana.title("Editor de texto")

def abrir():
    global ruta
    mensaje.set("Abrir documento")
    ruta = filedialog.askopenfilename(initialdir=".",
                                      filetypes=(("Ficheros texto", "*.txt"), ("Ficheros pdf", "*.pdf"),
                                                 ("Ficheros word", "*.odt"), ("Ficheros excel", "*.xlsx"),
                                                 ("Ficheros docx", "*.docx")),
                                      title="Abrir documento")  # "." directorio actual

    if ruta != "":
        contenido = ""
        try:
            if ruta.endswith(".txt"):
                with open(ruta, "r", encoding="utf-8") as fichero:
                    contenido = fichero.read()
            elif ruta.endswith(".pdf"):
                doc = fitz.open(ruta)
                for page in doc:
                    contenido += page.get_text()
            elif ruta.endswith(".odt"):
                doc = load_odt(ruta)
                for elem in doc.getElementsByType(P):
                    contenido += elem.firstChild.data + "\n"
            elif ruta.endswith(".xlsx"):
                wb = openpyxl.load_workbook(ruta)
                sheet = wb.active
                for row in sheet.iter_rows(values_only=True):
                    contenido += "\t".join([str(cell) if cell is not None else "" for cell in row]) + "\n"
            elif ruta.endswith(".docx"):
                doc = docx.Document(ruta)
                contenido += "\n".join(para.text for para in doc.paragraphs)

            texto_usuario.delete("1.0", "end")
            texto_usuario.insert("insert", contenido)
            ventana.title(ruta + " - Editor de texto")
        except Exception as e:
            mensaje.set(f"Error al abrir el archivo: {str(e)}")

def guardar():
    global ruta
    mensaje.set("Guardar documento")
    if ruta != "":
        contenido = texto_usuario.get("1.0", "end-1c")
        try:
            with open(ruta, "w", encoding="utf-8") as fichero:
                fichero.write(contenido)
            mensaje.set("Documento guardado correctamente")
        except Exception as e:
            mensaje.set(f"Error al guardar el archivo: {str(e)}")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar documento como")
    ruta = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=(("Ficheros texto", "*.txt"), ("Ficheros pdf", "*.pdf"),
                                                   ("Ficheros word", "*.odt"), ("Ficheros excel", "*.xlsx"),
                                                   ("Ficheros docx", "*.docx")),
                                        title="Guardar documento como")
    if ruta != "":
        contenido = texto_usuario.get("1.0", "end-1c")
        try:
            with open(ruta, "w", encoding="utf-8") as fichero:
                fichero.write(contenido)
            mensaje.set("Documento guardado como: " + ruta)
            ventana.title(ruta + " - Editor de texto")
        except Exception as e:
            mensaje.set(f"Error al guardar el archivo: {str(e)}")

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("Editor de texto")
ventana.encoding = "utf-8"
blanco = "#FFFFFF"
gris_claro = "#EEEEEE"
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.configure(background=blanco)

ventana.resizable(1, 1)

# Crear botones
## Crear botón Archivo del editor de texto - tendrá asociados
## botón de tipo menú

boton_archivo = tk.Menubutton(ventana, text="Archivo", bg=gris_claro, fg="black", padx=20)
boton_archivo.grid(row=0, column=0, sticky="w")

### Configuramos el menú
boton_archivo.menu = tk.Menu(boton_archivo, tearoff=0)
boton_archivo["menu"] = boton_archivo.menu
boton_archivo.menu.add_command(label="Nuevo", command=nuevo)
boton_archivo.menu.add_command(label="Abrir", command=abrir)
boton_archivo.menu.add_command(label="Guardar", command=guardar)
boton_archivo.menu.add_command(label="Guardar como", command=guardar_como)
boton_archivo.menu.add_command(label="Salir", command=ventana.quit)

## Crear espacio de escritura usuario
texto_usuario = tk.Text(ventana, wrap="word")
texto_usuario.grid(row=1, column=0, sticky="wesn", columnspan=2)
texto_usuario.config(font=("Arial", 12))

# Crear etiqueta monitor inferior
mensaje = tk.StringVar()
mensaje.set("Bienvenido...")
monitor_inferior = tk.Label(ventana, textvariable=mensaje)
monitor_inferior.grid(row=2, column=0, sticky="w")

ventana.mainloop()


