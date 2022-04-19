import math
import pygame.transform

class Utils:

    def angle(self,pX1,pY1,pX2,pY2):
        return math.atan2(pY2-pY1,pX2-pX1)


    def dist(self,pX1,pY1,pX2,pY2):
        return ((pX2-pX1)**2+(pY2-pY1)**2)**0.5


    def checkCollision(self,pX1,pY1,pW1,pH1,pX2,pY2,pW2,pH2):

        if pX1+pW1>=pX2 and pX1<=pX2+pW2:
            if pY1+pH1>=pY2 and pY1<=pY2+pH2:
                return True

        return False


    def easeInOutSine(self,t,b,c,d):
        return -c/2*(math.cos(math.pi*t/d)-1)+b


    def easeOutSine(self,t,b,c,d):
        return c*math.sin(t/d*(math.pi/2))+b


    def changeColorImg(self,pImg,pNewColor,pbIsCopy):
        img = None

        if pbIsCopy:
            img=pImg.copy()
        else:
            img=pImg

        img_width=pImg.get_width()
        img_height=pImg.get_height()

        for l in range(0,img_height):
            for c in range(0,img_width):
                x=c*1
                y=l*1

                p_color=img.get_at((x,y))

                if p_color[3]==255 and p_color!=(0,0,0,255):
                    img.set_at((x,y),pNewColor)


        return img