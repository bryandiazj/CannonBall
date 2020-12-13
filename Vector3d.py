import math
import sys

global PI 
PI = 3.1415926535897
global TWOPI
TWOPI = 6.2831853071794

def myRand():
	return math.rand() / sys.maxsize.__rand__()
def sqr(a):
    return a ** 2
def sign(x):
    if (x >= 0):
        return 1
    else:
        return -1
    
def degToRad(x):
    return (x*PI)/180
def radToDeg(x):
    return (x*180)/PI

def sind(x):
    return math.sin(degToRad(x))

def cosd(x):
    return math.cos(degToRad(x))

def tand(x):
    return math.tan(degToRad(x))

def asind(x):
    return radToDeg(math.asin(x))

def acosd(x):
    return radToDeg(math.acos(x))

def atand(x):
    return radToDeg(math.atan(x))

def atan2d(x,y):
    return radToDeg(math.atan2(x,y))
    

class Vector3d():
    def __init__(self,_x, _y, _z):
        self.__x = _x
        self.__y = _y
        self.__z = _z
        
    def operator(self, _x, _y, _z):
        self.__x = _x
        self.__y = _y
        self.__z = _z
        return self
        
    def operator_d(self, _d):
        self.__x = _d.GetX()
        self.__y = _d.GetY()
        self.__z = _d.GetZ()
        return self
        
    def GetX(self):
        return self.__x
    
    def GetY(self): 
        return self.__y
    
    def GetZ(self): 
        return self.__z
    
    def SetX(self, d): 
        self.__x = d    
        
    def SetY(self, d):
         self.__y = d
         
    def SetZ(self, d):
        self.__z = d
        
    def SetAll(self, d1, d2, d3):
        self.__x = d1
        self.__y = d2 
        self.__z = d3
        
    def print_vector(self):
        print(self.__x, self.__y, self.__z)
        
    def reset(self):
        self.__x = 0
        self.__y = 0
        self.__z = 0
        
    def op(self, **kwargs): #experiment
        self.__x = kwargs.get('a')
        self.__y = kwargs.get('b')
        self.__z = kwargs.get('c')
    
        
    def bol(self, a):
        if (self.__x == a.GetX() and self.__y == a.GetY() and self.__z == a.GetZ()):
            return True
        else:
            return False
        
    #add another vector    
    def sadd(self,a):      
        self.__x += a.GetX()
        self.__y += a.GetY()
        self.__z += a.GetZ()
        return self
        
    #substract another vector from this vector
    def ssub(self, a):       
         self.__x -= a.GetX()
         self.__y -= a.GetY()
         self.__z -= a.GetZ()
         return self
         
    #scalar multiplication
    def smul(self, _d):
        self.__x *= _d
        self.__y *= _d
        self.__z *= _d
        return self
        
    #scalar division    
    def sdiv(self, _d):
        self.__x /= _d
        self.__y /= _d
        self.__z /= _d
        return self

     #component multiplication
    def scom(self, a):
        self.__x *= a.GetX()
        self.__y *= a.GetY()
        self.__z *= a.GetZ()
        return self
        
        
    def scp(self, a):
        v0 = self.__x
        v1 = self.__y
        v2 = self.__z
        self.__x = v1 * a.GetZ() - v2 * a.GetY()
        self.__y = v2 * a.GetX() - v0 * a.GetZ()
        self.__z = v0 * a.GetY() - v1 * a.GetX()
        return self
     
    def neg(self):
        return Vector3d(-self.__x, -self.__y, -self.__z)
     
        
    def add(self, a):
        return Vector3d(self.__x + a.GetX(), self.__y + a.GetY(), self.__z + a.GetZ())
    def sub(self,a):
        return Vector3d(self.__x - a.GetX(), self.__y - a.GetY(), self.__z - a.GetZ())
    def mul(self,_d):
        return Vector3d(self.__x * _d, self.__y * _d, self.__z * _d)
    def div(self,_d):
        return Vector3d(self.__x / _d, self.__y / _d, self.__z / _d)
    def com(self, a):
        return Vector3d(self.__x * a.GetX(), self.__y * a.GetY(), self.__z * a.GetZ())
    
    
    def cp(self, _v):
        a = Vector3d(self.__x,self.__y,self.__z)
        return a.scp(_v)
    
    def dot(self,a):
        return self.__x*a.GetX() + self.__y*a.GetY() + self.__z*a.GetZ()
    
    def normsqr(self):
        return self.__x ** 2 + self.__y ** 2 + self.__z ** 2

    
    
    def norm(self):
        return math.sqrt(self.normsqr())

    
    def normalize(self):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return Vector3d(0,0,0)
        self.__x = self.__x/n
        self.__y = self.__y/n 
        self.__z = self.__z/n
        return self
        
        
    def snormalize(self):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return self.reset()
        self.__x = self.__x/n
        self.__y = self.__y/n 
        self.__z = self.__z/n
        return self        
        
        
    def comp(self,a):
        a.normalize()
        self.__x *= a.GetX() 
        self.__y *= a.GetY()
        self.__z *= a.GetZ()
        return self
    def scale(self,_1):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return Vector3d(0,0,0)
        self.__x *= (_1/n)
        self.__y *= (_1/n) 
        self.__z *= (_1/n)
        return self
        
    def sscale(self,_1):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return self.reset()
        self.__x *= (_1/n)
        self.__y *= (_1/n) 
        self.__z *= (_1/n)
        return self
    
    
    def rotateX(self,_rad):
        c = math.cos(_rad)
        s = math.sin(_rad)
        return self.operator(self.__x, self.__y*c - self.__z*s, self.__y*s + self.__z*c)
    
    def rotateXd(self, _deg):
        return self.rotateX(degToRad(_deg))
    
    def rotateY(self, _rad):
        c = math.cos(_rad)
        s = math.sin(_rad)
        return self.operator(self.__x*c + self.__z*s, self.__y, -self.__x*s + self.__z*c)
    
    def rotateYd(self, _deg):
        return self.rotateY(degToRad(_deg))
    
    def rotateZ(self, _rad):
        c = math.cos(_rad)
        s = math.sin(_rad)
        return self.operator(self.__x*c - self.__y*s, self.__x*s + self.__y*c, self.__z)
    
    def rotateZd(self, _deg):
        return self.rotateZ(degToRad(_deg))

