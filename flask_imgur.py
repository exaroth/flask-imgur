# -*- coding: utf-8 -*-

import base64
import json
from six.moves import urllib



class Imgur(object):

    """
    Simple class for handling Imgur image upload, and deletion
    """


    API_URL = "https://api.imgur.com/3/image"

    def __init__(self, app=None, client_id=None, **kwargs):
        
        if not client_id and not app.config.get("IMGUR_ID", None):
            raise Exception("Missing client id")
        self.client_id = client_id or app.config.get("IMGUR_ID")
        if 'api' in kwargs:
            self.API_URL = kwargs["api"]

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

    def _build_send_request(self, image=None, params=dict()):

        """
        Build request for sending an image
        """
        
        if not image:
            raise Exception("Missing image object")

        b64 = base64.b64encode(image.read())

        data = dict(
                image = b64,
                type = 'base64',
                )

        data.update(params)
        return urllib.parse.urlencode(data).encode("utf-8")

    def send_image(self, image, send_params=dict(), additional_headers=dict()):
        """
        Main handler for sending images

            :params image -- Image object
            :params send_params -- additional info to be sent to imgur
            :params additional_headers -- additional headers to be added to request
        """
        req = urllib.request.Request(url = self._get_api(),
                              data = self._build_send_request(image, send_params),
                              headers = self._add_authorization_header(additional_headers)
                             )
        data = urllib.request.urlopen(req)
        return json.loads(data.read().decode("utf-8"))

    def delete_image(self, delete_hash, additional_headers=dict()):
        """
        Delete image from imgur

            :params delete_hash -- string containing unique
            image hash optained when sending an image
            :params additional_headers -- aditional headers to be addd to request
        """
        opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        req = urllib.request.Request(url = self._get_api() + "/" + delete_hash,
                              headers = self._add_authorization_header(additional_headers))
        req.get_method = lambda: "DELETE"
        data = urllib.request.urlopen(req)
        return json.loads(data.read().decode("utf-8"))

