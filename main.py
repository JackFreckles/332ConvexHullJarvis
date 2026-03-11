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

def orientation(p, q, r):
    return (q[0] - p[0])*(r[1] - p[1]) - (q[1] - p[1])*(r[0] - p[0])

def convex_hull_jarvis(points: List[Point]) -> List[Point]:
    if (len(points) <= 3):
        return points
    
    hull = []

    start = min(points)
    current = start

    while True:
        hull.append(current)
        candidate = points[0]

        for p in points:
            if candidate == current or orientation(current, candidate, p) > 0:
                candidate = p

        current = candidate

        if current == start:
            break

    return hull


if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull) #Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]