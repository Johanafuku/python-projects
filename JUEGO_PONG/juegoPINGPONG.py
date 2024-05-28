import pygame, random

pygame.init()

#COLORES
blue = (0,0,255)
red = (255, 87,51)
#DIMENSION PANTALLA
ancho = 800
alto = 600
screen = (ancho,alto)

#CREAR LA PANTALLA
screen = pygame.display.set_mode(screen)
#CREAR RELOJ
clock = pygame.time.Clock()

##COORDENADAS JUGADORES Y VELOCIDAD JUGADORES
jugador1_x= 50
jugador1_y= 245
velocidad_jugador1 = 0

jugador2_x= 700
jugador2_y= 245
velocidad_jugador1 = 0
velocidad_jugador2 = 0

##COORDENADAS PELOTA, MITAD DE LA PANTALLA Y VELOCIDAD PELOTA
pelota_x = ancho /2
pelota_y = alto /2

velocidad_pelota_x = 3
velocidad_pelota_y = 3

#Inicializamos la variable principal de todo el juego
juego_pong = False

#FONDO DE PANTALLA y JUGADORES - PELOTA
fondo_pantalla = pygame.image.load("fondo.png").convert()

#CREAR FUNCION PARA DIBUJAR EL MARCADOR 
def dibujar_texto(superficie,texto,size, x, y):
    fuente = pygame.font.SysFont("arial", size)
    superficie_texto = fuente.render(texto, True,blue)
    texto_rect = superficie_texto.get_rect()
    texto_rect.midtop = (x,y)
    superficie.blit(superficie_texto, texto_rect)

#CLASE PELOTA
class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert()
        self.image.set_colorkey([0,0,0])
        #posicionar el sprite:
        self.rect = self.image.get_rect()

#Creamos la lista para almacenar todos los sprites
lista__all_sprites = pygame.sprite.Group()

#CLASE JUGADOR
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("jugador.png").convert()
        self.image.set_colorkey([0,0,0])
        #posicionar el sprite:
        self.rect = self.image.get_rect()


#Iniciamos la clase pelota
pelota = ball()
pelota.rect.x = pelota_x
pelota.rect.y = pelota_y
lista__all_sprites.add(pelota)

#Iniciamos la clase jugador
jugador_1 = player()
jugador_1.rect.x = jugador1_x
jugador_1.rect.y = jugador1_y
lista__all_sprites.add(jugador_1)

jugador_2 = player()
jugador_2.rect.x = jugador2_x
jugador_2.rect.y = jugador2_y
lista__all_sprites.add(jugador_2)

#CARGANDO SONIDO DE FONDO
sonido_fondo = pygame.mixer.Sound("musicafondo.mp3")


#Creamos variables de puntaje
puntaje1 = 0
puntaje2 = 0
puntaje_Ganador = 5
game_over = False

#LOOP PRINCIPAL

while not juego_pong:
    #Insertamos sonido al juego
    sonido_fondo.play()
    
    #ZONA DE LÓGICA
    for event in pygame.event.get():
        #Salgo del juego y ventana si presiono la X de exit
        if event.type == pygame.QUIT:
            juego_pong = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over: #reiniciar el juego
                jugador1_x = 50
                jugador1_y = 245
                velocidad_jugador1 = 0

                jugador2_x = 700
                jugador2_y = 245
                velocidad_jugador2 = 0

                pelota_x = ancho /2
                pelota_y = alto /2
                velocidad_pelota_x = 3
                velocidad_pelota_y = 3

                # Reset the score
                puntaje1 = 0
                puntaje2 = 0

                # Continuar el juego
                continue

        #Cuando presiono una tecla:
        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                velocidad_jugador1 = -3
            if event.key == pygame.K_s:
                velocidad_jugador1 = 3
            #jugador 2
            if event.key == pygame.K_UP:
                velocidad_jugador2 = -3
            if event.key == pygame.K_DOWN:
                velocidad_jugador2 = 3
        #Cuando suelto una tecla:
        if event.type == pygame.KEYUP:
            #jugador 1
            if event.key == pygame.K_w:
                velocidad_jugador1 = 0
            if event.key == pygame.K_s:
                velocidad_jugador1 = 0
            #jugador 2
            if event.key == pygame.K_UP:
                velocidad_jugador2 = 0
            if event.key == pygame.K_DOWN:
                velocidad_jugador2 = 0
        
        
    #LImites de los jugadores para que reboten con los bordes superiores
    if jugador_1.rect.y > 490 or jugador_1.rect.y <8:
        velocidad_jugador1 *=-1
    
    if jugador_2.rect.y > 490 or jugador_2.rect.y <8:
        velocidad_jugador2 *=-1
    #Limites de la pelota para que rebote con los bordes superiores o inferiores
    if pelota.rect.y > 590 or pelota.rect.y < 10:
        velocidad_pelota_y *= -1

    #Añadimos algo de random a la pelota
     
    #Si la pelota sale del lado derecho a lo ancho, que vuelva al centro
    if pelota.rect.x > 700:
        pelota.rect.x = ancho/2
        pelota.rect.y = alto /2
        #si sale de la pantalla invierte dirección
        velocidad_pelota_y *= -1
    
    #SI sale del lado izquierdo a lo ancho, vuelve al centro
    if pelota.rect.x <40:
        pelota.rect.x = ancho/2
        pelota.rect.y = alto /2
        #si sale de la pantalla invierte dirección
        velocidad_pelota_y *= -1

    #MOVIMIENTO A LOS JUGADORES y PELOTA
    ##se usa judadores en coordenada Y, porque se moveran a lo alto
    jugador_1.rect.y +=velocidad_jugador1
    jugador_2.rect.y += velocidad_jugador2

    ##movimiento pelota
    pelota.rect.x += velocidad_pelota_x
    pelota.rect.y += velocidad_pelota_y

    #Insertar fondo y los jugadores sprits
    screen.blit(fondo_pantalla,[0,0])
    lista__all_sprites.draw(screen)
    

    #Colisiones
    colisiones_jug1 = pygame.sprite.collide_rect(jugador_1,pelota)
    colisiones_jug2 = pygame.sprite.collide_rect(jugador_2,pelota)

    if colisiones_jug1 or colisiones_jug2:
        velocidad_pelota_x *= -1
        velocidad_pelota_y *= -1
    
    if colisiones_jug1:
        puntaje1 +=1
          
    if colisiones_jug2:
        puntaje2 +=1
    
    # GENERA LOS MENSAJES DE GANADOR
    if puntaje1 ==puntaje_Ganador:
        # Display "JUGADOR 1 GANA"
        font = pygame.font.Font(None, 50)
        text = font.render("JUGADOR 1 GANA - CLICK PARA CONTINUAR", True, blue)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
        game_over = True                 
        
    elif puntaje2 ==puntaje_Ganador:
        # Display "JUGADOR 2 GANA"
        font = pygame.font.Font(None, 50)
        text = font.render("JUGADOR 2 GANA - CLICK PARA CONTINUAR", True, blue)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)  
        game_over = True
          
    #MARCADOR 
    # 40 es el tamaño de la fuente, 200 es la coordenada x, 15 la coordenada y
    dibujar_texto(screen,str(puntaje1), 40, 200, 15) 
    dibujar_texto(screen, str(puntaje2), 40, 600, 15)

    #Actualizar la pantalla
    clock.tick(65)
    pygame.display.flip()

          
pygame.quit()

