import main
# import account



class MoneyReceiving:

    def receive_coins(self, val):
        from account import person
        person.Account.char_line('-', 65)
        try:
            if val <= person.client_balance:        #account.Account.client_balance:
                # self.client_balance -= val
                person.client_balance -= val
                # account.Account.client_balance -= val
                print(f'Confirmed: you receive {val}')
            else:
                print("Canceled: you got no money.")
                exit()

            print(f"Balance: {person.client_balance} coins")
            person.Account.char_line('-', 65)
        except ValueError:
            print("Error, value should be integer")




mr = MoneyReceiving()
while True:
    mr.receive_coins(int(input('>receive>')))

