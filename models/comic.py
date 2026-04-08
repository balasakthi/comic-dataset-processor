class Comic:
    def __init__(self, title, author, genre, year, isbn, language):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.isbn = isbn
        self.language = language
        self.years = [year]
        self.isbns = [isbn]

    def get_years(self):
        return ", ".join(self.years)

    def get_genres(self):
        return ", ".join([g.strip() for g in self.genre.split(";")])
