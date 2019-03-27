# Victor Manuel Cerón Navarrete


import math
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        radio = 100
        for theta in range(0, r // math.gcd(r, R) * 360, 1):
            a = math.radians(theta)
            x1 = int(radio * math.cos(a))
            y1 = int(radio * math.sin(a))

            #pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)

            k = r / R
            x2 = int(R * (((1 - k) * math.cos(a)) - (l * k * math.cos(((1 - k) / k) * a))))
            y2 = int(R * (((1 - k) * math.sin(a)) + (l * k * math.sin(((1 - k) / k) * a))))

            pygame.draw.circle(ventana, ROJO, (x2 + ANCHO // 2, ALTO // 2 - y2), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps



    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():

    radioMenor = int(input("¿Cuánto vale el radio menor? "))
    radioMayor = int(input("¿Cuánto vale el radio mayor? "))
    l = float(input("¿Cuánto vale l? "))

    dibujar(radioMenor, radioMayor, l)

# Llamas a la función principal
main()