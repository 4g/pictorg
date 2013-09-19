from pyhashxx import Hashxx 

def get_hash(fname):        
    return hashf(fname)

def chunks(filename, chunksize):
    f = open(filename, mode='rb')
    buf = "bufferobj"
    while len(buf):
        buf = f.read(chunksize)
        yield buf

def hashf(filename):
    d = Hashxx(seed=0) # seed is optional
    d1 = Hashxx(seed=128)
    for buf in chunks(filename, 1024):
        d.update(buf)
        d1.update(buf)
    return d.digest() , d1.digest()
