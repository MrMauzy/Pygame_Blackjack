import pygame
import random
import os

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CARD_WIDTH, CARD_HEIGHT = 120, 160
pygame.display.set_caption("Blackjack!")

# Image Loading
cBack = pygame.image.load(os.path.join('images', 'card_face_down.png'))
club_A = pygame.image.load(os.path.join('images', 'club_1.png'))
club_2 = pygame.image.load(os.path.join('images', 'club_2.png'))
club_3 = pygame.image.load(os.path.join('images', 'club_3.png'))
club_4 = pygame.image.load(os.path.join('images', 'club_4.png'))
club_5 = pygame.image.load(os.path.join('images', 'club_5.png'))
club_6 = pygame.image.load(os.path.join('images', 'club_6.png'))
club_7 = pygame.image.load(os.path.join('images', 'club_7.png'))
club_8 = pygame.image.load(os.path.join('images', 'club_8.png'))
club_9 = pygame.image.load(os.path.join('images', 'club_9.png'))
club_10 = pygame.image.load(os.path.join('images', 'club_10.png'))
club_J = pygame.image.load(os.path.join('images', 'club_11.png'))
club_Q = pygame.image.load(os.path.join('images', 'club_12.png'))
club_K = pygame.image.load(os.path.join('images', 'club_13.png'))

# Image resize
cBackR = pygame.transform.scale(cBack, (CARD_WIDTH, CARD_HEIGHT))
club_AR = pygame.transform.scale(club_A, (CARD_WIDTH, CARD_HEIGHT))
club_2R = pygame.transform.scale(club_2, (CARD_WIDTH, CARD_HEIGHT))
club_3R = pygame.transform.scale(club_3, (CARD_WIDTH, CARD_HEIGHT))
club_4R = pygame.transform.scale(club_4, (CARD_WIDTH, CARD_HEIGHT))
club_5R = pygame.transform.scale(club_5, (CARD_WIDTH, CARD_HEIGHT))
club_6R = pygame.transform.scale(club_6, (CARD_WIDTH, CARD_HEIGHT))
club_7R = pygame.transform.scale(club_7, (CARD_WIDTH, CARD_HEIGHT))
club_8R = pygame.transform.scale(club_8, (CARD_WIDTH, CARD_HEIGHT))
club_9R = pygame.transform.scale(club_9, (CARD_WIDTH, CARD_HEIGHT))
club_10R = pygame.transform.scale(club_10, (CARD_WIDTH, CARD_HEIGHT))
club_JR = pygame.transform.scale(club_J, (CARD_WIDTH, CARD_HEIGHT))
club_QR = pygame.transform.scale(club_Q, (CARD_WIDTH, CARD_HEIGHT))
club_KR = pygame.transform.scale(club_K, (CARD_WIDTH, CARD_HEIGHT))

# Board color
GREEN = (34,139,34)

# Frame Per Second for screen draw
FPS = 60

def draw_window():
    WIN.fill(GREEN)
    WIN.blit(cBackR, (300,100))
    WIN.blit(club_AR, (300,400))
    WIN.blit(club_QR, (310,400))
    WIN.blit(club_KR, (330,400))
    WIN.blit(club_JR, (350,400))
    WIN.blit(club_2R, (390,400))
    WIN.blit(club_5R, (410,400))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()




    pygame.quit()

if __name__ == "__main__":
    main()


