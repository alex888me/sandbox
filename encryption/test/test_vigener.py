import unittest

from encryption.vigener import Vigener


class TestVigener(unittest.TestCase):
    def test_init(self):
        cipher = Vigener('SPG')
        assert cipher.key == 'SPG'


    def test_encrypt(self):
        cipher = Vigener('Lemon')
        self.assertEqual(cipher.encrypt('AttackAtDown'), 'LXFOPVEFRBHR', "Should be AttackAtDown->LXFOPVEFRBHR")

    def test_decrypt(self):
        cipher = Vigener('Lemon')
        self.assertEqual(cipher.decrypt('LXFOPVEFRBHR'), 'ATTACKATDOWN', "Should be LXFOPVEFRBHR->ATTACKATDOWN")


if __name__ == '__main__':
    unittest.main()
