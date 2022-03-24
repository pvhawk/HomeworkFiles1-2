from pprint import pprint

def files_read(file_name: str, mode: str, encoding:str, data: dict):
    a = True
    with open(file_name, mode, encoding=encoding) as file:
        while a == True:
            key = file.readline().strip()
            count = file.readline().strip()
            ing_list = []
            for i in range(int(count)):
                temp_dict = {}
                string = file.readline().strip()
                str_list = string.split('|')
                temp_dict['ingredient_name'] = str_list[0].strip(' ')
                temp_dict['quantity'] = str_list[1].strip(' ')
                temp_dict['measure'] = str_list[2].strip(' ')
                ing_list.insert(i, temp_dict)
            data[key] = ing_list
            if not file.readline():
                a = False
    return data

def get_shop_list_by_dishes(dishes: str, person_count: str):
    new_dict = {}
    for name_dish in dishes:
        # print(name_dish)
        for ingred in cook_book[name_dish]:
            # print(ingred)
            tmp_dict = {}
            tmp_dict['measure'] = ingred['measure']
            tmp_dict['quantity'] = int(ingred['quantity']) * person_count
            # print(tmp_dict)
            if new_dict.get(ingred['ingredient_name']) == None:
                new_dict[ingred['ingredient_name']] = tmp_dict
            else:
                new_dict[ingred['ingredient_name']]['quantity'] = new_dict[ingred['ingredient_name']]['quantity'] + tmp_dict['quantity']

    return new_dict



if __name__ == '__main__':
    cook_book = {}
    files_read('data.txt', 'rt', 'UTF-8', cook_book)
    # Задание 1.
    pprint(cook_book)
    # Задание 2.
    pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 20))