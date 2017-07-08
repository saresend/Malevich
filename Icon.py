
from PIL import Image
import requests

class Icon(object):

    """ A class to make it easy to load in icons from urls, to load into a canvas """

    def __init__(self, url, size=None):
        """ Initializes an icon from a remote url, by using the requests library 
        :args 
            size : tuple(int, int)
            url  : string
        """
        self.image = Image.open(requests.get(url, stream=True).raw)
        if size != None:
            self.image = self.image.resize(size)
        self.title = ""
        self.connections = []
        self.description = ""
        self.connections = []