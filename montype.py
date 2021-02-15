from monstage import *

class MonType():

    def __init__(self,sprites=None,stage=egg,becomes=None):

        self.stage = stage
        self.becomes = becomes
        self._sprites = sprites
        
    

    def setSprites(self,sprites):

        if type(sprites) not in [list,tuple] or sprites == None:
            raise TypeError
        
        self._sprites = sprites
        
    def getSprites(self):
        return self._sprites

    sprites = property(getSprites,setSprites)
        
bobo = MonType(sprites=["img/bobo.png","img/bobo2.png"],stage=bab)
plainegg = MonType(sprites=["img/egg1.png","img/egg2.png"],becomes=[bobo])

