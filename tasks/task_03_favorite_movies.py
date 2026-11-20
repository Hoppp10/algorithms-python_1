def solve():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    # 1. Первый фильм (до первой запятой)
    print(my_favorite_movies[:10])
    # 2. Последний фильм (с конца до запятой)
    print(my_favorite_movies[-16:])
    # 3. Второй фильм (между первой и второй запятой)
    print(my_favorite_movies[12:25])
    # 4. Второй с конца (между предпоследней и последней запятой)
    print(my_favorite_movies[-22:-17])

if __name__ == "__main__":
    solve()