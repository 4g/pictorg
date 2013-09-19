from pyhashxx import Hashxx 

class FileHasher:

    def __init__(self):
        self.hash = self.hashf

    def chunks(self,filename, chunksize):
        f = open(filename, mode='rb')
        buf = "bufferobj"
        while len(buf):
            buf = f.read(chunksize)
            yield buf

    def hashf(self,filename):
        d = Hashxx(seed=0) # seed is optional
        d1 = Hashxx(seed=128)
        for buf in self.chunks(filename, 1024):
            d.update(buf)
            d1.update(buf)
        return d.digest() , d1.digest()
