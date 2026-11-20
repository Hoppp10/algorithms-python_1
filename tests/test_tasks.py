import io
import sys
import os

# Добавляем корневую папку проекта в пути поиска Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks import (
    task_00_distance, task_01_circle, task_02_operations, task_03_favorite_movies,
    task_04_my_family, task_05_zoo, task_06_songs_list, task_07_secret,
    task_08_garden, task_09_shopping, task_10_store
)

# Вспомогательная функция для перехвата вывода print()
def capture_output(func):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

def test_00_distance():
    distances = task_00_distance.solve()
    assert 'Moscow' in distances
    assert 'London' in distances['Moscow']
    assert 'Paris' in distances['Moscow']

def test_01_circle():
    output = capture_output(task_01_circle.solve)
    assert '5541.7693' in output
    assert 'True' in output

def test_02_operations():
    output = capture_output(task_02_operations.solve)
    assert '25' in output

def test_03_favorite_movies():
    output = capture_output(task_03_favorite_movies.solve)
    assert 'Терминатор' in output
    assert 'Назад в будущее' in output

def test_04_my_family():
    output = capture_output(task_04_my_family.solve)
    assert 'Рост отца' in output
    assert 'Общий рост' in output

def test_05_zoo():
    output = capture_output(task_05_zoo.solve)
    assert 'bear' in output
    assert 'lark' in output

def test_06_songs_list():
    output = capture_output(task_06_songs_list.solve)
    assert 'минут' in output

def test_07_secret():
    output = capture_output(task_07_secret.solve)
    # Проверяем, что вывелась хоть какая-то строка (расшифровка)
    assert len(output.strip()) > 0 

def test_08_garden():
    output = capture_output(task_08_garden.solve)
    assert 'одуванчик' in output
    assert 'ромашка' in output

def test_09_shopping():
    sweets = task_09_shopping.solve()
    assert 'печенье' in sweets
    assert 'конфеты' in sweets

def test_10_store():
    output = capture_output(task_10_store.solve)
    assert 'Лампа' in output
    assert 'Стол' in output