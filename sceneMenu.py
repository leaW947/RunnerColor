import math

import pygame.font


class SceneMenu:

    def __init__(self):
        self.gameplayService=None
        self.sceneLoader=None

        self.title=None
        self.textPlay=None
        self.textQuit=None
        self.selectText=None

        self.nSelect=1
        self.imgBG=None

        self.sndClick=None
        self.sndScroll=None

        self.lstColor={
            "darkBlue":[0, 4, 28],
            "blue":[0,18,135],
            "yellow":[255,246,74],
            "lightBlue":[90,159,255]
        }

        self.tweeningTitle={
            "time":0,
            "distance":0,
            "begin":0,
            "duration":0
        }

    def load(self,pGameplayService,pSceneLoader):
        self.gameplayService=pGameplayService
        self.sceneLoader=pSceneLoader

        self.imgBG=self.gameplayService.assetManager.getImage("images/BG/bgMenu.png")
        fontTitle=pygame.font.Font("fonts/sonic_advanced_2/Sonic Advanced 2.ttf",90)

        ###########title############
        self.title=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/3.5,
                                                              0-(self.gameplayService.screen.get_height()),fontTitle,
                                                              self.lstColor["lightBlue"],"Runner Color")

        self.tweeningTitle["time"]=0
        self.tweeningTitle["distance"]=math.fabs(self.title.y)+(self.gameplayService.screen.get_height()/7)
        self.tweeningTitle["begin"]=self.title.y
        self.tweeningTitle["duration"]=1

        fontText=pygame.font.Font("fonts/smallest_pixel_7/smallest_pixel-7.ttf",70)

        #####text play and quit####
        self.textPlay=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/2,
                                                                 self.gameplayService.screen.get_height()/2,
                                                                 fontText,self.lstColor["blue"],"PLAY")

        self.textQuit=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/2,
                                                                 self.gameplayService.screen.get_height()/2+70,
                                                                 fontText,self.lstColor["blue"],"QUIT")

        self.selectText=self.gameplayService.GuiManager.createText(self.gameplayService.screen.get_width()/2-70,
                                                                   self.textPlay.y,
                                                                   fontText,self.lstColor["blue"],">")



    def update(self,dt):

        ########tweening title###################
        self.title.y=self.gameplayService.utils.easeOutSine(self.tweeningTitle["time"],self.tweeningTitle["begin"],
                                                           self.tweeningTitle["distance"],self.tweeningTitle["duration"])


        if self.tweeningTitle["time"]>=self.tweeningTitle["duration"]:
            self.tweeningTitle["time"]=self.tweeningTitle["duration"]
        else:
            self.tweeningTitle["time"] += 0.02


        #####select item##########
        if self.nSelect==1:
            self.textPlay.color=self.lstColor["yellow"]
            self.textQuit.color = self.lstColor["blue"]

            self.selectText.y=self.textPlay.y

        elif self.nSelect==2:
            self.textPlay.color = self.lstColor["blue"]
            self.textQuit.color = self.lstColor["yellow"]

            self.selectText.y=self.textQuit.y

        if self.nSelect>2:
            self.nSelect=2
        if self.nSelect<1:
            self.nSelect=1


    def draw(self):
        self.gameplayService.screen.fill(self.lstColor["darkBlue"])

        self.gameplayService.screen.blit(self.imgBG,(0,0))
        self.title.draw(self.gameplayService.screen)

        if self.tweeningTitle["time"]==self.tweeningTitle["duration"]:
            self.textPlay.draw(self.gameplayService.screen)
            self.textQuit.draw(self.gameplayService.screen)
            self.selectText.draw(self.gameplayService.screen)


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
                self.gameplayService.currentLevel=1
                self.sceneLoader.init("gameplay")

            elif self.nSelect==2:
                pygame.quit()
                quit()