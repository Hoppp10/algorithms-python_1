def solve():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    
    print("Все виды цветов:", garden_set | meadow_set)
    print("Растут и там и там:", garden_set & meadow_set)
    print("Только в саду:", garden_set - meadow_set)
    print("Только на лугу:", meadow_set - garden_set)

if __name__ == "__main__":
    solve()