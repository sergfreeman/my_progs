import copy

# This project showing power of cryptographic

#                      Wehrmacht Enigma 1938

# Rotor I — V «Enigma»:

#    index   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
#            A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z
#    I       E   K   M   F   L   G   D   Q   V   Z   N   T   O   W   Y   H   X   U   S   P   A   I   B   R   C   J
#    II      A   J   D   K   S   I   R   U   X   B   L   H   W   T   M   C   Q   G   Z   N   P   Y   F   V   O   E
#    III     B   D   F   H   J   L   C   P   R   T   X   V   Z   N   Y   E   I   W   G   A   K   M   U   S   Q   O
#    IV      E   S   O   V   P   Z   J   A   Y   Q   U   I   R   H   X   L   N   F   T   G   K   D   C   M   W   B
#    V       V   Z   B   R   G   I   T   Y   U   P   S   D   N   H   L   X   A   W   M   J   Q   O   F   E   C   K


#           The Wehrmacht used the following abbreviations:
#    KLAM = Parenthesis                                             :not realized at this project
#    ZZ = Comma
#    X = Full stop (end of sentence)                                :not realized at this project
#    YY = Point or dot
#    X****X = Inverted commas                                       :not realized at this project


# Одночасно використовується лише три диски у певній послідовності. Генерується ключ з 3 літер!

# «Енігма» складалася з комбінації механічних і електричних систем. Механічна частина включала клавіатуру,
# набір обертових дисків (роторів), які були розташовані уздовж валу і прилягали до нього, і ступінчастого механізму,
# який рухав один або більше роторів при кожному натисненні клавіші.
# Конкретний механізм роботи міг відрізнятися, але загальний принцип був такий: при кожному натисненні клавіші
# крайній справа ротор зміщується на одну позицію, а за певних умов зміщуються й інші ротори.
# Рух роторів призводить до різних криптографічних перетворень при кожному наступному натисненні клавіші на клавіатурі.
# Механічні частини рухалися, утворюючи електричний контур, що змінюється, тобто, фактично, шифрування букв
# здійснювалося електрично.
# При натисненні клавіш, контур замикався, струм проходив через різні компоненти і в результаті вмикав одну
# з багатьох лампочок, яка відображувала букву, що виводилася.

rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I',
          'B', 'R', 'C', 'J']
rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y',
          'F', 'V', 'O', 'E']
rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M',
          'U', 'S', 'Q', 'O']
rotor4 = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D',
          'C', 'M', 'W', 'B']
rotor5 = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O',
          'F', 'E', 'C', 'K']
temp = []

entered_msg, prepared_msg, encrypted_msg, current_rotor, my_rotor1, my_rotor2, my_rotor3,  = [], [], [], [], [], [], []


# ENTER KEY (ONLY 3 LITERALS)
def enter_the_key():
    while True:
        print("\n\n\tEnter the KEY(some three literals)")
        str_key = input("Key: ")
        try:
            if len(str_key) == 3 and str_key.isalpha():
                str_key = str_key.upper()
                return str_key

        except ValueError:
            print("Error, length or symbols of key is not correct. Try it again.")


# SHOW LIST
def show_list(list_to_show):
    counter = 0
    for items in list_to_show:
        print(items, end="")
        counter += 1
        if counter % 4 == 0:
            print(" ", end="")
        if counter >= 20:
            print(" ")
            counter = 0


