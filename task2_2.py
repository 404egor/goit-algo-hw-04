


def get_cats_info(path):
    cats_dict=[]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats_dict.append({'id': id, 'name': name, 'age': int(age)})
    except FileNotFoundError:
        print("Файл не знайдено")
    except ValueError:
        print("Помилка при считуванні даних")
    return cats_dict




cats_info = get_cats_info(r'text2_2.txt')
print(cats_info)