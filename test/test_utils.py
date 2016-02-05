# -*- coding: utf-8 -*-
#    This file is part of Gtfslib-python.
#
#    Gtfslib-python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Gtfslib-python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with gtfslib-python.  If not, see <http://www.gnu.org/licenses/>.
from gtfslib.utils import ContinousPiecewiseLinearFunc
"""
@author: Laurent GRÉGOIRE <laurent.gregoire@mecatran.com>
"""

import unittest

class TestUtils(unittest.TestCase):

    def test_piecewise_linear_interpolation(self):

        # Empty function
        f = ContinousPiecewiseLinearFunc()
        catched = False
        try:
            self.assertAlmostEqual(f.interpolate(0), 0, 3)
        except:
            catched = True
        self.assertTrue(catched)

        # Single point function
        f = ContinousPiecewiseLinearFunc()
        f.append(0, 0)
        self.assertAlmostEqual(f.interpolate(0), 0, 6)
        self.assertAlmostEqual(f.interpolate(-1), 0, 6)
        self.assertAlmostEqual(f.interpolate(1), 0, 6)

        # A simple well-behaved function
        f = ContinousPiecewiseLinearFunc()
        f.append(0, 0)
        f.append(1, 100)
        self.assertAlmostEqual(f.interpolate(-0.000000001), 0, 6)
        self.assertAlmostEqual(f.interpolate(0), 0, 6)
        self.assertAlmostEqual(f.interpolate(0.000000001), 0, 6)
        self.assertAlmostEqual(f.interpolate(0.5), 50.0, 6)
        self.assertAlmostEqual(f.interpolate(0.9999999999), 100, 6)
        self.assertAlmostEqual(f.interpolate(1.0), 100, 6)
        self.assertAlmostEqual(f.interpolate(1.0000000001), 100, 6)

        # Function with double-point (infinite derivative)
        f = ContinousPiecewiseLinearFunc()
        f.append(0, 0)
        f.append(1, 0)
        f.append(1, 100)
        f.append(2, 100)
        self.assertAlmostEqual(f.interpolate(0), 0, 6)
        self.assertAlmostEqual(f.interpolate(1), 100, 6)
        self.assertAlmostEqual(f.interpolate(-1), 0, 6)

        # A more complex one
        f = ContinousPiecewiseLinearFunc()
        f.append(10, 9000)
        f.append(20, 10000)
        f.append(1000, 10980)
        self.assertAlmostEqual(f.interpolate(5), 9000.0, 6)
        self.assertAlmostEqual(f.interpolate(15), 9500.0, 6)
        self.assertAlmostEqual(f.interpolate(40), 10020.0, 3)
        self.assertAlmostEqual(f.interpolate(1010), 10980.0, 3)

if __name__ == '__main__':
    unittest.main()
