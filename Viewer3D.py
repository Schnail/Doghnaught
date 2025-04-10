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
    9 : ".",
    10 : " "
}

class GridCanvas:
    def __init__(self, size : Vector2d, maxdepth : float = 64, lightangle : Vector3d = Vector3d(1,-1,1), perspectivefac : float = 1):
        self.size = size
        self.maxdepth = maxdepth
        self.light = lightangle.normalize()
        self.perspective = perspectivefac
        self.cells : list[GridCell] = []
        self.makeCells()
    
    #this is way too slow. better save every cell in 2d array.   
    def cellAtPosition(self, position : Vector2d) -> GridCell | None:
        for cell in self.cells:
            if cell.pos.xy == position.xy:
                return cell
        return None
    
    def makeCells(self) -> None:
        for x in range(0, self.size.x):
            for y in range(0, self.size.y):
                cell = GridCell(Vector2d(x,y), self.maxdepth)
                self.cells.append(cell)
    
    def clearCanvas(self) -> GridCanvas:
        for x in range(0, self.size.x):
            for y in range(0, self.size.y):
                cell = self.cellAtPosition(Vector2d(x,y))
                cell.depth = self.maxdepth
                cell.color = Vector3d(255,255,255)
                    
        return self
    
    def drawObject(self, object : GridObject) -> GridCanvas:
        droped = 0
        drawn = 0
        
        for vertex in object.verts:
            pos = Vector2d(vertex.worldPosition().pos.x, vertex.worldPosition().pos.y)
            centervec = (self.size / 2) - pos
            pos = (pos + (centervec * self.perspective * 0.2)).round()
            
            cell = self.cellAtPosition(pos)
            if isinstance(cell, GridCell):
                if cell.depth > vertex.worldPosition().pos.z:
                    cell.depth = vertex.worldPosition().pos.z
                    cell.normal = vertex.worldPosition().normal
                    cell.color = (vertex.color * (1 - abs(dot(cell.normal, self.light)))).round()
                    drawn += 1
                else:
                    droped += 1
            else:
                droped += 1
        
        #print("total Verts:", len(object.verts))
        #print("drawn Verts:", drawn)          
        #print("droped Verts:", droped)    
        return self
    
    def outputImage(self) -> str:
        lines = []
        for sizey in range(0, self.size.y):
            line = ""    
            for sizex in range(0, self.size.x):
                invY = self.size.y - 1 - sizey
                cell = self.cellAtPosition(Vector2d(sizex,invY))
                hex = f"{cell.color.x:x}{cell.color.y:x}{cell.color.z:x}"
                #char = DepthConvert[min(round(cell.depth / (self.maxdepth / 11)), 10)]
                char = DepthConvert[round(cell.color.x / 255 * 10)]
                line = line + char + char
            lines.append(line)
        outstr = ""
        for line in lines:
            outstr = outstr + line + "\n"    
        return outstr 

#-------------------------------------------------------------------        
        
class GridCell:
    def __init__(self, position : Vector2d, depth : float, normal : Vector3d = Vector3d(0,0,-1), color : Vector3d = Vector3d(255,255,255)):
        self.pos = position
        self.depth = depth
        self.normal = normal
        self.color = color
    
    def __str__(self):
        return f"GridCell at {self.pos} with depth {self.depth} normal {self.normal} and color {self.color}"



