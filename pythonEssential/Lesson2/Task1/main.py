class Editor:
    """
    Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
edit_document выводит на экран информацию о том, что редактирование документов недоступно для
бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
иначе Editor. Вызовите методы просмотра и редактирования документов.
    """

    def view_document(self):
        print('We can view some documents')

    def edit_document(self):
        print('Edition available only in full version!')




class ProEditor(Editor):

    def edit_document(self):
        print('We can edit some document, our program version is full')


lic_key = input('Enter valid license key [KEY] for work in full version :')
if lic_key == 'KEY':
    print('We work in full version.')
    prog = ProEditor()
else:
    print('We work in trial version.')
    prog = Editor()

prog.view_document()
prog.edit_document()