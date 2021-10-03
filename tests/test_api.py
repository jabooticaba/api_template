import pytest
from os import listdir
from const import *

from api import Sara


sara = Sara()


class TestFunctions:

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_version(self):
        status = sara.get_version().status_code
        result = sara.get_version().json()

        assert status == 200
        assert result == SERVICE_VERSION

    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.parametrize('photo', listdir('../images'))
    def test_get_document_type(self, photo):
        photo_name = photo.split('.')[0]
        res = sara.add_photo(photo)
        status = res.status_code
        result = res.json()

        assert status == 200

        assert result['SITIZENSHIP'] == photo_name  # TODO correct argument parsing

    # For testing purpose
    @pytest.mark.parametrize('photo', listdir('../images'))
    def test_file_in_folder(self, photo):
        pass




