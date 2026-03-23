'''
Clinton Reimann
CSCI 332 Spring 2025
Programming Assignment #class18 (tests)

I acknowledge that I have worked on this assignment independently, except
where explicitly noted and referenced. Any collaboration or use of external
resources has been properly cited. I am fully aware of the consequences of
academic dishonesty and agree to abide by the university's academic integrity
policy. I understand the importance the consequences of plagiarism.
'''

import unittest
from main import convex_hull_jarvis


class TestMathFunctions(unittest.TestCase):
    
    def test_example_from_prompt(self):
        points = [(0.0, 3.0), (2.0, 2.0), (1.0, 1.0), (2.0, 1.0), (3.0, 0.0), (0.0, 0.0), (3.0, 3.0)] 
        hull = convex_hull_jarvis(points) 
        self.assertEqual(hull, [(0.0, 0.0), (0.0, 3.0), (3.0, 3.0), (3.0, 0.0)])

    def test_square_with_inner_points(self):
        points = [(1.0,1.0), (4.0,1.0), (1.0,4.0), (4.0,4.0), (0.0,0.0), (5.0,0.0), (0.0,5.0), (5.0,5.0)]
        hull = convex_hull_jarvis(points) 
        self.assertEqual(hull, [(0.0,0.0), (0.0,5.0), (5.0,5.0), (5.0,0.0)])

    def test_duplicates(self):
        points = [(0.0,0.0), (1.0,1.0), (2.0,2.0), (0.0,0.0), (2.0,2.0), (3.0,0.0)]
        hull = convex_hull_jarvis(points)
        self.assertEqual(hull, [(0.0,0.0), (2.0,2.0), (3.0,0.0)])

    def test_all_collinear(self):
        points = [(0.0,0.0), (1.0,1.0), (2.0,2.0), (3.0,3.0), (4.0,4.0)]
        hull = convex_hull_jarvis(points)
        # Expect just endpoints for collinear case
        self.assertEqual(hull, [(0.0,0.0), (4.0,4.0)])

    def test_two_points(self):
        points = [(0.0,0.0), (1.0,1.0)]
        hull = convex_hull_jarvis(points)
        self.assertEqual(hull, [(0.0,0.0), (1.0,1.0)])

    def test_single_point(self):
        points = [(0.0,0.0)]
        hull = convex_hull_jarvis(points)
        self.assertEqual(hull, [(0.0,0.0)])

    def test_triangle(self):
        points = [(0.0,0.0), (2.0,0.0), (1.0,2.0)]
        hull = convex_hull_jarvis(points)
        self.assertEqual(hull, [(0.0,0.0), (1.0,2.0), (2.0,0.0)])

    def test_collinear_on_edges(self):
        points = [(0.0,0.0), (2.0,0.0), (4.0,0.0), (4.0,4.0), (2.0,4.0), (0.0,4.0)]
        hull = convex_hull_jarvis(points)
        self.assertEqual(hull, [(0.0,0.0), (0.0,4.0), (4.0,4.0), (4.0,0.0)])

if __name__ == "__main__":
    unittest.main()