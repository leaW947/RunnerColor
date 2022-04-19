import math

import pygame


class SceneGameover:

    def __init__(self):
        self.gameplayService=None
        self.sceneLoader=None

        self.imgBG=None
        self.title=None

        self.nSelect=1

        self.lstColor={
            "darkRed":[182,0,0],
            "lightRed":[255,60,60],
            "yellow":[255,246,74]
        }

        self.textMenuReturn=None
        self.textReloadGame=None
        self.selectText=None

        self.tweeningTitle={
            "time":0,
            "duration":0,
            "begin":0,
            "distance":0
        }


    def load(self,pGameplayService,pSceneLoader):
        self.gameplayService=pGameplayService
        self.sceneLoader=pSceneLoader

        ##########title#########
        fontTitle=pygame.font.Font("fonts/sonic_advanced_2/Sonic Advanced 2.ttf",100)
        self.title=self.gameplayService.GuiManager.createText(0-self.gameplayService.screen.get_width(),
                                                              self.gameplayService.screen.get_height()/8,
                                                              fontTitle,self.lstColor["lightRed"],"GAMEOVER")

        self.tweeningTitle["time"]=0
        self.tweeningTitle["begin"]=self.title.x
        self.tweeningTitle["distance"]=math.fabs(self.title.x)+(self.gameplayService.screen.get_width()/3)
        self.tweeningTitle["duration"]=2


        ######text########
        fontText=pygame.font.Font("fonts/smallest_pixel_7/smallest_pixel-7.ttf",60)
        self.textReloadGame=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/3,
                                                                       self.gameplayService.screen.get_height()/2,
                                                                       fontText,self.lstColor["darkRed"],"REJOUER")

        self.textMenuReturn=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/3,
                                                                       self.gameplayService.screen.get_height()/2+60,
                                                                       fontText,self.lstColor["darkRed"],"MENU")

        self.selectText=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/4,
                                                                   self.textReloadGame.y,
                                                                   fontText,self.lstColor["darkRed"],">")

        #######bg
        self.imgBG=self.gameplayService.assetManager.getImage("images/BG/bgGameover.png")


    def update(self,dt):

        ###########tweening#####
        self.title.x=self.gameplayService.utils.easeOutSine(self.tweeningTitle["time"],self.tweeningTitle["begin"],
                                                            self.tweeningTitle["distance"],self.tweeningTitle["duration"])

        if self.tweeningTitle["time"]>=self.tweeningTitle["duration"]:
            self.tweeningTitle["time"]=self.tweeningTitle["duration"]
        else:
            self.tweeningTitle["time"] += 0.02


        #######select

        if self.nSelect==1:

            self.textReloadGame.color=self.lstColor["yellow"]
            self.textMenuReturn.color=self.lstColor["darkRed"]

            self.selectText.y=self.textReloadGame.y
        elif self.nSelect==2:

            self.textReloadGame.color = self.lstColor["darkRed"]
            self.textMenuReturn.color = self.lstColor["yellow"]

            self.selectText.y=self.textMenuReturn.y

        if self.nSelect > 2:
            self.nSelect = 2
        elif self.nSelect < 1:
            self.nSelect = 1


    def draw(self):
        self.gameplayService.screen.blit(self.imgBG,(0,0))

        self.title.draw(self.gameplayService.screen)

        if self.tweeningTitle["time"]==self.tweeningTitle["duration"]:
            self.selectText.draw(self.gameplayService.screen)
            self.textMenuReturn.draw(self.gameplayService.screen)
            self.textReloadGame.draw(self.gameplayService.screen)


    def keypressed(self,pKey):
        self.gameplayService.assetManager.getSound("sounds/FGBS(7).ogg")

        if pKey[pygame.K_UP]:
            pygame.mixer.music.play()
            self.nSelect-=1

        elif pKey[pygame.K_DOWN]:
            pygame.mixer.music.play()
            self.nSelect+=1

        elif pKey[pygame.K_RETURN]:

            if self.nSelect==1:
                self.sceneLoader.init("gameplay")

            elif self.nSelect==2:
                self.sceneLoader.init("menu")