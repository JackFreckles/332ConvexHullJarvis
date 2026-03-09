'''
Clinton Reimann
CSCI 332 Spring 2025
Programming Assignment #class18 (main)

I acknowledge that I have worked on this assignment independently, except
where explicitly noted and referenced. Any collaboration or use of external
resources has been properly cited. I am fully aware of the consequences of
academic dishonesty and agree to abide by the university's academic integrity
policy. I understand the importance the consequences of plagiarism.
'''

from typing import List, Tuple

Point = Tuple[float, float]

def convex_hull_jarvis(points: List[Point]) -> List[Point]:
    #angle = (p2[0] - p1[0])*(p3[1] - p2[1]) - (p2[1] - p1[1])*(p3[0] - p2[0])
    encapsulatingPoints = []
    for i in range(len(points)):
        for j in range(len(points)):
            orientation = None

if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]