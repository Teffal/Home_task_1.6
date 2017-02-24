recipes_book = {
    'яичница': [
        {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        ],
    'стейк': [
        {'ingredient_name': 'говядина', 'quantity': 300 , 'measure': 'гр.'},
        {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        ],
    'салат': [
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
        ]
    }

with open('Book_cook.txt', 'w', encoding='UTF8') as f:
    for recipe, ingredients in recipes_book.items():
        f.write('\n' + str(recipe) + '\n' + str(len(ingredients)) + '\n')
        for ingredient in ingredients:
            contain_list = []
            for contain in ingredient.values():
                contain_list.append(contain)
            f.write('|'.join(map(str, contain_list)) + '\n')

with open('Book_cook.txt', 'r', encoding='UTF8') as f:
    for line in f.readlines():
        print(line.strip())

