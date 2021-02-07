
import datetime


class Reviews:
    """
    This class create a reviews list
    b - name of the book
    t - text of review
    d - name of defendant

    review_list_text - list archive of reviews

    static methods:
    date_is       - get current date and time
    set_defendant - set current defendant name
    """

    def __init__(self, d=None, t=None, b='Alphabet'):
        self.defendant = d
        self.text = t
        self.book_is = b
        self.review_list_text = [
            'Serg Freeman 2021-02-07 14:32:33 Very interesting book.',
            'Hanna Smith 2021-02-07 14:33:12 It''s my first book, i did remembering my childhood.',
            'John Doe 2021-02-07 14:51:09 Simply Fantastic.',
            'Vasja Pupkin 2021-02-07 14:54:27 It''s a terrible, i crying from this bull shirt(( ',
            'Bomm Tahn    2021-02-07 14:57:48 i don''t now, i don''t understand this piece of paper'
        ]

    @staticmethod
    def date_is():
        d = datetime.datetime.now()
        return d.strftime('%Y-%m-%d %H:%M:%S')

    @ staticmethod
    def set_defendant():
        print()
        return input("What is your name:")

    def __str__(self):
        self.text = self.set_defendant()
        date = self.date_is()
        self.text = self.text + " " + date + "\n " + input(f"Pleas, write your review about {self.book_is}:")
        self.review_list_text.append(self.text)
        print()
        return self.text


my_review = Reviews()
while True:

    print("\n1\tCreate review\n2\tShow reviews\n0\tExit")
    select = input(">>")
    if select == "1":
        print(my_review.__str__())

    elif select == "2":
        print(f"\n\tReview for book: {my_review.book_is}")
        for item in my_review.review_list_text:
            print(item)
    elif select == "0":
        exit('Good Bye')
    else:
        print("Non correct value")
