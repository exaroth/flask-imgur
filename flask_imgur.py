# -*- coding: utf-8 -*-

import base64
import json
from six.moves import urllib



class Imgur(object):

    """
    Basic class for handling Imgur image upload,
    Accepts header containing user_id variable
    and dictionary containing request configuration
    """

    API_URL = "https://api.imgur.com/3/image"

    def __init__(self, app=None, client_id=None , config=dict()):
        
        if not client_id and not app.config.get("IMGUR_ID", None):
            raise Exception("Missing client id")
        self.client_id = client_id or app.config.get("IMGUR_ID")
        self.config = config
        if 'api' in self.config:
            self.API_URL = self.config['api']


    def _get_api(self):
        return self.API_URL


    def _add_authorization_header(self, additional = dict()):

        """
        Builds authorization headers for anonymous users
        """

        headers = dict(
            Authorization = "Client-ID " + self.client_id
        )
        headers.update(additional)
        return headers


    def _build_send_request(self, image_data=dict(), params=dict()):

        """
        Build request for sending an image
        """

        try:
            img = image_data["image"]
        except:
            raise Exception("Missing image file")

        b64 = base64.b64encode(img.read())

        data = dict(
                image = b64,
                type = 'base64',
                name = image_data.get("name", None),
                description = image_data.get("description", None)
                )

        data.update(params)
        return urllib.parse.urlencode(data).encode("utf-8")


    def send_image(self, image_data, send_params=dict(), additional_headers=dict()):
        req = urllib.request.Request(url = self._get_api(),
                              data = self._build_send_request(image_data, params),
                              headers = self._add_authorization_header(additional_headers)
                             )
        data = urllib.request.urlopen(req)
        return json.loads(data.read().decode("utf-8"))

    def delete_image(self, delete_hash, additional=dict()):
        opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        req = urllib.request.Request(url = self._get_api() + "/" + delete_hash,
                              headers = self._add_authorization_header(additional))
        req.get_method = lambda: "DELETE"
        data = urllib.request.urlopen(req)
        return json.loads(data.read().decode("utf-8"))

