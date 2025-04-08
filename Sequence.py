from Viewer3D import *


canvasSize : Vector2d = Vector2d(16,16)
canvasDepth : int = 16
frames : int = 100

#-------------------------------------------------------------------
#procedualy creating example Cube Gridobject

testCube = GridObject("TestCube", Vector3d(8,8,8), Vector3d(0,0,0), Vector3d(0.8,0.8,0.8), [])
bounds = range(-6,7)
for x in bounds:
    for y in bounds:
        for z in bounds:
            pos = Vector3d(x,y,z)  
            shortest = 1000000000
            likelynormal = Vector3d(1,1,1)
            for normals in [Vector3d(1,0,0), Vector3d(0,1,0), Vector3d(0,0,1), Vector3d(-1,0,0), Vector3d(0,-1,0), Vector3d(0,0,-1)]:
                length = (pos - normals).len()
                if length < shortest:
                    shortest = length
                    likelynormal = normals
                elif length == shortest:
                    likelynormal = (likelynormal + normals)/2
             
            normal = likelynormal
            color = Vector3d(255,255,255)
            testCube.makeVert(pos, normal, color)

testCube.rot = Vector3d(30,45,45)

testDonut = GridObject("TestDonut", Vector3d(8,8,8), Vector3d(0,0,0), Vector3d(0.8,0.8,0.8), [])


#-------------------------------------------------------------------
#Canvas and animation loop

objectToDraw = testCube

testCanvas = GridCanvas(canvasSize, canvasDepth)
testCanvas.draw(objectToDraw)
print(testCanvas.out())

for x in range(0,frames-1):
    testCanvas.clear()
    objectToDraw.rot += Vector3d(7,5,3)
    testCanvas.draw(objectToDraw)
    print(testCanvas.out())