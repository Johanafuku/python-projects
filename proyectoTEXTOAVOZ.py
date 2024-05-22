
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





#CASO DE USO - ingresa tu URL
url = "https://www.euroinnova.bo/blog/articulo-sobre-la-educacion-actual"
texto_a_voz(url)
