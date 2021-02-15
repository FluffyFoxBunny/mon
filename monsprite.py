import pygame

class MonSprite(pygame.sprite.Sprite):

    def __init__(self,pics,scalex,scaley,win):

        pygame.sprite.Sprite.__init__(self)

        self.initTick = pygame.time.get_ticks()
        self.scalex = scalex
        self.scaley = scaley
        self.pics = pics
        self.win = win
        self.shouldboop=False

        self.frame = 0
        self.direction=1

        img = pygame.image.load(pics[0])

        
        
        self.image = pygame.transform.scale(img, (16*self.scalex, 16*self.scaley))
        self.rect = self.image.get_bounding_rect()
        
        self.diffx = (abs(img.get_rect().height - self.rect.height) //2)
        self.diffy = abs(img.get_rect().height - self.rect.height) //2
        self.rect.x = self.win.get_width() // 2 - self.rect.width//2
        self.rect.y = self.win.get_height() //2 - self.rect.height//2

        
       # print (f"{self.rect.width} maskrect: {self.maskrect.width} mask:{self.mask.get_size()}")
   

        
        


    def update(self):

        timenow = pygame.time.get_ticks()

        
        #self.maskrect = self.mask.get_rect()
       # d1 = self.rect.width - self.maskrect.width
       # d2 = self.rect.height - self.maskrect.height
       # self.maskrect.center = (self.rect.centerx-d1,self.rect.centery-d2)

        
        
        if timenow-self.initTick>500:
            self.initTick=timenow
            self.shouldboop=True
            self.frame = int(not self.frame)
            
            #print(self.win.get_rect().width)
            c1 = self.rect.right + self.scalex >= self.win.get_rect().width +self.scalex
            c2 = self.rect.left-self.scalex <= 0-self.scalex
            if c1 or c2:
                self.direction*=-1
            self.rect.x += self.direction * (self.scalex)
           

        self.image = pygame.transform.scale( pygame.image.load(self.pics[self.frame]),
                                             (16*self.scalex, 16*self.scaley))
        #self.win.fill((255,0,0),self.rect)
        
        


        self.win.blit(self.image,(self.rect.x-self.diffx+self.scalex,self.rect.y-self.diffy))
                
        

        







