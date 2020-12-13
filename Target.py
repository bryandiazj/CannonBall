from Ball import *
from Vector3d import *

import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Target:
    def __init__(self):
        self.__center = Vector3d(0,10,-80);
        self.__color = Vector3d(0.8,0.7,0.8);
        self.__innerRadius = 0.5;
        self.__outerRadius = 4;
        self.__isMoving = False;
        self.__deltaX = 0.02;
        self.__bbx = None
        
    def Update(self,ballList):
        if self.__isMoving is True:
            self.__center.SetX( self.__center.GetX() + self.__deltaX );
        if( self.__center.GetX() < self.__bbx[0] ):
            self.__center.SetX( self.__bbx[0] )
            self.__deltaX *=-1
    
        if( self.__center.GetX() > self.__bbx[1] ):
            self.__center.SetX( self.__bbx[1] )
            self.__deltaX *=-1
            
        hit=False
        isLast = False
        for i in ballList:
            ballCenter=i.GetCenter()
            total1 = ballCenter.GetX() - self.__center.GetX()
            total2 =  ballCenter.GetY() - self.__center.GetY()
            total3 = ballCenter.GetZ() - self.__center.GetZ()
            v = Vector3d(0,0,0)
            v.SetAll(total1,total2,total3)
            k = v.norm()
            if (k < self.__outerRadius): 
                 if( math.fabs(ballCenter.GetZ()-self.__center.GetZ()) < 1.0 ):
                    hit = True
                    break


        if hit is True:
            self.__isMoving = True
            self.__color.SetX( random.random() )
            self.__color.SetY( random.random() )
            self.__color.SetZ( random.random() )
            self.__deltaX *=1.05          
            
  
    def Draw(self):
        glColor3f(self.__color.GetX(),self.__color.GetY(),self.__color.GetZ())
        glPushMatrix();
        glTranslated(self.__center.GetX(),self.__center.GetY(),self.__center.GetZ())
        glutSolidTorus(self.__innerRadius,self.__outerRadius,20,20);
        glPopMatrix()
    def SetBBX(self,_bbx):
        self.__bbx = _bbx
    def GetCenter(self):
        return self.__center
    
    


