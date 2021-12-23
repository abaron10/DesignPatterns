from Filter import Filter
class BlackAndWhiteFilter(Filter):
    def apply(self,filename):
        print(f"Applying B&W filter to {filename}")