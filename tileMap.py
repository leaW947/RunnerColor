import math
import pygame
import sprite

class TileMap:

    def __init__(self,pGameplayService):
        self.gameplayService=pGameplayService
        self.data=[]

        self.width=0
        self.height=0

        self.tilesImg=self.gameplayService.assetManager.getImage("images/tiles/tiles.png")

        self.lstColor = {
            "greyBlue": [101, 142, 173],
            "white":[255,255,255],
            "red": [255,0,0],
            "yellow": [255, 255, 0],
            "blue":[87,186,216],
            "green": [15,220,0],
            "purple": [155, 61, 186],
            "orange": [255, 127, 39]
        }

        ##############sprites brick############
        self.lstBrick={}

        #######brick through#######
        self.lstBrick["brickThrough"]=sprite.Sprite(self.tilesImg,0,0)
        self.lstBrick["brickThrough"].setTilesheet(32, 32)
        self.lstBrick["brickThrough"].currentFrame = 5


        ########hole
        self.lstBrick["hole"]=sprite.Sprite(self.tilesImg,0,0)
        self.lstBrick["hole"].setTilesheet(32, 32)
        self.lstBrick["hole"].currentFrame = 4


        ###white brick
        self.lstBrick["brick"]=sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brick"].setTilesheet(32,32)
        self.lstBrick["brick"].currentFrame=1

        self.lstBrick["brick"].image=self.gameplayService.utils.changeColorImg(self.lstBrick["brick"].image,
                                                                                     self.lstColor["greyBlue"],True)

        ####red brick
        self.lstBrick["brickRed"]=sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brickRed"].setTilesheet(32,32)
        self.lstBrick["brickRed"].currentFrame=0

        self.lstBrick["brickRed"].image = self.gameplayService.utils.changeColorImg(self.lstBrick["brickRed"].image,
                                                                                      self.lstColor["red"],True)

        ####blue brick
        self.lstBrick["brickBlue"]=sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brickBlue"].setTilesheet(32,32)
        self.lstBrick["brickBlue"].currentFrame=0

        self.lstBrick["brickBlue"].image = self.gameplayService.utils.changeColorImg(self.lstBrick["brickBlue"].image,
                                                                                      self.lstColor["blue"],True)

        ####yellow brick
        self.lstBrick["brickYellow"]=sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brickYellow"].setTilesheet(32,32)
        self.lstBrick["brickYellow"].currentFrame=0

        self.lstBrick["brickYellow"].image = self.gameplayService.utils.changeColorImg(self.lstBrick["brickYellow"].image,
                                                                                      self.lstColor["yellow"],True)

        #####orange brick
        self.lstBrick["brickOrange"] = sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brickOrange"].setTilesheet(32, 32)
        self.lstBrick["brickOrange"].currentFrame = 0

        self.lstBrick["brickOrange"].image = self.gameplayService.utils.changeColorImg(self.lstBrick["brickOrange"].image,
                                                                                      self.lstColor["orange"],True)

        ####green brick
        self.lstBrick["brickGreen"] = sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brickGreen"].setTilesheet(32, 32)
        self.lstBrick["brickGreen"].currentFrame = 0

        self.lstBrick["brickGreen"].image = self.gameplayService.utils.changeColorImg(self.lstBrick["brickGreen"].image,
                                                                                      self.lstColor["green"],True)

        ####purple brick
        self.lstBrick["brickPurple"] = sprite.Sprite(self.tilesImg, 0, 0)
        self.lstBrick["brickPurple"].setTilesheet(32, 32)
        self.lstBrick["brickPurple"].currentFrame = 0

        self.lstBrick["brickPurple"].image = self.gameplayService.utils.changeColorImg(self.lstBrick["brickPurple"].image,
                                                                                      self.lstColor["purple"],True)


        #######sprite ladder##########
        self.sprLadder=sprite.Sprite(self.tilesImg,0,0)
        self.sprLadder.setTilesheet(32,32)
        self.sprLadder.currentFrame=3

        ####sprite rope##########
        self.sprRope=sprite.Sprite(self.tilesImg,0,0)
        self.sprRope.setTilesheet(32,32)
        self.sprRope.currentFrame=2


        self.TILESIZE=32



    def initData(self):
        self.data = []

        #######read file txt#########
        file = open("txtFiles/Level" + str(self.gameplayService.currentLevel) + ".txt", "r")

        for line in file:
            self.data.append(line)

        file.close()

        self.height = len(self.data)
        self.width=len(self.data[0])-1

        ######placement objects#######
        for l in range(0, self.height):
            for c in range(0, self.width):
                id = self.data[l][c]

                x = c * self.TILESIZE
                y = l * self.TILESIZE

                if id != "0":

                    ###########paint Bucket#######
                    if id == "R":
                        self.gameplayService.objectManager.addPaintBucket(x, y, "red")
                    elif id == "Y":
                        self.gameplayService.objectManager.addPaintBucket(x, y, "yellow")
                    elif id == "B":
                        self.gameplayService.objectManager.addPaintBucket(x, y, "blue")
                    elif id=="W":
                        self.gameplayService.objectManager.addPaintBucket(x, y, "white")


                    ########gold bar#########
                    elif id=="*":
                        self.gameplayService.nbCoin+=1
                        self.gameplayService.objectManager.addCoin(x,y)


                    ###############enemy################
                    elif id=="#":
                        self.gameplayService.enemyManager.addEnemy(x,y)




    def changeData(self,pNewId,pPosTile):
        lin=math.floor(pPosTile["y"]/self.TILESIZE)
        col=math.floor(pPosTile["x"]/self.TILESIZE)

        if lin>=0 and col>=0 and lin<self.height and col<self.width:
            newLin=list(self.data[lin])
            newLin[col]=pNewId
            self.data[lin]="".join(newLin)



    def isBrick(self,pId):
        if pId=="1":
            return True

        return False


    def isThrough(self,pId):
        if pId=="_":
            return True

        return False


    def isLadder(self,pId):
        if pId=="H":
            return True
        elif pId=="|" and self.gameplayService.nbCoin<=0:
            return True

        return False


    def isRope(self,pId):
        if pId=="-":
            return True

        return False


    def isColorBrick(self,pId,pColorSprite):

        if pId=="r" and (pColorSprite=="red" or pColorSprite=="none"):
            return True
        elif pId=="b" and (pColorSprite=="blue" or pColorSprite=="none"):
            return True
        elif pId=="y" and (pColorSprite=="yellow" or pColorSprite=="none"):
            return True
        elif pId=="o" and (pColorSprite=="orange" or pColorSprite=="none"):
            return True
        elif pId=="g" and (pColorSprite=="green" or pColorSprite=="none"):
            return True
        elif pId=="p" and (pColorSprite=="purple" or pColorSprite=="none"):
            return True

        return False



    def collideRope(self,pSprite):
        id1=self.getTileAt(pSprite.x+3,pSprite.y+(self.TILESIZE/2))
        id2 = self.getTileAt(pSprite.x + (self.TILESIZE-3), pSprite.y+(self.TILESIZE/2))

        if self.isRope(id1) or self.isRope(id2):
            return True

        return False


    def collideLeft(self,pSprite,pColorSprite):
        id1=self.getTileAt(pSprite.x-1,pSprite.y+3)
        id2=self.getTileAt(pSprite.x-1,pSprite.y+(self.TILESIZE-3))

        if self.isBrick(id1) or self.isBrick(id2):
            return True

        if self.isColorBrick(id1, pColorSprite) or self.isColorBrick(id2, pColorSprite):
            return True

        return False


    def collideRight(self,pSprite,pColorSprite):
        id1=self.getTileAt(pSprite.x+(self.TILESIZE-1),pSprite.y+3)
        id2=self.getTileAt(pSprite.x+(self.TILESIZE-1),pSprite.y+(self.TILESIZE-3))

        if self.isBrick(id1) or self.isBrick(id2):
            return True

        if self.isColorBrick(id1, pColorSprite) or self.isColorBrick(id2, pColorSprite):
            return True

        return False


    def collideAbove(self,pSprite,pColorSprite):
        id1=self.getTileAt(pSprite.x+3,pSprite.y-1)
        id2=self.getTileAt(pSprite.x+(self.TILESIZE-3),pSprite.y-1)

        if self.isBrick(id1) or self.isBrick(id2):
            return True

        if self.isColorBrick(id1, pColorSprite) or self.isColorBrick(id2, pColorSprite):
            return True

        return False


    def collideBelow(self,pSprite,pColorSprite):
        id1=self.getTileAt(pSprite.x+(self.TILESIZE/4),pSprite.y+(self.TILESIZE-1))
        id2=self.getTileAt(pSprite.x+(self.TILESIZE-(self.TILESIZE/4)),pSprite.y+(self.TILESIZE-1))

        if self.isBrick(id1) or self.isBrick(id2):
            return True

        if self.isColorBrick(id1, pColorSprite) or self.isColorBrick(id2, pColorSprite):
            return True

        if self.isThrough(id1) or self.isThrough(id2):

            lin=math.floor((pSprite.y+(self.TILESIZE/2))/self.TILESIZE)
            yLin=lin*self.TILESIZE
            dist=pSprite.y-yLin

            if dist>0 and dist<=10:
                return True

        return False


    def onAlignColumn(self,pSprite):
        col=math.floor((pSprite.x+(self.TILESIZE/2))/self.TILESIZE)
        pSprite.x=col*self.TILESIZE


    def onAlignLine(self,pSprite):
        lin=math.floor((pSprite.y+(self.TILESIZE/2))/self.TILESIZE)
        pSprite.y=lin*self.TILESIZE


    def getTileAt(self,pX,pY):

        col=math.floor(pX/self.TILESIZE)
        lin=math.floor(pY/self.TILESIZE)

        if col>=0 and lin>=0 and col<self.width and lin<self.height:
            id=self.data[lin][col]
            return id

        return -1


    def getPosTile(self,pLin,pCol):
        x=pCol*self.TILESIZE
        y=pLin*self.TILESIZE

        if x>=0 and y>=0 and x<=self.gameplayService.screen.get_width() and y<=self.gameplayService.screen.get_height():
            pos={"x":x,"y":y}
            return pos

        return -1


    def draw(self,pColorSprite):

        for l in range(0,self.height):
            for c in range(0,self.width):

                id=self.data[l][c]

                x=c*self.TILESIZE
                y=l*self.TILESIZE

                if id!="0":

                    if id=="1":
                        self.lstBrick["brick"].x=x
                        self.lstBrick["brick"].y=y

                        self.lstBrick["brick"].draw(self.gameplayService.screen)

                    elif id=="2":
                        self.lstBrick["hole"].x=x
                        self.lstBrick["hole"].y = y

                        self.lstBrick["hole"].draw(self.gameplayService.screen)

                    elif id=="_":
                        self.lstBrick["brickThrough"].x=x
                        self.lstBrick["brickThrough"].y=y

                        self.lstBrick["brickThrough"].draw(self.gameplayService.screen)

                    elif id=="H":
                        self.sprLadder.x=x
                        self.sprLadder.y=y

                        self.sprLadder.draw(self.gameplayService.screen)

                    elif id=="|" and self.gameplayService.nbCoin<=0:
                        self.sprLadder.x = x
                        self.sprLadder.y = y

                        self.sprLadder.draw(self.gameplayService.screen)

                    elif id=="-":

                        self.sprRope.x=x
                        self.sprRope.y=y

                        self.sprRope.draw(self.gameplayService.screen)

                    #############brick color############

                    #####red brick

                    elif id=="r":

                        self.lstBrick["brickRed"].x = x
                        self.lstBrick["brickRed"].y = y

                        if pColorSprite!="red":
                            self.lstBrick["brickRed"].image.set_alpha(40)
                        else:
                            self.lstBrick["brickRed"].image.set_alpha(255)

                        self.lstBrick["brickRed"].draw(self.gameplayService.screen)

                    #######yellow brick
                    elif id=="y":
                        self.lstBrick["brickYellow"].x = x
                        self.lstBrick["brickYellow"].y = y

                        if pColorSprite != "yellow":
                            self.lstBrick["brickYellow"].image.set_alpha(40)
                        else:
                            self.lstBrick["brickYellow"].image.set_alpha(255)

                        self.lstBrick["brickYellow"].draw(self.gameplayService.screen)


                    ######blue brick
                    elif id=="b":
                        self.lstBrick["brickBlue"].x = x
                        self.lstBrick["brickBlue"].y = y

                        if pColorSprite != "blue":
                            self.lstBrick["brickBlue"].image.set_alpha(40)
                        else:
                            self.lstBrick["brickBlue"].image.set_alpha(255)

                        self.lstBrick["brickBlue"].draw(self.gameplayService.screen)


                    ######purple brick
                    elif id=="p":
                        self.lstBrick["brickPurple"].x = x
                        self.lstBrick["brickPurple"].y = y

                        if pColorSprite != "purple":
                            self.lstBrick["brickPurple"].image.set_alpha(40)
                        else:
                            self.lstBrick["brickPurple"].image.set_alpha(255)

                        self.lstBrick["brickPurple"].draw(self.gameplayService.screen)


                    #######orange brick
                    elif id=="o":
                        self.lstBrick["brickOrange"].x = x
                        self.lstBrick["brickOrange"].y = y

                        if pColorSprite != "orange":
                            self.lstBrick["brickOrange"].image.set_alpha(40)
                        else:
                            self.lstBrick["brickOrange"].image.set_alpha(255)

                        self.lstBrick["brickOrange"].draw(self.gameplayService.screen)


                    #####green brick
                    elif id=="g":
                        self.lstBrick["brickGreen"].x = x
                        self.lstBrick["brickGreen"].y = y

                        if pColorSprite != "green":
                            self.lstBrick["brickGreen"].image.set_alpha(40)
                        else:
                            self.lstBrick["brickGreen"].image.set_alpha(255)

                        self.lstBrick["brickGreen"].draw(self.gameplayService.screen)
