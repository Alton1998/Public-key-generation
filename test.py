import unittest
from public_key import PublicKeyCrypto
import numpy as np

# Class to test the PublicKeyCrypto Class
class TestPublickeyCypto(unittest.TestCase):

    # Test the generator matrix
    def test_generator_matrix_func(self):
        test_matrix = np.random.randint(1,10,size=(90,90))
        p=PublicKeyCrypto()
        matrix=p._PublicKeyCrypto__generate_matrix()
        self.assertEqual(test_matrix.shape,matrix.shape)
    
    # Test the select field
    def test_select_field_func(self):
        p=PublicKeyCrypto()
        self.assertIsNotNone(p._PublicKeyCrypto__select_field())
    
    # Test the private key
    def test_generate_private_key(self):
        p=PublicKeyCrypto()
        self.assertIsNotNone(p._PublicKeyCrypto__generate_private_key())

if __name__=='__main__':
    unittest.main()
