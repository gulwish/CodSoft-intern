import unittest


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        # Test the generate_password function with different lengths
        for length in [8, 12, 16]:
            password = generate_password(length)
            self.assertEqual(len(password), length)

if __name__ == '__main__':
    unittest.main()
