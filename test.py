import unittest
from unittest.mock import patch
from io import StringIO
import sys


sys.path.append('/Users/yang/Desktop/password')


from password import main

class TestPasswordGenerator(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '8', '2'])  
    @patch('sys.stdout', new_callable=StringIO)  
    def test_main_generate_password(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("welcome to the password generator", output)
        self.assertIn("Your password is:", output)

    @patch('builtins.input', side_effect=['2'])  
    @patch('sys.stdout', new_callable=StringIO)  
    def test_main_exit(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("welcome to the password generator", output)
        self.assertNotIn("Your password is:", output)

if __name__ == '__main__':
    unittest.main()
