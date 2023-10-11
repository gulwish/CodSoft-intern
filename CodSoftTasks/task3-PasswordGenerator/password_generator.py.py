import secrets
import string

def generate_password(length=12):
    # var combination of chacters used for generating 
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    '''
    each time selecting a random character 
    from the alphabet and joining them together to create the password.
      This password will be a random sequence of characters 
      selected from the combined character set defined in alphabet
      '''

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def main():
    print("Welcome to the Secure Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length (default is 12): "))
            if length < 1:
                print("Password length must be at least 1 character.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")

    password = generate_password(length)
    print("Generated Password:", password)

# if __name__ == "__main__":
#     main()


import unittest

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        # Test the generate_password function with different lengths
        for length in [8, 12, 16]:
            password = generate_password(length)
            self.assertEqual(len(password), length)

if __name__ == '__main__':
    unittest.main()
