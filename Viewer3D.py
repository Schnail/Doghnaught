from __future__ import annotations
from Objects3D import *
import json

class GridCanvas:
    def __init__(self, size : Vector2d, cells : list[GridCell] = None):
        self.size = size
        self.cells = cells
        
    def cellAtPosition(self, position : Vector2d) -> GridCell | None:
        for cell in self.cells:
            if cell.pos == position:
                return cell
        return None
    
    def draw(self, object : GridObject) -> GridCanvas:
        droped = 0
        drawn = 0
        
        for vertex in object.verts:
            pos = Vector2d(round(vertex.pos.x), round(vertex.pos.y))
            cell = self.cellAtPosition(pos)
            if isinstance(cell, GridCell):
                if cell.depth > vertex.pos.z:
                    cell.depth = vertex.pos.z
                    cell.color = vertex.color
                    drawn += 1
                else:
                    droped += 1
            else:
                droped += 1
        
        print("total Verts:", len(object.verts))
        print("drawn Verts:", drawn)          
        print("droped Verts:", droped)    
        return self
        
class GridCell:
    def __init__(self, position : Vector2d, depth : float, color : Vector3d):
        self.pos = position
        self.depth = depth
        self.color = color









print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("______________________@@__@@____________________________________")
print("________________________________________________________________")
print("____________________@@______@@__________________________________")
print("______________________@@@@@@____________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")
print("________________________________________________________________")


print("@#%0Oo*°+=-_")
print("@@ && ## 00 OO oo // [] () __ ")