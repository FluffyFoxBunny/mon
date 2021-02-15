import mon
import pygame

from pygame.locals import *
import monsprite



class Game:
    """
    The main game class. 

    takes in
    scalex - basically the core game is a 32x32 pixel window.
             this scales that shit up so human eyes can see
             it on today's newfangled screens
    scaley - ditto but for y in case you're a sick fuck who
             wants to strech the window weirdly
    

    tickrate - although the game runs at a constant 60fps
               the Mon only updates every x milliseconds

    """

    def __init__(self, scalex=16, scaley=16, tickrate = 1000):

        self.soundlist = ["sfx/boop1.wav","sfx/boop2.wav","sfx/boop3.wav","sfx/boop4.wav"]

        

        self.FPS = 60 #the framerate

        mon.clear() # clear the debug console so old shit fucks off
        self.tickRate = tickrate #no i'm not using getters and setters. 
        self.myMon = mon.Mon()  # this is the actual mon we'll use

        self.scalex = scalex
        self.scaley = scaley
        self.splay=1



        pygame.init()  #pygame init shit, make window and shapes, etc
        pygame.mixer.init()

        self.sounds = {s:pygame.mixer.Sound(s) for s in self.soundlist}
        self.gamewin = pygame.display.set_mode((32*scalex, 32*scaley))
        self.playarearect = pygame.rect.Rect(0*self.scalex, 8*self.scaley, 
                                        32*self.scalex, 16*self.scalex)
        pygame.display.set_caption("mon")
        icon = pygame.image.load("img/icon.png")
        pygame.display.set_icon(icon)

        self.monSpriteGroup = pygame.sprite.Group()
        self.myMonSprite = monsprite.MonSprite(self.myMon.sprites,
                                                self.scalex,self.scaley,
                                                self.gamewin)
        
        self.monSpriteGroup.add(self.myMonSprite)

        self.BG_COLOUR = (255, 255, 255)
        self.BG_COLOUR2 = (240, 240, 240)

        self.mainClock = pygame.time.Clock()
        self.debugfont = pygame.font.Font(pygame.font.get_default_font(), 16)


        #this bit needs explaining
        #pygame's default text rendering sucks ass
        #with text rendering
        #so i split the Mon's str() into a list of strings
        #each to be rendered separately

        st = self.myMon.splitStatus() 
        self.debugtexts = [[] for _ in range(len(st))] 
        self.debugrects = [[] for _ in range(len(st))] 


        self.lastTick = pygame.time.get_ticks()
        gameon = True

        #the fabled "Game Loop", it's p clean,
        #most of the heavy lifting is done in
        #the helper functions.
        while gameon:

            self.mainClock.tick(self.FPS)
            self.drawScreen()
            self.doMonTick()
            self.doControls()

            for event in pygame.event.get():
           
                if event.type == pygame.QUIT:
                    gameon = False

            pygame.display.flip()



        pygame.quit()

    def doControls(self):

        key = pygame.key.get_pressed()

        if key[K_SPACE] and not self.myMon.alive:
            self.myMon = mon.Mon()

    def setMonSprites(self,sprites):

        self.monSpriteGroup.empty()
        self.myMonSprite = monsprite.MonSprite(sprites,
                                    self.scalex,self.scaley,
                                    self.gamewin,8,8)
        self.monSpriteGroup.add(self.myMonSprite)

    def doMonTick(self):
        #get the mon to update if the number of 
        # milliseconds passed since the last mon "tick"
        # is greater than the tickRate
        
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastTick > self.tickRate:

            self.lastTick = currentTime
            if self.myMon.alive:
                self.myMon.update()

    def drawScreen(self):

        #hoooooooboy this is a doozy. the main draw function
        #again i tried to put this into separate helper functions
        #to increase readability. 

        self.gamewin.fill(self.BG_COLOUR) #main window is white

        #mon "area" is grey
        self.gamewin.fill(rect=self.playarearect, color=self.BG_COLOUR2)


        self.drawMon()
        self.drawPoo()
        self.drawDebugText()




    def drawPoo(self):

        if self.myMon.uncleanpoo and self.myMon.alive:

            pooimg = pygame.image.load("img/poo.png")
            bigspr = pygame.transform.scale(pooimg, (self.scalex*8, self.scaley*8))

            poopos = (self.playarearect.right-self.scalex*9,
                      self.playarearect.top+self.scaley*5)
            self.gamewin.blit(bigspr,poopos ) 

                        

    def drawMon(self):

        

        #draw the mon sprites. this is where the doozy is.
        

        if self.myMon.alive:
            
            self.monSpriteGroup.update()
            #self.monSpriteGroup.draw(self.gamewin)
            if self.myMonSprite.shouldboop:
                self.sounds[f"sfx/boop{self.splay}.wav"].play()
                self.myMonSprite.shouldboop=False
                self.splay+=1
                if self.splay>4:
                    self.splay=1
        else:
            montouse = pygame.image.load("img/grave.png")
            montouse = pygame.transform.scale(montouse, (16*self.scalex, 16*self.scaley))
            self.gamewin.blit(montouse, (8*self.scalex, 8*self.scaley)) 


        #scale up the pic i just got. 
        

        

    def drawDebugText(self):

        #fills the lists of the mons status updates
        #with current texts. 

        statuses = self.myMon.splitStatus()

        for i in range(len(statuses)):

            thisone = self.debugfont.render(statuses[i], True, (0, 0, 0))
            self.debugtexts[i] = thisone
            thisonesrect = thisone.get_rect()
            thisonesrect.x = 8
            thisonesrect.y = 16*(i+1)
            self.debugrects[i] = thisonesrect
            self.gamewin.blit(self.debugtexts[i], self.debugrects[i])


if __name__ == "__main__":

    theGame = Game() #gee i wonder what this does

        
