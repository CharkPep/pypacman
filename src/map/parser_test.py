import pytest
from pytest_mock import mocker
from parser import MapParser


class Parser_LoadAssetsTest:
    def test_loadAssets(self):
        mocker.patch("pygame.image.load", return_value="image")
        parser = MapParser()
        parser._MapParser__loadAssets()
        assert parser.assets == {
            "walls" : "image",
            "thin_walls" : "image",
            "one_ways" : "image",   
        }


