'''
Marco Rodriguez Gomez
04/23/2026
Assignment: Test Cases
'''     
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        # Test basic
        self.assertEqual(city_country('Santiago', 'Chile'), 'Santiago, Chile')
        # Test with population
        self.assertEqual(city_country('Santiago', 'Chile', 5000000), 'Santiago, Chile - population 5000000')
        # Test with population and language
        self.assertEqual(city_country('Santiago', 'Chile', 5000000, 'Spanish'), 'Santiago, Chile - population 5000000, Spanish')

if __name__ == '__main__':
    unittest.main()