import pygame

pygame.init()

#COLORES
black = (0,0,0)
red = (255, 87,51)
#PANTALLA
ancho = 800
alto = 600
pantalla = (ancho,alto)


#CLASE PELOTA
class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert()
        self.image.set_colorkey([0,0,0])
        #posicionar el sprite:
        self.rect = self.image.get_rect()
        self.rect.center = (ancho / 2, alto / 2)
        self.vel_x = 3
        self.vel_y = 3
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Rebote en los bordes
        if self.rect.top <= 0 or self.rect.bottom >= alto:
            self.vel_y *= -1
        if self.rect.right >= ancho:
            self.rect.center = (ancho / 2, alto / 2)
            self.vel_x = 3
            self.vel_y = 3
            return True
        if self.rect.left <= 0:
            self.rect.center = (ancho / 2, alto / 2)
            self.vel_x = -3
            self.vel_y = -3
            return True
        return False

#CLASE JUGADOR
class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("jugador.png").convert()
        self.image.set_colorkey([0,0,0])
        #posicionar el sprite:
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0

    def update(self):
        self.rect.y += self.vel_y
        # Limitar movimiento dentro de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > alto:
            self.rect.bottom = alto

#CREAMOS LA CLASE JUEGO
class Game(object):
    def __init__(self):
        self.game_over = False
        self.score1 = 0
        self.score2 = 0
        self.lista__all_sprites = pygame.sprite.Group()
        self.jugadores = pygame.sprite.Group()
        self.pelotas = pygame.sprite.Group()
        #INICIALIZAMOS JUGADORES
        jugador1_x= 50
        jugador1_y= 245
        jugador2_x= 700
        jugador2_y= 245
        self.jugador1 = player(jugador1_x,jugador1_y)
        self.jugador2 = player(jugador2_x,jugador2_y)
        self.lista__all_sprites.add(self.jugador1,self.jugador2)
        self.jugadores.add(self.jugador1,self.jugador2)

        #INICIALIZAMOS PELOTA
        self.pelota = ball()
        self.lista__all_sprites.add(self.pelota)
        self.pelotas.add(self.pelota)

#FUNCION PARA PROCESAR LOS EVENTOS QUE TIENE EL JUEGO
    def procesar_eventos(self):
        for event in pygame.event.get():
        #Salgo del juego y ventana si presiono la X de exit
            if event.type == pygame.QUIT:
                return True
           #Cuando de click con el mouse, reinicia el juego 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        #Cuando presiono una tecla:
            if event.type == pygame.KEYDOWN:
                #jugador 1
                if event.key == pygame.K_w:
                    self.jugador1.vel_y = -3
                if event.key == pygame.K_s:
                    self.jugador1.vel_y = 3
                #jugador 2
                if event.key == pygame.K_UP:
                    self.jugador2.vel_y = -3
                if event.key == pygame.K_DOWN:
                    self.jugador2.vel_y = 3
            #Cuando suelto una tecla:
            if event.type == pygame.KEYUP:
                #jugador 1
                if event.key == pygame.K_w:
                    self.jugador1.vel_y = 0
                if event.key == pygame.K_s:
                    self.jugador1.vel_y = 0
                #jugador 2
                if event.key == pygame.K_UP:
                    self.jugador2.vel_y = 0
                if event.key == pygame.K_DOWN:
                    self.jugador2.vel_y = 0
            
        return False
            
#FUNCION PARA REVISAR LA LOGICA DEL JUEGO, LO QUE HAY EN LOS SPRITES
    def logica_juego(self):
        if not self.game_over:
            self.lista__all_sprites.update()
            if pygame.sprite.spritecollide(self.pelota, self.jugadores, False):
                self.pelota.vel_x *= -1

            if self.pelotas.update():
                if self.pelota.rect.right >= ancho:
                    self.score1 += 1
                elif self.pelota.rect.left <= 0:
                    self.score2 += 1
            
            #REVISAR LOS PUNTAJES Y SI LLEGO AL PUNTAJE GANADOR
            if self.score1 ==1:
                self.game_over = True
            if self.score2 == 1:
                self.game_over = True

#MOSTRAR TODO EN PANTALLA, PINTAMOS LOS SPRITES
    def mostrar_pantalla(self, screen):
        #FONDO DE PANTALLA 
        fondo_pantalla = pygame.image.load("fondo.png").convert()
        screen.blit(fondo_pantalla,[0,0])

        if self.score1 ==1 and self.game_over:
            font = pygame.font.SysFont("arial",50)
            texto1 = font.render("JUGADOR 1 GANA, CLICK PARA CONTINUAR",True, red)
            coordenada_x= (ancho//2) - (texto1.get_width()//2)
            coordenada_y = (alto//2) - (texto1.get_height()//2)
            screen.blit(texto1, [coordenada_x,coordenada_y])
        elif self.score2 ==1 and self.game_over:
            font = pygame.font.SysFont("arial",50)
            texto2 = font.render("JUGADOR 2 GANA, CLICK PARA CONTINUAR",True, red)
            coordenada_x= (ancho//2) - (texto2.get_width()//2)
            coordenada_y = (alto//2) - (texto2.get_height()//2)
            screen.blit(texto2, [coordenada_x,coordenada_y])
        
        if not self.game_over:
            self.lista__all_sprites.draw(screen)

        pygame.display.flip()


#FUNCION PRINCIPAL
def main():
    pygame.init()
    #INICIALIZAMOS PANTALLA
    screen = pygame.display.set_mode(pantalla)
    done = False
    clock = pygame.time.Clock()

    juego_pong = Game()

    while not done:
        #Cargando sonido de fondo
        pygame.mixer.Sound("musicafondo.mp3")

        done = juego_pong.procesar_eventos()

        juego_pong.logica_juego()
        
        juego_pong.mostrar_pantalla(screen)

        clock.tick()
    pygame.quit()



if __name__ == "__main__":
    main()






