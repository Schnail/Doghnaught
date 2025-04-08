# Doghnaught
 3D Dnoghath

This is a personal project to sharpen my understanding for operations in rendering.
The goal was to create a short programm capable of editing and rendering primitive shapes on a 3D Canvas plus some additional features.
The titel of this project is supposed to read "Donut" but I had a typo.
This projekt is not meant to be overly performant as its completly written in python and therefore executed on the CPU only;
So not optimal for any vertex-transforming operations.

GridObjects
The rendered Objects are made up by Points in 3D space called vertecies.
Objects can be given a name and a transform made up by position rotation and scale.

GridVerts
These are not typical Vertecies but act more like a voxel. However they don't have any shape and are just given a normal for lighting purposes.
They also have a relative position to their parent Gridobject and a 3D vector that could theoretically be used to display color. Most Consoles don't support colored outputs so the vector gets ignored for now.

Canvas
This Object is basically a 2D plane that 3D Opjects can be projected on. the process is like Taking a photo of a 3D Object.
It defines the Bounds in which the objects can be rendered. Any vertecies outside these Bounds will be calculated but not visible in the render.
The Canvas unlike 3D Cameras in other engines is immovable.
The Canvas also dictates the light source angle used for shading the object and applies transforms to the object to mimic foreshortening.

Sequence.py
This is the file to run any operations in. It holds the instructions to generate a generic cube with normals and an animation loop that rotates the cube over 100 frames.
no other file inherits from this one so its safe to edit for testing.
