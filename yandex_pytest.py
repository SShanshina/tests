import pytest
from yandex import create_folder, check_folder


class TestYandex:

    def setup_class(self):
        print('method setUpClass')

    def setup(self):
        print('method setUp')

    def test_1_create_folder(self):
        assert create_folder('Папка').status_code == 201

    def test_2_double_create_folder(self):
        assert create_folder('Папка').status_code == 409

    def test_3_wrong_authorization(self):
        assert create_folder('Новая папка').status_code != 401

    def test_4_folder_created(self):
        assert 'Новая папка' in check_folder('disk:/')

    def teardown(self):
        print('method tearDown')

    def teardown_class(self):
        print('method tearDownClass')
