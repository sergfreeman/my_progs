import random


class Star:
    def __init__(self, x, y, z, s, sn):
        self.coord_x = x
        self.coord_y = y
        self.coord_z = z
        self.size = s
        self.star_list_name = sn

    star_list_name = list()
    star_list_coord = list()


# Created list of named stars
for quantity in range(0, random.randint(1, 3)):
    name = "star_" + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + str(quantity)
    
    star_list_name.append(name)
print(star_list_name)


# Created set coordinate parameters for each star from star_list_name

for coord in range(len(star_list_name)):
    x_coord = random.randint(0, 100)
    y_coord = random.randint(0, 100)
    z_coord = random.randint(0, 100)
    s_size = random.randint(1, 10)
    star_list_coord.append([x_coord, y_coord, z_coord, s_size])
print(star_list_coord)
print(star_list_coord[1][3])

    #
    # star = Star(x_coord, y_coord, z_coord, s_size)
    # print(f'{star_list_name[index]}: X={star.coord_x} Y={star.coord_y} Z={star.coord_z} sun size={star.size}')


