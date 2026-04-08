from services.data_loader import DataLoader
from services.filter_service import FilterService
from services.group_service import GroupService
from services.search_service import SearchService
from services.sort_service import SortService


class AppController:
    def __init__(self):
        self.loader = DataLoader()
        self.filter_service = FilterService()
        self.search_service = SearchService()
        self.sort_service = SortService()
        self.group_service = GroupService()

        # FEATURES
        self.search_history = []
        self.result_counter = {}
        self.saved_list = []

    def run(self):
        print("📚 Loading dataset...")
        comics = self.loader.load_data("data/names.csv")
        print(f"Total Records Loaded: {len(comics)}\n")

        # ---------------- FILTER ----------------
        print("Popular Genres: Fantasy, Horror, Fiction")
        genre = input("Enter genre (or press Enter to skip): ").strip().lower()

        if genre:
            filtered = self.filter_service.filter_by_genre(comics, genre)
        else:
            filtered = comics

        print(f"Filtered Count: {len(filtered)}\n")

        # ---------------- SEARCH ----------------
        print("\nSearch Options:")
        print("1. Simple Search")
        print("2. Advanced Search")

        choice = input("Choose (1/2): ").strip()

        if choice == "2":
            author = input("Author (optional): ").strip()
            year = input("Year (optional): ").strip()
            adv_genre = input("Genre (optional): ").strip()

            searched = self.search_service.advanced_search(
                filtered,
                author=author or None,
                year=year or None,
                genre=adv_genre or None,
            )

            self.search_history.append(
                f"Advanced (A={author or 'Any'}, Y={year or 'Any'}, G={adv_genre or 'Any'})"
            )

        else:
            keyword = input("Title keyword: ").strip()
            searched = self.search_service.search_by_title(filtered, keyword)
            self.search_history.append(keyword or "empty")

        print(f"🔍 Results: {len(searched)}\n")

        # Track results
        for comic in searched:
            self.result_counter[comic.title] = (
                self.result_counter.get(comic.title, 0) + 1
            )

        # ---------------- GROUP ----------------
        group_choice = input("Group by (author/year/none): ").strip().lower()

        if group_choice == "author":
            grouped = self.group_service.group_by_author(searched)
        elif group_choice == "year":
            grouped = self.group_service.group_by_year(searched)
        else:
            grouped = {"All": searched}

        # ---------------- SORT ----------------
        sort_choice = input("Sort (az/za): ").strip().lower()
        if sort_choice not in ["az", "za"]:
            sort_choice = "az"

        print("\n🎯 Results:\n")

        # ---------------- DISPLAY ----------------
        for group, items in grouped.items():
            print(f"\n📂 {group} ({len(items)} items)")

            if sort_choice == "za":
                sorted_items = self.sort_service.sort_za(items)
            else:
                sorted_items = self.sort_service.sort_az(items)

            for i, comic in enumerate(sorted_items[:5]):
                print(
                    f"{i+1}. {comic.title} | {comic.author} | {comic.get_years()} | {comic.get_genres()}"
                )

            # SAVE FEATURE
            save = input("💾 Save an item? Enter number or press Enter: ").strip()

            if save.isdigit():
                index = int(save) - 1
                if 0 <= index < len(sorted_items[:5]):
                    self.saved_list.append(sorted_items[index])
                    print("✅ Saved!")

        # ---------------- ANALYTICS ----------------
        print("\n📊 Analytics")

        # Top Searches
        print("\n🔎 Top Searches:")
        top_searches = sorted(
            set(self.search_history), key=self.search_history.count, reverse=True
        )[:10]

        for s in top_searches:
            print(f"- {s} ({self.search_history.count(s)} times)")

        # Top Results
        print("\n🏆 Top Results:")
        top_results = sorted(
            self.result_counter.items(), key=lambda x: x[1], reverse=True
        )[:10]

        for title, count in top_results:
            print(f"- {title} ({count} times)")

        # Saved List
        print("\n💾 Saved Items:")
        for comic in self.saved_list:
            print(
                f"- {comic.title} | {comic.author} | {comic.get_years()} | {comic.get_genres()}"
            )
