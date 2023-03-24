# import math
# import numpy as np
# import program

# def test_addNumber():
#     assert program.addNumber(2, 3) == 5
#     assert program.addNumber(-2, 3) == 1
#     assert program.addNumber(0, 0) == 0

# def test_area():
#     assert math.isclose(program.area(1), 3.14, rel_tol=1e-2)
#     assert math.isclose(program.area(0), 0, rel_tol=1e-2)
#     assert math.isclose(program.area(10), 314, rel_tol=1e-2)

# def test_binary():
#     assert program.binary([1, 2, 3, 4, 5], 0, 5, 4) == "Number found at 4"
#     assert program.binary([1, 2, 3, 4, 5], 0, 5, 6) == "Number is not there in the array"
#     assert program.binary([1, 2, 3, 4, 5], 0, 5, 1) == "Number found at 1"

# def test_compoundInterest():
#     assert math.isclose(program.compoundInterest(1000, 5, 5), 1284.25, rel_tol=1e-2)
#     assert math.isclose(program.compoundInterest(1000, 10, 5), 1610.51, rel_tol=1e-2)
#     assert math.isclose(program.compoundInterest(5000, 3, 10), 6655.35, rel_tol=1e-2)

# def test_dectobin():
#     assert program.dectobin(10) == "1010"
#     assert program.dectobin(0) == "0"
#     assert program.dectobin(7) == "111"

# def test_factorial():
#     assert program.factorial(5) == 120
#     assert program.factorial(0) == 1
#     assert program.factorial(1) == 1

# def test_fibonacci():
#     assert program.fibonacci(5) == [0, 1, 1, 2, 3]
#     assert program.fibonacci(0) == []
#     assert program.fibonacci(1) == [0]

# def test_file1():
#     # As file1 function generates random array, we can only check if it runs without error
#     program.file1()

# def test_remove_duplicates():
#     assert program.remove_duplicates([1, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]
#     assert program.remove_duplicates([]) == []
#     assert program.remove_duplicates([1, 2, 3]) == [1, 2, 3]

from file1 import *
from file2 import *
from file3 import *
from file4 import *
from file5 import *
from file6 import *
from file7 import *
from file8 import *
from file9 import *
from file10 import *
from file11 import *
from file12 import *
from file13 import *
from file14 import *
from file15 import *
from file16 import *
from file17 import *
from file18 import *
from file19 import *
from file20 import *
import inverseMatrix
import squareRoot
import palindrome
import unittest
import numpy as np
import factorial
import gcd
import random as rd
from io import StringIO
import sys
import math
import pytest
import unittest
import io
from contextlib import redirect_stdout
from unittest.mock import patch
from addNumbers import *
from area import *
from compoundInterest import *
from binSearchRecursion import *
from decToBin import *
from factorial import *
from fibonacci import *


