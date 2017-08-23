import unittest
from broadlink2mqtt.record import get_broadlink_rm
from broadlink2mqtt.record import execute_command
from broadlink2mqtt.play import put_on_humificator
from broadlink2mqtt.play import put_off_humificator
 
class TestMain(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_number(self):
        self.assertTrue(True)
 
if __name__ == '__main__':
    unittest.main()
