from __future__ import annotations
import math

class Vector3d:
    def __init__(self, x : float, y : float, z : float):
        self.x = x
        self.y = y
        self.z = z
        self.xy = [x, y, z]
        
    def __str__(self):
        return f"{self.x, self.y}"
    
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
            return Vector3d(x,y)
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