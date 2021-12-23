from Compressor import Compressor
class PngCompressor(Compressor):
    def compress(self, filename):
        print(f"Compressing {filename} using PNG")