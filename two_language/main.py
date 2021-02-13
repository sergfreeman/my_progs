class English:

    def greeting(self, text='Hello, England'):
        print(text)


class Spanish(English):
    pass


e = English()
s = Spanish()


def hello_friend():
    e.greeting()
    s.greeting('Buenos, Hispania')


hello_friend()