import time
import random
import os
import math
import pygame


class Mon:

    def __init__(self):

       
        self.image = pygame.image.load("img/bobo.png")
        

        self.timealive = 0
        self.age = 0
        self.stage = 0
        self.hunger = 50
        self.energy = 50
        self.sleeping=False
        self.alive=True
        self.love=60
        self.fuckedlove=False
        self.pooneed = 0
        self.health = 90
        self.sick = False
        self.maxlife=2400
        self.uncleanpoo=False
        self.fuckups = 0

    def feed(self):
        self.hunger-=20
        self.love+=2

    def givePets(self):
        self.love+=20

    def update(self):

        self.timealive+=1
        
        #self.energy-=1

        self.doHealth()
        
        if self.hunger<50 or random.randint(0,( 3 - int(self.hunger<25) ))==1:
            self.pooneed+=1
            if self.pooneed>100:
                self.pooneed=100

        if self.pooneed>55 or self.sick:
            if random.random()==self.pooneed/100:
                self.poo()

        if self.hunger>75:
            self.love-=1
            self.hunger+=1
        else:
            if random.randint(0,2)==2:
                self.hunger+=1
        

        if self.hunger>100:
            self.hunger=100
        if self.hunger<0:
            self.hunger=0
        if self.love<0:
            self.love=0

        if self.love<25 and not self.fuckedlove:
            self.fuckups+=1
            self.fuckedlove=True


        if self.love>=85 and self.fuckedlove:
            self.fuckedlove=False
            

        self.checkDeath()

    def doHealth(self):
        if random.randint(0,8)==1 or self.sick or (self.hunger > 77) or self.uncleanpoo:
            self.health-= (1 + int(self.uncleanpoo)+ int(random.randint(0,7)==1))

        if self.health<=0:
            self.health=0

        if not self.sick and self.health<60:
            self.doSick()

    def doSick(self):

        if self.health <= 15:
            self.sick = random.randint(0,1)==1
        elif self.health >15 and self.health <= 35:
            self.sick = random.randint(0,8)==1
        elif self.health >35 and self.health <=55:
            self.sick = random.randint(0,15)==1
        else:
            self.sick = random.randint(0,100)==1



        if self.sick:
            self.fuckups+=1
            print("Puuuuuke!")




    def checkDeath(self):
        nonhealth= 100 - self.health

        healthfactor = ((nonhealth/100) * self.maxlife)-10

        chanceofdeath = self.maxlife - (self.timealive/self.timealive) - healthfactor
        dieno = random.randint(1,math.ceil(chanceofdeath))
        
        doop = math.ceil(chanceofdeath)
        print (f"Chance of die: {doop} Die?: {dieno}:1 so {dieno==1}")
        if dieno==1:
            self.die()

    def cureSick():

        self.health+=35
        if self.health>100:
            self.health=100
        if not self.fuckedlove:
            self.love+=10

    def die(self):
        self.alive=False
        print(f"Dead after {self.timealive} cycles.")
        

    def poo(self):

        print("Shit himself.")
        self.uncleanpoo=True
        self.pooneed = 0
        self.hunger+=10
        self.love-=7
        self.fuckups+=1

    def __str__(self):

        st = f"""    Maxlife:  {self.maxlife}
        Lifetime: {self.timealive}
        Health:   {self.health}
        Hunger:   {self.hunger}
        Energy:   {self.energy}
        Love:     {self.love}
        Poo need: {self.pooneed}
        Pooed?:   {self.uncleanpoo}
        Alive:    {self.alive}
        Sick      {self.sick}
        Fuckups:  {self.fuckups}"""

        return st

    def splitStatus(self):
        p1= str(self).split("\n")
        return [p1[i].strip("\n") for i in range(len(p1))]

            
            



def clear():
    if os.name=='nt':
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":

    pass
        
        
