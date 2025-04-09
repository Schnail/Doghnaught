#Execute this file with the right settings to view the previously rendered animation
from time import sleep

frames : int = 100
repeat : int = 3
timeBetweenFrames : float = 0.05

for i in range(0,repeat):
    for x in range(1,frames+1):
        f = open(f"Frames/Frame{x}.txt", "rt")
        print(f.read())
        f.close()
        sleep(timeBetweenFrames)
        
