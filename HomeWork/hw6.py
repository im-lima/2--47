class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "прочитана" if self.read else "непрочитана"
        return f"название: {self.title}, автор: {self.author}, год: {self.year}, статус: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"книга '{book.title}' добавлена в библиотеку.")

    def list_books(self):
        if not self.books:
            print("библиотека пуста.")
        else:
            for book in self.books:
                print(book)

    def find_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print(f"книга с названием '{title}' не найдена.")

    def find_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print(f"книги автора '{author}' не найдены.")

    def mark_book_as_read(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                book.mark_as_read()
                print(f"книга '{title}' отмечена как прочитанная.")
                return
        print(f"книга с названием '{title}' не найдена.")

    def mark_book_as_unread(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                book.mark_as_unread()
                print(f"книга '{title}' отмечена как непрочитанная.")
                return
        print(f"книга с названием '{title}' не найдена.")

    def remove_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                self.books.remove(book)
                print(f"книга '{title}' удалена из библиотеки.")
                return
        print(f"книга с названием '{title}' не найдена.")

    def filter_by_status(self, read_status):
        filtered_books = [book for book in self.books if book.read == read_status]
        if not filtered_books:
            status = "прочитанные" if read_status else "непрочитанные"
            print(f"Нет {status} книг.")
        else:
            for book in filtered_books:
                print(book)

    def sort_by_year(self):
        sorted_books = sorted(self.books, key=lambda book: book.year)
        for book in sorted_books:
            print(book)


def main():
    library = Library()

    while True:
        print("\nкоманды:")
        print("1 - добавить книгу")
        print("2 - просмотреть все книги")
        print("3 - найти книгу по названию")
        print("4 - найти книги по автору")
        print("5 - отметить книгу как прочитанную")
        print("6 - отметить книгу как непрочитанную")
        print("7 - удалить книгу")
        print("8 - фильтрация книг (прочитанные/непрочитанные)")
        print("9 - сортировать книги по году")
        print("0 - выход")

        command = input("\nвведите команду: ")

        if command == "1":
            title = input("введите название книги: ")
            author = input("введите автора книги: ")
            year = input("введите год публикации книги: ")
            library.add_book(Book(title, author, year))
        elif command == "2":
            library.list_books()
        elif command == "3":
            title = input("введите название книги для поиска: ")
            library.find_by_title(title)
        elif command == "4":
            author = input("введите автора для поиска: ")
            library.find_by_author(author)
        elif command == "5":
            title = input("введите название книги для отметки как прочитанной: ")
            library.mark_book_as_read(title)
        elif command == "6":
            title = input("введите название книги для отметки как непрочитанной: ")
            library.mark_book_as_unread(title)
        elif command == "7":
            title = input("введите название книги для удаления: ")
            library.remove_book(title)
        elif command == "8":
            status = input("фильтровать по статусу (1 - прочитанные, 0 - непрочитанные): ")
            if status == "1":
                library.filter_by_status(True)
            elif status == "0":
                library.filter_by_status(False)
            else:
                print("неверный ввод.")
        elif command == "9":
            library.sort_by_year()
        elif command == "0":
            print("выход из программы.")
            break
        else:
            print("неверная команда. попробуйте снова.")


if __name__ == "__main__":
    main()