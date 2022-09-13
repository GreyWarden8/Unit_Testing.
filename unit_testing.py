from math import pi
#Pi method is required to get the area result.
import unittest
#from areacircle import area_of_circle

#There was no module named areacirlce so I turned it into a comment.

def area_of_circle(r):
    if r < 0:
        raise ValueError('Negative radius value error.')
    return pi*(r**2)

def test_values(self):
    #Test that bad values are caught
    self.assertRaises(ValueError, area_of_circle, -1)


class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):
        #Test radius >= 0

        self.assertAlmostEqual(area_of_circle(1), pi)   

        self.assertAlmostEqual(area_of_circle(0), 0)

        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5**2)


        

if __name__ == '__main__':
    unittest.main()


#Even though there are 2 tests, script passes the second one for some reason.
