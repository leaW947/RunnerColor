import math
import pygame


class Sprite:

    def __init__(self,pImg,pX,pY):
        self.gameplayService=None
        self.image=pImg

        self.x=pX
        self.y=pY

        self.currentFrame=0
        self.currentFrameInAnimation=0

        self.timerFrame=0

        self.lstAnimation=[]
        self.currentAnimation=None

        self.bIsTilesheet=False
        self.tileSize={"x":0,"y":0}

        self.bIsMirrorEffect=False


    def setTilesheet(self,pWFrame,pHFrame):
        self.bIsTilesheet=True

        self.tileSize["x"]=pWFrame
        self.tileSize["y"]=pHFrame


    def addAnimation(self,pName,pImg,pLstFrames,pSpeed,pbLoop):
        animation={
            "name":pName,
            "lstFrames":pLstFrames,
            "image":pImg,
            "speed":pSpeed,
            "bLoop":pbLoop,
            "bIsFinish":False
        }

        self.lstAnimation.append(animation)


    def startAnimation(self,pName):

        if self.currentAnimation!=None:
            if self.currentAnimation["name"]==pName:
                return


        for animation in self.lstAnimation:

            if animation["name"]==pName:

                self.currentAnimation=animation
                self.currentFrameInAnimation=0
                self.currentFrame=self.currentAnimation["lstFrames"][self.currentFrameInAnimation]
                self.currentAnimation["bIsFinish"]=False


    def update(self,dt):

        if self.currentAnimation!=None:

            self.timerFrame+=dt

            if self.timerFrame>=self.currentAnimation["speed"]:
                self.timerFrame=0
                self.currentFrameInAnimation+=1

                if self.currentFrameInAnimation>len(self.currentAnimation["lstFrames"])-1:

                    if self.currentAnimation["bLoop"]:
                        self.currentFrameInAnimation=0
                    else:
                        self.currentFrameInAnimation=len(self.currentAnimation["lstFrames"])-1
                        self.currentAnimation["bIsFinish"]=True

                self.currentFrame=self.currentAnimation["lstFrames"][self.currentFrameInAnimation]



    def draw(self,pScreen):

        if not self.bIsTilesheet:
            pScreen.blit(self.image,(self.x,self.y))

        elif self.bIsTilesheet:
            image=None
            nbCol=0

            if self.image != None:
                image=self.image
            else:
                image=self.currentAnimation["image"]


            nbCol = image.get_width() / self.tileSize["x"]

            l = math.floor(self.currentFrame / nbCol)
            c = math.floor(self.currentFrame - (l * nbCol))

            x = c * self.tileSize["x"]
            y = l * self.tileSize["y"]

            if self.bIsMirrorEffect:
                image = pygame.transform.flip(image, True, False)

            pScreen.blit(image, (self.x, self.y), (x, y, self.tileSize["x"],self.tileSize["y"]))
