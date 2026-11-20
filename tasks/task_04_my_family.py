def solve():
    my_family = ['Папа', 'Мама', 'Я']
    my_family_height = [
        ['Папа', 180],
        ['Мама', 165],
        ['Я', 175],
    ]
    
    # Рост отца
    for member in my_family_height:
        if member[0] == 'Папа':
            print(f"Рост отца - {member[1]} см")
            
    # Общий рост
    total_height = sum(member[1] for member in my_family_height)
    print(f"Общий рост моей семьи - {total_height} см")

if __name__ == "__main__":
    solve()