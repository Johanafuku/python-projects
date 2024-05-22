'''La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz.'''

import newspaper
from gtts import gTTS
import os


def texto_a_voz(url):
    #extraemos el articulo del URL
    articulo_url= newspaper.Article(url="%s" % (url), language="es")
    articulo_url.download()
    articulo_url.parse()

    #extraemos el texto del articulo
    texto_url = articulo_url.text

    #imprimir el resultado de la extraccion solo texto
    #print(texto_url)

    #convertir texto a voz
    texto_voz= gTTS(text=texto_url, lang="es",tld="es",slow=False)
    texto_voz.save("articulo1.mp3")
    os.system("articulo1.mp3")





#CASO DE USO
url = "https://www.euroinnova.bo/blog/articulo-sobre-la-educacion-actual"
texto_a_voz(url)
