import data
import unittest
from documents import get_name, get_shelf, get_all_data, add_data, delete_doc, move_doc, add_shelf


class TestDocuments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('method setUpClass')

    def setUp(self):
        print('method setUp')

    def test_get_name(self):
        self.assertEqual(get_name(data.documents, '11-2'), 'Владелец документа: Геннадий Покемонов.')

    def test_wrong_get_name(self):
        self.assertEqual(get_name(data.documents, '342'), 'Проверьте правильность введённых данных.')

    def test_get_shelf(self):
        self.assertEqual(get_shelf(data.directories, '10006'), 'Документ находится на 2 полке.')

    def test_get_all_data(self):
        self.assertIn(('passport "2207 876234" "Василий Гупкин"'
                       and 'invoice "11-2" "Геннадий Покемонов"'
                       and 'insurance "10006" "Аристарх Павлов"'),
                      get_all_data(data.documents))

    def test_add_data(self):
        self.assertEqual(add_data(data.documents, data.directories, 'passport', '5020 123456', 'Мария Иванова', '3'),
                         'Документ был успешно добавлен.')

    def test_delete_doc(self):
        self.assertEqual(delete_doc(data.documents, data.directories, '2207 876234'), 'Документ был успешно удалён.')

    def test_move_doc(self):
        self.assertEqual(move_doc(data.directories, '11-2', '3'), 'Документ был успешно перемещён на другую полку.')

    def test_add_shelf(self):
        self.assertEqual(add_shelf(data.directories, '4'), 'Новая полка была успешно добавлена.')

    def tearDown(self):
        print('method tearDown')

    @classmethod
    def tearDownClass(cls):
        print('method tearDownClass')
