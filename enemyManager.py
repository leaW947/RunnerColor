import math
import random
import pygame
import sprite


################################CLASS ENEMY#########################################
class Enemy:

    def __init__(self,pSprite,pGameplayService):
        self.gameplayService=pGameplayService
        self.sprite=pSprite

        self.id=0
        self.speed =1

        self.timerSpeed=3
        self.timerHole=0

        self.vx=math.fabs(random.randint(1,2))

        if self.vx==1:
            self.vx=self.speed
        elif self.vx==2:
            self.vx=-self.speed

        self.vy=0

        self.oldX=0
        self.oldY=0

        self.oldVx=0

        self.animation=""

        self.column=-1
        self.line=-1

        self.bIsLadder=False
        self.bOnLadder=False

        self.bInHole=False


    def updateCollideWithMap(self):

        ######right#######
        if self.gameplayService.currentMap.collideRight(self.sprite,"none") and self.vx>0:
            self.sprite.x=self.oldX
            self.vx*=-1


        ########left########
        if self.gameplayService.currentMap.collideLeft(self.sprite,"none") and self.vx<0:
            self.sprite.x=self.oldX
            self.vx*=-1


        #######down#######
        if self.gameplayService.currentMap.collideBelow(self.sprite,"none"):
            self.vy=0
            self.gameplayService.currentMap.onAlignLine(self.sprite)

        #######rope##########
        if self.gameplayService.currentMap.collideRope(self.sprite):
            self.vy=0
            self.animation="rope"


    def rndMoveX(self):
        rnd=math.fabs(random.randint(1,2))
        vx=0

        if rnd==1:
            vx=self.speed
        else:
            vx=-self.speed

        return vx


    def update(self,dt,pPlayer,pLstHole):
        self.animation=""

        self.line = math.floor((self.sprite.y + self.gameplayService.currentMap.TILESIZE / 2) / self.gameplayService.currentMap.TILESIZE)
        self.column = math.floor((self.sprite.x + self.gameplayService.currentMap.TILESIZE / 2) / self.gameplayService.currentMap.TILESIZE)

        self.sprite.x+=self.vx
        self.sprite.y+=self.vy

        self.oldX=self.sprite.x
        self.oldY=self.sprite.y

        ##########idLadder###################
        idLadder1=self.gameplayService.currentMap.getTileAt(self.sprite.x+(self.sprite.tileSize["x"]/2),
                                                           self.sprite.y+(self.sprite.tileSize["y"]+3))
        idLadder2 = self.gameplayService.currentMap.getTileAt(self.sprite.x + (self.sprite.tileSize["x"] / 2),
                                                            self.sprite.y + (self.sprite.tileSize["y"]-5))

        if self.gameplayService.currentMap.isLadder(idLadder1) or self.gameplayService.currentMap.isLadder(idLadder2):
            self.bIsLadder = True
        else:
            self.bIsLadder = False

        if not self.gameplayService.currentMap.isLadder(idLadder1) and not self.gameplayService.currentMap.isLadder(idLadder2):
            self.bOnLadder = True

        ############end hole(respawn)########################"
        if self.bInHole:
            self.timerHole += dt

            if self.timerHole >= self.timerSpeed:
                self.timerHole = self.timerSpeed

                pos={"x":self.column*self.gameplayService.currentMap.TILESIZE,"y":self.line*self.gameplayService.currentMap.TILESIZE}
                self.gameplayService.currentMap.changeData("1", pos)

                ########delete tileHole#######
                for i in range(0, len(pLstHole)):
                    hole = pLstHole[i]

                    if pos["x"]==hole["x"] and pos["y"]==hole["y"]:
                        pLstHole.pop(i)
                        break


                ########pos x and move#######
                if self.oldVx>0:

                    if self.column+1<self.gameplayService.currentMap.width and \
                        self.gameplayService.currentMap.data[self.line-1][self.column+1]=="0":

                        self.sprite.x=(self.column+1)*self.gameplayService.currentMap.TILESIZE
                        self.vx=self.speed

                    else:
                        self.sprite.x = (self.column - 1) * self.gameplayService.currentMap.TILESIZE
                        self.vx=-self.speed

                elif self.oldVx<0:

                    if self.column-1>0 and self.gameplayService.currentMap.data[self.line-1][self.column-1]=="0":

                        self.sprite.x=(self.column-1)*self.gameplayService.currentMap.TILESIZE
                        self.vx=-self.speed
                    else:
                        self.sprite.x = (self.column + 1) * self.gameplayService.currentMap.TILESIZE
                        self.vx = self.speed

                self.sprite.y = (self.line - 1) * self.gameplayService.currentMap.TILESIZE

                self.bInHole=False



        #########move ladder########
        if self.bOnLadder and not self.bInHole:
            self.animation="ladder"

            if self.line >= 0 and self.column >= 0 and self.column < self.gameplayService.currentMap.width - 1 and \
                self.line < self.gameplayService.currentMap.height - 1:

                if self.vy==0:
                    #########up########
                    if self.gameplayService.currentMap.isLadder(idLadder2) and \
                        self.gameplayService.currentMap.data[self.line][self.column] == "H":

                        if self.gameplayService.currentMap.data[self.line-1][self.column]=="H":
                            rnd=random.randint(1,2)

                            if rnd==1:
                                self.vx = 0
                                self.vy = -self.speed
                                self.gameplayService.currentMap.onAlignColumn(self.sprite)
                            else:
                                self.bOnLadder=False
                        else:
                            self.vx=0
                            self.vy=self.speed
                            self.gameplayService.currentMap.onAlignColumn(self.sprite)

                    ######down######
                    elif self.gameplayService.currentMap.isLadder(idLadder1) and \
                        self.gameplayService.currentMap.data[self.line+1][self.column]=="H":

                        rnd = random.randint(1, 2)

                        if rnd==1:
                            self.vx=0
                            self.vy=self.speed
                            self.gameplayService.currentMap.onAlignColumn(self.sprite)
                        else:
                            self.bOnLadder=False

                else:
                    ##########stop ladder###########
                    ####down###
                    if self.vy>0:

                        if self.gameplayService.currentMap.data[self.line + 1][self.column] != "H":
                            self.bOnLadder = False
                            self.gameplayService.currentMap.onAlignLine(self.sprite)
                            self.vy = 0

                            if self.gameplayService.currentMap.data[self.line+1][self.column]=="0":
                                ########with rope#######
                                if self.gameplayService.currentMap.data[self.line][self.column+1]=="-":
                                    self.vx = self.speed

                                elif self.gameplayService.currentMap.data[self.line][self.column-1]=="-":
                                    self.vx = -self.speed
                                else:
                                    self.vx=0
                                    self.vy=-self.speed

                            else:
                                self.vx = self.rndMoveX()

                    #########up######
                    elif self.vy<0:

                        if self.gameplayService.currentMap.data[self.line-1][self.column]!="H":
                            bIsStop=False

                            if self.gameplayService.currentMap.data[self.line][self.column+1]=="-":
                                self.vx = self.speed
                                bIsStop=True

                            elif self.gameplayService.currentMap.data[self.line][self.column-1]=="-":
                                self.vx = -self.speed
                                bIsStop = True

                            else:
                                if self.gameplayService.currentMap.data[self.line][self.column] != "H":
                                    self.vx = self.rndMoveX()
                                    bIsStop = True

                            if bIsStop:
                                self.vy=0
                                self.bOnLadder=False
                                self.gameplayService.currentMap.onAlignLine(self.sprite)


        ############collison with the map###########
        if not self.bInHole and not self.bIsLadder:

            if self.line>=0 and self.column>=0 and self.line<self.gameplayService.currentMap.height-1 and \
                self.column<self.gameplayService.currentMap.width-1:

                #######not brick####
                if self.vx>0:
                    if self.gameplayService.currentMap.data[self.line+1][self.column+1]=="0" and \
                        self.gameplayService.currentMap.data[self.line][self.column+1]!="-" and \
                        self.gameplayService.currentMap.data[self.line][self.column+1]!="H":

                        self.sprite.x=self.oldX
                        self.vx*=-1

                elif self.vx<0:
                    if self.gameplayService.currentMap.data[self.line + 1][self.column - 1] == "0" and \
                        self.gameplayService.currentMap.data[self.line][self.column-1]!="-" and \
                        self.gameplayService.currentMap.data[self.line][self.column-1]!="H":

                        self.sprite.x = self.oldX
                        self.vx *= -1


                ############in hole############
                if self.gameplayService.currentMap.data[self.line+1][self.column]=="2":
                    self.timerHole=0
                    self.bInHole=True

                    self.oldVx=self.vx

                    self.sprite.x=self.column*self.gameplayService.currentMap.TILESIZE
                    self.sprite.y=(self.line+1)*self.gameplayService.currentMap.TILESIZE

                    self.vx=0
                    self.vy=0


        ############rope############
        if self.gameplayService.currentMap.collideRope(self.sprite):
            self.vy=0
            self.gameplayService.currentMap.onAlignLine(self.sprite)


        ######collision with the screen
        if self.sprite.x<=0:
            self.sprite.x=0
            self.vx*=-1

        elif self.sprite.x+self.sprite.tileSize["x"]>=self.gameplayService.screen.get_width():
            self.sprite.x=self.gameplayService.screen.get_width()-self.sprite.tileSize["x"]
            self.vx*=-1


        #########animation move(horizontal)######
        if self.vx!=0:

            if not self.gameplayService.currentMap.collideRope(self.sprite):
                self.animation="move"

                if self.vx>0:
                    self.sprite.bIsMirrorEffect=True
                elif self.vx<0:
                    self.sprite.bIsMirrorEffect=False
        else:
            if not self.bIsLadder and not self.gameplayService.currentMap.collideRope(self.sprite):
                self.animation="idle"


        self.sprite.update(dt)
        self.updateCollideWithMap()

        ##########animation########
        if self.animation!="":
            if self.sprite.currentAnimation["bLoop"]:
                self.sprite.startAnimation(self.animation)

            else:
                if self.sprite.currentAnimation["bIsFinish"]:
                    self.sprite.startAnimation(self.animation)



    def draw(self):
        self.sprite.draw(self.gameplayService.screen)



