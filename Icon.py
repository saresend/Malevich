
from PIL import Image
import requests

class Icon(object):

    """ A class to make it easy to load in icons from urls, to load into a canvas """

    def __init__(self, url, size):
        """ Initializes an icon from a remote url, by using the requests library """
        self.image = Image.open(requests.get(url, stream=True).raw)
        self.image = self.image.resize(size)
        self.title = ""
        self.connections = []
        self.description = ""

