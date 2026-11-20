def solve():
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99}, {'name': 'конфеты', 'price': 34.99}, 
            {'name': 'карамель', 'price': 45.99}, {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99}, {'name': 'конфеты', 'price': 32.99}, 
            {'name': 'карамель', 'price': 46.99}, {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99}, {'name': 'конфеты', 'price': 30.99}, 
            {'name': 'карамель', 'price': 41.99}, {'name': 'пирожное', 'price': 62.99}
        ],
    }
    
    sweets = {}
    for shop_name, products in shops.items():
        for product in products:
            name = product['name']
            price = product['price']
            if name not in sweets:
                sweets[name] = []
            sweets[name].append({'shop': shop_name, 'price': price})
    
    # Оставляем только 2 магазина с минимальными ценами для каждого товара
    for name in sweets:
        sweets[name].sort(key=lambda x: x['price'])
        sweets[name] = sweets[name][:2]
    
    # Красиво выводим в консоль, как в примере
    for product_name, shop_list in sweets.items():
        print(f"{product_name}:")
        for shop_info in shop_list:
            print(f"  - {shop_info['shop']}: {shop_info['price']} руб.")
        
    return sweets

if __name__ == "__main__":
    solve()