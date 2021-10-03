import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from const import *


class Sara:
    def __init__(self):
        self.base_url = BASE_URL

    def get_version(self):
        """Method allows to get version of service
        """
        res = requests.get(self.base_url + '/version')

        return res

    def add_photo(self, photo, metadata=''):
        """Method allows to recognize fields of document. Takes image file and metadata info
        :return: json with recognised fields
        """
        data = MultipartEncoder(
            fields={
                'images': (photo, 'image/jpeg'),
                'metadata': {metadata}
            }
        )
        res = requests.post(self.base_url + '/endpoint', data=data)  # TODO add valid endpoint

        return res
