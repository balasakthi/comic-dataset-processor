from models.comic import Comic
from services.filter_service import FilterService
from services.search_service import SearchService
from services.sort_service import SortService


# 🟢 Sample Data (Mock Data)
def sample_comics():
    return [
        Comic("Devil Hero", "Author A", "Comic; Fantasy", "2020", "123", "EN"),
        Comic("Ghost Story", "Author B", "Horror", "2019", "456", "EN"),
        Comic("Space War", "Author C", "Sci-Fi", "2021", "789", "EN"),
    ]


# 🟢 Test Filter
def test_filter_by_genre():
    comics = sample_comics()
    service = FilterService()

    result = service.filter_by_genre(comics, "Fantasy")

    assert len(result) == 1
    assert result[0].title == "Devil Hero"


# 🟢 Test Search
def test_search_by_title():
    comics = sample_comics()
    service = SearchService()

    result = service.search_by_title(comics, "space")

    assert len(result) == 1
    assert result[0].title == "Space War"


# 🟢 Test Advanced Search
def test_advanced_search():
    comics = sample_comics()
    service = SearchService()

    result = service.advanced_search(comics, author="Author A")

    assert len(result) == 1
    assert result[0].author == "Author A"


# 🟢 Test Sorting
def test_sort_az():
    comics = sample_comics()
    service = SortService()

    result = service.sort_az(comics)

    assert result[0].title == "Devil Hero"
