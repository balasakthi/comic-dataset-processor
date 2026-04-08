class SearchService:

    def search_by_title(self, comics, keyword):
        if not keyword:
            return comics
        return [c for c in comics if keyword.lower() in c.title.lower()]

    def advanced_search(self, comics, author=None, year=None, genre=None):
        results = comics

        if author:
            results = [c for c in results if author.lower() in c.author.lower()]

        if year:
            results = [c for c in results if year in c.years]

        if genre:
            results = [c for c in results if genre.lower() in c.genre.lower()]

        return results
