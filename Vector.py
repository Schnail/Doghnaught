from __future__ import annotations
import math

class Vector2d:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
        self.xy = [self.x, self.y]
        
    def __str__(self):
        return f"{self.x, self.y}"
    
    def __iter__(self):
        self.i = 0
        return self.xy[self.i]
    
    def __next__(self):
        if self.i <= 1:
            i = self.i
            self.i += 1
            return self.xy[i]
        else:
            raise StopIteration
    
    def __invert__(self):
        x = ~self.x
        y = ~self.y
        return Vector2d(x,y)
    
    def __add__(self, other : Vector2d) -> Vector2d:
        x = self.x + other.x
        y = self.y + other.y
        return Vector2d(x,y)
    
    def __sub__(self, other : Vector2d) -> Vector2d:
        x = self.x - other.x
        y = self.y - other.y
        return Vector2d(x,y)
    
    def __mul__(self, other : float | int | Vector2d) -> Vector2d:
        if isinstance(other, (float, int)):    
            x = self.x * other
            y = self.y * other
            return Vector2d(x,y)
        elif isinstance(other, Vector2d):
            x = self.x * other.x
            y = self.y * other.y
            return Vector2d(x,y)
    
    def __truediv__(self, other : float | int | Vector2d) -> Vector2d:
        if isinstance(other, (float, int)):   
            x = self.x / other
            y = self.y / other
            return Vector2d(x,y)
        elif isinstance(other, Vector2d):
            x = self.x / other.x
            y = self.y / other.y
            return Vector2d(x,y)
             
        
    def len(self) -> float:
        return math.sqrt(pow(self.x,2)+pow(self.y,2))
    
    def normalize(self) -> Vector2d:
        return self / self.len()

#-------------------------------------------------------------------

class Vector3d:
    def __init__(self, x : float, y : float, z : float):
        self.x = x
        self.y = y
        self.z = z
        self.xy = Vector2d(self.x, self.y)
        self.xz = Vector2d(self.x, self.z)
        self.yz = Vector2d(self.y, self.z)
        self.xyz = [self.x, self.y, self.z]
        
    def __str__(self):
        return f"{self.x, self.y, self.z}"
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i <= 2:
            i = self.i
            self.i += 1
            return self.xyz[i]
        else:
            raise StopIteration
    
    def __invert__(self):
        x = ~self.x
        y = ~self.y
        z = ~self.z
        return Vector3d(x,y,z)
    
    def __add__(self, other : Vector3d) -> Vector3d:
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3d(x,y,z)
    
    def __sub__(self, other : Vector3d) -> Vector3d:
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3d(x,y,z)
    
    def __mul__(self, other : float | int | Vector3d) -> Vector3d:
        if isinstance(other, (float, int)):    
            x = self.x * other
            y = self.y * other
            z = self.z * other
            return Vector3d(x,y,z)
        elif isinstance(other, Vector3d):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            return Vector3d(x,y,z)
    
    def __truediv__(self, other : float | int | Vector3d) -> Vector3d:
        if isinstance(other, (float, int)):   
            x = self.x / other
            y = self.y / other
            z = self.z / other
            return Vector3d(x,y,z)
        elif isinstance(other, Vector3d):
            x = self.x / other.x
            y = self.y / other.y
            z = self.z / other.z
            return Vector3d(x,y,z)
        
        
    def len(self) -> float:
        return math.sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    
    def normalize(self) -> Vector3d:
        return self / self.len()
    
#-------------------------------------------------------------------   
       
def dot(vec1 : Vector2d | Vector3d, vec2 : Vector2d | Vector3d) -> float:
    nvec1 = vec1.normalize()
    nvec2 = vec2.normalize()
    scalar = 0
    for dimension, value in enumerate(nvec1):
        scalar += value * nvec2.xyz[dimension]

    return scalar
            
        
def cross(vec1 : Vector3d, vec2 : Vector3d) -> Vector3d:
    nvec1 = vec1.normalize()
    nvec2 = vec2.normalize()
    
    return Vector3d((nvec1.y * nvec2.z) - (nvec1.z * nvec2.y), (nvec1.z * nvec2.x) - (nvec1.x * nvec2.z), (nvec1.x * nvec2.y) - (nvec1.y * nvec2.x))        

#------------------------------------------------------------------- 

test1 = Vector3d(0,4,5)     
test2 = Vector3d(5,7,-3)

print(dot(test1, test2))

print(cross(test1, test2))