import pygame

class AssetManager:

    def __init__(self):
        self.lstImages={}
        self.lstSounds=[]


    def addImage(self,pPath):
        img=pygame.image.load(pPath)
        self.lstImages[pPath]=img


    def addSound(self,pPath):
        self.lstSounds.append(pPath)


    def getImage(self,pPath):
        return self.lstImages[pPath]


    def getSound(self,pPath):

        for snd in self.lstSounds:
            if pPath==snd:
                return pygame.mixer.music.load(snd)