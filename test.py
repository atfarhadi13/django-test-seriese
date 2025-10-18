import unittest

from app import Superhero

class TestSuperhero(unittest.TestCase):
    def setUp(self):
        self.superhero = Superhero(name="Superman", strength_level=50)
        self.other_superhero = Superhero(name="Batman", strength_level=35)

    def test_stringify(self):
        self.assertEqual(str(self.superhero), "Superman")

    def test_is_stronger_than_other_superhero(self):
        self.assertTrue(self.superhero.is_stronger_than(self.other_superhero))
        self.assertFalse(self.other_superhero.is_stronger_than(self.superhero))





