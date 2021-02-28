"""
Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.
"""

import pickle
import json

# create list of goods with three params: name, quantity, price

list_goods = [['apple'], 34, 185], [['pineapple'], 3, 711], [['watermelon'], 34, 380]


with open('list_goods.pickle', 'wb') as f:
    pickle.dump(list_goods, f)

with open('list_goods.pickle', 'rb') as f:
    data_new = pickle.load(f)

# convert to JSON:
my_json_date = json.dumps(data_new)

print(type(list_goods), list_goods)
print(type(data_new), data_new)
print(type(my_json_date), my_json_date)