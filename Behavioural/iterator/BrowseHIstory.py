class BrowseHistory():
    __urls = []

    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a <= len(self.__urls)-1:
            current = self.__urls[self.a]
            self.a += 1
            return current
        else:
            raise StopIteration

    def push(self,url):
        self.__urls.append(url)
    def pop(self):
        return self.__urls.pop()

    