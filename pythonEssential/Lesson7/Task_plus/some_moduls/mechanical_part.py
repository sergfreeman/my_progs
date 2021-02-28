from list_part import create_list

prime_numbers_list = create_list()


def search(interval):
    """
    Record all prime numbers in the list
    """

    print('In the module "mechanical_part" we create prime numbers and store them in the list "prime_numbers_list')
    for number in range(2, interval+1):
        for val in range(2, number):
            if number % val == 0:
                break
            else:
                if val == number - 1:
                    prime_numbers_list.append(number)

    return prime_numbers_list

