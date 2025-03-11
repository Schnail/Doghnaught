from __future__ import annotations
from Objects3D import *
import json

DepthConvert = {
    0 : "@",
    1 : "&",
    2 : "#",
    3 : "0",
    4 : "O",
    5 : "o",
    6 : "/",
    7 : "+",
    8 : "-",
    9 : "_"
}

class GridCanvas:
    def __init__(self, size : Vector2d, maxdepth : float = 64, lightangle : Vector3d = Vector3d(1,-1,1)):
        self.size = size
        self.maxdepth = maxdepth
        self.light = lightangle.normalize()
        self.cells : list[GridCell] = []
        self.makecells()
    
    #this is way too slow. better save every cell in 2d array.   
    def cellAtPosition(self, position : Vector2d) -> GridCell | None:
        for cell in self.cells:
            print(cell.pos.xy, position.xy, cell.pos.xy == position.xy)
            if cell.pos.xy == position.xy:
                return cell
        return None
    
    def makecells(self) -> None:
        for x in range(0, self.size.x):
            for y in range(0, self.size.y):
                cell = GridCell(Vector2d(x,y), self.maxdepth)
                self.cells.append(cell)
                print("made Cell at", x, y, ":", GridCell(Vector2d(x,y), self.maxdepth))
    
    def clear(self) -> GridCanvas:
        for x in range(0, self.size.x):
            for y in range(0, self.size.y):
                cell = self.cellAtPosition(Vector2d(x,y))
                if isinstance(cell, None):
                    self.cells.append(GridCell(Vector2d(x,y), self.maxdepth))
                else:
                    cell.depth = self.maxdepth
                    cell.color = Vector3d(256,256,256)
                    
        return self
    
    def draw(self, object : GridObject) -> GridCanvas:
        droped = 0
        drawn = 0
        
        for vertex in object.verts:
            pos = Vector2d(round(vertex.world().pos.x), round(vertex.world().pos.y))
            cell = self.cellAtPosition(pos)
            if isinstance(cell, GridCell):
                if cell.depth > vertex.world().pos.z:
                    cell.depth = vertex.world().pos.z
                    cell.normal = vertex.world().normal
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
    
    def out(self) -> None:
        lines = []
        for y in range(0, self.size.y):
            line = ""    
            for x in range(0, self.size.x):
                invY = self.size.y - 1 - y
                print("testing cell:", x, invY)
                cell = self.cellAtPosition(Vector2d(x,invY))
                char = DepthConvert[round(cell.depth)]
                line = line + char + char
            lines.append(line)
        for line in lines:
            print(line)   
        
        
class GridCell:
    def __init__(self, position : Vector2d, depth : float, normal : Vector3d = Vector3d(0,0,-1), color : Vector3d = Vector3d(256,256,256)):
        self.pos = position
        self.depth = depth
        self.normal = normal
        self.color = color
    
    def __str__(self):
        return f"GridCell at {self.pos} with depth {self.depth} normal {self.normal} and color {self.color}"



print("@#%0Oo*°+=-_")
print("@@ && ## 00 OO oo // [] () __ ")



testObject = GridObject("TestCube", Vector3d(5,5,5), Vector3d(0,0,0), Vector3d(1,1,1), [])
for x in range(-2,3):
    for y in range(-2,3):
        for z in range(-2,3):
            testObject.makeVert(Vector3d(x,y,z), Vector3d(256,256,256))

testObject.rot = Vector3d(30,45,45)

testCanvas = GridCanvas(Vector2d(10,10), 9)
testCanvas.draw(testObject)
testCanvas.out()