class TestFunctions(unittest.TestCase):
    def test_addNumber(self):
        with patch('builtins.input', side_effect=['3', '4']):
            f = io.StringIO()
            with redirect_stdout(f):
                addNumber()
            self.assertEqual(f.getvalue().strip(), "Sum: 7")

    def test_area(self):
        with patch('builtins.input', side_effect=['5']):
            f = io.StringIO()
            with redirect_stdout(f):
                area()
            self.assertEqual(f.getvalue().strip(), "The area is: 78.5")

    def test_binary(self):
        a = [1, 2, 3, 4, 5]
        self.assertEqual(binary(a, 0, len(a)-1, 4), "Number found at 4")

    def test_compoundInterest(self):
        with patch('builtins.input', side_effect=['100', '5', '2']):
            f = io.StringIO()
            with redirect_stdout(f):
                compoundInterest()
            self.assertAlmostEqual(float(f.getvalue().strip()), 110.25)

    def test_dectobin(self):
        n = 10
        f = io.StringIO()
        with redirect_stdout(f):
            dectobin(n)
        self.assertEqual(f.getvalue().strip(), "1010")

    def test_asdf(self):
        self.assertIsNone(asdf())

    def test_fibonacci(self):
        with patch('builtins.input', side_effect=['5']):
            f = io.StringIO()
            with redirect_stdout(f):
                fibonacci()
            self.assertEqual(f.getvalue().strip(), "0\n1\n1\n2\n3")

    def test_file1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            file1()
        output = f.getvalue().strip().split('\n')
        arr = np.array(output[0].split(), dtype=int).reshape((5, 5))
        self.assertTrue(np.array_equal(arr.T, np.array(output[1].split(), dtype=int).reshape((5, 5))))
        self.assertTrue(np.array_equal(arr.flatten(), np.array(output[2].split(), dtype=int)))
        self.assertEqual(np.sum(arr), int(output[3]))

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 3, 4, 4]), [1, 2, 3, 4])


    def test_inverse_matrix(self):
        expected_x = np.array([[1,2], [3,4]])
        expected_y = np.array([[-2. , 1. ], [1.5, -0.5]])
        # Capture output from stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        inverseMatrix()
        sys.stdout = sys.__stdout__
        # Convert captured output from string to list of lines
        output_lines = captured_output.getvalue().strip().split('\n')
        # Get the output values from the last two lines
        output_x = np.fromstring(output_lines[-2], sep=' ')
        output_y = np.fromstring(output_lines[-1], sep=' ')
        # Compare the expected and actual outputs
        np.testing.assert_array_equal(expected_x, output_x)
        np.testing.assert_array_almost_equal(expected_y, output_y)

    def test_palindrome(self):
        self.assertEqual(palindrome(121), "It is a palindrome")
        self.assertEqual(palindrome(123), "It is not a palindrome")

    def test_random(self):
        # Test the rd.random() function
        rand_float = rd.random()
        self.assertGreaterEqual(rand_float, 0.0)
        self.assertLessEqual(rand_float, 1.0)
        # Test the rd.randint() function
        rand_int = rd.randint(1, 100)
        self.assertGreaterEqual(rand_int, 1)
        self.assertLessEqual(rand_int, 100)
        # Test the rd.randrange() function
        rand_range = rd.randrange(1, 100)
        self.assertGreaterEqual(rand_range, 1)
        self.assertLess(rand_range, 100)
        # Test the rd.choice() function
        choices = [1,2,3,4,5,6,7]
        rand_choice = rd.choice(choices)
        self.assertIn(rand_choice, choices)

    def test_sqrt(self):
        # Test the sqrt() function
        n = 25
        expected_result = 5.0
        # Capture output from stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        squareRoot(n)
        sys.stdout = sys.__stdout__
        # Convert captured output from string to list of lines
        output_lines = captured_output.getvalue().strip().split('\n')
        # Get the output value from the last line
        output_result = float(output_lines[-1])
        # Compare the expected and actual outputs
        self.assertAlmostEqual(expected_result, output_result)


    def test_sum_of_squares_positive():
        assert np.allclose(sum_of_squares(1), 1)
        assert np.allclose(sum_of_squares(5), 55)
        assert np.allclose(sum_of_squares(10), 385)
    
    def test_sum_of_squares_negative():
        with pytest.raises(TypeError):
            sum_of_squares('a')
        with pytest.raises(ValueError):
            sum_of_squares(-5)




    def test_list_files():
        expected_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        assert list_files() == expected_files
        
    def test_list_files_with_nonexistent_directory():
        with pytest.raises(FileNotFoundError):
            os.chdir('/nonexistent/directory')
            list_files()



    def test_factorial_positive():
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        
    def test_factorial_negative():
        with pytest.raises(TypeError):
            factorial('a')
        with pytest.raises(ValueError):
            factorial(-5)


  

    def test_hypotenuse_positive():
        assert math.isclose(hypotenuse(3, 4), 5.0, rel_tol=1e-9, abs_tol=0.0)
        assert math.isclose(hypotenuse(5, 12), 13.0, rel_tol=1e-9, abs_tol=0.0)
        assert math.isclose(hypotenuse(8, 15), 17.0, rel_tol=1e-9, abs_tol=0.0)
        
    def test_hypotenuse_negative():
        with pytest.raises(TypeError):
            hypotenuse('a', 4)
        with pytest.raises(ValueError):
            hypotenuse(3, -4)



    def test_dice_roll():
        for i in range(100):
            roll = dice_roll()
            assert 1 <= roll <= 6
        
    def test_dice_roll_with_seed():
        random.seed(1234)
        rolls = [dice_roll() for i in range(10)]
        expected_rolls = [3, 2, 2, 5, 4, 1, 1, 5, 6, 5]
        assert rolls == expected_rolls


    import pytest

    def test_gcd_positive():
        assert gcd(10, 25) == 5
        assert gcd(14, 28) == 14
        assert gcd(27, 81) == 27
        
    def test_gcd_negative():
        with pytest.raises(TypeError):
            gcd('a', 4)
        with pytest.raises(ValueError):
            gcd(3, -4)

    if __name__ == '__main__':
        unittest.main()
