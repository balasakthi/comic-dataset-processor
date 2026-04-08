class SortService:

    def sort_az(self, comics):
        return sorted(comics, key=lambda c: c.title.lower())

    def sort_za(self, comics):
        return sorted(comics, key=lambda c: c.title.lower(), reverse=True)
