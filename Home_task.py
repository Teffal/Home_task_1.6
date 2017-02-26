


recipes_book = {
    'яичница': [
        {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
    'стейк': [
        {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
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
    line = f.readlines()
    cook_book = dict()
    for i in range(len(line)):
        # print(line[i])
        if line[i] == '\n':
            list_ingredients = []
            cook_book.update({line[i+1][:-1]:[]})
            for n in range(int(line[i+2][:-1])):
                value_dict = line[i+3+n][:-1].split('|')
                ingredient_dict = {
                    'ingredient_name': value_dict[0],
                    'quantity': int(value_dict[1]),
                    'measure': value_dict[2]}
                list_ingredients.append(ingredient_dict)
            cook_book[line[i+1][:-1]] = list_ingredients
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            # print(ingridient)
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list
# print(shop_list)
def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'],
                                shop_list_item['quantity'],
                                shop_list_item['measure']))
    for shop_list_item in shop_list.values():
        print('{1} {2} {0}'.format(shop_list_item['ingredient_name'],
                                shop_list_item['quantity'],
                                shop_list_item['measure']))
    for shop_list_item in shop_list.values():
        print('{quantity} {measure} {ingredient_name}'.format(**shop_list_item))

def create_shop_list():
    person_count = int(input('Enter count of person: '))
    # dishes = ['яичница', 'стейк', 'салат']
    dishes = input('Enter dishes for one person (you can list separated by "," without space): ').lower().split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()