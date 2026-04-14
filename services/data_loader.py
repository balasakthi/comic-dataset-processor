import csv

from models.comic import Comic


class DataLoader:
    def load_data(self, file_path):
        comics_dict = {}

        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                title = (row.get("Title") or "").strip()

                if not title:
                    continue

                # author = self.extract_author(row.get("Name"))
                author = (row.get("Name") or "").strip()
                genre = (row.get("Genre") or "").strip()
                year = (row.get("Date of publication") or "").strip()
                isbn = (row.get("ISBN") or "").strip() or "missing"
                language = (row.get("Languages") or "").strip()

                if title not in comics_dict:
                    comics_dict[title] = Comic(
                        title, author, genre, year, isbn, language
                    )
                else:
                    if year and year not in comics_dict[title].years:
                        comics_dict[title].years.append(year)
                    if isbn and isbn not in comics_dict[title].isbns:
                        comics_dict[title].isbns.append(isbn)

        return list(comics_dict.values())

    def extract_author(self, text):
        if not text:
            return "Unknown"

        parts = text.split(";")

        for part in parts:
            if "author" in part.lower():
                return part.split(", author")[0].strip()

        return parts[0].replace("[person]", "").strip()
