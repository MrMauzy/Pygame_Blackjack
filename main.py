import pygame
import random
import os


WIDTH, HEIGHT = 900, 600
CARD_WIDTH, CARD_HEIGHT = 120, 160

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
club_A = pygame.transform.scale(club_AO, (CARD_WIDTH, CARD_HEIGHT)) # was 53 x 73
club_2 = pygame.transform.scale(club_2O, (CARD_WIDTH, CARD_HEIGHT)) # x3 is 159x219
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

cards = { club_A:1, club_2:2, club_3:3, club_4:4, club_5:5, club_6:6, club_7:7, 
        club_8:8, club_9:9, club_10:10, club_J:11, club_Q:12, club_K:13 }

def getValue(card):
    cardV = cards.get(card)
    if cardV % 13 == 11: 
        return 10
    elif cardV % 13 == 12:
        return 10
    elif cardV % 13 == 0:
        return 10
    elif cardV % 13 == 1:
        return 11
    else:
        return cardV
        

def startingHand(cards, user, deal):

    userCard1 = random.choice(list(cards))
    userCard2 = random.choice(list(cards))
    userHand = [userCard1,userCard2]

    dealCard1 = random.choice(list(cards))
    dealCard2 = random.choice(list(cards))
    dealHand = [dealCard1,dealCard2]

    userSum = getValue(userCard1) + getValue(userCard2)
    dealSum = getValue(dealCard1) + getValue(dealCard2)

    return userSum, userHand, dealSum, dealHand
    
def main():

    winner = False

    userScore = 0
    dealerScore = 0
    userWin = 0
    dealWin = 0
    userCard = []
    dealCard = []

    # Start Game
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont('Comic Sans MS', 32)
    pygame.display.set_caption("Blackjack!")

    # Text
    
    winnerText = font.render("You WIN! ", True, PURPLE)
    hitText = font.render("Hit Me!", 1, BLACK)
    standText = font.render("Stand", 1, BLACK)
    restartText = font.render("Restart?", 1, WHITE)

    # Populate background
    background = pygame.Surface(WIN.get_size())
    background = background.convert()
    background.fill(GREEN)
    hitButton = pygame.draw.rect(background, PURPLE, (550, 400, 150, 50))
    standButton = pygame.draw.rect(background, (255, 0, 0), (205, 400, 110, 50))

    userScore, userCard, dealerScore, dealCard = startingHand(cards, userCard, dealCard)



    # Main loop
    while True:
        gameover = True  if (userScore >= 21) else False
        if len(dealCard) == 2 and dealerScore == 21:
            gameover = True
        elif len(userCard) == 2 and userScore == 21:
            gameover = True
            winner = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover) and hitButton.collidepoint(pygame.mouse.get_pos()):
                card1 = random.choice(list(cards))
                userCard.append(card1)
                userScore += getValue(card1) 
                if userScore > 21:
                    gameover = True
                elif userScore == 21:
                    gameover = True
                    winner = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover) and standButton.collidepoint(pygame.mouse.get_pos()):
                if dealerScore < 17:
                    card1 = random.choice(list(cards))
                    dealCard.append(card1)
                    dealerScore += getValue(card1)
                    if dealerScore > 21:
                        gameover = True
                        winner = True
                    elif dealerScore == 21:
                        gameover = True
                elif userScore > dealerScore:
                    gameover = True
                    winner = True
                elif userScore == dealerScore:
                    pass
                else:
                    gameover = True

            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover) and restartButton.collidepoint(pygame.mouse.get_pos()):
                if userScore == dealerScore:
                    pass
                elif userScore <= 21 and len(userCard) == 5:
                    userWin += 1
                elif userScore <= 21 and userScore > dealerScore or dealerScore > 21:
                    userWin += 1
                else:
                    dealWin += 1

                gameover = False
                userScore = 0
                dealerScore = 0
                userCard = []
                dealCard = []
                userScore, userCard, dealerScore, dealCard = startingHand(cards, userCard, dealCard)

        #draw_window()
        WIN.blit(background, (0,0))
        WIN.blit(hitText, (560, 400))
        WIN.blit(standText, (220, 400))
        userScoreText = font.render("Player: " + str(userScore), False, (255,255,255))
        WIN.blit(userScoreText, (10,300))
        


        for card in dealCard:
            #x = 350 + (dealCard.index(card)*60)
            WIN.blit(card, (350, 100)) # was 350
        WIN.blit(cBack, (410,100))

        for card in userCard:
            #userScore += getValue(card)
            x = 350 + (userCard.index(card)*60)
            WIN.blit(card, (x, 400))
        
        if gameover:
            restartButton = pygame.draw.rect(background, BLACK, (WIDTH/2, HEIGHT/2, 140, 40))
            WIN.blit(restartText, ((WIDTH/2 + 5), HEIGHT/2))
            dealScoreText = font.render("House: " + str(dealerScore), False, (255,255,255))
            WIN.blit(dealScoreText, (10,100))
            if winner == False:
                gameoverText = font.render("House Wins! ", True, PURPLE)
            else:
                gameoverText = font.render("YOU WON!!! ", True, PURPLE)
            background.blit(gameoverText, (250,250))

        

        pygame.display.update()
        clock.tick(10)


        




    pygame.quit()

if __name__ == "__main__":
    main()


