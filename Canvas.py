from PIL import Image, ImageFilter

class Canvas(object):

    """ The primary class which holds all of the different elements that are going into building
    the diagram """

    def __init__(self, width=400, height=400, backgroundcolor=(0,0,0,0)):
        """ Initializes a blank canvas, with a specified width and height (defaults to 400x400), and
        a background color (default transparent)"""
        self.__canvas = Image.new("RGBA", (width, height), backgroundcolor)
        self.__bg = backgroundcolor
        self.__elements = [] # Stores Icon objects
        self.__position = [] # Stores tuples : (leftOffset, topOffset)
        self.__connections = [] # Stores connections between elements : ( 1, 3)


    def addElement(self, element, leftOffset, topOffset):
        """ Function for adding Icons/Text/Canvases to the canvas for future rendering """
        self.__elements.append(element)
        self.__position.append((leftOffset, topOffset))


    def createConnection(self, elInd1, elInd2):
        


    def Render(self, outputname="out.png"):
        """ Renders the Canvas object as an image for use """
        for i, el in enumerate(self.__elements):
            self.__canvas.paste(el.image, self.__position[i])

        # Checks to make sure there is no transparency:
        if self.__bg == (0,0,0,0):
            self.__canvas = self.__canvas.filter(ImageFilter.SMOOTH)
            self.__canvas.save(outputname)
            return
        
        i = self.__canvas.convert("RGBA")
        data = i.getdata()
        newData = []
        for val in data:
            if val[3] == 0:
                newData.append(self.__bg)
            else:
                newData.append(val)
        i.putdata(newData)
        i = i.filter(ImageFilter.SMOOTH_MORE)
        i = i.filter(ImageFilter.EDGE_ENHANCE)
        i.save(outputname)
        