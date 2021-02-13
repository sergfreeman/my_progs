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
    def __init__(self, n, x, y, z, size,  type_c="Galaxy", status=True):
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
    type_of_creatures = 'Galaxy'

# Generate random values of the coordinates of galaxies and stars
    @staticmethod
    def generator(object_type, quantity):
        if object_type == Galaxy.galaxys_list:
            type_of_creatures = 'Galaxy'
            multiplicative = 0.5
            min_of_quantity = 1
        else:
            type_of_creatures = 'Star'
            multiplicative = 5
            min_of_quantity = len(Star.stars_list)
        for _ in range(0, random.randint(min_of_quantity, quantity)):
            name = type_of_creatures + "_" + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) \
                   + str(random.randint(1, 10))
            x_coord = random.randint(0, 500)
            y_coord = random.randint(0, 500)
            z_coord = random.randint(0, 500)
            s_size = random.randint(1, 500) / multiplicative

            object_type.append([name, x_coord, y_coord, z_coord, s_size])

# Draw line
    @staticmethod
    def draw_line(sign, quantity):
        print(f'{sign}'*quantity)

# Created report about galaxys and stars
    @classmethod
    def show_world(cls):

        if cls.type_of_creatures == 'Galaxy':
            current_list = cls.galaxys_list
        else:
            current_list = cls.stars_list

        for _ in range(len(current_list)):
            print(f'\t{current_list[_][0]} X:{current_list[_][1]} Y:{current_list[_][2]} Z:{current_list[_][3]} '
                  f'SIZE:{current_list[_][4]}')
        return cls

    @staticmethod
    def sort_stars_by_galaxies():
        for galactic in Galaxy.galaxys_list:

            gal_name = list()

            for star in Star.stars_list:
                if star[1] - galactic[4]/2 < galactic[1] < star[1] + galactic[4]/2:
                    if star[2] - galactic[4]/2 < galactic[2] < star[2] + galactic[4]/2:
                        if star[3] - galactic[4]/2 < galactic[3] < star[3] + galactic[4]/2:
                            gal_name.append(star)

            if len(gal_name) == 0:
                pass
            else:
                print(f'{galactic[0]}\n\t( X:{galactic[1]} Y:{galactic[2]} Z:{galactic[3]} SIZE:{galactic[4]} ),'
                      f' consist of a stars:')
                # print(gal_name)
                for i in range(len(gal_name)):
                    # print(gal_name[i][0])
                    print(f'\t{gal_name[i][0]} X:{gal_name[i][1]} Y:{gal_name[i][2]} Z:{gal_name[i][3]}'
                          f' SIZE:{gal_name[i][4]}')

    @staticmethod
    def set_title(msg):
        Galaxy.draw_line('-', 60)
        print(msg)
        Galaxy.draw_line('-', 60)


class Star(Galaxy):
    type_of_creatures = 'Star'


Galaxy.set_title("""
step 1          * LET'S CREATE THE WORLD *
""")
# Show galaxys
print("Galaxys:")
g = Galaxy
g.generator(Galaxy.galaxys_list, 5)
g.show_world()

# Show stars
print("Stars:")
s = Star
s.generator(Star.stars_list, 100)
s.show_world()
Galaxy.set_title("""
step 2          * SORT STARS BY GALAXIES *
""")
# Show sort star lists
Galaxy.sort_stars_by_galaxies()

