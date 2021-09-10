import pygame
import random
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CARD_WIDTH, CARD_HEIGHT = 120, 160
font = pygame.font.SysFont('Comic Sans MS', 32)
pygame.display.set_caption("Blackjack!")

# Image Loading
cBackO = pygame.image.load(os.path.join('images', 'card_face_down.png'))
club_AO = pygame.image.load(os.path.join('images', 'club_1.png'))
club_2O = pygame.image.load(os.path.join('images', 'club_2.png'))
club_3O = pygame.image.load(os.path.join('images', 'club_3.png'))
club_4O = pygame.image.load(os.path.join('images', 'club_4.png'))
club_5O = pygame.image.load(os.path.join('images', 'club_5.png'))
club_6O = pygame.image.load(os.path.join('images', 'club_6.png'))
club_7O = pygame.image.load(os.path.join('images', 'club_7.png'))
club_8O = pygame.image.load(os.path.join('images', 'club_8.png'))
club_9O = pygame.image.load(os.path.join('images', 'club_9.png'))
club_10O = pygame.image.load(os.path.join('images', 'club_10.png'))
club_JO = pygame.image.load(os.path.join('images', 'club_11.png'))
club_QO = pygame.image.load(os.path.join('images', 'club_12.png'))
club_KO = pygame.image.load(os.path.join('images', 'club_13.png'))

# Image resize
cBack = pygame.transform.scale(cBackO, (CARD_WIDTH, CARD_HEIGHT))
club_A = pygame.transform.scale(club_AO, (CARD_WIDTH, CARD_HEIGHT))
club_2 = pygame.transform.scale(club_2O, (CARD_WIDTH, CARD_HEIGHT))
club_3 = pygame.transform.scale(club_3O, (CARD_WIDTH, CARD_HEIGHT))
club_4 = pygame.transform.scale(club_4O, (CARD_WIDTH, CARD_HEIGHT))
club_5 = pygame.transform.scale(club_5O, (CARD_WIDTH, CARD_HEIGHT))
club_6 = pygame.transform.scale(club_6O, (CARD_WIDTH, CARD_HEIGHT))
club_7 = pygame.transform.scale(club_7O, (CARD_WIDTH, CARD_HEIGHT))
club_8 = pygame.transform.scale(club_8O, (CARD_WIDTH, CARD_HEIGHT))
club_9 = pygame.transform.scale(club_9O, (CARD_WIDTH, CARD_HEIGHT))
club_10 = pygame.transform.scale(club_10O, (CARD_WIDTH, CARD_HEIGHT))
club_J = pygame.transform.scale(club_JO, (CARD_WIDTH, CARD_HEIGHT))
club_Q = pygame.transform.scale(club_QO, (CARD_WIDTH, CARD_HEIGHT))
club_K = pygame.transform.scale(club_KO, (CARD_WIDTH, CARD_HEIGHT))



#Global Constants
GREEN = (34,139,34)
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (127,0,255)
clock = pygame.time.Clock()

gameoverText = font.render("Restart? ", True, PURPLE)

cards = { club_A:1, club_2:2, club_3:3, club_4:4, club_5:5, club_6:6, club_7:7, 
        club_8:8, club_9:9, club_J:10, club_Q:11, club_K:12 }

def draw_window():
    WIN.fill(GREEN)
    pygame.display.update()

def getValue(card):
    return cards.get(card)
    
def main():

    userScore = 0
    dealerScore = 0

    userCard = []
    dealCard = []

    userCard.append(random.choice(list(cards)))
    userCard.append(random.choice(list(cards)))

    dealCard.append(random.choice(list(cards)))
    dealCard.append(random.choice(list(cards)))

    


    # Main loop
    while True:
        gameover = True  if (userScore >= 21) else False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and gameover and restartB.collidepoint(pygame.mouse.get_pos()):
                gameover = True

        draw_window()
        userScoreText = font.render("Player: " + str(userScore), False, (255,255,255))
        dealScoreText = font.render("House: " + str(dealerScore), False, (255,255,255))
        WIN.blit(userScoreText, (10,400))
        WIN.blit(dealScoreText, (10,100))



        for card in dealCard:
            #dealerScore = 10 #+= getValue(card)
            WIN.blit(card, (350, 100))
        WIN.blit(cBack, (410,100))

        for card in userCard:
            #userScore += getValue(card)
            x = 350 + (userCard.index(card)*60)
            WIN.blit(card, (x, 400))
        
        if gameover:
            WIN.blit(gameoverText, (250,250))
            restartB = pygame.draw.rect(WIN, WHITE, (WIDTH/2, HEIGHT/2, 140, 40))

        pygame.display.update()
        clock.tick(10)


        




    pygame.quit()

if __name__ == "__main__":
    main()


