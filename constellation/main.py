import random
"""
    З огляду на те, що маса ядра зірки пропорційна її повній масі (М), 
    шляхом розрахунків одержуємо приблизне співвідношення: 
    тривалість перетворення водню в гелій дорівнює 10 M/L млрд. років, 
    де маса М і світність L зірки виражені в масах і світності Сонця. 
    Для зірок з масою, близькою до сонячної, L = М  (це випливає зі спостережень). 
    Звідси знаходимо, що час їхнього життя 10/М  млрд. років.
"""


class Galaxy:
    def __init__(self, n, x, y, z, size,  type_c="Galaxy's", status=True):
        self.names = n
        self.coord_x = x
        self.coord_y = y
        self.coord_z = z
        self.size = size
        self.type_of_creature = type_c
        self.status = status

    def life_time(self):
        pass


class Star(Galaxy):
    type_of_creatures = 'Star'


galaxys_list = list()
stars_list = list()


def generator(object_type, quantity):
    if object_type == galaxys_list:
        multiplicative = 0.5
    else:
        multiplicative = 5
    for _ in range(0, random.randint(1, quantity)):
        name = type_of_creatures + "_" + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) \
               + str(random.randint(1, 10))
        x_coord = random.randint(0, 100)
        y_coord = random.randint(0, 100)
        z_coord = random.randint(0, 100)
        s_size = random.randint(1, 100) / multiplicative

        object_type.append([name, x_coord, y_coord, z_coord, s_size])


for obj in range(random.randint(1, 5)):
    type_of_creatures = 'Galaxy: '
    object_type = galaxys_list
    generator(galaxys_list, 1)

for obj in range(random.randint(1, 25)):
    type_of_creatures = 'Star: '
    object_type = stars_list
    generator(stars_list, len(galaxys_list))
    # print(len(galaxys_list))
print('\t\t\t* LETS CREATE THE WORLD *')

print("Galaxys:")
for _ in range(len(galaxys_list)):
    print(f'\t{galaxys_list[_][0]} X:{galaxys_list[_][1]}  Y:{galaxys_list[_][2]}  Z:{galaxys_list[_][3]} '
          f'SIZE:{galaxys_list[_][4]}')


print('Stars:')
for _ in range(len(stars_list)):
    print(f'\t{stars_list[_][0]} X:{stars_list[_][1]}  Y:{stars_list[_][2]}  Z:{stars_list[_][3]} '
          f'SIZE:{stars_list[_][4]}')

