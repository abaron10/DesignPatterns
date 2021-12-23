from Compressor import Compressor
class JpegCompressor(Compressor):
    def compress(self,filename):
        print(f"Compressing {filename} using JPEG")