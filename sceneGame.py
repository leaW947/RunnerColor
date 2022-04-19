import math
import pygame

import tileMap
import player
import objectManager
import enemyManager


class SceneGame:

    def __init__(self):
        self.gameplayService=None
        self.sceneLoader=None

        self.myObjectManager=None
        self.myEnemyManager=None

        self.myMap=None
        self.myPlayer=None

        self.timerSpeed=3
        self.timerRespawnBrick=0
        self.lstHole=[]

        self.textLevel=None

        self.bOnGameover=False

        self.mapConcentricCircle=[]
        self.circle={"x":0,"y":0,"radius":50,"bOnAnim":False,"bOnReverseAnim":False,"minRadius":0,"maxRadius":300}


    def initGame(self):

        ##########enemy manager########
        self.myEnemyManager = enemyManager.EnemyManager(self.gameplayService)
        self.gameplayService.setEnemyManager(self.myEnemyManager)

        ######object manager#####
        self.myObjectManager=objectManager.ObjectManager(self.gameplayService)
        self.gameplayService.setObjectManager(self.myObjectManager)

        self.gameplayService.nbCoin=0
        self.timerRespawnBrick = 0

        #######tileMap#######
        self.myMap=tileMap.TileMap(self.gameplayService)
        self.myMap.initData()

        self.gameplayService.setMap(self.myMap)

        #######player#####
        self.myPlayer=player.Player(3*self.myMap.TILESIZE,(self.myMap.height-2)*self.myMap.TILESIZE,self.gameplayService)

        self.mapConcentricCircle = []
        self.circle["radius"]=self.circle["minRadius"]
        self.circle["bOnAnim"]=True
        self.circle["bOnReverseAnim"]=False
        self.circle["x"]=(self.gameplayService.screen.get_width()/2)-(self.circle["radius"]/2)
        self.circle["y"]=(self.gameplayService.screen.get_height()/2)-(self.circle["radius"]/2)

        ###map animation concentric circle
        for l in range(0,self.myMap.height*3):
            self.mapConcentricCircle.append([])
            for c in range(0,self.myMap.width*3):
                self.mapConcentricCircle[l].append(1)


        #######text
        fontText=pygame.font.Font("fonts/smallest_pixel_7/smallest_pixel-7.ttf",50)
        self.textLevel=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/2.5,
                                                                  self.gameplayService.screen.get_height()-50,
                                                                  fontText,[40,40,40],"LEVEL ")


    def load(self,pGameplayService,pSceneLoader):
        self.gameplayService=pGameplayService
        self.sceneLoader=pSceneLoader

        self.initGame()
        self.bOnGameover=False


    def update(self,dt):
        self.textLevel.text="LEVEL "+str(self.gameplayService.currentLevel)

        #################not animation concentric circle#################
        if not self.circle["bOnAnim"] and not self.circle["bOnReverseAnim"]:
            self.myPlayer.update(dt)

            ###########rebuild hole##########
            if len(self.lstHole)>0:
                self.timerRespawnBrick+=dt

                if self.timerRespawnBrick>=self.timerSpeed:

                    hole = self.lstHole[0]
                    self.gameplayService.currentMap.changeData("1", hole)
                    self.lstHole.pop(0)

                    self.timerRespawnBrick = 0


            ###########collision player with the objects of the map##############
            for i in range(len(self.myObjectManager.lstObject)-1,-1,-1):
                myObject=self.myObjectManager.lstObject[i]

                bCollide = self.gameplayService.utils.checkCollision(self.myPlayer.sprite.x, self.myPlayer.sprite.y,
                                                                     self.myPlayer.TILESIZE, self.myPlayer.TILESIZE,
                                                                     myObject.sprite.x, myObject.sprite.y,
                                                                     myObject.sprite.tileSize["x"], myObject.sprite.tileSize["y"])
                if myObject.type=="paintBucket":

                    if bCollide:
                        self.myPlayer.changeColor(myObject.colorType)
                        self.myObjectManager.lstObject.pop(i)

                elif myObject.type=="coin":

                    if bCollide:
                        self.gameplayService.nbCoin-=1
                        self.myObjectManager.lstObject.pop(i)


            ################collision player with enemy############"
            for i in range(len(self.myEnemyManager.lstEnemy)-1,-1,-1):
                myEnemy=self.myEnemyManager.lstEnemy[i]

                #######in hole######
                if myEnemy.bInHole:
                    self.timerRespawnBrick = 0

                ############collide enemy with player########
                bCollide = self.gameplayService.utils.checkCollision(myEnemy.sprite.x+5, myEnemy.sprite.y+5,
                                                                     myEnemy.sprite.tileSize["x"]-5, myEnemy.sprite.tileSize["y"]-5,
                                                                     self.myPlayer.sprite.x+5, self.myPlayer.sprite.y+5,
                                                                     self.myPlayer.sprite.tileSize["x"]-5, self.myPlayer.sprite.tileSize["y"]-5)

                if bCollide:
                    ##########gameover#################
                    myEnemy.vx=0
                    myEnemy.vy=0
                    self.circle["bOnReverseAnim"]=True
                    self.bOnGameover = True


            #############change level############
            if self.gameplayService.nbCoin<=0:
                if self.myPlayer.sprite.y+self.myPlayer.sprite.tileSize["y"]<=0 and self.myPlayer.bIsLadder:
                    self.circle["bOnReverseAnim"] = True
                    self.bOnGameover = False


            ########hole player(gameover)##
            if self.myPlayer.line>=0 and self.myPlayer.line<self.gameplayService.currentMap.height:
                if self.gameplayService.currentMap.data[self.myPlayer.line][self.myPlayer.column]=="1":
                    ####gameover
                    self.circle["bOnReverseAnim"] = True
                    self.bOnGameover = True

            if self.myPlayer.sprite.y>self.gameplayService.screen.get_height():
                self.circle["bOnReverseAnim"] = True
                self.bOnGameover = True


            self.myObjectManager.update(dt)
            self.myEnemyManager.update(dt,self.myPlayer,self.lstHole)


        ########################animation concentric circle###################
        else:
            ################animation concentric circle############
            if self.circle["bOnAnim"]==True:
                self.circle["radius"]+=5

                if self.circle["radius"]>=self.circle["maxRadius"]:
                    self.circle["radius"]=self.circle["maxRadius"]
                    self.circle["bOnAnim"]=False
                    self.circle["bOnReverseAnim"] = False

                    self.gameplayService.assetManager.getSound("sounds/musics/game-over-danijel-zambo-main-version-02-03-1394.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)


            elif self.circle["bOnReverseAnim"]==True:
                pygame.mixer.music.stop()
                self.circle["radius"] -= 10

                if self.circle["radius"]<=self.circle["minRadius"]:
                    self.circle["radius"]=self.circle["minRadius"]
                    self.circle["bOnReverseAnim"] = False
                    self.circle["bOnAnim"] = False

                    if self.bOnGameover:
                        self.myPlayer.changeColor("white")
                        self.sceneLoader.init("gameover")
                    else:
                        if self.gameplayService.currentLevel<self.gameplayService.maxLevel:
                            self.gameplayService.currentLevel += 1
                            self.initGame()
                        else:
                            self.myPlayer.changeColor("white")
                            self.sceneLoader.init("menu")


            ###############clear tiles ################
            for l in range(0, len(self.mapConcentricCircle) - 1):
                for c in range(0, len(self.mapConcentricCircle[l]) - 1):

                    x = c * self.myMap.TILESIZE / 2
                    y = l * self.myMap.TILESIZE / 2

                    distance = self.gameplayService.utils.dist(x, y, self.circle["x"], self.circle["y"])

                    if math.fabs(distance) <= self.circle["radius"] * 2:
                        self.mapConcentricCircle[l][c] = 0

                    else:
                        self.mapConcentricCircle[l][c] = 1



    def draw(self):
        self.myMap.draw(self.myPlayer.strColor)
        self.myObjectManager.draw()
        self.myEnemyManager.draw()

        self.myPlayer.draw()

        if self.circle["bOnAnim"] or self.circle["bOnReverseAnim"]:

            for l in range(0, len(self.mapConcentricCircle)-1):
                for c in range(0, len(self.mapConcentricCircle[l])-1):

                    x=c*self.myMap.TILESIZE/2
                    y=l*self.myMap.TILESIZE/2

                    if self.mapConcentricCircle[l][c]==1:
                        pygame.draw.rect(self.gameplayService.screen,[0,0,0],(x,y,self.myMap.TILESIZE/2,self.myMap.TILESIZE/2))


    def keypressed(self,pKey):

        if pKey[pygame.K_s]:
            ######player make a hole#####
            idHole="0"

            posTile={"x":0,"y":0}

            linSprite=math.floor((self.myPlayer.sprite.y+(self.myPlayer.TILESIZE/2))/self.myPlayer.TILESIZE)
            colSprite=math.floor((self.myPlayer.sprite.x+(self.myPlayer.TILESIZE/2))/self.myPlayer.TILESIZE)

            if not self.myPlayer.sprite.bIsMirrorEffect:

                posTile["x"]=(colSprite+1)*self.myPlayer.TILESIZE
                posTile["y"]=(linSprite+1)*self.myPlayer.TILESIZE

            else:
                posTile["x"] = (colSprite - 1) * self.myPlayer.TILESIZE
                posTile["y"] = (linSprite + 1) * self.myPlayer.TILESIZE


            idHole=self.myMap.getTileAt(posTile["x"],posTile["y"])

            if idHole=="1":
                if self.gameplayService.currentMap.data[self.myPlayer.line+1][self.myPlayer.column]!="0":

                    self.myMap.changeData("2",posTile)
                    self.lstHole.append(posTile)


