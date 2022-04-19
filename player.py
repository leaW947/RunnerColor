import math

import pygame
import sprite

class Player:

    def __init__(self,pX,pY,pGameplayService):
        self.gameplayService=pGameplayService

        self.currentMap = self.gameplayService.currentMap
        self.TILESIZE = self.currentMap.TILESIZE

        self.sprite=sprite.Sprite(None,pX,pY)
        self.sprite.setTilesheet(32,32)

        #####add animation#####
        self.sprite.addAnimation("idle",self.gameplayService.assetManager.getImage("images/player/idle.png"),
                                 [0,1,2,3],0.5,True)
        self.sprite.addAnimation("ladder", self.gameplayService.assetManager.getImage("images/player/ladder.png"),
                                 [0, 1], 0.2, True)
        self.sprite.addAnimation("ladder_idle", self.gameplayService.assetManager.getImage("images/player/ladder.png"),
                                 [0], 0.2, True)
        self.sprite.addAnimation("move", self.gameplayService.assetManager.getImage("images/player/move.png"),
                                 [0, 1, 2, 3], 0.1, True)
        self.sprite.addAnimation("rope", self.gameplayService.assetManager.getImage("images/player/rope.png"),
                                 [0, 1,2,3], 0.1, True)
        self.sprite.addAnimation("rope_idle", self.gameplayService.assetManager.getImage("images/player/rope.png"),
                                 [0], 0.1, True)

        self.sprite.startAnimation("idle")

        self.vx=0
        self.vy=0

        self.oldX=0
        self.oldY=0

        self.lstColor={
            "red":[255,0,0],
            "blue":[36,179,218],
            "yellow":[255,255,0],
            "orange":[255,127,39],
            "green":[0,255,0],
            "purple":[155,61,186],
            "white":[255,255,255],
            "brown": [104, 57, 25]
        }

        self.color=self.lstColor["white"]
        self.strColor="white"

        self.bOnJump=False
        self.bOnSpace=False

        self.bInHole=False

        self.bIsLadder=False
        self.animation=""

        self.line=0
        self.column=0


    def changeColor(self,pStrColor):

        #########current color-->white###########
        if self.strColor=="white":

            if pStrColor=="red":
                self.color=self.lstColor["red"]

            elif pStrColor=="blue":
                self.color = self.lstColor["blue"]

            elif pStrColor=="yellow":
                self.color = self.lstColor["yellow"]

            self.strColor = pStrColor


        ############current color-->red###########
        elif self.strColor=="red":

            if pStrColor == "red":
                self.strColor="red"
                self.color = self.lstColor["red"]

            elif pStrColor == "blue":
                self.strColor="purple"
                self.color = self.lstColor["purple"]

            elif pStrColor == "yellow":
                self.strColor="orange"
                self.color = self.lstColor["orange"]


        ###################current color-->blue########
        elif self.strColor=="blue":

            if pStrColor == "red":
                self.strColor = "purple"
                self.color = self.lstColor["purple"]

            elif pStrColor == "blue":
                self.strColor=pStrColor
                self.color = self.lstColor["blue"]

            elif pStrColor == "yellow":
                self.strColor="green"
                self.color = self.lstColor["green"]


        ##################current color-->yellow#############
        elif self.strColor=="yellow":

            if pStrColor == "red":
                self.strColor="orange"
                self.color = self.lstColor["orange"]

            elif pStrColor == "blue":
                self.strColor="green"
                self.color = self.lstColor["green"]

            elif pStrColor == "yellow":
                self.strColor=pStrColor
                self.color = self.lstColor["yellow"]

        elif self.strColor=="orange" or self.strColor=="purple" or self.strColor=="green":
            self.strColor="brown"
            self.color=self.lstColor["brown"]


        #######clear color#######
        if pStrColor=="white":
            self.strColor=pStrColor
            self.color=self.lstColor["white"]


        ########color apply#########
        for anim in self.sprite.lstAnimation:
            anim["image"]=self.gameplayService.utils.changeColorImg(anim["image"],self.color,False)



    def updateCollideWithMap(self,dt,pKey):

        ######right##########
        if self.currentMap.collideRight(self.sprite,self.strColor) or \
                self.sprite.x+self.TILESIZE>=self.gameplayService.screen.get_width():

            self.currentMap.onAlignColumn(self.sprite)


        ######left#############
        if self.currentMap.collideLeft(self.sprite,self.strColor) or self.sprite.x<=0:
            self.currentMap.onAlignColumn(self.sprite)


        #########above#########
        if self.currentMap.collideAbove(self.sprite,self.strColor) or self.sprite.y<=0:

            if not self.bIsLadder:
                self.currentMap.onAlignLine(self.sprite)

                if self.vy<0:
                    self.vy*=-1


        ###########below############
        if (self.currentMap.collideBelow(self.sprite,self.strColor) and self.vy>0):
            self.currentMap.onAlignLine(self.sprite)

            self.vy=0
            self.bOnJump=False


        ##########collide rope#############
        if self.currentMap.collideRope(self.sprite) and not pKey[pygame.K_DOWN]:
            self.vy=0
            self.currentMap.onAlignLine(self.sprite)

            ########animation rope########
            if self.vx==0:
                self.animation="rope_idle"
            else:
                self.animation="rope"



    def update(self,dt):
        self.sprite.x+=self.vx*dt
        self.sprite.y+=self.vy*dt

        self.oldY=self.sprite.y
        self.oldX=self.sprite.x

        self.line=math.floor((self.sprite.y+self.TILESIZE/2)/self.TILESIZE)
        self.column=math.floor((self.sprite.x+self.TILESIZE/2)/self.TILESIZE)

        key=pygame.key.get_pressed()
        self.animation=""

        maxSpeed = 200
        gravity = 25

        #########ladder ############
        idLadder1=self.currentMap.getTileAt(self.sprite.x+(self.TILESIZE/2),self.sprite.y+(self.TILESIZE-1))
        idLadder2=self.currentMap.getTileAt(self.sprite.x+(self.TILESIZE/2),self.sprite.y+(self.TILESIZE-5))
        idLadder3=self.currentMap.getTileAt(self.sprite.x+(self.TILESIZE/2),self.sprite.y+(self.TILESIZE+3))

        if self.currentMap.isLadder(idLadder1) or self.currentMap.isLadder(idLadder2):
            self.bIsLadder=True
        else:
            self.bIsLadder=False


        ########move (horizontal)#######
        if key[pygame.K_RIGHT]:

            self.vx+=25
            self.sprite.bIsMirrorEffect=False

            if self.vx>=maxSpeed:
                self.vx=maxSpeed

        elif key[pygame.K_LEFT]:
            self.vx-=25
            self.sprite.bIsMirrorEffect = True

            if self.vx<=-maxSpeed:
                self.vx=-maxSpeed

        else:
            self.vx=0


        ########animation move (horizontal)######
            ###no jump             ###no rope
        if self.vy==0 and not self.currentMap.collideRope(self.sprite):
            if self.vx>0:
                self.animation="move"
            elif self.vx<0:
                self.animation="move"
            else:
                self.animation="idle"


        if not self.bIsLadder:

            ########jump#########
            if key[pygame.K_SPACE] and not self.bOnJump and self.bOnSpace:
                if self.sprite.y+self.TILESIZE<self.gameplayService.screen.get_height():
                    self.vy=-500
                    self.bOnJump=True
                    self.bOnSpace=False

            if not key[pygame.K_SPACE] and not self.bOnSpace:
                self.bOnSpace=True


            #####gravity####
            if self.bOnJump or not self.currentMap.collideBelow(self.sprite,self.strColor):
                if not self.bInHole:
                    if self.vy<250:
                        self.vy+=gravity


        ########ladder move#####
        if self.bIsLadder:

            ######move ladder
            if key[pygame.K_UP]:

                ####move up####
                if self.currentMap.isLadder(idLadder1) and self.currentMap.isLadder(idLadder2):
                    self.vy=-100
                else:
                    self.vy=0
                    self.currentMap.onAlignLine(self.sprite)

                ####animation ladder
                if self.gameplayService.currentMap.isLadder(idLadder2) and self.vy<0:
                    self.animation = "ladder"


            elif key[pygame.K_DOWN]:

                ###move down###
                self.vy=100

                ####animation ladder
                if self.gameplayService.currentMap.isLadder(idLadder3) and self.vy>0:
                    self.animation = "ladder"

            else:
                self.vy = 0

                if self.vx==0 and self.currentMap.isLadder(idLadder2):
                    self.animation = "ladder_idle"


        self.sprite.update(dt)
        self.updateCollideWithMap(dt,key)

        #############animation#######
        if self.animation!="":
            if self.sprite.currentAnimation["bLoop"]:
                self.sprite.startAnimation(self.animation)
            else:
                if self.sprite.currentAnimation["bIsFinish"]:
                    self.sprite.startAnimation(self.animation)


    def draw(self):

        if self.line<self.gameplayService.currentMap.height:
            if self.gameplayService.currentMap.data[self.line][self.column]!="1":
                self.sprite.draw(self.gameplayService.screen)