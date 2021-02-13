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
        self.type_of_creatures = type_c
        self.status = status

    def life_time(self):
        pass
    galaxys_list = list()
    stars_list = list()
    type_of_creatures = 'Galaxys'

# Generate random values of the coordinates of galaxies and stars
    @staticmethod
    def generator(object_type, quantity):
        if object_type == Galaxy.galaxys_list:
            type_of_creatures = 'Galaxy'
            multiplicative = 0.5
            min_of_quantity = 1
        else:
            type_of_creatures = 'Stars'
            multiplicative = 5
            min_of_quantity = len(Star.stars_list)
        for _ in range(0, random.randint(min_of_quantity, quantity)):
            name = type_of_creatures + "_" + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) \
                   + str(random.randint(1, 10))
            x_coord = random.randint(0, 1000)
            y_coord = random.randint(0, 1000)
            z_coord = random.randint(0, 1000)
            s_size = random.randint(1, 100) / multiplicative

            object_type.append([name, x_coord, y_coord, z_coord, s_size])

# Draw line
    @staticmethod
    def draw_line(sign, quantity):
        print(f'{sign}'*quantity)

# Created report about galaxys and stars
    @classmethod
    def show_world(cls):

        if cls.type_of_creatures == 'Galaxys':
            current_list = cls.galaxys_list
        else:
            current_list = cls.stars_list

        for _ in range(len(current_list)):
            print(f'\t{current_list[_][0]} X:{current_list[_][1]} Y:{current_list[_][2]} Z:{current_list[_][3]} '
                  f'SIZE:{current_list[_][4]}')
        return cls


class Star(Galaxy):
    type_of_creatures = 'Star'


Galaxy.draw_line('-', 55)

print("\t\t\t* LET'S CREATE THE WORLD *")

# All galaxys
print("Galaxys:")
g = Galaxy
g.generator(Galaxy.galaxys_list, 5)


g.show_world()

# All stars
print("Stars:")
s = Star
s.generator(Star.stars_list, 15)
s.show_world()
Galaxy.draw_line('-', 55)

