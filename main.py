from tasks import (
    task_00_distance, task_01_circle, task_02_operations, task_03_favorite_movies,
    task_04_my_family, task_05_zoo, task_06_songs_list, task_07_secret,
    task_08_garden, task_09_shopping, task_10_store
)

tasks_map = {
    "0": ("Расстояния", task_00_distance.solve),
    "1": ("Окружность", task_01_circle.solve),
    "2": ("Операции", task_02_operations.solve),
    "3": ("Любимые фильмы", task_03_favorite_movies.solve),
    "4": ("Моя семья", task_04_my_family.solve),
    "5": ("Зоопарк", task_05_zoo.solve),
    "6": ("Песни Depeche Mode", task_06_songs_list.solve),
    "7": ("Секретное сообщение", task_07_secret.solve),
    "8": ("Сад и луг", task_08_garden.solve),
    "9": ("Магазины", task_09_shopping.solve),
    "10": ("Склад", task_10_store.solve),
}

def main():
    while True:
        print("\n" + "="*30)
        print("Доступные задания:")
        for key, (name, _) in tasks_map.items():
            print(f"  {key}. {name}")
        
        choice = input("\nВыберите номер задания (или 'q' для выхода): ").strip()
        
        if choice.lower() == 'q':
            print("Выход из программы. До свидания!")
            break
            
        if choice in tasks_map:
            name, func = tasks_map[choice]
            print(f"\n--- Запуск: {name} ---")
            
            result = func()
            if result is not None:
                print("Результат:", result)
                
            print("-" * 23)
            
            # ЖДЕМ ENTER
            input("Нажмите Enter, чтобы вернуться в меню...")
            
        else:
            print("Неверный выбор!")
            input("Нажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()