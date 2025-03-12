from __future__ import annotations
from Vector import *
import json

class GridObject:
    def __init__(self, name : str, position : Vector3d , rotation : Vector3d, scale : Vector3d, vertecies : list[GridVertex], parent : GridObject = None):
        self.name = name
        self.pos = position
        self.bpos = position
        self.rot = rotation
        self.scale = scale
        self.verts = vertecies
        self.parent = parent
        
    def __str__(self):
        return f"GridObject '{self.name}' at position {self.pos} with rotation {self.rot} containing {len(self.verts)} vertecies"
        
    def makeVert(self, position : Vector3d, normal : Vector3d, color : Vector3d) -> GridVertex:
        newVert = GridVertex(len(self.verts), position, normal, color, self)
        self.verts.append(newVert)
        return newVert
    
    def deleteVert(self, index) -> None:
        oldVert = self.verts[index]
        self.verts.pop(index)
        for vert in self.verts[index:]:
            vert.id += -1
        return oldVert
    
    def move(self, vector : Vector3d) -> GridObject:
        self.pos += vector
        return self
    
    def addrotation(self, rotation : Vector3d) -> GridObject:
        self.rot += rotation
        return self
    
    def scaleXYZ(self, factor : Vector3d) -> GridObject:
        self.scale = self.scale * factor
        return self.copy()
    
    """def transforms(self) -> GridObject:
        if self.parent == None:
            return self
        else:
            Parent = self.parent.transforms()"""
    
    def makeFile(self):
        verts = []
        for vert in self.verts:
            verts.append([vert.id, vert.pos.xyz, vert.normal.xyz, vert.color.xyz])
        content = [self.name, self.pos.xyz, self.rot.xyz, self.scale.xyz, verts]
        
        return json.dumps(content)

#-------------------------------------------------------------------

class GridVertex:
    def __init__(self, index : int, position : Vector3d, normal : Vector3d = Vector3d(1,1,1), color : Vector3d = Vector3d(255,255,255), parent : GridObject = None):
        self.id = index
        self.pos = position
        self.normal = normal.normalize()
        self.color = color
        self.parent = parent
        
    def __str__(self):
        return f"GridVertex with id {self.id} at local position {self.pos} with color {self.color}"
        
    def move(self, vector : Vector3d) -> GridVertex:
        self.pos += vector
        return self
    
    def paint(self, color : Vector3d) -> GridVertex:
        self.color = color
        return self
    
    def world(self) -> GridVertex:
        wpos = self.pos * self.parent.scale
        wpos = rotatevector(wpos, self.parent.rot)
        wpos += self.parent.pos 
        wnormal = rotatevector(self.normal, self.parent.rot)
        
        return GridVertex(self.id, wpos, wnormal, self.color, self.parent)
        
#-------------------------------------------------------------------

#ugly as f-. might change later but need for testing
def loadGridObject(jsonobject) -> GridObject:
    name = jsonobject[0] 
    pos = Vector3d(jsonobject[1][0],jsonobject[1][1],jsonobject[1][2])
    rot = Vector3d(jsonobject[2][0],jsonobject[2][1],jsonobject[2][2])
    scale = Vector3d(jsonobject[3][0],jsonobject[3][1],jsonobject[3][2])
    object = GridObject(name,pos,rot,scale,[])
    for x in jsonobject[4]:
        object.makeVert(Vector3d(x[1][0],x[1][1],x[1][2]),Vector3d(x[2][0],x[2][1],x[2][2]),Vector3d(x[3][0],x[3][1],x[3][2]))
    
    return object
