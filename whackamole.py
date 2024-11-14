import pygame
import random


def draw_grid(screen):
    for x in range(0, 640, 32):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 512))  # Vertical lines
    for y in range(0, 512, 32):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (640, y))  # Horizontal lines


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole :)")

        #import mole image
        mole_image = pygame.image.load("mole.png")
        mole_x, mole_y = 0, 0 #og mole position
        clock = pygame.time.Clock()
        running = True

        while running:
            screen.fill("light green") #green screen
            draw_grid(screen) #draw grid
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))  # og mole

            for event in pygame.event.get(): #automatically given formatting
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #mouse input
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + 32 and mole_y <= mouse_y < mole_y + 32:
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32

            pygame.display.flip()
            clock.tick(60) # 60 milliseconds 
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()