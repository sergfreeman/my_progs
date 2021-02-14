

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

            #
            # f.write("Now the file has more content!")
            # f.close()
            # f = open("myfile.txt", "x")
            # # open and read the file after the appending:
            # f = open("demofile2.txt", "r")
            # print(f.read())


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
                # print(f.read())
                f.close()



                start.menu()
            elif new_report_choice == 'E':
                start.menu()
            else:
                print("Error, invalid value")








class OpenReport:
    pass


class DeleteReport:
    pass


class Notebook:

    folder_path = '/'
    @staticmethod
    def chars_line(sign, len_of_line):
        print(f"{sign}" * len_of_line)

    def show_report(self):
        pass

    @staticmethod
    def create_new_report():
        report = NewReport('report', '')


    def open_report(self):
        f = open("serg.txt", "r")
        print(f.read())

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



