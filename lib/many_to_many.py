class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be Author")
        if not isinstance(book, Book):
            raise Exception("book must be Book")
        if not isinstance(date, str):
            raise Exception("date must be str")
        if not isinstance(royalties, int):
            raise Exception("royalties must be int")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]