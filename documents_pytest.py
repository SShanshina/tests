import pytest
import data
from documents import get_name, get_shelf, get_all_data, add_data, delete_doc, move_doc, add_shelf


class TestDocuments:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def test_get_name(self):
        assert get_name(data.documents, '11-2') == 'Владелец документа: Геннадий Покемонов.'

    def test_wrong_get_name(self):
        assert get_name(data.documents, '342') == 'Проверьте правильность введённых данных.'

    def test_get_shelf(self):
        assert get_shelf(data.directories, '10006') == 'Документ находится на 2 полке.'

    def test_get_all_data(self):
        assert ('passport "2207 876234" "Василий Гупкин"'
               and 'invoice "11-2" "Геннадий Покемонов"'
               and 'insurance "10006" "Аристарх Павлов"') in get_all_data(data.documents)

    def test_add_data(self):
        assert add_data(data.documents, data.directories, 'passport', '5020 123456', 'Мария Иванова', '3') \
               == 'Документ был успешно добавлен.'

    def test_delete_doc(self):
        assert delete_doc(data.documents, data.directories, '2207 876234') == 'Документ был успешно удалён.'

    def test_move_doc(self):
        assert move_doc(data.directories, '11-2', '3') == 'Документ был успешно перемещён на другую полку.'

    def test_add_shelf(self):
        assert add_shelf(data.directories, '4') == 'Новая полка была успешно добавлена.'

    def teardown(self):
        print('method teardown')

    def teardown_class(self):
        print('method teardown_class')
