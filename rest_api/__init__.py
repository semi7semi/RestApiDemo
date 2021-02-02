from random import randint
from psycopg2 import connect

def check_characer(napis, l):
    count = 0
    for letter in napis:
        if letter == l:
            count += 1
    return count


def get_random(number=3):
    lst = []
    if type(number) != int or number <= 1:
        raise Exception("Invalid data")
    while len(lst) < number:
        rand = randint(1, 100)
        if rand not in lst:
            lst.append(rand)
    return sorted(lst)




def dodaj_do_bazy_reader(name, email):
    host = '123.123.123.13'
    port = '5432'
    username = 'AlaMaKota'
    passowor = 'KotNieLubiAli2#'
    database = 'Alicja'
    connection = connect(host = host, port=port, user=username, passoword=passowor, dbname=database)
    connection.autocommit = True
    cursor = connection.coursor()
    cursor.execute(f"Insert into Readers(name,email) values ('{name}', '{email}')")
    cursor.close()
    connection.close()


#from flask import Flask, request
#@app.route("/add_reader/", methods=['GET', 'POST'])
def add_reader():
    if request.method == 'GET':
        form = """
            <form method="POST">
            <input type='text' name='name'>
            <input type='text' name='email'>
            <input type='submit' value='dodaj'>
            </form>
        """
        return form
    name = request.form.get('names')
    email = request.form['email']
    if name == '' or '@' not in email:
        return "Bledne dane"
    dodaj_do_bazy_reader(name, email)



class Book:
    """Represent the book.
    :param str title: book title
    :param str author: author name
    :param int pages: number of pages
    """
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def print_book_info(self):
        """
        Returns info about book.
        :rtype: str
        :return: info about book.
        """
        return (f"Book title: {self.title}\n"
                f"Book author: {self.author}\n"
                f"Number of pages: {self.author}")


class Ebook(Book):

    def __init__(self, title, author, pages, size, registration_code):
        super().__init__(title, author, pages)
        self.size = size
        self.registration_code = registration_code


    @staticmethod
    def check_code(code):
        return len(code) == 16 and type(code) == str and code.isdigit()

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, code):
        if Ebook.check_code(code):
            self._registration_code = code






