

class NewReport:
    def __init__(self, n, rt, r_q=0):
        try:

            self.name = n
            self.name = input("Enter the name of your new report:")
            if self.name == '':
                print("Error, empty name")
                start.menu()
            elif len(self.name) > 255:
                self.name = self.name[0:255]

        except (NameError, ValueError):

            print("Error, invalid name of new report")
            start.menu()

        else:

            self.report_text = rt
            self.report_text = list()

            self.new_report_menu()
        try:
            f = open("ini.txt", "x")
            print(f.read())
        except FileExistsError:
            f = open("ini.txt", "w")
            self.report_quantity = list()

    def enter_new_line(self):
        text = input(">write some text>")
        self.report_text.append(""+text+"\n")

# Report actions menu
    def new_report_menu(self):
        NewReport.enter_new_line(self)
        while True:
            new_report_choice = input("Enter the action (N:new line/S:save and exit/E:exit without saving):")

            if new_report_choice == 'N':
                self.enter_new_line()
            elif new_report_choice == 'S':

                f = open(self.name + '.txt', "w")
                for line in self.report_text:
                    f.write(line)
                    print(line)
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
        open_file_list = list()

        f = open('ini.txt', "r")
        tmp_str = f.read()
        print(tmp_str)
        open_file_list = tmp_str.split(sep=',')
        open_file_list.pop()  # delete last empty element

        # Show all reports files
        print("\n\t\tAll reports files(choose number to open):")
        for idx, file in enumerate(open_file_list):
            print(idx, "\t File:" + file)

        report_files_choice = input('>')




class DeleteReport:
    pass


class Notebook:

    @staticmethod
    def chars_line(sign, len_of_line):
        print(f"{sign}" * len_of_line)

    def show_report(self):
        pass

    @staticmethod
    def create_new_report():
        report = NewReport('report', '')

    @staticmethod
    def open_report():
        report = OpenReport('self')


    def delete_report(self):
        pass

    def print_report(self):
        pass

    def menu(self):
        while True:
            self.chars_line('-', 80)
            print("""
                            MENU
                1.  CREATE NEW REPORT
                2.  OPEN REPORT
                3.  PRINT REPORT
                4.  DELETE REPORT
                0.  EXIT PROGRAM
            """)
            self.chars_line('-', 80)
            m_choice = input(">>")

            if m_choice == "1":
                self.create_new_report()
            elif m_choice == "2":
                self.open_report()
            elif m_choice == "3":
                self.print_report()
            elif m_choice == "4":
                self.delete_report()
            elif m_choice == "0":
                exit('Good Bye')
            else:
                print("Wrong, value must be in 0 to 5")


start = Notebook()
start.menu()



