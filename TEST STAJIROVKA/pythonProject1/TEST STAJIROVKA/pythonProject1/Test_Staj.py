import pytest


# Тесты для tuple
def test_tuple_operations(capsys):
    t = (1, 2, 3)
    assert len(t) == 3
    print("Длина tuple: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Длина tuple: успешно\n"

    assert t[1] == 2
    print("Доступ к элементу tuple: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Длина tuple: успешно\nДоступ к элементу tuple: успешно\n"

    with pytest.raises(TypeError):
        t[1] = 5
    print("Попытка изменить элемент tuple: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Длина tuple: успешно\nДоступ к элементу tuple: успешно\nПопытка изменить элемент tuple: успешно\n"


@pytest.mark.parametrize("index, expected_value", [(0, 1), (2, 3)])
def test_tuple_parameterized_access(index, expected_value, capsys):
    t = (1, 2, 3)
    assert t[index] == expected_value
    print("Параметризованный доступ к элементу tuple: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Параметризованный доступ к элементу tuple: успешно\n"


# Тесты для dict
def test_dict_operations(capsys):
    d = {'a': 1, 'b': 2, 'c': 3}
    assert len(d) == 3
    print("Длина словаря: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Длина словаря: успешно\n"

    assert d['b'] == 2
    print("Доступ к значению по ключу: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Длина словаря: успешно\nДоступ к значению по ключу: успешно\n"


@pytest.mark.parametrize("key, expected_value", [('a', 1), ('c', 3)])
def test_dict_parameterized_access(key, expected_value, capsys):
    d = {'a': 1, 'b': 2, 'c': 3}
    assert d[key] == expected_value
    print("Параметризованный доступ к значению по ключу в словаре: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Параметризованный доступ к значению по ключу в словаре: успешно\n"


def test_division_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0
    print("Деление на ноль: успешно")

    captured = capsys.readouterr()
    assert captured.out == "Деление на ноль: успешно\n"


if __name__ == "__main__":
    pytest.main()