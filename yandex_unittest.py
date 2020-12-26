import unittest
from yandex import create_folder, check_folder


class TestYandex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('method setUpClass')

    def setUp(self):
        print('method setUp')

    def test_1_create_folder(self):
        self.assertEqual(create_folder('Папка').status_code, 201)

    def test_2_double_create_folder(self):
        self.assertEqual(create_folder('Папка').status_code, 409)

    def test_3_wrong_authorization(self):
        self.assertNotEqual(create_folder('Новая папка').status_code, 401)

    def test_4_folder_created(self):
        self.assertIn('Новая папка', check_folder('disk:/'))

    def tearDown(self):
        print('method tearDown')

    @classmethod
    def tearDownClass(cls):
        print('method tearDownClass')
