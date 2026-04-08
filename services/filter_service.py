class FilterService:

    def filter_by_genre(self, comics, genre):
        result = []

        for comic in comics:
            if comic.genre:
                genres = comic.genre.split(";")

                if any(genre.lower() in g.strip().lower() for g in genres):
                    result.append(comic)

        return result
