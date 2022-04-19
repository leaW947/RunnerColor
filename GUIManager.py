import pygame

#############################################CLASS BUTTON###########################
class Button:

    def __init__(self,pX,pY):
        self.x=pX
        self.y=pY

        self.type="button"

        self.width=0
        self.height=0

        self.colorNormal=[255,255,255]
        self.colorHover = [255, 255, 255]
        self.colorPressed = [255, 255, 255]

        self.imgHover=None
        self.imgPressed=None
        self.imgNormal=None

        self.bIsHover=False
        self.bIsPressed=False

        self.text=None


    def addImages(self,pImgNormal,pImgHover,pImgPressed):
        self.imgNormal=pImgNormal
        self.imgHover=pImgHover
        self.imgPressed=pImgPressed

        self.width=self.imgNormal.get_width()
        self.height=self.imgNormal.get_height()


    def addColors(self,pColorNormal,pColorHover,pColorPressed):
        self.colorNormal=pColorNormal
        self.colorHover=pColorHover
        self.colorPressed=pColorPressed


    def setText(self,pFont,pColor,pText):
        self.text=Text(self.x,self.y,pColor,pFont,pText)



    def draw(self,pScreen):

        #normal
        if not self.bIsPressed and not self.bIsHover:

            if self.imgNormal!=None:
                pScreen.blit(self.imgNormal,(self.x,self.y))
            else:
                pygame.draw.rect(pScreen,self.colorNormal,(self.x,self.y,self.width,self.height))

        #hover
        elif self.bIsHover and not self.bIsPressed:

            if self.imgHover != None:
                pScreen.blit(self.imgHover, (self.x, self.y))
            else:
                pygame.draw.rect(pScreen, self.colorHover, (self.x, self.y, self.width, self.height))

        #pressed
        elif not self.bIsHover and self.bIsPressed:

            if self.imgPressed != None:
                pScreen.blit(self.imgPressed, (self.x, self.y))
            else:
                pygame.draw.rect(pScreen, self.colorPressed, (self.x, self.y, self.width, self.height))


    def mousepressed(self,pBtn,pPos):

        if pBtn[0]:
            if pPos[0]>=self.x and pPos[0]<=self.x+self.width and pPos[1]>=self.y and pPos[1]<=self.y+self.height:

                    if not self.bIsPressed:
                        self.bIsPressed=True
                        self.bIsHover=False



    def mousemove(self,pPos):

        if not self.bIsPressed:
            if pPos[0] >= self.x and pPos[0] <= self.x + self.width and pPos[1] >= self.y and pPos[1] <= self.y + self.height:

                if not self.bIsHover:
                    self.bIsHover = True

            else:
                self.bIsHover = False




##############################################CLASS CHECKBOX####################################
class CheckBox:
    def __init__(self,pX,pY):
        self.x=pX
        self.y=pY

        self.width=0
        self.height=0

        self.type="checkbox"

        self.colorNormal=[255,255,255]
        self.colorSelect = [255, 255, 255]

        self.bIsSelect=False

        self.imgNormal=None
        self.imgSelect=None


    def addImages(self,pImgNormal,pImgSelect):
        self.imgNormal=pImgNormal
        self.imgSelect=pImgSelect

        self.width=self.imgNormal.get_width()
        self.height=self.imgNormal.get_height()


    def draw(self,pScreen):

        #deselect
        if not self.bIsSelect:

            if self.imgNormal!=None:
                pScreen.blit(self.imgNormal,(self.x,self.y))
            else:
                pygame.draw.rect(pScreen,self.colorNormal,(self.x,self.y,self.width,self.height))

        #select
        else:
            if self.imgSelect != None:
                pScreen.blit(self.imgSelect, (self.x, self.y))
            else:
                pygame.draw.rect(pScreen, self.colorSelect, (self.x, self.y, self.width, self.height))


    def mousepressed(self,pBtn,pPos):

        if pBtn[0]:
            if pPos[0]>=self.x and pPos[0]<=self.x+self.width and pPos[1]<=self.y and pPos[1]>=self.y+self.heigth:

                if not self.bIsSelect:
                    self.bIsSelect=True
                else:
                    self.bIsSelect=False




###########################################CLASS PROGRESS BAR#########################
class ProgressBar:
    def __init__(self,pX,pY,pMaxValue,pValue):
        self.x=pX
        self.y=pY

        self.type="progressBar"

        self.width=0
        self.height=0

        self.colorBar=[255,255,255]
        self.colorProgress=[255,255,255]

        self.imgBar=None
        self.imgProgress=None

        self.coef=0
        self.maxValue=pMaxValue
        self.value=pValue


    def update(self,dt):
        self.coef=self.value/self.maxValue



    def addImages(self,pImgProgress,pImgBar):
        self.imgProgress=pImgProgress
        self.imgBar=pImgBar

        self.width=self.imgBar.get_width()
        self.height=self.imgBar.get_height()


    def draw(self,pScreen):
        pScreen.blit(self.imgBar,(self.x,self.y))
        pScreen.blit(self.imgProgress,(self.x,self.y))
        pygame.transform.scale(self.imgProgress,(self.imgProgress.get_width()*self.coef,self.imgProgress.get_height()))




#######################################CLASS TEXT######################################
class Text:
    def __init__(self,pX,pY,pColor,pFont,pText):
        self.x=pX
        self.y=pY

        self.font=pFont
        self.color=pColor

        self.type="text"

        self.text=pText


    def draw(self,pScreen):
        text=self.font.render(self.text,1,self.color)
        pScreen.blit(text,(self.x,self.y))



###############################################CLASS GUI######################
class GUI:

    def __init__(self):
        self.lstGUI=[]


    def totalDelete(self):
        self.lstGUI=[]


    def createButton(self,pX,pY):
        myButton=Button(pX,pY)

        self.lstGUI.append(myButton)
        return myButton


    def createCheckBox(self,pX,pY):
        myCheckBox=CheckBox(pX,pY)

        self.lstGUI.append(myCheckBox)
        return myCheckBox


    def createProgressBar(self,pX,pY,pMaxValue,pValue):
        myProgressBar=ProgressBar(pX,pY,pMaxValue,pValue)

        self.lstGUI.append(myProgressBar)
        return myProgressBar


    def createText(self,pX,pY,pFont,pColor,pText):
        myText=Text(pX,pY,pColor,pFont,pText)

        self.lstGUI.append(myText)
        return myText


    def update(self,dt):
        for gui in self.lstGUI:
            if gui.type=="progressBar":
                gui.update(dt)


    def draw(self,pScreen):

        for gui in self.lstGUI:
            gui.draw(pScreen)


    def mousepressed(self,pBtn,pPos):

        for gui in self.lstGUI:

            if gui.type=="button" or gui.type=="checkbox":
                gui.mousepressed(pBtn,pPos)


    def mousemove(self,pPos):

        for gui in self.lstGUI:

            if gui.type == "button":
                gui.mousemove(pPos)