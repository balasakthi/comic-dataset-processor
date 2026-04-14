from models.comic import Comic
from services.data_loader import DataLoader
from services.filter_service import FilterService
from services.search_service import SearchService
from services.sort_service import SortService


# Sample Data (Mock Data)
def sample_comics():
    return [
        Comic("Devil Hero", "Author A", "Comic; Fantasy", "2020", "123", "EN"),
        Comic("Ghost Story", "Author B", "Horror", "2019", "456", "EN"),
        Comic("Space War", "Author C", "Sci-Fi", "2021", "789", "EN"),
    ]


# Test Filter
def test_filter_by_genre():
    comics = sample_comics()
    service = FilterService()

    result = service.filter_by_genre(comics, "Fantasy")

    assert len(result) == 1
    assert result[0].title == "Devil Hero"


# Test Search
def test_search_by_title():
    comics = sample_comics()
    service = SearchService()

    result = service.search_by_title(comics, "space")

    assert len(result) == 1
    assert result[0].title == "Space War"


# Test Advanced Search
def test_advanced_search():
    comics = sample_comics()
    service = SearchService()

    result = service.advanced_search(comics, author="Author A")

    assert len(result) == 1
    assert result[0].author == "Author A"


# Test Sorting
def test_sort_az():
    comics = sample_comics()
    service = SortService()

    result = service.sort_az(comics)

    assert result[0].title == "Devil Hero"


# Tests how multiple components work together
def test_filter_then_search_then_sort():
    comics = DataLoader().load_data("data/names.csv")

    # Filter -> Search -> Sort pipeline
    filtered = FilterService().filter_by_genre(comics, "Fantasy")
    searched = SearchService().search_by_title(filtered, "hero")
    sorted_results = SortService().sort_az(searched)

    assert len(sorted_results) > 0
    assert sorted_results[0].title.lower() < sorted_results[-1].title.lower()


# Tests unusual/extreme inputs
def test_filter_empty_list():
    service = FilterService()
    result = service.filter_by_genre([], "Horror")
    assert result == []


def test_search_none_keyword():
    comics = sample_comics()
    service = SearchService()
    result = service.search_by_title(comics, None)
    assert result == comics  # Should return all


def test_sort_single_comic():
    comics = [Comic("Title", "Author", "Genre", "2020", "123", "EN")]
    service = SortService()
    result = service.sort_az(comics)
    assert len(result) == 1