# SELECT THREE FROM FIVE ROTORS TO USAGE
def select_three_rotors():
    while True:
        select_rotor = [None, False, False, False, False, False]
        rotor_error_msg = "Error,  this rotor maybe is used or her number is not correct. Retry is."
        global my_rotor1, my_rotor2, my_rotor3

        try:
            print("\n\t\tSelect 3 of 5 coding rotors")

            first_rotor = int(input("   I:"))
            if 0 < first_rotor < 6:
                if first_rotor == 1:
                    my_rotor1 = copy.deepcopy(rotor1)
                elif first_rotor == 2:
                    my_rotor1 = copy.deepcopy(rotor2)
                elif first_rotor == 3:
                    my_rotor1 = copy.deepcopy(rotor3)
                elif first_rotor == 4:
                    my_rotor1 = copy.deepcopy(rotor4)
                else:
                    my_rotor1 = copy.deepcopy(rotor5)
                select_rotor[first_rotor] = True
            else:
                print(rotor_error_msg)
                continue

            second_rotor = int(input("  II:"))
            if 0 < second_rotor < 6 and select_rotor[second_rotor] is False:
                select_rotor[second_rotor] = True
                if second_rotor == 1:
                    my_rotor2 = copy.deepcopy(rotor1)
                elif second_rotor == 2:
                    my_rotor2 = copy.deepcopy(rotor2)
                elif second_rotor == 3:
                    my_rotor2 = copy.deepcopy(rotor3)
                elif second_rotor == 4:
                    my_rotor2 = copy.deepcopy(rotor4)
                else:
                    my_rotor2 = copy.deepcopy(rotor5)
            else:
                print(rotor_error_msg)
                continue

            third_rotor = int(input(" III:"))
            if 0 < third_rotor < 6 and select_rotor[third_rotor] is False:
                if third_rotor == 1:
                    my_rotor3 = copy.deepcopy(rotor1)
                elif third_rotor == 2:
                    my_rotor3 = copy.deepcopy(rotor2)
                elif third_rotor == 3:
                    my_rotor3 = copy.deepcopy(rotor3)
                elif third_rotor == 4:
                    my_rotor3 = copy.deepcopy(rotor4)
                else:
                    my_rotor3 = copy.deepcopy(rotor5)
                return my_rotor1, my_rotor2, my_rotor3
            else:
                print(rotor_error_msg)
                continue
        except ValueError:
            print(rotor_error_msg)
            continue


# CHANGE VALUE OF ROTOR ELEMENTS FROM KEY
def rotor_key_correct(rotor_input, key):
    rotor_output = copy.deepcopy(rotor_input)
    for element in range(26):
        tmp = ord(rotor_output[element]) + ord(key) - 65
        if tmp > 90:
            # print("value error", tmp)
            tmp -= 26

        rotor_output[element] = chr(tmp)
        return rotor_output


# ENCRYPT PARTS
def encrypt():

    to_encoding_list = []

    while True:
        print()
        str_tmp = input("Enter some simple text(only 500 literals alphabet or special symbols like: '.', ','):")
        for char in str_tmp:
            if char.isalpha():
                to_encoding_list.extend([char.upper()])
            elif char == ".":
                to_encoding_list.append('Y')
                to_encoding_list.append('Y')
            elif char == ",":
                to_encoding_list.append('Z')
                to_encoding_list.append('Z')
        if len(to_encoding_list) > 500:
            to_encoding_list = to_encoding_list[:500]

        print("\nPREPARING TEXT TO ENCRYPT:")
        show_list(to_encoding_list)
        break

    # CREATE ENCODING LIST FROM PREVIOUS PREPARING
    str_key = copy.deepcopy(enter_the_key())
    encoding_list = copy.deepcopy(to_encoding_list)

    # print(encoding_list)


#                       THREE STAGE OF ROTOR CORRECTION AND ENCRYPT PROCESS

    counter_of_rotor = 0

    # TAKE A ROTORS AND USE THE KEY CORRECTION FOR HIM
    select_three_rotors()

    for stage in range(3):
        for encrypt_cycle_value in range(len(encoding_list)):

            if stage == 0:
                rotor = my_rotor1
                rotor = rotor_key_correct(rotor, str_key[0])
            elif stage == 1:
                rotor = my_rotor2
                rotor = rotor_key_correct(rotor, str_key[1])
            else:
                rotor = my_rotor3
                rotor = rotor_key_correct(rotor, str_key[2])

            # ENCRYPT PROCESS
            # print("counter: ", counter_of_rotor)
            temp_index_of_char = ord((encoding_list[encrypt_cycle_value])) + ord((rotor[counter_of_rotor])) - 65

            if temp_index_of_char > 90:
                temp_index_of_char -= 26

            encoding_list[encrypt_cycle_value] = chr(temp_index_of_char)
            counter_of_rotor += 1

            if counter_of_rotor >= 26:
                counter_of_rotor = 0

    print("\n\tENCRYPT MESSAGE IS:")
    show_list(encoding_list)


while True:
    print("\n\n\t EMULATOR OF ENCRYPT MACHINE 'Wehrmacht Enigma 1938'")
    print("-" * 58)
    print("""
    \t1...Encrypt text
    \t2...Decrypt text
    \t0...Exit
    """)

    menu_choice = input("Enter your choice: ")
    if menu_choice == "0":
        quit(0)
    elif menu_choice == "1":
        encrypt()
