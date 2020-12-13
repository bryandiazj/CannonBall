from Vector3d import *

import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLE import *

from OpenGL.GL.ARB.framebuffer_object import *
from OpenGL.GL.EXT.framebuffer_object import *

from ctypes import *

global damping
damping = 0.95
global collisionDamping 
collisionDamping = 0.3

class Ball:
    def __init__(self):
        self.__center = Vector3d(0,0,0)
        self.__velocity = Vector3d(0,0,0)
        self.__accel = Vector3d(0,0,0)
        self.__color = Vector3d(0.3,0.2,0.8)
    
    def SetValues(self, _radius, _center, _vel, _accel,  _bbx):
        self.__radius = _radius
        self.__center = _center
        self.__velocity = _vel
        self.__accel = _accel
        self.__bbx = _bbx
    def SetRandomColor(self):
        self.__color.SetX(random.random())
        self.__color.SetY(random.random())
        self.__color.SetZ(random.random())
    def IsMoving(self):
        vel = self.__velocity.norm()
        if( vel < 0.2 ):
            return True
        else:
            return False
        
        
    def Update(self, dt):
        self.__center.operator_d(self.__center.sadd(self.__velocity.smul(dt)))
        oldVelocity = self.__velocity
        self.__velocity.operator_d(self.__center.sadd(self.__accel.smul(dt)))
        oldAccelY = self.__accel.GetY()
        oldAccelY -= 9.8
        self.__accel.SetY(oldAccelY)
#        self.__accel *= damping
        self.__accel.smul(damping)

        self.ResolveCollision()
        if(self.__accel.norm() < 0.5 ):
            self.__accel.SetAll(0,0,0)
        if(self.__velocity.norm() < 0.5):
            self.__velocity.SetAll(0,0,0)
            
            
    def ResolveCollision(self):
        if(self.__center.GetX()-self.__radius < self.__bbx[0]): 
            oldCenterX = self.__center.GetX()
            self.__center.SetX(self.__bbx[0]+self.__radius)
            self.__velocity.SetX( -1*self.__velocity.GetX() )
            self.__velocity.smul(collisionDamping)
            self.__accel.smul(collisionDamping)
  
        if( self.__center.GetX()+self.__radius > self.__bbx[1] ):
            oldCenterX = self.__center.GetX()
            self.__center.SetX(self.__bbx[1]-self.__radius)
            self.__velocity.SetX( -1*self.__velocity.GetX() )
            self.__velocity.smul(collisionDamping)
            self.__accel.smul(collisionDamping)
  
        if( self.__center.GetY()-self.__radius < self.__bbx[2] ):
            oldCenterY = self.__center.GetY()
            self.__center.SetY(self.__bbx[2]+self.__radius)
            self.__velocity.SetY( -1*self.__velocity.GetY() )
            self.__velocity.smul(collisionDamping)
            self.__accel.smul(collisionDamping)
  
        if( self.__center.GetY()+self.__radius > self.__bbx[3] ):
            oldCenterY = self.__center.GetY()
            self.__center.SetY(self.__bbx[3]-self.__radius)
            self.__velocity.SetY( -1*self.__velocity.GetY() )
            self.__velocity.smul(collisionDamping)
            self.__accel.smul(collisionDamping)
            
        if( self.__center.GetZ()-self.__radius < self.__bbx[4] ):
            oldCenterZ = self.__center.GetZ()
            self.__center.SetZ(self.__bbx[4]+self.__radius)
            self.__velocity.SetZ( -1*self.__velocity.GetZ() )
            self.__velocity.smul(collisionDamping)
            self.__accel.smul(collisionDamping)
            
        if( self.__center.GetZ()+self.__radius > self.__bbx[5] ):
            oldCenterZ = self.__center.GetZ()
            self.__center.SetZ(self.__bbx[5]-self.__radius)
            self.__velocity.SetZ( -1*self.__velocity.GetZ() )
            self.__velocity.smul(collisionDamping)
            self.__accel.smul(collisionDamping)
            
    def GetCenter(self):
        return self.__center 
    
    def Draw(self):
        glColor3f(self.__color.GetX(),self.__color.GetY(),self.__color.GetZ())
        glPushMatrix();
        glTranslated(self.__center.GetX(),self.__center.GetY(),self.__center.GetZ())
        glutSolidSphere(self.__radius,10,10);
        glPopMatrix();

        

