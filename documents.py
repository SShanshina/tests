import data


def get_name(catalog, doc_num):
    result = 'Проверьте правильность введённых данных.'
    doc_number = doc_num
    for data in catalog:
        if doc_number == data['number']:
            return f"Владелец документа: {data['name']}."
    return result


def get_shelf(storage, doc_num):
    result = 'Проверьте правильность введённых данных.'
    doc_number = doc_num
    for shelf, docs in storage.items():
        if doc_number in docs:
            return f'Документ находится на {shelf} полке.'
    return result


def get_all_data(catalog):
    result = ''
    for data in catalog:
        doc_type = data['type']
        doc_number = data['number']
        name = data['name']
        result += f'{doc_type} "{doc_number}" "{name}"\n'
    return result


def add_data(catalog, storage, doc_t, doc_num, doc_name, shelf_num):
    new_doc = {}
    doc_type = doc_t
    doc_number = doc_num
    name = doc_name
    shelf_number = shelf_num
    new_doc.setdefault('type', doc_type)
    new_doc.setdefault('number', doc_number)
    new_doc.setdefault('name', name)
    catalog.append(new_doc)
    while shelf_number not in storage.keys():
        print(f'Такой полки не существует. Введите значение от 1 до {len(storage)}.')
        shelf_number = input('Введите номер полки для размещения документа: ')
    else:
        storage[shelf_number].append(doc_number)
        return 'Документ был успешно добавлен.'


def delete_doc(catalog, storage, doc_num):
    result = 'Проверьте правильность введённых данных.'
    doc_number = doc_num
    for i, data in enumerate(catalog):
        if doc_number == data['number']:
            del (catalog[i])
            result = 'Документ был успешно удалён.'
    for shelf, numbers in storage.items():
        if doc_number in numbers:
            numbers.remove(doc_number)
            result = 'Документ был успешно удалён.'
    return result


def move_doc(storage, doc_num, shelf_num):
    result = 'Проверьте правильность введённых данных.'
    doc_number = doc_num
    shelf_number = shelf_num
    if shelf_number in storage.keys():
        for shelf, numbers in storage.items():
            if doc_number in numbers:
                numbers.remove(doc_number)
                storage[shelf_number].append(doc_number)
                result = 'Документ был успешно перемещён на другую полку.'
    return result


def add_shelf(storage, new_shelf_num):
    new_shelf = new_shelf_num
    while new_shelf in storage:
        print('Такая полка уже существует.')
        new_shelf = input('Введите номер новой полки: ')
    else:
        storage.setdefault(new_shelf, [])
        return 'Новая полка была успешно добавлена.'


def main(catalog, storage):
    while True:
        user_input = (input('Введите команду: '))
        if user_input == 'p':
            print(get_name(catalog,
                           input('Введите номер документа: ')))
        elif user_input == 's':
            print(get_shelf(storage,
                            input('Введите номер документа: ')))
        elif user_input == 'l':
            print(get_all_data(catalog))
        elif user_input == 'a':
            print(add_data(catalog, storage,
                           input('Введите тип документа: '),
                           input('Введите номер документа: '),
                           input('Введите имя владельца документа: '),
                           input('Введите номер полки для размещения документа: ')))
        elif user_input == 'd':
            print(delete_doc(catalog, storage, input('Введите номер документа: ')))
        elif user_input == 'm':
            print(move_doc(storage,
                           input('Введите номер документа: '),
                           input('Введите номер полки для перемещения документа: ')))
        elif user_input == 'as':
            print(add_shelf(storage,
                            input('Введите номер новой полки: ')))
        else:
            print('Такой команды не существует.')
            break


if __name__ == '__main__':
    main(data.documents, data.directories)
