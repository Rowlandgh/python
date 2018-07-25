import unittest
from format_nation_city import nation_city

class Test_format_nc(unittest.TestCase):
    def test_naion_city(self):
        final_nation_city = nation_city('china','beijing','5')
        self.assertEqual(final_nation_city,'beijing,china,5')  
unittest.main()