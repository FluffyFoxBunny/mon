

class MonStage():

    def __init__(self, leadsTo, canDie=True, isEgg=False, stageLength=400):


        self.stageLength = stageLength
        self.canDie = canDie
        self.isEgg = isEgg
        self.leadsTo = leadsTo


shower = MonStage(None)
grower = MonStage(shower)
kiddo = MonStage(grower)
bab = MonStage(kiddo,canDie=False,stageLength=100)
egg = MonStage(bab,False,True,20)

monstages = [egg,bab,kiddo,grower,shower]

maxlife = 0
for m in monstages:
    maxlife+=m.stageLength

