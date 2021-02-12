import mon
import pygame


class Game:

    def __init__(self, scalex=32, scaley=32, timescale=1):

        timescale = 0.05
        mon.clear()
        myMon = mon.Mon()

        scalex = 24
        scaley = 24

        pygame.init()
        gamewin = pygame.display.set_mode((32*scalex, 32*scaley))
        pygame.display.set_caption("mon")

        BG_COLOUR = (255, 255, 255)
        BG_COLOUR2 = (240, 240, 240)

        mainClock = pygame.time.Clock()
        debugfont = pygame.font.Font(pygame.font.get_default_font(), 16)

        statuses = myMon.splitStatus()

        stexts = []
        srects = []

        for i in range(len(statuses)):

            thisone = debugfont.render(statuses[i], True, (0, 0, 0))
            stexts.append(thisone)
            thisonesrect = thisone.get_rect()
            thisonesrect.x = 16
            thisonesrect.y = 16*(i+1)
            srects.append(thisonesrect)

        gameon = True

        timedoober = 0
        secs = 0

        frame = 0

        while gameon:

            mainClock.tick(60)

            gamewin.fill(BG_COLOUR)

            playarearect = pygame.rect.Rect(
                0*scalex, 8*scaley, 32*scalex, 16*scalex)

            gamewin.fill(rect=playarearect, color=BG_COLOUR2)

            if myMon.alive:
                if frame == 0:
                    montouse = pygame.image.load("img/bobo.png")
                else:
                    montouse = pygame.image.load("img/bobo2.png")

            else:
                montouse = pygame.image.load("img/grave.png")
            bigspr = pygame.transform.scale(montouse, (16*scalex, 16*scaley))
            gamewin.blit(bigspr, (8*scalex, 8*scaley))

            statuses = myMon.splitStatus()

            for i in range(len(stexts)):

                stexts[i] = debugfont.render(statuses[i], True, (0, 0, 0))
                gamewin.blit(stexts[i], srects[i])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameon = False

            timedoober += 1
            if timedoober >= 60:
                frame += 1
                timedoober = 0
                secs += 1
            if secs >= timescale:
                secs = 0
                if myMon.alive:
                    myMon.update()

            if frame > 1:
                frame = 0

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":

    theGame = Game()
