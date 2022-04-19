import pygame
import sprite

class Coin:

    def __init__(self,pSprite):

        self.sprite=pSprite
        self.type="coin"


    def update(self,dt):
        self.sprite.update(dt)


    def draw(self,pScreen):
        self.sprite.draw(pScreen)


class PaintBucket:

    def __init__(self,pSprite,pColoType):

        self.type="paintBucket"

        self.colorType=pColoType
        self.sprite=pSprite

        if self.colorType=="red":
            self.sprite.currentFrame=1

        elif self.colorType=="yellow":
            self.sprite.currentFrame=3

        elif self.colorType=="blue":
            self.sprite.currentFrame=2

        elif self.colorType=="white":
            self.sprite.currentFrame=0


    def update(self,dt):
        self.sprite.update(dt)


    def draw(self,pScreen):
        self.sprite.draw(pScreen)


class ObjectManager:

    def __init__(self,pGameplayService):
        self.lstObject=[]
        self.gameplayService=pGameplayService


    def addPaintBucket(self,pX,pY,pColorType):

        sprPaintBucket=sprite.Sprite(self.gameplayService.assetManager.getImage("images/objects/paintBuckets.png"),pX,pY)
        sprPaintBucket.setTilesheet(32,32)

        myPaintBucket=PaintBucket(sprPaintBucket,pColorType)
        self.lstObject.append(myPaintBucket)


    def addCoin(self,pX,pY):
        sprCoin=sprite.Sprite(self.gameplayService.assetManager.getImage("images/objects/cleMolette.png"),pX,pY)
        sprCoin.setTilesheet(32,32)
        sprCoin.currentFrame=0

        myCoin=Coin(sprCoin)

        self.lstObject.append(myCoin)



    def update(self,dt):

        for myObject in self.lstObject:
            myObject.update(dt)


    def draw(self):

        for myObject in self.lstObject:
            myObject.draw(self.gameplayService.screen)