#####################################CLASS ENEMY MANAGER##################################
class EnemyManager:

    def __init__(self,pGameplayService):
        self.gameplayService=pGameplayService
        self.lstEnemy=[]


    def addEnemy(self,pX,pY):

        sprEnemy=sprite.Sprite(None,pX,pY)
        sprEnemy.setTilesheet(32,35)

        sprEnemy.addAnimation("idle",self.gameplayService.assetManager.getImage("images/enemy/idle.png"),[0],0.1,True)
        sprEnemy.addAnimation("move",self.gameplayService.assetManager.getImage("images/enemy/move.png"),[0,1,2,3],0.1,True)
        sprEnemy.addAnimation("ladder",self.gameplayService.assetManager.getImage("images/enemy/ladder.png"),[0,1],0.2,True)
        sprEnemy.addAnimation("rope",self.gameplayService.assetManager.getImage("images/enemy/rope.png"),[0,1,2,3],0.1,True)

        sprEnemy.startAnimation("idle")

        myEnemy=Enemy(sprEnemy,self.gameplayService)
        myEnemy.id=len(self.lstEnemy)

        self.lstEnemy.append(myEnemy)



    def update(self,dt,pPlayer,pLstHole):

        for i in range(len(self.lstEnemy)-1,-1,-1):
            myEnemy=self.lstEnemy[i]

            ##########is active#########
            myEnemy.update(dt, pPlayer,pLstHole)



    def draw(self):

        for myEnemy in self.lstEnemy:
            myEnemy.draw()