def file_cook_book(my_file_path):
    with open(my_file_path, 'r', encoding='UTF8') as f:
        line = f.readline()
        cook_book = dict()
        while line:
            while not len(line.strip()):
                line = f.readline()
            my_kye = line.strip()
            list_ingredients = []
            ingridients_num = int(f.readline().strip())
            for _ in range(ingridients_num):
                value_dict = f.readline().strip().split('|')
                ingredient_dict = {
                    'ingredient_name': value_dict[0],
                    'quantity': int(value_dict[1]),
                    'measure': value_dict[2]}
                list_ingredients.append(ingredient_dict)
            cook_book[my_kye] = list_ingredients
            line = f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, my_file_path):
    shop_list = {}
    for dish in dishes:
        for ingridient in file_cook_book(my_file_path)[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingredient_name}: {quantity} {measure} '.format(**shop_list_item))

def create_shop_list():
    my_file_path = input('Enter the path to your file (default path: Book_cook.txt):')
    if not my_file_path:
        my_file_path = 'Book_cook.txt'
    person_count = int(input('Enter count of person: '))
    dishes = input('Enter dishes for one person (you can list separated by "," without space): ').lower().split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count, my_file_path)
    print_shop_list(shop_list)

create_shop_list()