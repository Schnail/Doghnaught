# Doghnaught – ASCII 3D Renderer in Python

**Doghnaught** (originally intended to be "Donut", but the typo stuck) is a personal project built to deepen my understanding of 3D operations and rendering.  
It renders simple 3D shapes made of point data to a 2D canvas using ASCII characters, with transformations and basic lighting.  
The project is written entirely in Python, runs on CPU only, and is not meant to be high-performance.

---

## 🔍 Overview

The goal of this project is to render basic 3D objects in a purely text-based way, and allow transformations like translation, rotation, and scaling.  
No external graphics libraries are used – everything is custom-built to learn the fundamentals behind rendering logic.

---

## 📦 Project Structure

```text
Vector.py       - Custom 2D and 3D vector classes, math utilities, rotation
Objects3D.py    - GridObject and GridVertex structures with local-to-world transforms
Viewer3D.py     - GridCanvas for projecting 3D points into 2D ASCII output
Sequence.py     - Example run file: generates and rotates a cube across 100 frames
README.md       - This file
Frames/         - Output directory for ASCII frame files (created at runtime)
```
---

## 💡 How It Works

```text
GridObjects

These represent 3D objects, made up of GridVertex points with:

-Local position
-Normal (used for shading)
-Optional color (currently not visualized)

Each object can be moved, rotated, and scaled.
```
```text
GridCanvas

This is a virtual 2D screen that simulates a camera.
It takes 3D vertices, applies projection, depth-sorting, and lighting, and prints them as ASCII characters.
The camera is fixed – it doesn't move, but the objects do.

Lighting is directional and based on dot product between vertex normals and a light angle.
```

---

## ▶️ How to Run

**Requirements:**

```text
-Python 3.10+
-NumPy
-Make sure you have a folder named 'Frames' in the project's directory
```

**Run the sample animation:**

```text
-run Sequence.py
```

This will generate 100 Frames of a rotating cube one at a time in your console and save them as .txt in Frames/ and afterwards play them back as an animation

**Output Example:**
```text
                                
            &&&&//              
          OO&&&&//////          
          &&&&&&//////////--    
        &&&&&&&&////////////    
      &&&&&&00@@////////////    
      &&&&&&00..////////////    
      &&&&00........////////    
      &&0000............////    
      &&00................OO    
      00..................      
      --................        
            --........OO        
                --..OO
```
You can play with Sequence.py to generate different results.




