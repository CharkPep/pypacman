import pytest
from unittest.mock import patch
from lib.map.parser import DefaultMapParser


@pytest.fixture
def mock_surface():

    pass

@pytest.fixture
def mock_json_load():
    test_data = {
        "map": [["1", "2", "3"], ["4", "5", "6"]],
        "ghost_house": [0, 0],
        "chase_duration": 5,
        "scatter_duration": 10
    }
    with patch("lib.map.parser.json.load") as mock_load:
        mock_load.return_value = test_data
        yield mock_load

def test_parse_map(mock_surface, mock_json_load):
    parser = DefaultMapParser("tests/test_file.json", mock_surface)

    game_map = parser.parse((100, 100))

    assert game_map is not None

