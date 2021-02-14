import os

"""
        Create and deletes reports, print from him.
"""


class NewReport:

    def __init__(self, n):
        try:

            # Create name of new report
            self.name = n
            self.name = input(">Enter the name of your new report>")
            if self.name == '':
                print("Error, empty name")
                start.menu()
            elif len(self.name) > 255:
                self.name = self.name[0:255]

        except (NameError, ValueError):

            print("Error, invalid name of new report")
            start.menu()

        else:
            self.report_text = list()
            self.new_report_menu()

        # Add new report to the report list
        try:
            f = open("ini.txt", "x")
            print(f.read())
        except FileExistsError:
            f = open("ini.txt", "w")
            self.report_quantity = list()

    # Add new text to the report file
    def enter_new_line(self):
        text = input(">Write some text>")
        self.report_text.append(""+text+"\n")

    # Report actions menu
    def new_report_menu(self):
        NewReport.enter_new_line(self)
        while True:
            Notebook.chars_line('-', 80)
            new_report_choice = input("Enter the action (A:add new line/S:save and exit/E:exit without saving):")

            if new_report_choice == 'A':
                self.enter_new_line()

            elif new_report_choice == 'S':
                f = open(self.name + '.txt', "w")
                for line in self.report_text:
                    f.write(line)
                    # print(line)
                f.close()

                f = open('ini.txt', "a")
                f.write(self.name + ",")
                f.close()
                start.menu()

            elif new_report_choice == 'E':
                start.menu()

            else:
                print("Error, invalid value")


class OpenReport:
    def __init__(self, ol):
        self.open_file_list = ol

        f = open('ini.txt', "r")
        tmp_str = f.read()
        open_file_list = tmp_str.split(sep=',')
        open_file_list.pop()  # delete last empty element

        # Show all reports files

        print("\n\t\tAll reports files(choose number to open):")

        if len(open_file_list) == 0:  # Exits to main menu if have not report files
            print('You have not report files')
            start.menu()

        for idx, file in enumerate(open_file_list):
            print(idx, "\t File:" + file)
        Notebook.chars_line('-', 80)

        # To open files menu
        while True:
            try:

                report_files_choice = int(input('>>'))
                Notebook.chars_line('-', 80)
                if 0 <= report_files_choice < len(open_file_list):
                    f = open(open_file_list[report_files_choice] + '.txt', "r")
                    print(f'\n\t\tReport: {open_file_list[report_files_choice]}\n')
                    print(f.read())
                    f.close()

                    Notebook.chars_line('-', 80)
                    break

                else:
                    print('Error, invalid number of your report')
            except (ValueError, TypeError, NameError):
                print("Type Error")

        while True:

            new_report_choice = input("Enter the action (P:print current report/D:delete current report/"
                                      "E:exit to the main menu):")

            if new_report_choice == 'P':  # Print report on printer
                os.startfile(open_file_list[report_files_choice] + '.txt', "print")

            elif new_report_choice == 'D':  # Delete report file
                os.remove(open_file_list[report_files_choice] + '.txt')
                f.close()

                # Delete file from file list (open_file_list())
                f = open('ini.txt', "r")
                tmp_str = f.read()
                f.close()
                open_file_list = tmp_str.split(sep=',')
                open_file_list.pop()  # delete last empty element
                open_file_list.pop(report_files_choice)

                # Write new file list
                new_ini_str = ''
                for elem in open_file_list:
                    new_ini_str += elem + ','
                f = open('ini.txt', "w")
                f.write(new_ini_str)
                f.close()
                start.menu()

            elif new_report_choice == 'E':  # Exit to the main menu
                start.menu()

            else:
                print("Error, invalid value")


class Notebook:

    @staticmethod
    def chars_line(sign, len_of_line):
        print(f"{sign}" * len_of_line)

    @staticmethod
    def create_new_report():
        Notebook.chars_line('-', 80)
        report = NewReport('report')

    @staticmethod
    def open_report():
        Notebook.chars_line('-', 80)
        report = OpenReport('self')

    def menu(self):
        while True:
            self.chars_line('-', 80)
            print("""
                            MENU
                1.  CREATE NEW REPORT
                2.  OPEN REPORT
                    PRINT REPORT
                    DELETE REPORT
                0.  EXIT PROGRAM
            """)
            self.chars_line('-', 80)
            m_choice = input(">>")

            if m_choice == "1":
                self.create_new_report()
            elif m_choice == "2":
                self.open_report()
            elif m_choice == "0":
                exit('Good Bye')
            else:
                print("Wrong, value must be in 0 to 5")


start = Notebook()
start.menu()



