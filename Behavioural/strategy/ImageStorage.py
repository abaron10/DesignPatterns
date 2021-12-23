

class ImageStorage():
    __compressor = ""
    __filter =""

    def __init__(self,compressor,filter):
        self.__compressor = compressor
        self.__filter = filter

    
    def store(self, filename):

        self.__compressor.compress(filename)
        self.__filter.apply(filename)

