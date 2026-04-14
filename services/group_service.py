class GroupService:
    def group_by_author(self, comics):
        grouped = {}

        for comic in comics:
            key = comic.author or "Unknown"
            grouped.setdefault(key, []).append(comic)

        return grouped

    def group_by_year(self, comics):
        grouped = {}

        for comic in comics:
            key = comic.year or "Unknown"
            grouped.setdefault(key, []).append(comic)

        return grouped
