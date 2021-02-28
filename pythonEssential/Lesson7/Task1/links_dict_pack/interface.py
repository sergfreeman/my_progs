from Lesson7.Task1.links_dict_pack.main import LinksDict

links_dict_obj = LinksDict()

while True:
    print("""
            MENU
        1.  Add new link
        2.  Open link
        3.  Show links list

        0.  Exit
    """)
    choice = input('>>')

    if choice == '1':
        links_dict_obj.add_component()
    elif choice == '2':
        links_dict_obj.find_component()
    elif choice == '3':
        print(links_dict_obj.my_dict.keys())
    elif choice == '0':
        exit()


