import pywhatkit
import time
from pytube import YouTube

#Leer los enlaces del archivo y guardarlos en una lista
def get_links():
    link_caciones = []
    with open("enlaces.txt") as file:
        url = file.readlines()
        for line in url:
            link_caciones.append(line.strip())
        return link_caciones


#Función para medir el largo de la canción del link de youtube
def get_video_length(video_url):
    yt = YouTube(video_url)
    return yt.length

#Función para reproducir los videos
def reproducir_videos():
    songs_to_play = get_links()

    for song in songs_to_play:
        pywhatkit.playonyt(song)
        time.sleep(get_video_length(song))




#Programar cuando reproducir las canciones y reproducirlas

hours = int(input("Dentro de cuantas horas quieres que suene la música: "))
minutes = int(input("Dentro de cuantos minutos quieres que suene la música: "))
seconds = int(input("Dentro de cuantos segundos quieres que suene la música: "))
total_time = (hours*60*60) + (minutes*60) + seconds

time.sleep(total_time)
reproducir_videos()
